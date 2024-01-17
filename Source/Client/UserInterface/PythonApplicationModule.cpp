/// 1.
// Search
	PyModule_AddIntConstant(poModule, "CAMERA_STOP", CPythonApplication::CAMERA_STOP);

// Add below
#if defined(ENABLE_GAME_OPTION_ESCAPE)
	PyModule_AddIntConstant(poModule, "ENABLE_GAME_OPTION_ESCAPE", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_GAME_OPTION_ESCAPE", 0);
#endif
