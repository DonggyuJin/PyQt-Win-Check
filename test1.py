# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win10.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1012, 743)
        Dialog.setSizeGripEnabled(False)
        self.btn_01 = QtWidgets.QPushButton(Dialog)
        self.btn_01.setGeometry(QtCore.QRect(480, 210, 161, 91))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_01.setFont(font)
        self.btn_01.setObjectName("btn_01")
        self.btn_04 = QtWidgets.QPushButton(Dialog)
        self.btn_04.setGeometry(QtCore.QRect(480, 310, 161, 91))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_04.setFont(font)
        self.btn_04.setObjectName("btn_04")
        self.btn_02 = QtWidgets.QPushButton(Dialog)
        self.btn_02.setGeometry(QtCore.QRect(650, 210, 161, 91))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_02.setFont(font)
        self.btn_02.setObjectName("btn_02")
        self.btn_05 = QtWidgets.QPushButton(Dialog)
        self.btn_05.setGeometry(QtCore.QRect(650, 310, 161, 91))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_05.setFont(font)
        self.btn_05.setObjectName("btn_05")
        self.btn_03 = QtWidgets.QPushButton(Dialog)
        self.btn_03.setGeometry(QtCore.QRect(820, 210, 161, 91))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_03.setFont(font)
        self.btn_03.setObjectName("btn_03")
        self.btn_06 = QtWidgets.QPushButton(Dialog)
        self.btn_06.setGeometry(QtCore.QRect(820, 310, 161, 91))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_06.setFont(font)
        self.btn_06.setObjectName("btn_06")
        self.lbl_copyright = QtWidgets.QLabel(Dialog)
        self.lbl_copyright.setGeometry(QtCore.QRect(750, 720, 261, 16))
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lbl_copyright.setFont(font)
        self.lbl_copyright.setObjectName("lbl_copyright")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(480, 180, 501, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(470, 510, 511, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lbl_picture = QtWidgets.QLabel(Dialog)
        self.lbl_picture.setGeometry(QtCore.QRect(830, 20, 151, 151))
        self.lbl_picture.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_picture.setObjectName("lbl_picture")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(470, 670, 511, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lbl_main = QtWidgets.QLabel(Dialog)
        self.lbl_main.setGeometry(QtCore.QRect(30, 20, 791, 161))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Bold")
        font.setPointSize(36)
        self.lbl_main.setFont(font)
        self.lbl_main.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_main.setObjectName("lbl_main")
        self.btn_07 = QtWidgets.QPushButton(Dialog)
        self.btn_07.setGeometry(QtCore.QRect(480, 410, 161, 91))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_07.setFont(font)
        self.btn_07.setObjectName("btn_07")
        self.btn_08 = QtWidgets.QPushButton(Dialog)
        self.btn_08.setGeometry(QtCore.QRect(650, 410, 161, 91))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_08.setFont(font)
        self.btn_08.setObjectName("btn_08")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(330, 700, 331, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.lbl_date = QtWidgets.QLabel(Dialog)
        self.lbl_date.setGeometry(QtCore.QRect(10, 720, 141, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.lbl_date.setFont(font)
        self.lbl_date.setObjectName("lbl_date")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(760, 550, 221, 111))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.textBrowser.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 247, 255);\n"
"font: 9pt \"나눔바른고딕\";")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.btn_09 = QtWidgets.QPushButton(Dialog)
        self.btn_09.setGeometry(QtCore.QRect(820, 410, 161, 91))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_09.setFont(font)
        self.btn_09.setObjectName("btn_09")
        self.text_result = QtWidgets.QTextEdit(Dialog)
        self.text_result.setGeometry(QtCore.QRect(30, 190, 431, 491))
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕")
        self.text_result.setFont(font)
        self.text_result.setReadOnly(True)
        self.text_result.setObjectName("text_result")
        self.btn_11 = QtWidgets.QPushButton(Dialog)
        self.btn_11.setGeometry(QtCore.QRect(620, 560, 131, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.btn_11.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("나눔명조")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_11.setFont(font)
        self.btn_11.setAutoFillBackground(False)
        self.btn_11.setAutoDefault(False)
        self.btn_11.setDefault(False)
        self.btn_11.setFlat(True)
        self.btn_11.setObjectName("btn_11")
        self.lbl_copyright_2 = QtWidgets.QLabel(Dialog)
        self.lbl_copyright_2.setGeometry(QtCore.QRect(610, 640, 151, 21))
        font = QtGui.QFont()
        font.setFamily("나눔손글씨 펜")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_copyright_2.setFont(font)
        self.lbl_copyright_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_copyright_2.setScaledContents(True)
        self.lbl_copyright_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_copyright_2.setObjectName("lbl_copyright_2")
        self.btn_10 = QtWidgets.QPushButton(Dialog)
        self.btn_10.setGeometry(QtCore.QRect(480, 560, 131, 71))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_10.setFont(font)
        self.btn_10.setObjectName("btn_10")
        self.lbl_copyright_3 = QtWidgets.QLabel(Dialog)
        self.lbl_copyright_3.setGeometry(QtCore.QRect(480, 640, 121, 21))
        font = QtGui.QFont()
        font.setFamily("나눔손글씨 펜")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_copyright_3.setFont(font)
        self.lbl_copyright_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_copyright_3.setScaledContents(True)
        self.lbl_copyright_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_copyright_3.setObjectName("lbl_copyright_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_01.setText(_translate("Dialog", "01. Administrator\n"
"계정 관리"))
        self.btn_04.setText(_translate("Dialog", "04. 암호\n"
"정책 설정"))
        self.btn_02.setText(_translate("Dialog", "02. Guest \n"
"계정 관리"))
        self.btn_05.setText(_translate("Dialog", "05. UAC 설정"))
        self.btn_03.setText(_translate("Dialog", "03. 계정 잠금 \n"
"정책 설정"))
        self.btn_06.setText(_translate("Dialog", "06. CMD 파일\n"
"권한 설정"))
        self.lbl_copyright.setText(_translate("Dialog", "© DonggyuJin. all rights reserved."))
        self.lbl_picture.setText(_translate("Dialog", "logo"))
        self.lbl_main.setText(_translate("Dialog", "Automation tools v0.1"))
        self.btn_07.setText(_translate("Dialog", "07. 사용자 \n"
"디렉토리 접근제한"))
        self.btn_08.setText(_translate("Dialog", "08. 하드디스크\n"
"기본 공유 제거"))
        self.lbl_date.setText(_translate("Dialog", "Date"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'나눔바른고딕\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'NanumGothic,serif\'; font-size:10pt;\">과 목 명 : 침입탐지 및 차단</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'NanumGothic,serif\'; font-size:10pt;\">교 수 명 : 김동원 교수님</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'NanumGothic,serif\'; font-size:10pt;\">학     과 : 사이버보안공학과 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'NanumGothic,serif\'; font-size:10pt;\">학     번 : 18501040</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'NanumGothic,serif\'; font-size:10pt;\">이     름 : 진동규</span></p></body></html>"))
        self.btn_09.setText(_translate("Dialog", "09. SAM 파일\n"
"접근 통제"))
        self.btn_11.setText(_translate("Dialog", "INITIAL RUN"))
        self.lbl_copyright_2.setText(_translate("Dialog", "↑ 최초 실행 시 한번만 눌러주세요 ↑"))
        self.btn_10.setText(_translate("Dialog", "10. 통합 점검"))
        self.lbl_copyright_3.setText(_translate("Dialog", "↑ 통합 점검 시 눌러주세요 ↑"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())