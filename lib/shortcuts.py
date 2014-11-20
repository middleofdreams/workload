from PySide.QtCore import QThread,Signal
    
class ShortcutsHandler(QThread):
    show=Signal()
    error=Signal()
    def __init__(self,parent,key):
        QThread.__init__(self,parent)
        self.parent=parent
        self.key=key
        self.winKeyMap={
                        ",":188,
                        ".":190,
                        "/":191,
                        ";":186,
                        "'":221,
                        "[":219,
                        "]":220,
                        "\\":187,
                        "-":189,
                        "=":187}
        self.show.connect(parent.toggle)
        self.error.connect(parent.hoyKeyError)
        self.setTerminationEnabled(True)
        self.start()
        
    def run(self):
        import sys
        if sys.platform=="win32":
            import win32con
            import ctypes
            k,mods=self.readShortcut_Win()
            if not ctypes.windll.user32.RegisterHotKey(None,0,mods,k):
                self.error.emit()
                return False
            msg = ctypes.wintypes.MSG ()
            while ctypes.windll.user32.GetMessageA (ctypes.byref (msg), None, 0, 0) != 0:
                if msg.message == win32con.WM_HOTKEY:
                    self.show.emit()
                    
        elif sys.platform.startswith("linux"):
            from Xlib.display import Display
            from Xlib import X
            disp = Display()
            root = disp.screen().root
            root.change_attributes(event_mask = X.KeyPressMask)
            try:
                root.grab_key(65, X.ControlMask, 1,X.GrabModeAsync, X.GrabModeAsync)
            except:
                self.error.emit()
                return False
            while True:
                event=root.display.next_event()
                if event.type==X.KeyPress:
                    if event.detail==65:
                        self.show.emit()
                        
    def readShortcut_Win(self):
        import win32con
        k=self.key
        if "Ctrl" in k:
            mods=win32con.MOD_CONTROL
        if "Alt" in k:
            try:
                mods|= win32con.MOD_ALT
            except:
                mods=win32con.MOD_ALT
        if "Shift" in k:
            try:
                mods|=win32con.MOD_SHIFT
            except:
                mods=win32con.MOD_SHIFT
        if "Win" in k:
            try:
                mods|=win32con.MOD_WIN
            except:
                mods=win32con.MOD_WIN        
        k=k.split(" + ")[-1]
        if k=="Space":
            k=win32con.VK_SPACE
        elif k in self.winKeyMap.keys():
            k=self.winKeyMap[k]
        else:
            k=ord(k)
        return k,mods
                
    
            