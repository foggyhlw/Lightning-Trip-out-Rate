# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\雷击跳闸率.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import thunder
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(771, 449)
        self.formLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(280, 200, 198, 181))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_isolator = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_isolator.setObjectName(_fromUtf8("label_isolator"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_isolator)
        self.label_number = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_number.setObjectName(_fromUtf8("label_number"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_number)
        self.number_set = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.number_set.setObjectName(_fromUtf8("number_set"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.number_set)
        self.label_Up = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_Up.setObjectName(_fromUtf8("label_Up"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_Up)
        self.Up_set = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.Up_set.setObjectName(_fromUtf8("Up_set"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.Up_set)
        self.label_Un = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_Un.setObjectName(_fromUtf8("label_Un"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_Un)
        self.Un_set = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.Un_set.setObjectName(_fromUtf8("Un_set"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.Un_set)
        self.label_Uth = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_Uth.setObjectName(_fromUtf8("label_Uth"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_Uth)
        self.Uth_set = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.Uth_set.setObjectName(_fromUtf8("Uth_set"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.Uth_set)
        self.label_lig = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_lig.setObjectName(_fromUtf8("label_lig"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_lig)
        self.lig_set = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.lig_set.setObjectName(_fromUtf8("lig_set"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.lig_set)
        self.line_3 = QtGui.QFrame(self.formLayoutWidget_2)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.line_3)
        self.line = QtGui.QFrame(self.formLayoutWidget_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.line)
        self.formLayoutWidget = QtGui.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 247, 415))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_tower = QtGui.QLabel(self.formLayoutWidget)
        self.label_tower.setObjectName(_fromUtf8("label_tower"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_tower)
        self.label_ht = QtGui.QLabel(self.formLayoutWidget)
        self.label_ht.setObjectName(_fromUtf8("label_ht"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_ht)
        self.ht_set = QtGui.QLineEdit(self.formLayoutWidget)
        self.ht_set.setObjectName(_fromUtf8("ht_set"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.ht_set)
        self.label_la = QtGui.QLabel(self.formLayoutWidget)
        self.label_la.setObjectName(_fromUtf8("label_la"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_la)
        self.label_lw = QtGui.QLabel(self.formLayoutWidget)
        self.label_lw.setObjectName(_fromUtf8("label_lw"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_lw)
        self.label_ng = QtGui.QLabel(self.formLayoutWidget)
        self.label_ng.setObjectName(_fromUtf8("label_ng"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_ng)
        self.label_b = QtGui.QLabel(self.formLayoutWidget)
        self.label_b.setObjectName(_fromUtf8("label_b"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_b)
        self.label_hgg = QtGui.QLabel(self.formLayoutWidget)
        self.label_hgg.setObjectName(_fromUtf8("label_hgg"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_hgg)
        self.hgg_set = QtGui.QLineEdit(self.formLayoutWidget)
        self.hgg_set.setObjectName(_fromUtf8("hgg_set"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.hgg_set)
        self.label_hag = QtGui.QLabel(self.formLayoutWidget)
        self.label_hag.setObjectName(_fromUtf8("label_hag"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_hag)
        self.hag_set = QtGui.QLineEdit(self.formLayoutWidget)
        self.hag_set.setObjectName(_fromUtf8("hag_set"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.hag_set)
        self.label_fg = QtGui.QLabel(self.formLayoutWidget)
        self.label_fg.setObjectName(_fromUtf8("label_fg"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_fg)
        self.label_fa = QtGui.QLabel(self.formLayoutWidget)
        self.label_fa.setObjectName(_fromUtf8("label_fa"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_fa)
        self.label_k0 = QtGui.QLabel(self.formLayoutWidget)
        self.label_k0.setObjectName(_fromUtf8("label_k0"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.LabelRole, self.label_k0)
        self.label_k1 = QtGui.QLabel(self.formLayoutWidget)
        self.label_k1.setObjectName(_fromUtf8("label_k1"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.LabelRole, self.label_k1)
        self.label_rsu = QtGui.QLabel(self.formLayoutWidget)
        self.label_rsu.setObjectName(_fromUtf8("label_rsu"))
        self.formLayout.setWidget(13, QtGui.QFormLayout.LabelRole, self.label_rsu)
        self.label_ls = QtGui.QLabel(self.formLayoutWidget)
        self.label_ls.setObjectName(_fromUtf8("label_ls"))
        self.formLayout.setWidget(14, QtGui.QFormLayout.LabelRole, self.label_ls)
        self.label_th = QtGui.QLabel(self.formLayoutWidget)
        self.label_th.setObjectName(_fromUtf8("label_th"))
        self.formLayout.setWidget(15, QtGui.QFormLayout.LabelRole, self.label_th)
        self.label_beta = QtGui.QLabel(self.formLayoutWidget)
        self.label_beta.setObjectName(_fromUtf8("label_beta"))
        self.formLayout.setWidget(16, QtGui.QFormLayout.LabelRole, self.label_beta)
        self.lw_set = QtGui.QLineEdit(self.formLayoutWidget)
        self.lw_set.setObjectName(_fromUtf8("lw_set"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lw_set)
        self.ha_set = QtGui.QLineEdit(self.formLayoutWidget)
        self.ha_set.setObjectName(_fromUtf8("ha_set"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.ha_set)
        self.ng_set = QtGui.QLineEdit(self.formLayoutWidget)
        self.ng_set.setObjectName(_fromUtf8("ng_set"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.ng_set)
        self.b_set = QtGui.QLineEdit(self.formLayoutWidget)
        self.b_set.setObjectName(_fromUtf8("b_set"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.b_set)
        self.fg_set = QtGui.QLineEdit(self.formLayoutWidget)
        self.fg_set.setObjectName(_fromUtf8("fg_set"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.fg_set)
        self.fa_set = QtGui.QLineEdit(self.formLayoutWidget)
        self.fa_set.setObjectName(_fromUtf8("fa_set"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.fa_set)
        self.k0_set = QtGui.QLineEdit(self.formLayoutWidget)
        self.k0_set.setObjectName(_fromUtf8("k0_set"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.k0_set)
        self.k1_set = QtGui.QLineEdit(self.formLayoutWidget)
        self.k1_set.setObjectName(_fromUtf8("k1_set"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.FieldRole, self.k1_set)
        self.rsu_set = QtGui.QLineEdit(self.formLayoutWidget)
        self.rsu_set.setObjectName(_fromUtf8("rsu_set"))
        self.formLayout.setWidget(13, QtGui.QFormLayout.FieldRole, self.rsu_set)
        self.ls_set = QtGui.QLineEdit(self.formLayoutWidget)
        self.ls_set.setObjectName(_fromUtf8("ls_set"))
        self.formLayout.setWidget(14, QtGui.QFormLayout.FieldRole, self.ls_set)
        self.th_set = QtGui.QLineEdit(self.formLayoutWidget)
        self.th_set.setObjectName(_fromUtf8("th_set"))
        self.formLayout.setWidget(15, QtGui.QFormLayout.FieldRole, self.th_set)
        self.beta_set = QtGui.QLineEdit(self.formLayoutWidget)
        self.beta_set.setObjectName(_fromUtf8("beta_set"))
        self.formLayout.setWidget(16, QtGui.QFormLayout.FieldRole, self.beta_set)
        self.line_2 = QtGui.QFrame(self.formLayoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.line_2)
        self.trip_out_rate = QtGui.QTextBrowser(Dialog)
        self.trip_out_rate.setGeometry(QtCore.QRect(300, 20, 161, 41))
        self.trip_out_rate.setObjectName(_fromUtf8("trip_out_rate"))
        self.line_5 = QtGui.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(10, 430, 751, 16))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(0, 10, 20, 431))
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.line_7 = QtGui.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(10, 0, 751, 16))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_8 = QtGui.QFrame(Dialog)
        self.line_8.setGeometry(QtCore.QRect(480, 10, 20, 431))
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.line_9 = QtGui.QFrame(Dialog)
        self.line_9.setGeometry(QtCore.QRect(270, 180, 221, 16))
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.line_10 = QtGui.QFrame(Dialog)
        self.line_10.setGeometry(QtCore.QRect(260, 10, 20, 431))
        self.line_10.setFrameShape(QtGui.QFrame.VLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.line_11 = QtGui.QFrame(Dialog)
        self.line_11.setGeometry(QtCore.QRect(270, 380, 491, 16))
        self.line_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.N_Line_choose = QtGui.QComboBox(Dialog)
        self.N_Line_choose.setGeometry(QtCore.QRect(380, 150, 91, 31))
        self.N_Line_choose.setObjectName(_fromUtf8("N_Line_choose"))
        self.N_Line_choose.addItem(_fromUtf8(""))
        self.N_Line_choose.addItem(_fromUtf8(""))
        self.Voltage_choose = QtGui.QComboBox(Dialog)
        self.Voltage_choose.setEnabled(True)
        self.Voltage_choose.setGeometry(QtCore.QRect(380, 110, 91, 31))
        self.Voltage_choose.setMaxCount(6)
        self.Voltage_choose.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.Voltage_choose.setObjectName(_fromUtf8("Voltage_choose"))
        self.Voltage_choose.addItem(_fromUtf8(""))
        self.Voltage_choose.addItem(_fromUtf8(""))
        self.Voltage_choose.addItem(_fromUtf8(""))
        self.Voltage_choose.addItem(_fromUtf8(""))
        self.Voltage_choose.addItem(_fromUtf8(""))
        self.label_sysem = QtGui.QLabel(Dialog)
        self.label_sysem.setGeometry(QtCore.QRect(290, 80, 89, 22))
        self.label_sysem.setObjectName(_fromUtf8("label_sysem"))
        self.Voltage = QtGui.QLabel(Dialog)
        self.Voltage.setGeometry(QtCore.QRect(290, 110, 89, 36))
        self.Voltage.setObjectName(_fromUtf8("Voltage"))
        self.label_N_line = QtGui.QLabel(Dialog)
        self.label_N_line.setGeometry(QtCore.QRect(290, 130, 89, 78))
        self.label_N_line.setObjectName(_fromUtf8("label_N_line"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(500, 60, 251, 311))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.line_12 = QtGui.QFrame(Dialog)
        self.line_12.setGeometry(QtCore.QRect(750, 10, 20, 431))
        self.line_12.setFrameShape(QtGui.QFrame.VLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(510, 30, 131, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_calculate = QtGui.QPushButton(Dialog)
        self.pushButton_calculate.setGeometry(QtCore.QRect(540, 400, 41, 23))
        self.pushButton_calculate.setObjectName(_fromUtf8("pushButton_calculate"))
        self.pushButton_open = QtGui.QPushButton(Dialog)
        self.pushButton_open.setGeometry(QtCore.QRect(610, 400, 41, 23))
        self.pushButton_open.setObjectName(_fromUtf8("pushButton_open"))
        self.pushButton_save = QtGui.QPushButton(Dialog)
        self.pushButton_save.setGeometry(QtCore.QRect(680, 400, 41, 23))
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 390, 211, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(280, 410, 201, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_isolator.setText(_translate("Dialog", "绝缘子参数", None))
        self.label_number.setText(_translate("Dialog", "绝缘子片数", None))
        self.label_Up.setText(_translate("Dialog", "正极性冲击电压(kV)", None))
        self.label_Un.setText(_translate("Dialog", "负极性冲击电压(kV)", None))
        self.label_Uth.setText(_translate("Dialog", "雷电冲击耐受电压(kV)", None))
        self.label_lig.setText(_translate("Dialog", "绝缘子串闪络距离（mm)", None))
        self.label_tower.setText(_translate("Dialog", "杆塔参数", None))
        self.label_ht.setText(_translate("Dialog", "杆塔高度(m)", None))
        self.label_la.setText(_translate("Dialog", "横担对地高度(m)", None))
        self.label_lw.setText(_translate("Dialog", "木横担线路的线间距离", None))
        self.label_ng.setText(_translate("Dialog", "地线根数", None))
        self.label_b.setText(_translate("Dialog", "两根地线之间的距离(m)", None))
        self.label_hgg.setText(_translate("Dialog", "地线在杆塔上的悬挂点高度(m)", None))
        self.label_hag.setText(_translate("Dialog", "导线在杆塔上的悬挂点高度(m)", None))
        self.label_fg.setText(_translate("Dialog", "地线弧垂(m)", None))
        self.label_fa.setText(_translate("Dialog", "导线弧垂(m)", None))
        self.label_k0.setText(_translate("Dialog", "地线对外侧导线的几何耦合系数", None))
        self.label_k1.setText(_translate("Dialog", "雷击塔顶时的电晕矫正系数", None))
        self.label_rsu.setText(_translate("Dialog", "杆塔冲击接地电阻", None))
        self.label_ls.setText(_translate("Dialog", "杆塔单位高度电感(μH/m)", None))
        self.label_th.setText(_translate("Dialog", "线路保护角(角度)", None))
        self.label_beta.setText(_translate("Dialog", "分流系数", None))
        self.trip_out_rate.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.16364pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">雷击跳闸率计算</span></p></body></html>", None))
        self.N_Line_choose.setItemText(0, _translate("Dialog", "直接接地", None))
        self.N_Line_choose.setItemText(1, _translate("Dialog", "不接地", None))
        self.Voltage_choose.setItemText(0, _translate("Dialog", "35", None))
        self.Voltage_choose.setItemText(1, _translate("Dialog", "66", None))
        self.Voltage_choose.setItemText(2, _translate("Dialog", "110", None))
        self.Voltage_choose.setItemText(3, _translate("Dialog", "220", None))
        self.Voltage_choose.setItemText(4, _translate("Dialog", "750", None))
        self.label_sysem.setText(_translate("Dialog", "系统参数", None))
        self.Voltage.setText(_translate("Dialog", "电压等级(kV)", None))
        self.label_N_line.setText(_translate("Dialog", "中性点运行方式", None))
        self.label.setText(_translate("Dialog", "计算结果", None))
        self.pushButton_calculate.setText(_translate("Dialog", "计算", None))
        self.pushButton_open.setText(_translate("Dialog", "打开", None))
        self.pushButton_save.setText(_translate("Dialog", "保存", None))
        self.label_2.setText(_translate("Dialog", "注：所有参数必须为数字形式", None))
        self.label_3.setText(_translate("Dialog", "鼠标停留于文本框会有参数提示", None))

#增加按钮动作
        self.pushButton_calculate.clicked.connect(self.calculate)
        self.pushButton_save.clicked.connect(self.save_file)
        self.pushButton_open.clicked.connect(self.open_file)
#增加说明tooltip
        self.lw_set.setToolTip('铁和钢筋混凝土横担为0')
        self.ls_set.setToolTip('见设计手册P126表2-7-3')
        self.k0_set.setToolTip('见设计手册P134表2-7-8')
        self.k1_set.setToolTip('见设计手册P134表2-7-9')
        self.beta_set.setToolTip('见设计手册P126表2-7-4')
        self.Uth_set.setToolTip('查阅绝缘子参数手册')
        self.rsu_set.setToolTip('一般取7或15Ω')
        

    def read_vars(self):
        var=dict()
        var['hgg']=self.hgg_set.text()
        var['hag']=self.hag_set.text()
        var['fg']=self.fg_set.text()
        var['fa']=self.fa_set.text()
        var['k0']=self.k0_set.text()
        var['k1']=self.k1_set.text()
        var['ls']=self.ls_set.text()
        var['ht']=self.ht_set.text()
        var['n']=self.number_set.text()
        var['Uth']=self.Uth_set.text()
        var['rsu']=self.rsu_set.text()
        var['ha']=self.ha_set.text()
        var['th']=self.th_set.text()
        var['lig']=self.lig_set.text()
        var['lw']=self.lw_set.text()
        var['U']=self.Voltage_choose.currentText()
        var['N_line']=self.N_Line_choose.currentIndex()
        var['b']=self.b_set.text()
        var['ng']=self.ng_set.text()
        var['beta']=self.beta_set.text()
        return var
    
    def calculate(self):
        var=self.read_vars()
        suss,result=thunder.transform_vars(var)
        if suss==True:
            output=thunder.calculate_trip_out_rate(result)
            self.textBrowser.insertPlainText(output)
        if suss==False:
            self.textBrowser.insertPlainText(result)

    def save_file(self):
        fd=QtGui.QFileDialog()
        conf_file=fd.getSaveFileName()
        if conf_file!=None:
            with open(conf_file,'w',encoding='utf-8') as f:
                conf_var=self.read_vars()
                for key,value in conf_var.items():
                    f.write(str(key)+'='+str(value)+'\r\n')
            self.textBrowser.insertPlainText('文件保存成功！')

    def open_file(self):
        fd=QtGui.QFileDialog()
        try:
            conf_file=fd.getOpenFileName()
            var=thunder.read_from_configure_file(conf_file)
            self.hgg_set.setText(str(var['hgg']))
            self.hag_set.setText(str( var['hag']))
            self.fg_set.setText(str(var['fg']))
            self.fa_set.setText(str(var['fa']))
            self.k0_set.setText(str( var['k0']))
            self.k1_set.setText(str(var['k1']))
            self.ls_set.setText(str(var['ls']))
            self.ht_set.setText(str(var['ht']))
            self.number_set.setText(str(var['n']))
            self.Uth_set.setText(str(var['Uth']))
            self.rsu_set.setText(str(var['rsu']))
            self.ha_set.setText(str(var['ha']))
            self.th_set.setText(str( var['th']))
            self.lig_set.setText(str(var['lig']))
            self.lw_set.setText(str(var['lw']))
    ##        var['U']=self.Voltage_choose.currentText()
    ##        var['N_line']=self.N_Line_choose.currentIndex()
            self.b_set.setText(str( var['b']))
            self.ng_set.setText(str(var['ng']))
            self.beta_set.setText(str(var['beta']))
        except FileNotFoundError:
            pass

