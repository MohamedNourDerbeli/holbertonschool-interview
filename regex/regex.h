#ifndef REGEX_H
#define REGEX_H

int regexSubstrMatch(char const *str, char const *pattern,
		     const char **s_match_end, const char **p_match_end);
int regex_match(char const *str, char const *pattern);

#endif /* REGEX_H */
