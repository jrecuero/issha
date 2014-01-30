import wx

#------------------------------------------------------------------------------
class Cell(object):
    """ Cell class contains all information related with a graphical cell.

    Cell contains information about the graphical cell and game information
    related with that position.
    """

    def __init__(self, x, y, gX=None, gY=None):
        """ Cell class initialization method.
        """
        self.setPos(x, y)
        self.setGPos(gX, gY)

    def setPost(self, x, y):
        """ Set cell in game position.

        :type x: int
        :param x: In game x-coordinate.

        :type y: int
        :param y: In game y-coordinate.
        """
        self.pos = (x, y)

    def setGPos(self, gX, gY):
        """ Set cell graphical position.

        :type gX: int
        :param gX: Graphical x-coordinate.

        :type gY: int
        :param gY: Graphical y-coordinate.
        """
        self.gpos = (gX, gY)

    @property
    def x(self):
        """ Get in game x-coordinate.

        :rtype: int
        :return: In game x-coordinate.
        """
        return self.pos[0]

    @property
    def y(self):
        """ Get in game y-coordinate.

        :rtype: int
        :return: In game y-coordinate.
        """
        return self.pos[1]

    @property
    def gx(self):
        """ Get graphical x-coordinate.

        :rtype: int
        :return: Graphical x-coordinate.
        """
        return self.gpos[0]

    @property
    def gy(self):
        """ Get graphical y-coordinate.

        :rtype: int
        :return: Graphical y-coordinate.
        """
        return self.gpos[1]


#------------------------------------------------------------------------------
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
        upButton       = self.createButton('Up', self.OnUpButton)
        leftButton     = self.createButton('Left', self.OnLeftButton)
        rightButton    = self.createButton('Right', self.OnRightButton)
        downButton     = self.createButton('Down', self.OnDownButton)
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
    
    def OnUpButton(self, event):
        self.gamePanel.moveMainActor(wx.UP)
    
    def OnDownButton(self, event):
        self.gamePanel.moveMainActor(wx.DOWN)
    
    def OnRightButton(self, event):
        self.gamePanel.moveMainActor(wx.RIGHT)
    
    def OnLeftButton(self, event):
        self.gamePanel.moveMainActor(wx.LEFT)

        
#------------------------------------------------------------------------------
class GamePanel(wx.Panel):
    """ Class with the Main Game Panel.
    """
    
    def __init__(self, parent):
        """ Class initialization method. It display main game elements.
        """
        wx.Panel.__init__(self, parent)
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
    
    def moveMainActor(self, keyCode):
        """ Handle key pressed by the user.
        """
        if keyCode == wx.RIGHT:
            self.image['x'] += 16
        elif keyCode == wx.LEFT:
            self.image['x'] -= 16
        elif keyCode == wx.UP:
            self.image['y'] -= 16
        elif keyCode == wx.DOWN:
            self.image['y'] += 16
        self.Refresh()
    
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
    
