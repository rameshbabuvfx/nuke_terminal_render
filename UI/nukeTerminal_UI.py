# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nukeTerminal_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(992, 479)
        Form.setStyleSheet(u"background-color: rgb(63, 63, 63);")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.render_pushButton = QPushButton(Form)
        self.render_pushButton.setObjectName(u"render_pushButton")
        self.render_pushButton.setMinimumSize(QSize(0, 27))
        font = QFont()
        font.setFamily(u"MS Reference Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.render_pushButton.setFont(font)
        self.render_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.render_pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(114, 108, 163);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(85, 81, 122);\n"
"}")

        self.horizontalLayout.addWidget(self.render_pushButton)

        self.clear_pushButton = QPushButton(Form)
        self.clear_pushButton.setObjectName(u"clear_pushButton")
        self.clear_pushButton.setMinimumSize(QSize(0, 27))
        font1 = QFont()
        font1.setFamily(u"MS Reference Sans Serif")
        font1.setBold(True)
        font1.setWeight(75)
        self.clear_pushButton.setFont(font1)
        self.clear_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(114, 108, 163);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(85, 81, 122);\n"
"}")

        self.horizontalLayout.addWidget(self.clear_pushButton)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.write_node_listWidget = QListWidget(Form)
        self.write_node_listWidget.setObjectName(u"write_node_listWidget")
        self.write_node_listWidget.setMaximumSize(QSize(350, 16777215))
        font2 = QFont()
        font2.setFamily(u"MS Reference Sans Serif")
        font2.setPointSize(7)
        self.write_node_listWidget.setFont(font2)
        self.write_node_listWidget.setStyleSheet(u"QListWidget{\n"
"	selection-background-color: rgb(85, 170, 127);\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(204, 204, 204);\n"
"	border-radius:10px;\n"
"}")
        self.write_node_listWidget.setFrameShape(QFrame.NoFrame)
        self.write_node_listWidget.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout.addWidget(self.write_node_listWidget, 1, 0, 1, 1)

        self.terminal_plainTextEdit = QTextEdit(Form)
        self.terminal_plainTextEdit.setObjectName(u"terminal_plainTextEdit")
        font3 = QFont()
        font3.setFamily(u"MS Reference Sans Serif")
        self.terminal_plainTextEdit.setFont(font3)
        self.terminal_plainTextEdit.setAcceptDrops(False)
        self.terminal_plainTextEdit.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"color: rgb(204, 204, 204);\n"
"border-radius:10px;")
        self.terminal_plainTextEdit.setFrameShape(QFrame.NoFrame)
        self.terminal_plainTextEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.terminal_plainTextEdit, 0, 1, 2, 1)

        self.nuke_file_listWidget = QListWidget(Form)
        self.nuke_file_listWidget.setObjectName(u"nuke_file_listWidget")
        self.nuke_file_listWidget.setMaximumSize(QSize(350, 16777215))
        self.nuke_file_listWidget.setFont(font2)
        self.nuke_file_listWidget.setAcceptDrops(True)
        self.nuke_file_listWidget.setStyleSheet(u"QListWidget{\n"
"	selection-background-color: rgb(85, 170, 127);\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(204, 204, 204);\n"
"	border-radius:10px;\n"
"}")
        self.nuke_file_listWidget.setFrameShape(QFrame.NoFrame)
        self.nuke_file_listWidget.setDragDropMode(QAbstractItemView.DropOnly)
        self.nuke_file_listWidget.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.nuke_file_listWidget.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.gridLayout.addWidget(self.nuke_file_listWidget, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.nuke_exec_lineEdit = QLineEdit(Form)
        self.nuke_exec_lineEdit.setObjectName(u"nuke_exec_lineEdit")
        self.nuke_exec_lineEdit.setMinimumSize(QSize(0, 25))
        self.nuke_exec_lineEdit.setFont(font3)
        self.nuke_exec_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(204, 204, 204);\n"
"	border-radius:5px;\n"
"}")
        self.nuke_exec_lineEdit.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.horizontalLayout_2.addWidget(self.nuke_exec_lineEdit)

        self.browse_pushButton = QPushButton(Form)
        self.browse_pushButton.setObjectName(u"browse_pushButton")
        self.browse_pushButton.setMinimumSize(QSize(100, 25))
        font4 = QFont()
        font4.setFamily(u"MS Reference Sans Serif")
        font4.setPointSize(7)
        font4.setBold(True)
        font4.setWeight(75)
        self.browse_pushButton.setFont(font4)
        self.browse_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.browse_pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(114, 108, 163);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(85, 81, 122);\n"
"}")

        self.horizontalLayout_2.addWidget(self.browse_pushButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.render_pushButton.setText(QCoreApplication.translate("Form", u"Render", None))
        self.clear_pushButton.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.browse_pushButton.setText(QCoreApplication.translate("Form", u"Browse", None))
    # retranslateUi

