import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='HELLO WORLD')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL) #boxsizer sizer
        self.text_ctrl = wx.TextCtrl(panel) #this controls text
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        my_btn = wx.Button(panel, label='Click Here')
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()