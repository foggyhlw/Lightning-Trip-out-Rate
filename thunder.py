# -*-coding=utf-8 -*-
import math
import sys
import fractions

#计算线路雷击跳闸率
#铁塔雷击跳闸率计算
#从配置文件读取数据
def read_from_configure_file(file_dir):
#从配置文件中读取数据
    comment=['#','[',';']
    with open(file_dir,'r',encoding='utf-8') as f:
        content=f.readlines()
        content=[c for c in content if c[0] not in comment]
        content=[c.strip() for c in content if c!='\n']
        content=[c.strip('\n').split('=') for c in content]
    var=dict()
#gp,gs  是用分数给出的，不能全读成float型
    for key,num in content:
        var[key]=num
    print(var)
    return var

def transform_vars(var):
    assert type(var)==dict
    for key,value in var.items():
        try:
            if var[key]!='':
                var[key]=float(value)
        except ValueError:
            return False,key
    return True,var
    
def calculate_trip_out_rate(var):
#step1
#导地线平均高度hav=ha-2/3*fa       P125
#hgg-地线在杆塔上的悬挂点高度m
    hgg=var['hgg']
#hag-导线在杆塔上的悬挂点高度m
    hag=var['hag']
#fg-地线弧垂m
    fg=var['fg']
#fa-导线弧垂m
    fa=var['fa']
#地线弧垂fg
#地线平均高度hgv
    hgv=hgg-2/3.0*fg
#导线平均高度hav
    hav=hag-2/3.0*fa

#step2
#地线对外侧导线的几何耦合系数k0   查表P134  2-7-8
    k0=var['k0']
#有点晕下的耦合系数k=k0*k1
#k1为雷击塔顶时的电晕矫正系数   查表P134  2-7-9
    k1=var['k1']
    k=k0*k1

#step3
#杆塔电感lt  查表P126   2-7-3 
#对于铁塔，表中波阻抗为150Ω，杆塔电感为0.5μH/m
#单位长度电感ls
    ls=var['ls']
#lt等于杆塔高度ha*单位长度电感   μH
    ht=var['ht']
    lt=ht*ls

#step4
#分流系数β   查表P126   2-7-4
    beta=var['beta']
#雷击杆塔时的耐雷水平    

#I1为雷击塔顶时的耐雷水平(有地线情况下)
#I1=U50/[(1-k)*beta*Rsu+(ha/ht-k)*beta*Lt/2.6+(1-hgv/hav*k0)*hav/2.6]   kA
### U50为50%冲击放电电压 kV 
#U50=绝缘子片数*绝缘子雷电冲击耐受电压
#n-绝缘子片数
#Uth-绝缘子雷电冲击耐受电压  kV
    U50=var['Uth']*var['n']
    #U50=var['U50']
#rsu-杆塔冲击接地电阻  Ω
    rsu=var['rsu']
#ht-杆塔高度
#ha-横担对地高度
    ha=var['ha']
    I1=U50/((1-k)*beta*rsu+(ha/ht-k)*beta*lt/2.6+(1-hgv/hav*k0)*hav/2.6)
#P1-雷电流超过I1的概率
#对于年平均雷暴日大于20的地区有logP=-Im/88
#对于年平均雷暴日小于20的地区有LogP=-Im/44
    P1=10**(-I1/88)

#绕击率Pth（平原线路）
#th-线路保护角    °
    th=var['th']
#绕击率lgPth=th*sqrt(h)/86-3.9
    Pthp=10**(th*math.sqrt(hgg)/86-3.9)
#绕击率（山区线路）
#绕击率lgPth=th*sqrt(h)/86-3.35
#Pths=10**(th*math.sqrt(hgg)/86-3.35)
    Pths=10**(th*math.sqrt(hgg)/86-3.35)

#I2-雷绕击于导线时的耐雷水平  kA
    I2=U50/100
#雷电流超过I2的概率
#对于年平均雷暴日大于20的地区有logP=-Im/88
#对于年平均雷暴日小于20的地区有LogP=-Im/44
    P2=10**(-I2/88)    #以大于20日计

#ita-建弧率
#建弧率公式ita=(4.5*E**0.75-14)/100.0  

