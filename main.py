import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

# UI파일 연결 (단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.)
form_class = uic.loadUiType("win10.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(1481, 846)
        self.center()
        self.setWindowTitle("Automation tools win10")
        self.setWindowIcon(QIcon('src/10.png'))

        self.btn_17.setStyleSheet("""
                    background-color: transparent;
                    border: false;
        """)

        self.date = QDate.currentDate()

        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("src/logo.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(150)
        self.lbl_picture.setPixmap(self.qPixmapFileVar)

        self.lbl_date.setText(self.date.toString('yyyy.MM.dd'))

        self.setStyleSheet(""" 
        
                QPushButton {
                    background-color: #f5f5f5;
                    border: 1px solid black;
                    border-radius: 3px;
                    }
                    
                QPushButton::pressed {
                    background-color : #d7f7e0;
                }
        
                QProgressBar {
                    border-style: solid;
                    border-color: #ff4f72;
                    border-radius: 4px;
                    border-width: 2px;
                    text-align: center;
                }
                
                QProgressBar::chunk { 
                    width: 3px;
                    background-color: #47ff47;
                    margin: 2px;
                }
                
        """)

        self.text = ''

        # Push Button 기능 connect
        self.btn_01.clicked.connect(self.button1Function)
        self.btn_02.clicked.connect(self.button2Function)
        self.btn_03.clicked.connect(self.button3Function)
        self.btn_04.clicked.connect(self.button4Function)
        self.btn_05.clicked.connect(self.button5Function)
        self.btn_06.clicked.connect(self.button6Function)
        self.btn_07.clicked.connect(self.button7Function)
        self.btn_08.clicked.connect(self.button8Function)
        self.btn_09.clicked.connect(self.button9Function)
        self.btn_10.clicked.connect(self.button10Function)
        self.btn_11.clicked.connect(self.button11Function)
        self.btn_12.clicked.connect(self.button12Function)
        self.btn_13.clicked.connect(self.button13Function)
        self.btn_14.clicked.connect(self.button14Function)
        self.btn_15.clicked.connect(self.button15Function)
        self.btn_16.clicked.connect(self.button16Function)
        self.btn_17.clicked.connect(self.button17Function)

    def button1Function(self):
        self.progressInit()
        os.startfile('c:/win/01. Administrator_계정관리.bat')
        self.progressIng()

        self.text = 'c:/win/01_Administrator_계정관리_점검결과.txt'
        self.textReview()

    def button2Function(self):
        self.progressInit()
        os.startfile('c:/win/02. Guest_계정관리.bat')
        self.progressIng()

        self.text = 'c:/win/02_Guest_계정관리_점검결과.txt'
        self.textReview()

    def button3Function(self):
        self.progressInit()
        os.startfile('c:/win/03. 계정잠금정책설정.bat')
        self.progressIng()

        self.text = 'c:/win/03_계정잠금정책설정_점검결과.txt'
        self.textReview()

    def button4Function(self):
        self.progressInit()
        os.startfile('c:/win/04. 암호정책설정.bat')
        self.progressIng()

        self.text = 'c:/win/04_암호정책설정_점검결과.txt'
        self.textReview()

    def button5Function(self):
        self.progressInit()
        os.startfile('c:/win/05. UAC설정.bat')
        self.progressIng()

        self.text = 'c:/win/05_UAC설정_점검결과.txt'
        self.textReview()

    def button6Function(self):
        self.progressInit()
        os.startfile('c:/win/06. CMD_파일권한설정.bat')
        self.progressIng()

        self.text = 'c:/win/06_CMD_파일권한설정_점검결과.txt'
        self.textReview()

    def button7Function(self):
        self.progressInit()
        os.startfile('c:/win/07. 사용자디렉터리접근제한.bat')
        self.progressIng()

        self.text = 'c:/win/07_사용자디렉터리접근제한_점검결과.txt'
        self.textReview()

    def button8Function(self):
        self.progressInit()
        os.startfile('c:/win/08. 하드디스크기본공유제거.bat')
        self.progressIng()

        self.text = 'c:/win/08_하드디스크기본공유제거_점검결과.txt'
        self.textReview()

    def button9Function(self):
        self.progressInit()
        os.startfile('c:/win/09. SAM_파일접근통제.bat')
        self.progressIng()

        self.text = 'c:/win/09_SAM_파일접근통제_점검결과.txt'
        self.textReview()

    def button10Function(self):
        self.progressInit()
        os.startfile('c:/win/10.최신_서비스팩_적용.bat')
        self.progressIng()

        self.text = 'c:/win/10_최신_서비스팩_적용_점검결과.txt'
        self.textReview()

    def button11Function(self):
        self.progressInit()
        os.startfile('c:/win/11.공유권한_및_사용자그룹_설정.bat')
        self.progressIng()

        self.text = 'c:/win/11_공유권한_및_사용자그룹_설정_점검결과.txt'
        self.textReview()

    def button12Function(self):
        self.progressInit()
        os.startfile('c:/win/12.로그오프나_워크스테이션_잠김.bat')
        self.progressIng()

        self.text = 'c:/win/12_로그오프나_워크스테이션_잠김_점검결과.txt'
        self.textReview()

    def button13Function(self):
        self.progressInit()
        os.startfile('c:/win/13.이벤트뷰어_설정.bat')
        self.progressIng()

        self.text = 'c:/win/13_이벤트뷰어_설정_점검결과.txt'
        self.textReview()

    def button14Function(self):
        self.progressInit()
        os.startfile('c:/win/14.마지막_로그온_사용자_계정_숨김.bat')
        self.progressIng()

        self.text = 'c:/win/14_마지막_로그온_사용자_계정_숨김_점검결과.txt'
        self.textReview()

    def button15Function(self):
        self.progressInit()
        os.startfile('c:/win/15.로그온하지_않은_사용자_시스템종료_방지.bat')
        self.progressIng()

        self.text = 'c:/win/15_로그온하지_않은_사용자_시스템종료_방지_점검결과.txt'
        self.textReview()

    def button16Function(self):
        self.progressInit()
        os.startfile('c:/win/통합_점검.bat')
        self.progressIng()

        self.text = 'c:/win/통합_점검결과.txt'
        self.textReview()

    def button17Function(self):
        self.progressInit()
        os.startfile('c:/win/Initial run.bat')

    def progressInit(self):
        self.progressBar.setValue(0)

    def progressIng(self):
        self.progressBar.setRange(0, 99)
        for i in range(0, 100):
            self.progressBar.setValue(i)

    def textReview(self):
        self.text_result.clear()
        text = open(self.text).read()
        self.text_result.setText(text)

    def closeEvent(self, event):
        self.deleteLater()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    guiBatch = WindowClass()
    guiBatch.show()
    # 프로그램을 이벤트 루프로 진입
    app.exec_()
