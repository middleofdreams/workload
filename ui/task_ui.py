# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task.ui'
#
# Created: Thu Nov 13 14:00:06 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(626, 542)
        font = QtGui.QFont()
        font.setFamily("monofur")
        Dialog.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.priorityText = QtGui.QLabel(self.groupBox_2)
        self.priorityText.setObjectName("priorityText")
        self.gridLayout.addWidget(self.priorityText, 1, 5, 1, 1)
        self.closeDate = QtGui.QLabel(self.groupBox_2)
        self.closeDate.setText("")
        self.closeDate.setObjectName("closeDate")
        self.gridLayout.addWidget(self.closeDate, 0, 4, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.priority = QtGui.QSpinBox(self.groupBox_2)
        self.priority.setMinimumSize(QtCore.QSize(20, 0))
        self.priority.setMaximumSize(QtCore.QSize(35, 16777215))
        self.priority.setMaximum(5)
        self.priority.setObjectName("priority")
        self.gridLayout.addWidget(self.priority, 1, 4, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 6, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dueOn = QtGui.QCheckBox(self.groupBox_2)
        self.dueOn.setText("")
        self.dueOn.setObjectName("dueOn")
        self.horizontalLayout_4.addWidget(self.dueOn)
        self.dueDate = QtGui.QDateTimeEdit(self.groupBox_2)
        self.dueDate.setEnabled(False)
        self.dueDate.setMinimumSize(QtCore.QSize(100, 0))
        self.dueDate.setCalendarPopup(True)
        self.dueDate.setObjectName("dueDate")
        self.horizontalLayout_4.addWidget(self.dueDate)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.createDate = QtGui.QLabel(self.groupBox_2)
        self.createDate.setMinimumSize(QtCore.QSize(150, 0))
        self.createDate.setMaximumSize(QtCore.QSize(200, 16777215))
        self.createDate.setText("")
        self.createDate.setObjectName("createDate")
        self.gridLayout.addWidget(self.createDate, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.taskName = QtGui.QLineEdit(Dialog)
        self.taskName.setObjectName("taskName")
        self.gridLayout_3.addWidget(self.taskName, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setMinimumSize(QtCore.QSize(0, 22))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 39))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtGui.QGridLayout(self.frame)
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_4 = QtGui.QPushButton(self.frame)
        self.pushButton_4.setMaximumSize(QtCore.QSize(55, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_4.addWidget(self.pushButton_4, 0, 4, 1, 1)
        self.fontComboBox = QtGui.QComboBox(self.frame)
        self.fontComboBox.setMinimumSize(QtCore.QSize(120, 0))
        self.fontComboBox.setObjectName("fontComboBox")
        self.gridLayout_4.addWidget(self.fontComboBox, 0, 8, 1, 1)
        self.fontSize = QtGui.QSpinBox(self.frame)
        self.fontSize.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.fontSize.setMinimum(8)
        self.fontSize.setMaximum(72)
        self.fontSize.setProperty("value", 10)
        self.fontSize.setObjectName("fontSize")
        self.gridLayout_4.addWidget(self.fontSize, 0, 9, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editorBGcolor = QtGui.QPushButton(self.frame)
        self.editorBGcolor.setMaximumSize(QtCore.QSize(60, 20))
        self.editorBGcolor.setCheckable(False)
        self.editorBGcolor.setObjectName("editorBGcolor")
        self.horizontalLayout.addWidget(self.editorBGcolor)
        self.currentBGcolor = QtGui.QPushButton(self.frame)
        self.currentBGcolor.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.currentBGcolor.setFont(font)
        self.currentBGcolor.setAutoFillBackground(True)
        self.currentBGcolor.setText("")
        self.currentBGcolor.setCheckable(False)
        self.currentBGcolor.setDefault(False)
        self.currentBGcolor.setFlat(False)
        self.currentBGcolor.setObjectName("currentBGcolor")
        self.horizontalLayout.addWidget(self.currentBGcolor)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 4, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.editorTextColor = QtGui.QPushButton(self.frame)
        self.editorTextColor.setMaximumSize(QtCore.QSize(80, 20))
        self.editorTextColor.setObjectName("editorTextColor")
        self.horizontalLayout_2.addWidget(self.editorTextColor)
        self.currentTextColor = QtGui.QPushButton(self.frame)
        self.currentTextColor.setMaximumSize(QtCore.QSize(20, 16777215))
        self.currentTextColor.setAutoFillBackground(True)
        self.currentTextColor.setText("")
        self.currentTextColor.setFlat(False)
        self.currentTextColor.setObjectName("currentTextColor")
        self.horizontalLayout_2.addWidget(self.currentTextColor)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 5, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 10, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.editorBold = QtGui.QPushButton(self.frame)
        self.editorBold.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setWeight(75)
        font.setBold(True)
        self.editorBold.setFont(font)
        self.editorBold.setFlat(False)
        self.editorBold.setObjectName("editorBold")
        self.horizontalLayout_3.addWidget(self.editorBold)
        self.editorItalic = QtGui.QPushButton(self.frame)
        self.editorItalic.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setItalic(True)
        self.editorItalic.setFont(font)
        self.editorItalic.setObjectName("editorItalic")
        self.horizontalLayout_3.addWidget(self.editorItalic)
        self.editorUnderline = QtGui.QPushButton(self.frame)
        self.editorUnderline.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setUnderline(True)
        self.editorUnderline.setFont(font)
        self.editorUnderline.setObjectName("editorUnderline")
        self.horizontalLayout_3.addWidget(self.editorUnderline)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.editorResetColor = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editorResetColor.sizePolicy().hasHeightForWidth())
        self.editorResetColor.setSizePolicy(sizePolicy)
        self.editorResetColor.setMaximumSize(QtCore.QSize(40, 16777215))
        self.editorResetColor.setObjectName("editorResetColor")
        self.gridLayout_4.addWidget(self.editorResetColor, 0, 6, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.taskDescription = QtGui.QTextBrowser(Dialog)
        self.taskDescription.setMinimumSize(QtCore.QSize(100, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.taskDescription.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.taskDescription.setFont(font)
        self.taskDescription.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.taskDescription.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.taskDescription.setAutoFormatting(QtGui.QTextEdit.AutoNone)
        self.taskDescription.setUndoRedoEnabled(True)
        self.taskDescription.setReadOnly(False)
        self.taskDescription.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'monofur\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.taskDescription.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.taskDescription.setOpenExternalLinks(False)
        self.taskDescription.setOpenLinks(False)
        self.taskDescription.setObjectName("taskDescription")
        self.verticalLayout.addWidget(self.taskDescription)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setMaximumSize(QtCore.QSize(16777215, 22))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.priorityText.setText(QtGui.QApplication.translate("Dialog", "Now", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Due", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Priority", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Created:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Closed:", None, QtGui.QApplication.UnicodeUTF8))
        self.dueDate.setSpecialValueText(QtGui.QApplication.translate("Dialog", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Task Name: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Task Description", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Dialog", "bg color", None, QtGui.QApplication.UnicodeUTF8))
        self.editorBGcolor.setText(QtGui.QApplication.translate("Dialog", "BGcolor", None, QtGui.QApplication.UnicodeUTF8))
        self.editorTextColor.setText(QtGui.QApplication.translate("Dialog", "Text color", None, QtGui.QApplication.UnicodeUTF8))
        self.editorBold.setText(QtGui.QApplication.translate("Dialog", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.editorItalic.setText(QtGui.QApplication.translate("Dialog", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.editorUnderline.setText(QtGui.QApplication.translate("Dialog", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.editorResetColor.setText(QtGui.QApplication.translate("Dialog", "reset", None, QtGui.QApplication.UnicodeUTF8))

