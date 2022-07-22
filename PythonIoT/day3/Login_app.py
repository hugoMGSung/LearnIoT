import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QGridLayout,
                               QPushButton, QHBoxLayout, QVBoxLayout)
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt

import Login_app_rc

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = QWidget()
    
    lblId = QLabel('&Id : ')
    lblId.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
    lblPw = QLabel('&Password : ')
    
    edtId = QLineEdit()
    edtPw = QLineEdit()
    edtPw.setEchoMode(QLineEdit.Password)
    
    lblId.setBuddy(edtId)
    lblPw.setBuddy(edtPw)
    
    btnOk = QPushButton('&Ok')
    btnOk.setIcon(QIcon(':/images/ok_icon.png'))
    
    layout1 = QGridLayout()
    layout1.addWidget(lblId, 0, 0)
    layout1.addWidget(edtId, 0, 1)
    layout1.addWidget(lblPw, 1, 0)
    layout1.addWidget(edtPw, 1, 1)

    layout2 = QHBoxLayout()
    layout2.addStretch()
    layout2.addWidget(btnOk)

    mainLayout = QVBoxLayout()
    mainLayout.addLayout(layout1)
    mainLayout.addLayout(layout2)

    login.setLayout(mainLayout)
    login.setWindowTitle('Log in')
    login.setWindowIcon(QIcon(":/images/ok_icon.png"))  # 

    btnOk.clicked.connect(app.quit)

    login.show()
    app.exec_()  