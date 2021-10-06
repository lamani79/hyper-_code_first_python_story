
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import sys
import os
from os import path
import webbrowser

FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"decod.ui"))

# هذي ليست فيها كل الحروف الارقام و بعض الرموز الأساسية يمكنك ضيف فيها كيفما تشاء
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','!', 'l', 'm','؟','?', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
        'v',
        'w', 'x', 'y', 'z', ' ', '(', ')', '&', '0', '1',';','2', '3', '4', '5', '6', '7', '8', '9', '"', '-', 'ض',
        'ص', 'ث',
        'ق', 'ف', 'غ', 'ع', 'ه','.', 'خ', 'ح', 'ج', 'د',',', 'ش', 'س', 'ي', 'ب', 'ل', 'ا', 'أ', 'ن', 'م', 'ك', 'ط', 'ذ',
        'ئ',
        'ء', 'ؤ', 'ر', 'ى', 'ة', 'و', 'ز', 'ظ', '\n','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U'
    'V','W','X','Y','Z','   ','*','+','×','÷','{','}','<','>','ت']


class MainApp(QMainWindow,FORM_CLASS):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.costimize()
        self.Hunt_Buttons()
    def costimize(self): # دالة مسؤولة عن تخصيص المظهر الخاص بالواجهى الرسومية
        self.setWindowIcon(QIcon('key (1).png'))
        self.setFixedSize(611,474)
        self.setWindowTitle('Hyper Coder')

    def Hunt_Buttons(self): # دالة لتشغيل الأزرار
        self.pushButton.clicked.connect(self.chifre)
        self.pushButton_2.clicked.connect(self.dechifre)
        self.pushButton_4.clicked.connect(self.chifre_file)
        self.pushButton_3.clicked.connect(self.Brows)

    # دالة التشفير العادي
    def chifre(self):
        user_input=self.textEdit.toPlainText()
        s = len(user_input)
        #  لا تنسى !!! إجعل الكلمات صغيرة بدالة تحويل كل النص الى صغير
        x_code = ""
        for x in range(0, s):
            if user_input[x] in list:
                if x == 0:
                    x_code = x_code + "" + str(list.index(user_input[x]))
                else:
                    x_code = x_code + "," + str(list.index(user_input[x]))
        self.textEdit_3.setText(x_code)
     # دالة فك التشفير
    def dechifre(self):
        user=self.textEdit_2.toPlainText()
        user = user.split(',')
        decod = ""
        for x in range(0, len(user)):
            for j in list:
                if list.index(j) == int(user[x]):
                    decod = decod + list[int(user[x])]
        self.textEdit_4.setText(decod)
    # دالة التشفير من النوع الثاني تأتي بملف text يختاره المستخدم و تشفيره
    def chifre_file(self):
        #  C:\Users\Python\Desktop\code.txt
        chois_file=self.lineEdit.text()
        file=open(chois_file,'r')
        user_input_2=file.read()
        s = len(user_input_2)
        x_code = ""
        for x in range(0, s):
            if user_input_2[x] in list:
                if x == 0:
                    x_code = x_code + "" + str(list.index(user_input_2[x]))
                else:
                    x_code = x_code + "," + str(list.index(user_input_2[x]))

        file.close()
        self.textEdit_5.setText(x_code)

    # دالة الزر الذي منه يختار المستخدم مكان الملف
    def Brows(self):
        # تمت إضافة هاذا الكود لإجبار المستخدم على إختيار ملف text فقط لا غير للايحدث مشكل
        save =QFileDialog.getOpenFileName(self,'إختر النص الخاص بك',"", '*.txt')
        self.lineEdit.setText(save[0])

def main():
    app = QApplication(sys.argv)
    window= MainApp()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()