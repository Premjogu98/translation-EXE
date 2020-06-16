import wx

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Google Translation GUI',pos = (100,150), size =(800,300))
        panel = wx.Panel(self)

        # self.Source_lbl = wx.StaticText(panel,label = "Add Source : ",pos=(10, 10))
        self.Source_btn = wx.Button(panel, label='Add Source', pos=(10, 10))

        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.Source_btn.SetFont(font)

        self.Source_TB = wx.TextCtrl(panel, pos=(110, 10),size=(200, 25))
        

        self.Select_Source_lbl = wx.StaticText(panel,label = "Select Source : ",pos=(340, 11))
        self.Select_Source_lbl.SetFont(font)

        # languages = ['C', 'C++', 'Python', 'Java', 'Perl'] 
        f = open("D:\\Translation EXE\\source_list.txt", "r")
        f = f.read()
        self.Source_list = str(f).splitlines()
        self.combo = wx.ComboBox(panel,choices = self.Source_list,pos=(460, 10),size=(250, 25))
        font1 = wx.Font(11, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.combo.SetFont(font1)
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()