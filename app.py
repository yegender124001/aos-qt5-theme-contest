#!/bin/bash
'''
Author: Yegender Kumar

A test app just to show your creativity.
Make good looking it as possible you can and share it on instagram with tagging me: @unknown_brain_v2.0

Post bugs and issues on github
'''
import sys
import os
import threading
try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
except:
    print("PyQt5 is not installed. Would you like to install ?")
    print("     1. Yes")
    print("     2. No")
    while True:
        opt=int(input("Choose your option: "))
        if opt == 1:
            os.system("pip install PyQt5")
            break
        if opt == 2:
            exit()
        else:
            continue

class Application(QWidget):
    def _applystylesheet(this):
        this.newstyles = this.lineEdit2.toPlainText()
        this.setStyleSheet(this.newstyles)
    def _stylesheet(this):
        this.dialog1 = QWidget()
        this.layout2 = QVBoxLayout()
        this.dialog1.setLayout(this.layout2)
        this.label2 = QLabel("Enter StyleSheet Here")
        this.lineEdit2 = QTextEdit()
        this.lineEdit2.setText("""/*
NOTE: Box Shadow is not available for now,
Shadow is not a part of CSS as on Qt StyleSheet
It is just a basic css Syntax.
.widget => Main Window Class
.label => Label Class
.button1 => PushButton Class
.button2 => ToolButton Class
.lineEdit => Text Input Box Class
.radio => Radio Button Class
.checkbox => Check Box Class*/




.widget{

}
.label{

}
.button1{

}
.button2{

}
.lineEdit{

}
.radio{

}
.checkbox{

}
""")
        this.button3 = QPushButton("Apply")
        this.button3.clicked.connect(lambda:this._applystylesheet())
        this.label3 = QLabel("Templates:")
        this.template1button = QPushButton("Metro")
        this.template1 = """
/*
NOTE: Box Shadow is not available for now,
Shadow is not a part of CSS as on Qt StyleSheet
It is just a basic css Syntax.
.widget => Main Window Class
.label => Label Class
.button1 => PushButton Class
.button2 => ToolButton Class
.lineedit => Text Input Box Class
.radio => Radio Button Class
.checkbox => Check Box Class*/




.widget{
background-color:rgba(0,0,0,0);
color:white;
}
.label{
font-size:17px;
color:white;
background-color:transparent;
border:none
}
.button1{
font-size:17px;
height:30px;
color:white;
background-color:#222;
border:2px solid #222;
padding:5px;
}
.button2{
font-size:17px;
height:30px;
color:white;
background-color:#222;
border:2px solid #222;
padding:5px;
}
.lineEdit{
font-size:17px;
background-color:transparent;
color:white;
border:3px solid rgb(205,204,205);
padding:5px;
}
.lineEdit:hover{
border-color:white;
}
.lineEdit::focus{
background-color:white;
border-color:green;
color:black;
}
.radio{
font-size:17px;
background-color:transparent;
color:white;
padding:5px;
}
.radio::indicator{
border:2px solid rgb(205,204,205);
border-radius:10px;
height:17px;
width:17px;
}
.radio::indicator:checked{
border:2px solid green;
background-color:green;
height:17px;
width:17px;
}
.radio::indicator:hover{
border:2px solid #ddd;
}
.checkbox{
font-size:17px;
background-color:transparent;
color:white;
padding:5px;
}
.checkbox::indicator{
border:2px solid rgb(205,204,205);
height:17px;
width:17px;
}
.checkbox::indicator:checked{
border:2px solid green;
background-color:green;
height:17px;
width:17px;
}
.checkbox::indicator:hover{
border:2px solid #ddd
}
.button1:hover{
border:2px solid #ddd;
}
.button2:hover{
border:2px solid #ddd;
}
        """
        this.layout2.addWidget(this.label2)
        this.layout2.addWidget(this.lineEdit2)
        this.layout2.addWidget(this.button3)
        this.layout2.addWidget(this.label3)
        this.layout2.addWidget(this.template1button)
        this.template1button.clicked.connect(lambda:this.lineEdit2.setText(this.template1))
        this.dialog1.show()
    def _widgets(this):
        this.layout = QVBoxLayout()
        this.label1=QLabel("A Label: (.label)")
        this.label1.setProperty("class","label")
        this.button1 = QPushButton("I am a PushButton(.button1)")
        this.button1.setProperty("class","button1")
        this.button2 = QToolButton()
        this.button2.setProperty("class","button2")
        this.button2.setText("I am a ToolButton(.button2)")
        this.textedit = QLineEdit("You can enter here anything inside me(.lineEdit)")
        this.textedit.setProperty("class","lineEdit")
        this.radio1 = QRadioButton("I am a Radio Button(.radio)")
        this.radio1.setProperty("class","radio")
        this.checkbox1 = QCheckBox("Just a Checkbox, Nice to meet you(.checkbox)")
        this.checkbox1.setProperty("class","checkbox")
        this.layout.addWidget(this.label1)
        this.layout.addWidget(this.button1)
        this.layout.addWidget(this.button2)
        this.layout.addWidget(this.textedit)
        this.layout.addWidget(this.radio1)
        this.layout.addWidget(this.checkbox1)

    def __init__(this, *args,**kwargs):
        super().__init__(*args,**kwargs)
        this.setWindowTitle("Avdan OS Test App: Just to see your theming creativity")
        #c = "xprop -f _KDE_NET_WM_BLUR_BEHIND_REGION 32c -set _KDE_NET_WM_BLUR_BEHIND_REGION 0 -id " + str(this.winId())
        this._widgets()
        this._stylesheet()
        this.setProperty("class","widget")
        this.setLayout(this.layout)
        #os.system(c)

if __name__ == '__main__':
    app = QApplication([])
    window = Application()
    window.show()
    sys.exit(app.exec_())
