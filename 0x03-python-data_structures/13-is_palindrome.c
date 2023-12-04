#include "lists.h"

/**
 * is_palindrome - checks a single list if it is a palindrome
 * @head: pointer to pointer to the first element
 * Return: 0 if not palindrome, 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	size_t n = 0, i;
	listint_t *current = *head, *last = *head;
	int *arr;

	if (!(*head))
		return (1);
	while (last)
	{
		n++;
		last = last->next;
	}
	if (n <= 2)
		return (1);
	arr = malloc(n * sizeof(int));
	if (!arr)
		return (0);
	for (i = 0; i < n; i++)
	{
		arr[i] = current->n;
		current = current->next;
	}
	for (i = 0; i < n / 2; i++)
	{
		if (arr[i] != arr[n - 1 - i])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
