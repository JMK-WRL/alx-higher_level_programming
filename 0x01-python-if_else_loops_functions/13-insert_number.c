#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserting a number to a linked list
 * @head: A pointer to the head of the linked list
 * @number: number to be inserted
 * Return: NULL if function fails, otherwise a pointer
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;
	
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
	{
		node = node->next;
	}

	new->next = node->next;
	node->next = new;

	return (new);
}
