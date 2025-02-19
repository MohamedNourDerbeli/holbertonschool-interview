#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if there is a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	const listint_t *current;

	if (list == NULL || list->next == NULL)
		return (0);

	current = list;
	while (current != NULL && current->next != NULL)
	{
		if (current->next == list)
			return (1); /* Cycle detected */
		current = current->next;
	}

	return (0); /* No cycle found */
}
