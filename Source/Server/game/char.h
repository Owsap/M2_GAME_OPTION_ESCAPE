/// 1.
// Search
};

ESex GET_SEX(LPCHARACTER ch);

// Add above
#if defined(__GAME_OPTION_ESCAPE__)
public:
	void SetEscapeCooltime(const DWORD dwTime) { m_dwEscapeCooltime = dwTime; }
	DWORD GetEscapeCooltime() const { return m_dwEscapeCooltime; }
private:
	DWORD m_dwEscapeCooltime;
#endif
