''' 1. '''
# Search @ class QuestionDialog.__init__
		self.__CreateDialog()

# Add below
		if app.ENABLE_GAME_OPTION_ESCAPE:
			self.accept_event_func = None
			self.cancel_event_func = None

''' 2. '''
# Search @ class QuestionDialog.__del__
		ui.ScriptWindow.__del__(self)

# Add below
		if app.ENABLE_GAME_OPTION_ESCAPE:
			self.accept_event_func = None
			self.cancel_event_func = None

''' 3. '''
# Search @ class QuestionDialog.SAFE_SetAcceptEvent
		self.acceptButton.SAFE_SetEvent(event)

# Add above
		if app.ENABLE_GAME_OPTION_ESCAPE:
			self.accept_event_func = ui.__mem_func__(event)

''' 4. '''
# Search @ class QuestionDialog.SAFE_SetCancelEvent
		self.cancelButton.SAFE_SetEvent(event)

# Add above
		if app.ENABLE_GAME_OPTION_ESCAPE:
			self.cancel_event_func = ui.__mem_func__(event)

''' 5. '''
# Search @ class QuestionDialog.SetAcceptEvent
		self.acceptButton.SAFE_SetEvent(event)

# Add above
		if app.ENABLE_GAME_OPTION_ESCAPE:
			self.accept_event_func = event

''' 6. '''
# Search @ class QuestionDialog.SetCancelEvent
		self.cancelButton.SAFE_SetEvent(event)

# Add above
		if app.ENABLE_GAME_OPTION_ESCAPE:
			self.cancel_event_func = event

''' 7. '''
# Search @ class QuestionDialog.OnPressEscapeKey
		self.Close()
		return True

# Add above
		if app.ENABLE_GAME_OPTION_ESCAPE:
			if self.cancel_event_func:
				apply(self.cancel_event_func)
