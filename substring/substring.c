#include "substring.h"
/* strlen strncmp */
#include <string.h>
/* calloc malloc free */
#include <stdlib.h>
/* fprintf */
#include <stdio.h>


/**
 * find_substring - Finds all the possible substrings containing a list of
 *   words within a given string. A valid substring of `s` is the concatenation
 *   of each word in `words` exactly once and without any intervening
 *   characters
 *
 * @s: string to scan
 * @words: array of words all substrings must be a concatenation of to be
 *   valid; all words in this array are the same length
 * @nb_words: number of elements in the array words
 * @n: holds the address at which to store the number of elements in the
 *   returned array.
 *
 * Return: an allocated array storing each index in s at which a substring was
 *   found, or NULL on failure
 */
int *find_substring(char const *s, char const **words, int nb_words, int *n)
{
	int *matched_word, *indices;
	int i, j, k, l, _n, s_len, word_len, any_word_match, substr_match;
	int _indices[50] = {-1};

	if (!s || !words || !*words || !n)
	{
		fprintf(stderr, "find_substring: NULL parameter(s)\n");
		return (NULL);
	}

	s_len = strlen(s);
	word_len = strlen(words[0]);
	matched_word = malloc(nb_words * sizeof(int));
	if (!matched_word)
	{
		fprintf(stderr, "find_substring: malloc failure\n");
		return (NULL);
	}

	for (i = 0, k = 0, _n = 0; i < s_len;)
	{
		substr_match = 0;
		bzero(matched_word, nb_words * sizeof(int));
		l = i;
		do {
			for (j = 0, any_word_match = 0; j < nb_words; j++)
			{
				if (!matched_word[j])
				{
					if (strncmp(words[j],
						    s + l, word_len) == 0)
					{
						any_word_match = 1;
						matched_word[j] = 1;
						l += word_len;
					}
				}
			}
		} while (any_word_match);

		for (j = 0, substr_match = 1; j < nb_words; j++)
			substr_match &= matched_word[j];

		if (substr_match)
		{
			_n++;
			_indices[k] = i;
			k++;
			i += word_len;
		}
		else
			i++;
	}
	free(matched_word);

	indices = malloc(_n * sizeof(int));
	if (!indices)
	{
		fprintf(stderr, "find_substring: malloc failure\n");
		return (NULL);
	}
	for (k = 0; k < _n; k++)
		indices[k] = _indices[k];

	*n = _n; /* n indirectly modifided to avoid -Werror=unused-value */
	return (indices);
}
