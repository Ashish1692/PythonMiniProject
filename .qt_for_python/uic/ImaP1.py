# Form implementation generated from reading ui file 'c:\Users\DELL\Downloads\imap-Image-to-PDF-Converter-Application-For-Windows-master\ImaP1.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 500)
        MainWindow.setMinimumSize(QtCore.QSize(978, 500))
        MainWindow.setMaximumSize(QtCore.QSize(978, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Downloads\\imap-Image-to-PDF-Converter-Application-For-Windows-master\\icons/main_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(963, 461))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.tabWidget.setToolTip("")
        self.tabWidget.setToolTipDuration(291)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(680, 120, 51, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_up = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_up.setMaximumSize(QtCore.QSize(57, 50))
        self.pushButton_up.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_up.setStyleSheet("\n"
"QPushButton::hover{\n"
"    background-color: rgb(35,35,35);\n"
"};\n"
"\n"
"\n"
"background-color: rgb(3, 30, 35);\n"
"border-style: solid;\n"
"border-color: rgb(5,10,28);\n"
"border-width: 1px;\n"
"border-radius: 20px;")
        self.pushButton_up.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Downloads\\imap-Image-to-PDF-Converter-Application-For-Windows-master\\icons/collapse_arrow_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_up.setIcon(icon1)
        self.pushButton_up.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_up.setObjectName("pushButton_up")
        self.verticalLayout.addWidget(self.pushButton_up)
        self.pushButton_down = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_down.setMaximumSize(QtCore.QSize(57, 50))
        self.pushButton_down.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_down.setStyleSheet("\n"
"QPushButton::hover{\n"
"    background-color: rgb(35,35,35);\n"
"};\n"
"\n"
"\n"
"background-color: rgb(3, 30, 35);\n"
"border-style: solid;\n"
"border-color: rgb(5,10,28);\n"
"border-width: 1px;\n"
"border-radius: 20px;")
        self.pushButton_down.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Downloads\\imap-Image-to-PDF-Converter-Application-For-Windows-master\\icons/expand_arrow_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_down.setIcon(icon2)
        self.pushButton_down.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_down.setObjectName("pushButton_down")
        self.verticalLayout.addWidget(self.pushButton_down)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 0, 661, 361))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 3, 0, 0)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(45, 6, 0, 6)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 37))
        self.pushButton.setMaximumSize(QtCore.QSize(122, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("\n"
"\n"
"QPushButton::hover{\n"
"    \n"
"    background-color: rgb(40,40,40);\n"
"    border: 1px solid rgb(3,3,3);\n"
"    border-radius: 6px;\n"
"    \n"
"};\n"
"\n"
"\n"
"background-color: rgb(0, 35, 107);\n"
"border: 1px solid rgb(5,5,5);\n"
"border-radius: 6px;\n"
"\n"
"\n"
"\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Downloads\\imap-Image-to-PDF-Converter-Application-For-Windows-master\\icons/Add Folder_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_add = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_add.setMinimumSize(QtCore.QSize(80, 37))
        self.pushButton_add.setMaximumSize(QtCore.QSize(122, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_add.setStyleSheet("\n"
"\n"
"QPushButton::hover{\n"
"    \n"
"    background-color: rgb(40,40,40);\n"
"    border: 1px solid rgb(3,3,3);\n"
"    border-radius: 6px;\n"
"    \n"
"};\n"
"\n"
"\n"
"background-color: rgb(0, 102, 0);\n"
"border: 1px solid rgb(5,5,5);\n"
"border-radius: 6px;\n"
"\n"
"\n"
"\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Downloads\\imap-Image-to-PDF-Converter-Application-For-Windows-master\\icons/plus_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_add.setIcon(icon4)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout.addWidget(self.pushButton_add)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.layoutWidget1)
        self.listWidget.setStyleSheet("border: 2px solid rgb(0,20,32);")
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 2)
        self.layoutWidget2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(430, 370, 260, 40))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_7.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_7.setSpacing(14)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_remove = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_remove.setMinimumSize(QtCore.QSize(103, 37))
        self.pushButton_remove.setMaximumSize(QtCore.QSize(122, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_remove.setFont(font)
        self.pushButton_remove.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_remove.setStyleSheet("\n"
"QPushButton::hover{\n"
"    \n"
"    background-color: rgb(40,40,40);\n"
"    border-color: rgb(3,3,3);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius:5px;\n"
"\n"
"};\n"
"\n"
"\n"
"background-color: rgb(181, 0, 0);\n"
"border-color: rgb(5,5,5);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius:4px;\n"
"\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Downloads\\imap-Image-to-PDF-Converter-Application-For-Windows-master\\icons/minus_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_remove.setIcon(icon5)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.horizontalLayout_7.addWidget(self.pushButton_remove)
        self.pushButton_clear = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_clear.setMinimumSize(QtCore.QSize(103, 37))
        self.pushButton_clear.setMaximumSize(QtCore.QSize(122, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_clear.setStyleSheet("\n"
"QPushButton::hover{\n"
"    \n"
"    background-color: rgb(40,40,40);\n"
"    border-color: rgb(3,3,3);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius:5px;\n"
"\n"
"};\n"
"\n"
"\n"
"background-color: rgb(181, 0, 0);\n"
"border-color: rgb(5,5,5);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius:4px;\n"
"\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Downloads\\imap-Image-to-PDF-Converter-Application-For-Windows-master\\icons/clear_symbol_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_clear.setIcon(icon6)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout_7.addWidget(self.pushButton_clear)
        self.layoutWidget3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget3.setGeometry(QtCore.QRect(750, 90, 192, 261))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_make_pdf = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_make_pdf.setMinimumSize(QtCore.QSize(190, 43))
        self.pushButton_make_pdf.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_make_pdf.setFont(font)
        self.pushButton_make_pdf.setStyleSheet("\n"
"QPushButton::hover{\n"
"    \n"
"    background-color: rgb(90, 90, 90);\n"
"};\n"
"\n"
"\n"
"\n"
"background-color: rgb(129, 53, 129);\n"
"border-color: rgb(1, 1, 1);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius:5px;\n"
"\n"
"")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Downloads\\imap-Image-to-PDF-Converter-Application-For-Windows-master\\icons/export_pdf_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_make_pdf.setIcon(icon7)
        self.pushButton_make_pdf.setObjectName("pushButton_make_pdf")
        self.verticalLayout_2.addWidget(self.pushButton_make_pdf)
        self.pushButton_make_pdf_2 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_make_pdf_2.setMinimumSize(QtCore.QSize(190, 43))
        self.pushButton_make_pdf_2.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_make_pdf_2.setFont(font)
        self.pushButton_make_pdf_2.setStyleSheet("\n"
"QPushButton::hover{\n"
"    \n"
"    background-color: rgb(90, 90, 90);\n"
"};\n"
"\n"
"\n"
"background-color: rgb(52, 52, 111);\n"
"border-color: rgb(1, 1, 1);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius:5px;\n"
"\n"
"")
        self.pushButton_make_pdf_2.setIcon(icon7)
        self.pushButton_make_pdf_2.setObjectName("pushButton_make_pdf_2")
        self.verticalLayout_2.addWidget(self.pushButton_make_pdf_2)
        self.pushButton_make_pdf_3 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_make_pdf_3.setMinimumSize(QtCore.QSize(190, 43))
        self.pushButton_make_pdf_3.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_make_pdf_3.setFont(font)
        self.pushButton_make_pdf_3.setStyleSheet("\n"
"QPushButton::hover{\n"
"    \n"
"    background-color: rgb(90, 90, 90);\n"
"};\n"
"\n"
"\n"
"background-color: rgb(173, 0, 86);\n"
"border-color: rgb(1, 1, 1);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius:5px;\n"
"\n"
"")
        self.pushButton_make_pdf_3.setIcon(icon7)
        self.pushButton_make_pdf_3.setObjectName("pushButton_make_pdf_3")
        self.verticalLayout_2.addWidget(self.pushButton_make_pdf_3)
        self.pushButton_make_pdf_4 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_make_pdf_4.setMinimumSize(QtCore.QSize(190, 43))
        self.pushButton_make_pdf_4.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_make_pdf_4.setFont(font)
        self.pushButton_make_pdf_4.setStyleSheet("\n"
"QPushButton::hover{\n"
"    \n"
"    background-color: rgb(90, 90, 90);\n"
"};\n"
"\n"
"\n"
"background-color: rgb(48, 0, 144);\n"
"border-color: rgb(1, 1, 1);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius:5px;\n"
"\n"
"")
        self.pushButton_make_pdf_4.setIcon(icon7)
        self.pushButton_make_pdf_4.setObjectName("pushButton_make_pdf_4")
        self.verticalLayout_2.addWidget(self.pushButton_make_pdf_4)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Downloads\\imap-Image-to-PDF-Converter-Application-For-Windows-master\\icons/top_menu_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.tab, icon8, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setOpenExternalLinks(True)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setMinimumSize(QtCore.QSize(81, 16))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setMinimumSize(QtCore.QSize(191, 16))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(283)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setMinimumSize(QtCore.QSize(81, 0))
        self.label_4.setMaximumSize(QtCore.QSize(188, 20))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setMinimumSize(QtCore.QSize(191, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 4, 0, 1, 1)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Downloads\\imap-Image-to-PDF-Converter-Application-For-Windows-master\\icons/info_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.tab_2, icon9, "")
        self.horizontalLayout_6.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File Format Converter"))
        self.pushButton_up.setToolTip(_translate("MainWindow", "Up"))
        self.pushButton_down.setToolTip(_translate("MainWindow", "Down"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">List Of Files :</span></p></body></html>"))
        self.pushButton.setToolTip(_translate("MainWindow", "Add New Folder"))
        self.pushButton.setText(_translate("MainWindow", " Add Folder"))
        self.pushButton_add.setToolTip(_translate("MainWindow", "Add New File"))
        self.pushButton_add.setText(_translate("MainWindow", " Add File"))
        self.listWidget.setToolTip(_translate("MainWindow", "Items"))
        self.pushButton_remove.setToolTip(_translate("MainWindow", "Remove Selected"))
        self.pushButton_remove.setText(_translate("MainWindow", " Remove"))
        self.pushButton_clear.setToolTip(_translate("MainWindow", "Clear All"))
        self.pushButton_clear.setText(_translate("MainWindow", " Clear All"))
        self.pushButton_make_pdf.setText(_translate("MainWindow", " Make PDF"))
        self.pushButton_make_pdf_2.setText(_translate("MainWindow", " Make PDF"))
        self.pushButton_make_pdf_3.setText(_translate("MainWindow", " Make PDF"))
        self.pushButton_make_pdf_4.setText(_translate("MainWindow", " Make PDF"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Home"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><strong>Developers:</strong></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Rohan Godbole, Ashish Moghe, Chinmay Puranik, Soham Pathre</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Icons Credit:</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://icons8.com\"><span style=\" font-size:9pt; text-decoration: underline; color:#0055ff;\">Icons8.com</span></a></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Contact Info:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">&lt;emails&gt;</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Technologies Used:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Python 3.10, PyQt5, PILLOW (PIL).</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">License</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Copyright (c) 2022</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the &quot;Software&quot;), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">The above copyright notice and this permission notice shall be included in all</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">copies or substantial portions of the Software.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "About"))
