/// 1.
// Search
void initPlayer()

// Add above
#if defined(ENABLE_GAME_OPTION_ESCAPE)
PyObject* playerCanEscapeState(PyObject* poSelf, PyObject* poArgs)
{
	if (CPythonPlayer::Instance().IsDead() || CPythonPlayer::Instance().IsPoly())
		return Py_BuildValue("b", false);

	return Py_BuildValue("b", true);
}
#endif

/// 2.
// Search
		{ NULL, NULL, NULL },

// Add above
#if defined(ENABLE_GAME_OPTION_ESCAPE)
		{ "CanEscapeState", playerCanEscapeState, METH_VARARGS },
#endif
