# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nukeTerminal_UI.ui',
# licensing of 'nukeTerminal_UI.ui' applies.
#
# Created: Mon Oct 18 19:23:27 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(992, 479)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.render_pushButton = QtWidgets.QPushButton(Form)
        self.render_pushButton.setObjectName("render_pushButton")
        self.horizontalLayout.addWidget(self.render_pushButton)
        self.stop_pushButton = QtWidgets.QPushButton(Form)
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.horizontalLayout.addWidget(self.stop_pushButton)
        self.clear_pushButton = QtWidgets.QPushButton(Form)
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.horizontalLayout.addWidget(self.clear_pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.write_node_listWidget = QtWidgets.QListWidget(Form)
        self.write_node_listWidget.setMaximumSize(QtCore.QSize(350, 16777215))
        self.write_node_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.write_node_listWidget.setObjectName("write_node_listWidget")
        self.gridLayout.addWidget(self.write_node_listWidget, 1, 0, 1, 1)
        self.nuke_file_listWidget = QtWidgets.QListWidget(Form)
        self.nuke_file_listWidget.setMaximumSize(QtCore.QSize(350, 16777215))
        self.nuke_file_listWidget.setAcceptDrops(True)
        self.nuke_file_listWidget.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.nuke_file_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.nuke_file_listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.nuke_file_listWidget.setObjectName("nuke_file_listWidget")
        self.gridLayout.addWidget(self.nuke_file_listWidget, 0, 0, 1, 1)
        self.terminal_plainTextEdit = QtWidgets.QTextEdit(Form)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.terminal_plainTextEdit.setFont(font)
        self.terminal_plainTextEdit.setAcceptDrops(False)
        self.terminal_plainTextEdit.setStyleSheet("background-color: rgb(163, 163, 163);\n"
"color: rgb(7, 7, 7);")
        self.terminal_plainTextEdit.setReadOnly(False)
        self.terminal_plainTextEdit.setObjectName("terminal_plainTextEdit")
        self.gridLayout.addWidget(self.terminal_plainTextEdit, 0, 1, 2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nuke_exec_lineEdit = QtWidgets.QLineEdit(Form)
        self.nuke_exec_lineEdit.setObjectName("nuke_exec_lineEdit")
        self.horizontalLayout_2.addWidget(self.nuke_exec_lineEdit)
        self.browse_pushButton = QtWidgets.QPushButton(Form)
        self.browse_pushButton.setObjectName("browse_pushButton")
        self.horizontalLayout_2.addWidget(self.browse_pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.render_pushButton.setText(QtWidgets.QApplication.translate("Form", "Render", None, -1))
        self.stop_pushButton.setText(QtWidgets.QApplication.translate("Form", "Stop", None, -1))
        self.clear_pushButton.setText(QtWidgets.QApplication.translate("Form", "Clear", None, -1))
        self.browse_pushButton.setText(QtWidgets.QApplication.translate("Form", "Browse", None, -1))

