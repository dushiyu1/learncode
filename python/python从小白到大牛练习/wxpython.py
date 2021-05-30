import wx
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="第一个gui程序",size=(400,300))
        self.Centre()
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel,pos=(110,20))
        b1 = wx.Button(parent=panel,label="1",id = 11, pos=(100,50))
        b2 = wx.Button(parent=panel,label="2",id = 12, pos=(100,100))
        b2 = wx.Button(parent=panel,label="2",id = 13, pos=(100,150))

        self.Bind(wx.EVT_BUTTON,self.on_click,id=10,id2=20)
        self.Bind(wx.EVT_BUTTON,self.on_click,b2)
        
        #statictext = wx.StaticText(parent=panel,label="hello,world",pos=(100,100))
    def on_click(self,event):
        event_id = event.GetId()
        if event_id == 11:
            self.statictext.SetLabelText("11")
        elif event_id == 12:
            self.statictext.SetLabelText("12")
        else:
            self.statictext.SetLabelText("13")
class App(wx.App):
    
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True
    
if __name__ == '__main__':
    app = App()
    app.MainLoop()
