#include "lists.h"
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new = NULL;

	if (!head)
		return (NULL);

	
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	
	if (*head == NULL)
	{
		*head = new;
		(*head)->next = NULL;
		return (new);
	}
	while (temp->next != NULL)
	{
		if (new->n < temp->n)
		{
			new->next = temp;
			*head = new;
			return (new);
		}
		if (((new->n > temp->n) && (new->n < (temp->next)->n)) ||
		    (new->n == temp->n))
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		temp = temp->next;
	}
	
	temp->next = new;
	return (new);
}
