''' 1. '''
# Add at the top of the file
if app.ENABLE_GAME_OPTION_ESCAPE:
	import uiEscapePopup

''' 2. '''
# Search @ class Interface.__init__
		event.SetInterfaceWindow(self)

# Add above
		if app.ENABLE_GAME_OPTION_ESCAPE:
			self.wndEscapePopup = None

''' 3. '''
# Search @ class Interface.Close
		self.wndChatLog.Destroy()

# Add above
		if app.ENABLE_GAME_OPTION_ESCAPE:
			if self.wndEscapePopup:
				self.wndEscapePopup.Destroy()
				del self.wndEscapePopup

''' 4. '''
# Search
if __name__ == "__main__":

# Add above
	if app.ENABLE_GAME_OPTION_ESCAPE:
		def IsEscapeQuestionPopupOpen(self):
			return self.wndEscapePopup and self.wndEscapePopup.IsEscapeQuestionPopupOpen()

		def OpenEscapeQuestionPopup(self):
			if not self.wndEscapePopup:
				self.wndEscapePopup = uiEscapePopup.EscapeManager()
			self.wndEscapePopup.OpenEscapePopup()

''' 5. '''
# Search
		self.dlgSystem.SetOpenHelpWindowEvent(ui.__mem_func__(self.OpenHelpWindow))

# Add below
		if app.ENABLE_GAME_OPTION_ESCAPE:
			self.dlgSystem.BindInterface(self)
