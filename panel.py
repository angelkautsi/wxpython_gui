import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='HELLO ANGEL')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.output_label = wx.StaticText(panel, label="")
        my_sizer.Add(self.output_label, 0, wx.ALL | wx.EXPAND, 5)
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        check = wx.CheckBox(panel, label="Agreed to the terms and conditions")
        my_sizer.Add(check, 0, wx.ALL, 5)
        radio1 = wx.RadioButton(panel, label="Option 1", style=wx.RB_GROUP)
        my_sizer.Add(radio1, 0, wx.ALL, 5)
        radio2 = wx.RadioButton(panel, label="Option 2")
        my_sizer.Add(radio2, 0, wx.ALL, 5)
        my_btn = wx.Button(panel, label='Click Here')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            self.output_label.SetLabel("You didn't enter anything!")
        else:
            self.output_label.SetLabel(f'You typed: "{value}"')


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()