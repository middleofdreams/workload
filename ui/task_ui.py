# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task.ui'
#
# Created: Mon Dec  1 14:51:35 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(620, 529)
        font = QtGui.QFont()
        font.setFamily("Serif")
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(15, 6, 15, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(70, 0))
        self.label_4.setMaximumSize(QtCore.QSize(99, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.createDate = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createDate.sizePolicy().hasHeightForWidth())
        self.createDate.setSizePolicy(sizePolicy)
        self.createDate.setMinimumSize(QtCore.QSize(150, 0))
        self.createDate.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.createDate.setText("")
        self.createDate.setObjectName("createDate")
        self.horizontalLayout_6.addWidget(self.createDate)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label_6 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(70, 0))
        self.label_6.setMaximumSize(QtCore.QSize(99, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.closeDate = QtGui.QLabel(Dialog)
        self.closeDate.setMinimumSize(QtCore.QSize(150, 0))
        self.closeDate.setText("")
        self.closeDate.setObjectName("closeDate")
        self.horizontalLayout_6.addWidget(self.closeDate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(15, -1, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dueOn = QtGui.QCheckBox(Dialog)
        self.dueOn.setText("")
        self.dueOn.setObjectName("dueOn")
        self.horizontalLayout_4.addWidget(self.dueOn)
        self.dueDate = QtGui.QDateTimeEdit(Dialog)
        self.dueDate.setEnabled(False)
        self.dueDate.setMinimumSize(QtCore.QSize(150, 0))
        self.dueDate.setCalendarPopup(True)
        self.dueDate.setObjectName("dueDate")
        self.horizontalLayout_4.addWidget(self.dueDate)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.priority = QtGui.QSpinBox(Dialog)
        self.priority.setMinimumSize(QtCore.QSize(20, 20))
        self.priority.setMaximumSize(QtCore.QSize(40, 16777215))
        self.priority.setMaximum(5)
        self.priority.setObjectName("priority")
        self.horizontalLayout_5.addWidget(self.priority)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.priorityText = QtGui.QLabel(Dialog)
        self.priorityText.setObjectName("priorityText")
        self.horizontalLayout_5.addWidget(self.priorityText)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setContentsMargins(15, -1, 15, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.taskName = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taskName.sizePolicy().hasHeightForWidth())
        self.taskName.setSizePolicy(sizePolicy)
        self.taskName.setMinimumSize(QtCore.QSize(400, 0))
        self.taskName.setObjectName("taskName")
        self.gridLayout_3.addWidget(self.taskName, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setMinimumSize(QtCore.QSize(0, 27))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtGui.QGridLayout(self.frame)
        self.gridLayout_4.setContentsMargins(-1, 3, -1, 3)
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.fontComboBox = QtGui.QComboBox(self.frame)
        self.fontComboBox.setMinimumSize(QtCore.QSize(120, 20))
        self.fontComboBox.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fontComboBox.setObjectName("fontComboBox")
        self.gridLayout_4.addWidget(self.fontComboBox, 0, 8, 1, 1)
        self.fontSize = QtGui.QSpinBox(self.frame)
        self.fontSize.setMinimumSize(QtCore.QSize(20, 20))
        self.fontSize.setMaximumSize(QtCore.QSize(40, 20))
        self.fontSize.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
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
        self.editorBGcolor.setMinimumSize(QtCore.QSize(0, 20))
        self.editorBGcolor.setMaximumSize(QtCore.QSize(60, 20))
        self.editorBGcolor.setCheckable(False)
        self.editorBGcolor.setObjectName("editorBGcolor")
        self.horizontalLayout.addWidget(self.editorBGcolor)
        self.currentBGcolor = QtGui.QPushButton(self.frame)
        self.currentBGcolor.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.currentBGcolor.setFont(font)
        self.currentBGcolor.setAutoFillBackground(False)
        self.currentBGcolor.setText("")
        self.currentBGcolor.setIconSize(QtCore.QSize(22, 22))
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
        self.editorTextColor.setMinimumSize(QtCore.QSize(0, 20))
        self.editorTextColor.setMaximumSize(QtCore.QSize(80, 20))
        self.editorTextColor.setObjectName("editorTextColor")
        self.horizontalLayout_2.addWidget(self.editorTextColor)
        self.currentTextColor = QtGui.QPushButton(self.frame)
        self.currentTextColor.setMaximumSize(QtCore.QSize(20, 20))
        self.currentTextColor.setAutoFillBackground(False)
        self.currentTextColor.setText("")
        self.currentTextColor.setIconSize(QtCore.QSize(20, 20))
        self.currentTextColor.setFlat(False)
        self.currentTextColor.setObjectName("currentTextColor")
        self.horizontalLayout_2.addWidget(self.currentTextColor)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 5, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 10, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.editorBold = QtGui.QPushButton(self.frame)
        self.editorBold.setMinimumSize(QtCore.QSize(0, 20))
        self.editorBold.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setWeight(75)
        font.setBold(True)
        self.editorBold.setFont(font)
        self.editorBold.setCheckable(True)
        self.editorBold.setFlat(False)
        self.editorBold.setObjectName("editorBold")
        self.horizontalLayout_3.addWidget(self.editorBold)
        self.editorItalic = QtGui.QPushButton(self.frame)
        self.editorItalic.setMinimumSize(QtCore.QSize(0, 20))
        self.editorItalic.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setItalic(True)
        self.editorItalic.setFont(font)
        self.editorItalic.setCheckable(True)
        self.editorItalic.setObjectName("editorItalic")
        self.horizontalLayout_3.addWidget(self.editorItalic)
        self.editorUnderline = QtGui.QPushButton(self.frame)
        self.editorUnderline.setMinimumSize(QtCore.QSize(0, 20))
        self.editorUnderline.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setUnderline(True)
        self.editorUnderline.setFont(font)
        self.editorUnderline.setCheckable(True)
        self.editorUnderline.setObjectName("editorUnderline")
        self.horizontalLayout_3.addWidget(self.editorUnderline)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.editorResetColor = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editorResetColor.sizePolicy().hasHeightForWidth())
        self.editorResetColor.setSizePolicy(sizePolicy)
        self.editorResetColor.setMinimumSize(QtCore.QSize(0, 20))
        self.editorResetColor.setMaximumSize(QtCore.QSize(40, 20))
        self.editorResetColor.setObjectName("editorResetColor")
        self.gridLayout_4.addWidget(self.editorResetColor, 0, 6, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
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
        self.taskDescription.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.taskDescription.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.taskDescription.setFrameShape(QtGui.QFrame.NoFrame)
        self.taskDescription.setFrameShadow(QtGui.QFrame.Plain)
        self.taskDescription.setLineWidth(1)
        self.taskDescription.setAutoFormatting(QtGui.QTextEdit.AutoAll)
        self.taskDescription.setTabChangesFocus(False)
        self.taskDescription.setUndoRedoEnabled(True)
        self.taskDescription.setReadOnly(False)
        self.taskDescription.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Serif\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'monofur\'; font-size:10pt;\"><br /></p></body></html>")
        self.taskDescription.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.taskDescription.setOpenExternalLinks(False)
        self.taskDescription.setOpenLinks(False)
        self.taskDescription.setObjectName("taskDescription")
        self.verticalLayout_2.addWidget(self.taskDescription)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 0, 15, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        self.fontComboBox.setCurrentIndex(-1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Created:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Closed:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Due", None, QtGui.QApplication.UnicodeUTF8))
        self.dueDate.setSpecialValueText(QtGui.QApplication.translate("Dialog", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Priority:", None, QtGui.QApplication.UnicodeUTF8))
        self.priorityText.setText(QtGui.QApplication.translate("Dialog", "Now", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Task Name: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Task Description", None, QtGui.QApplication.UnicodeUTF8))
        self.editorBGcolor.setText(QtGui.QApplication.translate("Dialog", "BGcolor", None, QtGui.QApplication.UnicodeUTF8))
        self.editorTextColor.setText(QtGui.QApplication.translate("Dialog", "Text color", None, QtGui.QApplication.UnicodeUTF8))
        self.editorBold.setText(QtGui.QApplication.translate("Dialog", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.editorItalic.setText(QtGui.QApplication.translate("Dialog", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.editorUnderline.setText(QtGui.QApplication.translate("Dialog", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.editorResetColor.setText(QtGui.QApplication.translate("Dialog", "reset", None, QtGui.QApplication.UnicodeUTF8))

