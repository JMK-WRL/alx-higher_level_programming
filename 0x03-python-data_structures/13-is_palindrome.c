#include "lists.h"
#include <stddef.h>

/**
 * reverse_listint - function that reverses a linked list
 * @head: pointer to first node
 * Return: pointer to first node in new list
 */

void reverse_listint(listint_t **head)
{
	listint_t *p = NULL;
	listint_t *now = *head;
	listint_t *next = NULL;

	while (now)
	{
		next = now->next;
		now->next = p;
		p = now;
		now = next;
	}

	*head = p;
}

/**
 * is_palindrome - function that checked list if its a palindrome
 * @head: double pointer
 * Return: 1 (success) - palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *a = *head;
	listint_t *f = *head;
	listint_t *temp = *head;
	listint_t *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return(1);
	while (1)
	{
		f = f->next->next;
		if(!f)
		{
			dup = a->next;
			break;
		}
		if (!f->next)
		{
			dup = a->next->next;
			break;
		}
		a = a->next;
	}
	
	reverse_listint(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	if (!dup)
		return (1);
	return (0);
}
