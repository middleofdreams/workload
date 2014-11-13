from PySide.QtCore import QThread,Signal
    
class ShortcutsHandler(QThread):
    show=Signal()
    def __init__(self,parent):
        QThread.__init__(self,parent)
        self.show.connect(parent.toggle)
        self.setTerminationEnabled(True)
        self.start()
        
    def run(self):
        import sys
        if sys.platform=="win32":
            import win32con
            import ctypes
            if not ctypes.windll.user32.RegisterHotKey(None,0,win32con.MOD_CONTROL,win32con.VK_SPACE):
                raise Exception("Unable to register hotkey")
            msg = ctypes.wintypes.MSG ()
            while ctypes.windll.user32.GetMessageA (ctypes.byref (msg), None, 0, 0) != 0:
                if msg.message == win32con.WM_HOTKEY:
                    self.show.emit()
