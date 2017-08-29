import sys
from PyQt4 import QtCore, QtGui
from dialog import *

class TripOutDialog(QtGui.QDialog,Ui_Dialog):  
    def __init__(self,parent=None):  
        super(TripOutDialog,self).__init__(parent)  
        self.setupUi(self)
        
def main():
    app=QtGui.QApplication(sys.argv)  
    dialog=TripOutDialog()  
    dialog.show()  
    app.exec_()  



##def main():
##    app = QtGui.QApplication(sys.argv)
##    ex = Mainwindow()
##    sys.exit(app.exec_())

if __name__ == '__main__':
    main()    
