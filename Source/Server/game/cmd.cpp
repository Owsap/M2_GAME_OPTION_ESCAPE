/// 1.
// Search
struct command_info cmd_info[] =

// Add above
#if defined(__GAME_OPTION_ESCAPE__)
ACMD(do_escape);
#endif

/// 1.
// Search
	{ "\n", NULL, 0, POS_DEAD, GM_IMPLEMENTOR } /* �ݵ�� �� ���� �������̾�� �Ѵ�. */

// Add above
#if defined(__GAME_OPTION_ESCAPE__)
	{ "escape", do_escape, 0, POS_DEAD, GM_PLAYER },
#endif
