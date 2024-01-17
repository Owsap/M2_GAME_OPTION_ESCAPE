/// 1.
// Search
struct command_info cmd_info[] =

// Add above
#if defined(__GAME_OPTION_ESCAPE__)
ACMD(do_escape);
#endif

/// 1.
// Search
	{ "\n", NULL, 0, POS_DEAD, GM_IMPLEMENTOR } /* 반드시 이 것이 마지막이어야 한다. */

// Add above
#if defined(__GAME_OPTION_ESCAPE__)
	{ "escape", do_escape, 0, POS_DEAD, GM_PLAYER },
#endif
