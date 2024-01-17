''' 1. '''
# Add to the top of the file
if app.ENABLE_GAME_OPTION_ESCAPE:
	import uiToolTip, wndMgr

''' 2. '''
# Search @ class SystemDialog.__init__
			self.__Initialize()

# Add below
		if app.ENABLE_GAME_OPTION_ESCAPE:
			self.tooltip = uiToolTip.ToolTip()

''' 3. '''
# Search @ class SystemDialog.__del__
		ui.ScriptWindow.__del__(self)

# Add below
		if app.ENABLE_GAME_OPTION_ESCAPE:
			del self.tooltip

''' 4. '''
# Search @ class SystemDialog.__Initialize
		self.gameOptionDlg = None

# Add below
		if app.ENABLE_GAME_OPTION_ESCAPE:
			self.interface = None
			self.is_show_tooltip = False

''' 5. '''
# Search @ class SystemDialog.__LoadSystemMenu_Default
		self.GetChild("cancel_button").SAFE_SetEvent(self.Close)

# Add below
		if app.ENABLE_GAME_OPTION_ESCAPE:
			self.GetChild("escape_button").SAFE_SetEvent(self.__ClickEscapeButton)
			self.GetChild("escape_button").ShowToolTip = lambda arg = localeInfo.OPTION_ESCAPE_SYSTEM_BUTTON_TOOLTIP : self.OverInToolTipButton(arg)
			self.GetChild("escape_button").HideToolTip = lambda : self.OverOutToolTipButton()

''' 6. '''
# Add to the bottom of the file inside the class SystemDialog
	if app.ENABLE_GAME_OPTION_ESCAPE:
		def BindInterface(self, interface):
			from _weakref import proxy
			self.interface = proxy(interface)

	if app.ENABLE_GAME_OPTION_ESCAPE:
		def __ClickEscapeButton(self):
			self.Close()

			if self.interface and not self.interface.IsEscapeQuestionPopupOpen():
				self.interface.OpenEscapeQuestionPopup()

		def ToolTipProgress(self):
			if self.is_show_tooltip:
				pos_x, pos_y = wndMgr.GetMousePosition()
				self.tooltip.SetToolTipPosition(pos_x + 50, pos_y + 50)

		def OverInToolTipButton(self, arg):
			arglen = len(str(arg))
			pos_x, pos_y = wndMgr.GetMousePosition()

			self.tooltip.ClearToolTip()
			self.tooltip.SetThinBoardSize(11 * arglen)
			self.tooltip.SetToolTipPosition(pos_x + 50, pos_y + 50)
			self.tooltip.AppendTextLine(arg, 0xffffffff)
			self.tooltip.Show()
			self.is_show_tooltip = True

		def OverOutToolTipButton(self):
			self.tooltip.Hide()
			self.is_show_tooltip = False

		def OnUpdate(self):
			self.ToolTipProgress()
