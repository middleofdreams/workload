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
#     font=QtGui.QFont(main.settings["fontFamily"])
#     font.setPointSize(int(main.settings["fontSize"]))
#     main.ui.taskList.setFont(font)
    main.show()
    main.adjustHeight(downSize=True, init=False)
    main.ui.statusbar.showMessage("Hello! Ready to work ;-)",3600)
    
    
def changeStyle(main,settings={}):
    '''apply css style for window'''
    settingList=["tasklistFontColor","windowBG","windowFrame","selectedItem",
                 "tasklistBG","tasklistFrame","alternateListItem","taskEditorBG",
                 "taskEditorFrame","buttonBG","textInputBG","fontFamily","fontSize","workloadFontColor","tasklistFontSize"]
    s=settings.copy()
    for i in settingList:
        if i not in s.keys():
            s[i]=main.settings[i]

    WindowStyle="QMainWindow{border:2px solid rgba"+s["windowFrame"]+";border-radius:6px; background-color:rgba"+s["windowBG"]+"\
    ;font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+";font:"+s["fontSize"]+"px}\
    QMessageBox{background-color:rgba"+s["windowBG"]+";font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+";font:"+s["fontSize"]+"px} \
    QDialog{background-color:rgba"+s["windowBG"]+";\
    border:2px solid rgba"+s["windowFrame"]+";border-radius:6px;font:"+s["fontSize"]+"px;\
    ;font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+"}\
    \
    QTreeWidget{alternate-background-color:rgba"+s["alternateListItem"]+";background-color:rgba"+s["tasklistBG"]+"\
    ;border: 1px solid rgba"+s["tasklistFrame"]+";color:rgba"+s["tasklistFontColor"]+";font:"+s["tasklistFontSize"]+"px;font-family:"+s["fontFamily"]+"}\
    \
    QTabWidget::pane{border: 1px solid rgba(15,15,15,100);font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+";font:"+s["fontSize"]+"px}\
    \
    QTabBar::tab{height:15px;border:1px solid rgba(15,15,15,100);padding: 1px;min-width: 10ex;\
    ;font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+";font:"+s["fontSize"]+"px;\
    margin-left:1px;border-top-left-radius: 3px;border-top-right-radius: 3px}\
    QTabBar::tab::selected{background-color:rgba"+s["selectedItem"]+";\
    ;font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+";font:"+s["fontSize"]+"px;\
    border:1px solid rgba(15,15,15,100);padding: 2px;min-width: 10ex}\
    \
    QListWidget{background-color:rgba"+s["tasklistBG"]+";font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+";font:"+s["fontSize"]+"px}\
    \
    QDialog[dialog=taskEditor]{border: 2px solid rgba"+s["taskEditorFrame"]+";\
    border-radius: 8px; background-color:rgba"+s["taskEditorBG"]+"\
    ;font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+";font:"+s["fontSize"]+"px}\
    \
    QComboBox{background-color:rgba"+s["buttonBG"]+";border:1px solid rgba(15,15,15,100);border-radius:3px;min-width:10ex;min-height:13px;\
    padding-top:2px;padding-bottom:2px;padding-left:5px;padding-right:5px;border-style:outset;\
    font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+";font:"+s["fontSize"]+"px}\
    QComboBox::down-arrow{image:url(:res/ui/down_arrow.png)}\
    QComboBox QAbstractItemView{background:rgba"+s["buttonBG"]+";border:1px solid rgba(15,15,15,100);border-radius:3px;min-width:30ex}\
    QComboBox::item::selected{background-color:rgba"+s["selectedItem"]+"}\
    QComboBox::hover{background-color:rgba"+s["selectedItem"]+"}\
    \
    QSpinBox{background-color:rgba"+s["buttonBG"]+";border:1px solid rgba(15,15,15,100);border-radius:3px;min-height:18px;\
    font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+";font:"+s["fontSize"]+"px}\
    QSpinBox::hover{background-color:rgba"+s["selectedItem"]+"}\
    QSpinBox::up-button{image:url(:res/ui/spin_up.png)}QSpinBox::down-button{image:url(:res/ui/spin_down.png)}\
    \
    QPushButton[custom=skinny]{border:1px solid rgba(15,15,15,100); border-radius:3px;\
    background-color:rgba"+s["buttonBG"]+";padding-left:2px;padding-right:2px;color:rgba"+s["workloadFontColor"]+"}\
    QPushButton::hover[custom=skinny]{border: 1px solid rgba(15,15,15,100); border-radius:2px;\
    background-color:rgba"+s["selectedItem"]+"}\
    \
    QPushButton{border: 1px solid rgba(15,15,15,100); border-radius:3px;\
    padding-top:5px;padding-bottom:5px;padding-left:15px;padding-right:15px;border-style:outset;background-color:rgba"+s["buttonBG"]+";\
    font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+";font:"+s["fontSize"]+"px}\
    QPushButton::hover{border: 1px solid rgba(15,15,15,200); border-radius:3px;\
    padding-top:7px;border-style:inset;background-color:rgba"+s["selectedItem"]+"}\
    \
    QPushButton[button=taskEditor]{min-height:18px;min-width:16px;margin-left:2px;border:1px solid rgba(15,15,15,100); border-radius:3px;\
    background-color:rgba"+s["buttonBG"]+";padding-left:2px;padding-right:2px;padding-top:0px;padding-bottom:0px;border-style:outset;\
    ;color:rgba"+s["workloadFontColor"]+"}\
    QPushButton::hover[button=taskEditor]{border: 1px solid rgba(15,15,15,100); border-radius:2px;\
    background-color:rgba"+s["selectedItem"]+"}\
    QPushButton::flat[button=taskEditor]{border: 1px solid rgba(15,15,15,200); border-radius:2px;\
    background-color:rgba"+s["selectedItem"]+"}\
    \
    QPushButton[button=taskEditorBold]{min-height:18px;min-width:16px;margin-left:2px;border:1px solid rgba(15,15,15,100); border-radius:3px;\
    background-color:rgba"+s["buttonBG"]+";padding-left:2px;padding-right:2px;padding-top:0px;padding-bottom:0px;border-style:outset;\
    ;color:rgba"+s["workloadFontColor"]+";font:bold "+s["fontSize"]+"px}\
    QPushButton::hover[button=taskEditorBold]{border: 1px solid rgba(15,15,15,100); border-radius:2px;\
    background-color:rgba"+s["selectedItem"]+"}\
    QPushButton::flat[button=taskEditorBold]{border: 1px solid rgba(15,15,15,200); border-radius:2px;\
    background-color:rgba"+s["selectedItem"]+"}\
        \
    QPushButton[button=taskEditorItalic]{min-height:18px;min-width:16px;margin-left:2px;border:1px solid rgba(15,15,15,100); border-radius:3px;\
    background-color:rgba"+s["buttonBG"]+";padding-left:2px;padding-right:2px;padding-top:0px;padding-bottom:0px;border-style:outset;\
    ;color:rgba"+s["workloadFontColor"]+";font:italic "+s["fontSize"]+"px}\
    QPushButton::hover[button=taskEditorItalic]{border: 1px solid rgba(15,15,15,100); border-radius:2px;\
    background-color:rgba"+s["selectedItem"]+"}\
    QPushButton::flat[button=taskEditorItalic]{border: 1px solid rgba(15,15,15,200); border-radius:2px;\
    background-color:rgba"+s["selectedItem"]+"}\
