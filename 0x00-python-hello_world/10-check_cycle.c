#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks for a cycle in a linked list
 * @list: linked list to check
 * Return: 0 if no cycle, 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	slow = list;
	fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
