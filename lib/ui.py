from PySide import QtCore,QtGui
from lib.settingsWindow import SettingsWindow
'''Some functions for application init'''
def guiSettings(main):
    '''setting window flags, position'''
    main.setWindowFlags(QtCore.Qt.FramelessWindowHint
                        | QtCore.Qt.WindowStaysOnTopHint)
    
    desktop = QtGui.QApplication.desktop()
    if desktop.height() > 800:
        main.move(10, (desktop.height() / 2) - (main.height()))
    else:
        main.move(15, 150)
    main.resizeColumns()
        
def connectSignals(main):
    '''connect signals to functions'''
    main.ui.taskList.keyPressEvent = main.getKeysOnList
    main.ui.taskInput.keyPressEvent= main.getKeysOnInput
    main.ui.taskList.activated.connect(main.openTask)
    sc = QtGui.QShortcut(main)
    sc.setKey("Escape")
    sc.activated.connect(main.closeEvent)
    
    sc = QtGui.QShortcut(main)
    sc.setKey("Ctrl+R")
    sc.activated.connect(main.adjustHeight)
    
    main.ui.taskList.focusInEvent=main.taskListFocusIn
    main.ui.taskList.drawRow=main.drawRow


#CONNECT MENU ITEMS
    main.ui.actionExit.triggered.connect(main.exit)
    main.ui.actionImport_tasklist.triggered.connect(main.importTasklist)
    main.ui.actionAbout_2.triggered.connect(main.about)
    main.ui.actionAdd_new.triggered.connect(main.createTask)
    main.ui.actionEdit.triggered.connect(main.openTask)
    main.ui.actionDelete.triggered.connect(main.deleteSelectedTasks)
    main.ui.actionComplete.triggered.connect(main.completeTasks)
    main.ui.actionHistory.triggered.connect(main.showHistory)
    main.ui.actionSettings.triggered.connect(lambda s=main:SettingsWindow(s))
    main.ui.actionExport_tasklist.triggered.connect(main.exportTaskList)
    main.ui.taskInput.dropEvent = main.dropTask
        
def finalizeInit(main):
    '''show window and adjust it's size'''
    windowOpacity=main.settings["mainWindowOpacity"]
    main.setWindowOpacity(int(windowOpacity)/100)
    font=QtGui.QFont(main.settings["tasklistFont"])
    font.setPointSize(int(main.settings["tasklistFontSize"]))
    main.ui.taskList.setFont(font)

    main.show()
    main.adjustHeight(downSize=True, init=False)

    main.ui.statusbar.showMessage("Hello! Ready to work ;-)",3600)
    
    
def setStyle(main):
    '''apply css style for window'''
    windowBG=main.settings["windowBG"]
    windowFrame=main.settings["windowFrame"]
    selectedMenuItemBG="(170,213,255)"
    
    taskListBG=main.settings["tasklistBG"]
    taskListFrame=main.settings["tasklistFrame"]
    alternateListItem="(170,213,255)"
    
    WindowStyle="QMainWindow{border:2px solid rgb"+windowFrame+"; border-radius: 2px;background-color:rgb"+windowBG+";}\
    QMessageBox{background-color:rgb"+windowBG+"}"
    selectedMenuItemBG="(85, 170, 220,80)"
    alternateListItem="(170,213,255,250)"
    main.WindowStyle="QMainWindow{border:2px solid rgb"+windowFrame+";  border-radius: 2px;background-color:rgb"+windowBG+";}\
    QMessageBox{background-color:rgb"+windowBG+"} QDialog{background-color:rgb"+windowBG+"}\
    QTreeWidget{background-color:rgb"+windowBG+";alternate-background-color:rgb"+alternateListItem+"}"
    
    StatusbarStyle="QStatusBar{background-color:transparent;border-top: 0px transparent; border-radius:2px;\
    border-bottom: 3px solid rgb(85, 170, 255,150);border-left: 2px solid rgb(85, 170, 255,150);border-right: 2px solid rgb(85, 170, 255,150)}"
    
    MenubarStyle="QMenuBar{padding:2px 2px;background-color:rgb"+windowBG+";border-top: 3px solid rgb(85, 170, 255,150);\
    border-left:2px solid rgb(85, 170, 255,150);border-right: 2px solid rgb(85, 170, 255,150);border-radius: 2px}\
    QMenuBar::item{padding: 2px 2px;background-color:transparent;color:rgb(55, 55, 55);border-radius:3px}"
    
    MenuStyle="QMenu{background-color:rgb"+windowBG+";color:black;border:1px solid rgb"+windowFrame+";\
    border-left:3px solid rgb"+windowFrame+";border-radius:3px} \
    QMenu::item{padding: 2px 20px;background-color:rgb"+windowBG+";color:rgb(55, 55, 55)}\
    QMenu::item::selected{background-color:rgb"+selectedMenuItemBG+";color:rgb(55, 55, 55);border:1px solid rgb(85, 170, 255);\
    border-radius:3px}QMenu::separator{background-color:rgb"+windowFrame+";border 1px solid:rgb(55,55,55);height:2px;margin-left:5px;margin-right:5px;}"
    
    main.setStyleSheet(main.WindowStyle)

    main.ui.menubar.setStyleSheet(MenubarStyle)
    main.ui.menuFile.setStyleSheet(MenuStyle)
    main.ui.menuTask.setStyleSheet(MenuStyle)
    main.ui.menuContext.setStyleSheet(MenuStyle)
    main.ui.statusbar.setStyleSheet(StatusbarStyle)
    

        