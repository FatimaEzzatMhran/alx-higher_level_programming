#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a number into a sorted link
 * @head: stores the address of the pointer to the variable
 * @number: number to be inserted
 * Return: Allow success
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *before, *tmp, *first;
	int count = 0;
	
	first = *head;
	new = (listint_t *)malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	while (*head)
	{
		count++;
		if ((*head)->n > number)
		{
			if (count == 1)
			{
				*head = new;
				new->next = first;
				return (new);
			}
			else
			{
				tmp = *head;
				break;
			}
		}
		before = *head;
		*head = (*head)->next;
	}
	if (*head)
	{
		before->next = new;
		new->next = tmp;
	}
	else if (*head == NULL)
	{
		before->next = new;
		new->next = NULL;
	}
	*head = first;
	return (new);
}
