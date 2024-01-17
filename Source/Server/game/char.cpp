/// 1.
// Search @ void CHARACTER::Initialize
	m_dwLastPlay = 0;

// Add below
#if defined(__GAME_OPTION_ESCAPE__)
	m_dwEscapeCooltime = 0;
#endif
