import wx

class MainFrame(wx.Frame):
    """ Class with the main frame used by the game.
    """
    
    def __init__(self, parent, ID):
        """ Class initialization method. It creates the GUI for the game.
        """
        wx.Frame.__init__(self, parent, ID, 'IsshA', size=(800, 400))
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        buttonSizer = self.createControlButtons()        
        self.SetSizer(mainSizer)
        self.gamePanel= GamePanel(self)
        mainSizer.Add(self.gamePanel, 2, wx.EXPAND)
        mainSizer.Add(buttonSizer, 1, wx.EXPAND)
        self.Layout()
    
    def createButton(self, label, handler):
        button = wx.Button(self, -1, label)
        self.Bind(wx.EVT_BUTTON, handler, button)
        return button
    
    def createControlButtons(self):
        buttonSizer    = wx.GridSizer(rows=5, cols=3)        
        upButton       = self.createButton('Up', self.OnButton)
        leftButton     = self.createButton('Left', self.OnButton)
        rightButton    = self.createButton('Right', self.OnButton)
        downButton     = self.createButton('Down', self.OnButton)
        partyButton    = self.createButton('Party', self.OnButton)
        mapButton      = self.createButton('Map', self.OnButton)
        questButton    = self.createButton('Quest', self.OnButton)
        settingsButton = self.createButton('Settings', self.OnButton)
        
        buttonSizer.AddSpacer(0)
        buttonSizer.Add(upButton, 1, wx.EXPAND)
        buttonSizer.AddSpacer(0)
        
        buttonSizer.Add(leftButton, 1, wx.EXPAND)
        buttonSizer.AddSpacer(0)
        buttonSizer.Add(rightButton, 1, wx.EXPAND)
        
        buttonSizer.AddSpacer(0)
        buttonSizer.Add(downButton, 1, wx.EXPAND)
        buttonSizer.AddSpacer(0)
        
        buttonSizer.Add(partyButton, 1, wx.EXPAND)
        buttonSizer.AddSpacer(0)
        buttonSizer.Add(mapButton, 1, wx.EXPAND)
        
        buttonSizer.Add(questButton, 1, wx.EXPAND)
        buttonSizer.AddSpacer(0)
        buttonSizer.Add(settingsButton, 1, wx.EXPAND)
        
        return buttonSizer
    
    def OnButton(self, event):
        pass

        
class GamePanel(wx.Panel):
    """ Class with the Main Game Panel.
    """
    
    def __init__(self, parent):
        """ Class initialization method. It display main game elements.
        """
        wx.Panel.__init__(self, parent)
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
                
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Update, self.timer)
        self.timer.Start(50)
        
        # batch contains all objects to be painted
        self.batch = []
        self.image = {'image': wx.Image("resources/hero.png").ConvertToBitmap(),
                      'x': 100,
                      'y': 100}
        self.batch.append(self.image)
        
    def Update(self, event):
        """ Update game panel graphics.
        """
        pass
    
    def OnKeyDown(self, event):
        """ Handle key pressed by the user.
        """
        keyCode = event.GetKeyCode()
        if keyCode == wx.WXK_NUMPAD6:
            self.image['x'] += 16
        elif keyCode == wx.WXK_NUMPAD4:
            self.image['x'] -= 16
        elif keyCode == wx.WXK_NUMPAD8:
            self.image['y'] -= 16
        elif keyCode == wx.WXK_NUMPAD2:
            self.image['y'] += 16
        self.Refresh()
        event.Skip()  
    
    def OnPaint(self, event):
        """ Paint on the GamePanel.
        """
        dc = wx.PaintDC(self)
        brush = wx.Brush("sky blue")
        dc.SetBackground(brush)
        dc.Clear()
        self.Paint()
        
    def Paint(self):
        dc = wx.PaintDC(self)
        for img in self.batch:
            dc.DrawBitmap(img['image'], img['x'], img['y'], True)
    
    
    
if __name__ == '__main__':
    app = wx.PySimpleApp(False)
    frame = MainFrame(parent=None, ID=-1)
    frame.Show()
    app.MainLoop()
    