#E-绝缘子串平均运行电压梯度有效值
#对于中性点不接地系统 E=U/(2*lig+lw)
#对于中性点直接接地系统 E=U/sqrt(3)/lig
#lig-绝缘子串的闪络距离 mm 如 146mm   155mm
    lig=var['lig']/1000
#lw-木横担线路的线间距离，对于铁和钢筋混凝土横担为0
    lw=var['lw']
    U=var['U']
#N_line-中性点运行方式  0：不直接接地   1：直接接地
    N_line=var['N_line']
#n-绝缘子片数
    n=var['n']
#中性点不直接接地情况
    if N_line==0:
        E=U/(2*lig+lw)/n
#中性点直接接地情况
    if N_line==1:
        E=U/math.sqrt(3)/lig/n

    ita=(4.5*E**0.75-14)/100.0  

#n-一般高度的有地线线路的雷击跳闸率
#n=N*ita*(g*P1+Pth*P2)
#N-每年每100km线路的雷击次数    N=0.28*(b+4*hav)
#b-两根地线之间的距离，单地线或无地线取0
    b=var['b']
#ng-地线根数  根据地形和地线根数查表得击杆率  P125  2-7-2
    form_g=[[1/4,1/6],[1/3,1/4]]
    ng=int(var['ng'])
#通过查表获得击杆率的方式
    gp=form_g[0][ng-1]
    gs=form_g[1][ng-1]
#直接输入击杆率的方式
#gp-平原击杆率   查表P125    2-7-2
#    temp=fractions.Fraction((var['gp']))
#    gp=temp.numerator/temp.denominator
#gs-山区击杆率   查表P125    2-7-2
#    temp=fractions.Fraction((var['gs']))
#    gs=temp.numerator/temp.denominator

    N=0.28*(b+4*hgv)
#雷击跳闸率（有地线）
#np-平原地区雷击跳闸率
    np=N*ita*(gp*P1+Pthp*P2)
#ns-山区雷击跳闸率
    ns=N*ita*(gs*P1+Pths*P2)
    
    print('\n')
    print('建弧率ita:                             '+str(int(ita*10000)/10000)+'%')
    print('雷击杆塔时的耐雷水平I1:    '+str(int(I1*10000)/10000)+' kA')
    print('雷电流超过I1的概率P1:       '+str(int(P1*100000)/1000)+'%')

    print('雷击导线时的耐雷水平I2:    '+str(I2)+' kA')
    print('雷电流超过I2的概率P2:       '+str(int(P2*100000)/1000)+'%')
    print('平原地区绕击率:                  '+str(int(Pthp*100000)/1000)+'%')
    print('山区绕击率:                         '+str(int(Pths*100000)/1000)+'%')

    print('平原地区跳闸率 np:             '+str(int(np*10000)/10000))
    print('山区跳闸率 ns :                   '+str(int(ns*10000)/10000))
    return('\n'+\
            '建弧率ita:                             '+str(int(ita*10000)/10000)+'%'+'\n'\
            '雷击杆塔时的耐雷水平I1:    '+str(int(I1*10000)/10000)+' kA'+'\n'\
            '雷电流超过I1的概率P1:       '+str(int(P1*100000)/1000)+'%'+'\n'\
            '雷击导线时的耐雷水平I2:    '+str(I2)+' kA'+'\n'\
            '雷电流超过I2的概率P2:       '+str(int(P2*100000)/1000)+'%'+'\n'\
            '平原地区绕击率:           '+str(int(Pthp*100000)/1000)+'%'+'\n'\
            '山区绕击率:         '+str(int(Pths*100000)/1000)+'%'+'\n'\
            '平原地区跳闸率 np:        '+str(int(np*10000)/10000)+'\n'\
            '山区跳闸率 ns:           '+str(int(ns*10000)/10000)+'\n\n')
if __name__ == '__main__':
    try:
        varsInput=input('choose vars input ways: 1:configure file , 2:manually\n')
        while(varsInput not in ['1','2']):
            print('invalid input!')
            varsInput=input('choose vars input ways: 1:configure file , 2:manually')
        if varsInput=='1':
            var=read_from_configure_file('var.txt')

            suss,result=transform_vars(var)
            for i,j in var.items():
                print(type(j))
                
            if suss==True:
                calculate_trip_out_rate(result)
            if suss==False:
                print(result)
    except:
        print(sys.exc_info())
    input('press return to exit')

