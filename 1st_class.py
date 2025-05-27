import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='HELLO ANGEL')
        self.Show()
if __name__=='__main__':
    app = wx.App()
    frame = wx.Frame()
    app.MainLoop()