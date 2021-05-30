import wx
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="第一个gui程序",size=(400,300))
        self.Centre()
        panel = wx.Panel(parent=self)
        statictext = wx.StaticText(parent=panel,label="hello,world",pos=(100,100))
class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True
    
if __name__ == '__main__':
    app = App()
    app.MainLoop()
