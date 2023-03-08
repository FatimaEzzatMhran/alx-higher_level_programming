#include "lists.h"
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *newNode = NULL;

	if (!head)
		return (NULL);

	/* malloc new node */
	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;

	/* if no linked list, insert node as the only member */
	if (*head == NULL)
	{
		*head = newNode;
		(*head)->next = NULL;
		return (newNode);
	}
	while (temp->next != NULL)
	{
		if (newNode->n < temp->n)
		{
			newNode->next = temp;
			*head = newNode;
			return (newNode);
		}
		if (((newNode->n > temp->n) && (newNode->n < (temp->next)->n)) ||
		    (newNode->n == temp->n))
		{
			newNode->next = temp->next;
			temp->next = newNode;
			return (newNode);
		}
		temp = temp->next;
	}
	/* if new node is greatest and never inserted, insert now */
	temp->next = newNode;
	return (newNode);
}
