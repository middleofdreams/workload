from PySide import QtCore,QtGui

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
    from lib.settingsWindow import SettingsWindow
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
    
    
def changeStyle(main,settings={}):
    '''apply css style for window'''
    settingList=["tasklistFontColor","windowBG","windowFrame","selectedMenuItem","tasklistBG","tasklistFrame","alternateListItem","taskEditorBG","taskEditorFrame"]
    s=settings.copy()
    for i in settingList:
        if i not in s.keys():
            s[i]=main.settings[i]

    WindowStyle="QMainWindow{border:2px solid rgba"+s["windowFrame"]+";border-radius:6px;  \
    background-color:rgba"+s["windowBG"]+"}\
    QMessageBox{background-color:rgba"+s["windowBG"]+"} QDialog{background-color:rgba"+s["windowBG"]+";\
    border:2px solid rgba"+s["windowFrame"]+";border-radius:6px}\
    QTreeWidget{alternate-background-color:rgba"+s["alternateListItem"]+";background-color:rgba"+s["tasklistBG"]+"\
    ;border: 1px solid rgba"+s["tasklistFrame"]+";color:rgba"+s["tasklistFontColor"]+"}\
    QTabWidget::pane{border: 1px solid rgba(15,15,15,100)}\
    QTabBar::tab{height:15px;border:1px solid rgba(15,15,15,100);\
    padding: 1px;min-width: 10ex;margin-left:1px;border-top-left-radius: 3px;border-top-right-radius: 3px}\
    QTabBar::tab::selected{background-color:rgba"+s["selectedMenuItem"]+";border:1px solid rgba(15,15,15,100);padding: 2px;min-width: 10ex}\
    QListWidget{background-color:rgba"+s["tasklistBG"]+"}\
    QPushButton[custom=buttonbox]{border: 1px rgba(15,15,15,100); border-radius:3px;\
    padding-top:5px;padding-bottom:5px;padding-left:15px;padding-right:15px;border-style:outset;background-color:rgba"+s["alternateListItem"]+";}\
    QPushButton[custom=buttonbox]::hover{border: 1px rgba(15,15,15,200); border-radius:3px;\
    padding-top:7px;border-style:inset;background-color:rgba"+s["selectedMenuItem"]+"}"\
    "QDialog[dialog=taskEditor]{border: 2px solid rgba"+s["taskEditorFrame"]+";\
    border-radius: 8px; background-color:rgba"+s["taskEditorBG"]+"}"
    
    StatusbarStyle="QStatusBar{background-color:transparent;border-top: 3px transparent; border-radius:5px;\
    border-bottom: 3px transparent;border-left: 3px transparent;border-right: 3px transparent}"
    
    MenubarStyle="QMenuBar{padding:2px 2px;transparent;border-top: 3px transparent;\
    border-left:2px transparent ;border-right: 2px transparent ;border-bottom: 3px transparent ;border-radius: 2px}\
    QMenuBar::item{padding: 2px 2px;background-color:transparent;color:rgb(55, 55, 55)}"
    
    MenuStyle="QMenu{color:black; border:1px solid rgba"+s["windowFrame"]+";\
    border-left:3px solid rgba"+s["windowFrame"]+";border-bottom:3px solid rgba"+s["windowFrame"]+";border-radius:3px;background-color:rgba"+s["windowBG"]+"} \
    QMenu::item{padding: 2px 20px;background-color: rgba"+s["windowBG"]+";color:rgb(55, 55, 55)}\
    QMenu::item::selected{background-color:rgba"+s["selectedMenuItem"]+";color:rgb(55, 55, 55);\
    border:1px solid rgb(85, 170, 255);\
    border-radius:3px}QMenu::separator{background-color:rgba"+s["windowFrame"]+";\
    border 1px solid:rgb(55,55,55);height:2px;margin-left:5px;margin-right:5px;}"
    main.setStyleSheet(WindowStyle)
    try:
        main.ui.menubar.setStyleSheet(MenubarStyle)
        main.ui.menuFile.setStyleSheet(MenuStyle)
        main.ui.menuTask.setStyleSheet(MenuStyle)
        main.ui.menuContext.setStyleSheet(MenuStyle)
        main.ui.statusbar.setStyleSheet(StatusbarStyle) 
    except:
        pass
        