\
    QPushButton[button=taskEditorUnderline]{min-height:18px;min-width:16px;margin-left:2px;border:1px solid rgba(15,15,15,100); border-radius:3px;\
    background-color:rgba"+s["buttonBG"]+";padding-left:2px;padding-right:2px;padding-top:0px;padding-bottom:0px;border-style:outset;\
    ;color:rgba"+s["workloadFontColor"]+";font:underline "+s["fontSize"]+"px}\
    QPushButton::hover[button=taskEditorUnderline]{border: 1px solid rgba(15,15,15,100); border-radius:2px;\
    background-color:rgba"+s["selectedItem"]+"}\
    QPushButton::flat[button=taskEditorUnderline]{border: 1px solid rgba(15,15,15,200); border-radius:2px;\
    background-color:rgba"+s["selectedItem"]+"}\
        \
    QDateTimeEdit{background-color:rgba"+s["buttonBG"]+";border:1px solid rgba(15,15,15,100);border-radius:3px;min-width:10ex;min-height:13px;\
    padding-top:2px;padding-bottom:2px;padding-left:5px;padding-right:5px;border-style:outset;\
    font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+";font:"+s["fontSize"]+"px}\
    QDateTimeEdit::down-arrow{image:url(:res/ui/down_arrow.png)}\
    QDateTimeEdit::hover{background-color:rgba"+s["selectedItem"]+"}\
    \
    QCheckBox::indicator{width:15px;height:15px;background:rgba"+s["buttonBG"]+";image:url(:res/ui/checkbox.png);border:1px solid rgba(15,15,15,100);border-radius:2px}\
    QCheckBox::indicator::checked{background:rgba"+s["selectedItem"]+"}\
    QCheckBox{font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+";font:"+s["fontSize"]+"px}\
    \
    QStatusBar{background-color:transparent;border-top: 3px transparent; border-radius:5px;\
    border-bottom: 3px transparent;border-left: 3px transparent;border-right: 3px transparent}\
    \
    QMenuBar{padding:2px 2px;transparent;border-top: 3px transparent;\
    border-left:2px transparent ;border-right: 2px transparent ;border-bottom: 3px transparent ;border-radius: 2px;\
    ;font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+";font:"+s["fontSize"]+"px}\
    QMenuBar::item{padding: 2px 2px;background-color:transparent;color:rgb(55, 55, 55);\
    ;font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+";font:"+s["fontSize"]+"px}\
    \
    QMenu{border:1px solid rgba"+s["windowFrame"]+"\
    ;font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+";font:"+s["fontSize"]+"px;\
    border-left:3px solid rgba"+s["windowFrame"]+";border-bottom:3px solid rgba"+s["windowFrame"]+";\
    border-radius:3px;background-color:rgba"+s["windowBG"]+"} \
    QMenu::item{padding: 2px 20px;background-color: rgba"+s["windowBG"]+";color:rgb(55, 55, 55)\
    ;font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+";font:"+s["fontSize"]+"px}\
    QMenu::item::selected{background-color:rgba"+s["selectedItem"]+";color:rgb(55, 55, 55);\
    border:1px solid rgb(85, 170, 255);border-radius:3px}\
    QMenu::separator{background-color:rgba"+s["windowFrame"]+";\
    border 1px solid:rgb(55,55,55);height:2px;margin-left:5px;margin-right:5px;}\
    QLineEdit{background:rgba"+s["textInputBG"]+";border:1px solid rgba"+s["windowFrame"]+";border-radius:2px\
    ;font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+";font:"+s["fontSize"]+"px}\
    QLabel{font-family:"+s["fontFamily"]+";color:rgba"+s["workloadFontColor"]+";font:"+s["fontSize"]+"px}\
    \
    QSizeGrip{width:16px;height:16px;image:url(:res/ui/size_grip.png)}"
    
    main.setStyleSheet(WindowStyle)

        
