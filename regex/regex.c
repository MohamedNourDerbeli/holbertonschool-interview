#include "regex.h"
/* fprintf */
#include <stdio.h>


/**
 * regexSubstrMatch - when in an open wildcard state after a `.*` in the regex
 *   pattern, regexSubstrMatch is called as a helper to regex_match to
 *   determine if there is a substring in str matching the substring in
 *   pattern immediately following the wildcard
 *
 * @str: string to scan
 *   - can be empty, or contain any ASCII values other than '.' or '*'
 * @pattern: regular expression pattern to match
 *   - can be empty, or contain any ASCII values
 * @s_match_end: pointer to first index in str after the **last** instance of a
 *   matching substring
 * @p_match_end: pointer to the first index in pattern after a substring
 *   bounded by an open wildcard to the left, and another wildcard or the end
 *   of the pattern on the right
 *
 * Return: 1 if matching substring found after wildcard, or 0 if not or on
 *   failure
 */
int regexSubstrMatch(char const *str, char const *pattern,
		     const char **s_match_end, const char **p_match_end)
{
	const char *p_match_start;
	int match = 0;

	if (!str || !pattern)
	{
		fprintf(stderr, "regexSubstrMatch: NULL parameter(s)\n");
		return (0);
	}

	while (*str)
	{
		/* skip past any chars not matching pattern after `.*` */
		while (*str && *str != *pattern)
			str++;

		p_match_start = pattern;

		/* attempt to match exit substring */
		while (*str == *pattern && *pattern != '.' &&
		       *pattern != '*' && *pattern != '\0' &&
		       *(pattern + 1) != '*')
		{
			str++;
			pattern++;
		}

		/* record end of current substr match in str */
		if (*pattern == '.' || *pattern == '*' ||
		    *pattern == '\0' || *(pattern + 1) == '*')
		{
			*p_match_end = pattern;
			*s_match_end = str;
			match = 1;
		}

		pattern = p_match_start;
	}

	return (match);
}


/**
 * regex_match - checks whether a given pattern matches a given string
 *
 * @str: string to scan
 *   - can be empty, or contain any ASCII values other than '.' or '*'
 * @pattern: regular expression pattern to match
 *   - can be empty, or contain any ASCII values
 *
 * Return: 1 on successful match, 0 if not or on failure
 */
int regex_match(char const *str, char const *pattern)
{
	char repeat;
	const char *s_match_end = NULL, *p_match_end = NULL;

	if (!str || !pattern)
	{
		fprintf(stderr, "regex_match: NULL parameter(s)\n");
		return (0);
	}

	while (*pattern)
	{
		if (*(pattern + 1) == '*')
		{
			if (*pattern == '.')
			{
				pattern += 2;
				if (regexSubstrMatch(str, pattern, &s_match_end,
						     &p_match_end))
				{
					str = s_match_end;
					pattern = p_match_end;
				}
			}
			else
			{
				repeat = *pattern;
				pattern += 2;
				while (*str == repeat)
					str++;
			}
		}
		else if (*pattern == '.' || *pattern == *str)
		{
			pattern++;
			str++;
		}
		else
			break;
	}
	return (!(*str) && !(*pattern));
}
