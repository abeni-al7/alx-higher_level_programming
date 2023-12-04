#include "lists.h"

/**
 * is_palindrome - checks a single list if it is a palindrome
 * @head: pointer to pointer to the first element
 * Return: 0 if not palindrome, 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	unsigned int n = 0, i = 0;
	listint_t *current = *head, *last = *head;
	int *arr;

	if ((*head) == NULL)
		return (1);
	while (last != NULL)
	{
		n++;
		last = last->next;
	}
	if (n == 1 || n == 2 || n == 0)
		return (1);
	arr = malloc(n * sizeof(int));
	if (arr == NULL)
		return (0);
	while (i < n)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}
	for (i = 0, n -= 1; i < (n + 1) / 2; i++, n--)
	{
		if (arr[i] != arr[n])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
