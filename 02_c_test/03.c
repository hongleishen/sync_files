#define n_my_dbg(format, ...)              \
    do {                                   \
		if (g_cmd_open_my_dbg) { \
			const char *new_format_ = format;  \
			while (*new_format_ == '\n') {     \
				new_format_++;                 \
				printf("\n");                  \
			}                                  \
			printf("[dbg: %s, %s, %d] ", __FILE__, __func__, __LINE__); \
			printf(new_format_, ##__VA_ARGS__);\
		} \
    } while (0)




#if 1
/* Show a message if DEBUG is defined in a file */
#define debug(fmt, args...)			\
	debug_cond(_DEBUG, fmt, ##args)

#else
    #define shl_debug_cond(cond, fmt, args...)			\
	do {						\
		if (1)				\
			printf(pr_fmt(fmt), ##args);	\
	} while (0)

#define debug(fmt, args...)			\
	shl_debug_cond(_DEBUG, fmt, ##args)

#endif