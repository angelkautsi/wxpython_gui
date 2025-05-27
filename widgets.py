import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='HELLO ANGEL')
        panel = wx.Panel(self) #creating panels / widget1

        self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
        my_btn = wx.Button(panel, label='Click Here', pos=(5, 55)) #creating button

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()