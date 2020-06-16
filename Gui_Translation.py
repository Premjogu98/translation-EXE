import wx

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Google Translation GUI',pos = (100,150), size =(800,300))
        self.panel = wx.Panel(self)

        self.Source_lbl = wx.StaticText(self.panel,label = "Add Source Name Like This -> SourcName~Server",pos=(13, 40))

        self.Source_TB = wx.TextCtrl(self.panel, pos=(110, 10),size=(200, 25))

        self.Source_btn = wx.Button(self.panel, label='Add Source', pos=(10, 10))
        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.Source_btn.SetFont(font)
        self.Source_btn.Bind(wx.EVT_BUTTON, self.Add_Source)
        
        self.Select_Source_lbl = wx.StaticText(self.panel,label = "Select Source : ",pos=(340, 11))
        self.Select_Source_lbl.SetFont(font)

        f = open("D:\\Translation EXE\\source_list.txt", "r")
        f = f.read()
        self.Source_list = str(f).splitlines()
        self.combo = wx.ComboBox(self.panel,choices = self.Source_list,pos=(460, 10),size=(250, 25))
        font1 = wx.Font(11, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.combo.SetFont(font1)

        self.Show()

    def Add_Source(self,event):
        Source_Name = self.Source_TB.GetValue()
        if str(Source_Name) != '':
            f = open("D:\\Translation EXE\\source_list.txt", "a")
            f.write(f'{str(Source_Name)}\n')
            f.close()
            print(f'{str(Source_Name) This Source Name & Server added On Text File}')
            self.combo.AppendItems(Source_Name)
            print(f'{str(Source_Name) This Source Name Updated On Dropdown}')
            self.Source_btn.SetForegroundColour('Black')
            self.Source_btn.SetBackgroundColour('Green')
        else:
            self.Source_btn.SetForegroundColour('White')
            self.Source_btn.SetBackgroundColour('Red')
            print('Null value Not Accepted Please Add Source Name & Server on TextBox')
        
    

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()