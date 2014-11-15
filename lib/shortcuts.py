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
                    
        elif sys.platform.startswith("linux"):
            from Xlib.display import Display
            from Xlib import X
            disp = Display()
            root = disp.screen().root
            root.change_attributes(event_mask = X.KeyPressMask)
            root.grab_key(65, X.ControlMask, 1,X.GrabModeAsync, X.GrabModeAsync)
            while True:
                event=root.display.next_event()
                if event.type==X.KeyPress:
                    if event.detail==65:
                        self.show.emit()
