#include "lists.h"

/**
 * insert_node - inserts a node to a sorted linked list
 * @head: pointer to pointer to the first element of linked list
 * @number: number to be added to the linked list
 * Return: the address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *temp;
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
		*head = new;
	if (number < (*head)->n)
	{
		temp = *head;
		new->next = temp;
		*head = new;
		return (new);
	}

	while (current->next != NULL && current->next->n < number)
		current = current->next;
	if (current->next == NULL)
	{
		current->next = new;
		new->next = NULL;
		return (new);
	}
	temp = current->next;
	current->next = new;
	new->next = temp;
	return (new);
}
