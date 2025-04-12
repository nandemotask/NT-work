# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NandemoEmailzTgHGO.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(570, 430)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 141, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.EmailType_comboBox = QComboBox(self.centralwidget)
        self.EmailType_comboBox.addItem("")
        self.EmailType_comboBox.addItem("")
        self.EmailType_comboBox.setObjectName(u"EmailType_comboBox")
        self.EmailType_comboBox.setGeometry(QRect(10, 70, 141, 24))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 71, 16))
        self.Content_textEdit = QTextEdit(self.centralwidget)
        self.Content_textEdit.setObjectName(u"Content_textEdit")
        self.Content_textEdit.setGeometry(QRect(230, 50, 331, 331))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 30, 81, 16))
        self.AccRecSetting_BT = QPushButton(self.centralwidget)
        self.AccRecSetting_BT.setObjectName(u"AccRecSetting_BT")
        self.AccRecSetting_BT.setGeometry(QRect(10, 120, 191, 24))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 100, 131, 16))
        self.Att_listWidget = QListWidget(self.centralwidget)
        self.Att_listWidget.setObjectName(u"Att_listWidget")
        self.Att_listWidget.setGeometry(QRect(10, 300, 211, 81))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 280, 71, 16))
        self.Att_groupBox = QGroupBox(self.centralwidget)
        self.Att_groupBox.setObjectName(u"Att_groupBox")
        self.Att_groupBox.setGeometry(QRect(10, 150, 211, 91))
        self.Directory_radioButton = QRadioButton(self.Att_groupBox)
        self.Directory_radioButton.setObjectName(u"Directory_radioButton")
        self.Directory_radioButton.setGeometry(QRect(10, 20, 94, 20))
        self.File_radioButton = QRadioButton(self.Att_groupBox)
        self.File_radioButton.setObjectName(u"File_radioButton")
        self.File_radioButton.setGeometry(QRect(10, 40, 94, 20))
        self.Folder_radioButton = QRadioButton(self.Att_groupBox)
        self.Folder_radioButton.setObjectName(u"Folder_radioButton")
        self.Folder_radioButton.setGeometry(QRect(10, 60, 94, 20))
        self.Compressed_checkBox = QCheckBox(self.centralwidget)
        self.Compressed_checkBox.setObjectName(u"Compressed_checkBox")
        self.Compressed_checkBox.setGeometry(QRect(130, 240, 91, 20))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(460, 390, 91, 31))
        self.Save_BT = QPushButton(self.centralwidget)
        self.Save_BT.setObjectName(u"Save_BT")
        self.Save_BT.setGeometry(QRect(364, 390, 91, 31))
        self.AttFind_BT = QPushButton(self.centralwidget)
        self.AttFind_BT.setObjectName(u"AttFind_BT")
        self.AttFind_BT.setGeometry(QRect(10, 240, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Nandemo Email", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u".Nandemo Email", None))
        self.EmailType_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Gmail", None))
        self.EmailType_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Naver", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u".Email Type", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u".Mail Content", None))
        self.AccRecSetting_BT.setText(QCoreApplication.translate("MainWindow", u"Account and Recipient Settings", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u".Account and Recipient", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u".Attachment", None))
        self.Att_groupBox.setTitle(QCoreApplication.translate("MainWindow", u".Attachment Settings", None))
        self.Directory_radioButton.setText(QCoreApplication.translate("MainWindow", u"Directory", None))
        self.File_radioButton.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.Folder_radioButton.setText(QCoreApplication.translate("MainWindow", u"Folder", None))
        self.Compressed_checkBox.setText(QCoreApplication.translate("MainWindow", u"Compressed", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.Save_BT.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.AttFind_BT.setText(QCoreApplication.translate("MainWindow", u"Find", None))
    # retranslateUi

