#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a list contains a cycle
 * @list: linked list to check
 * Return: 1 ( if if its a cycle) 0 (NOT)
 */

int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}

		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
