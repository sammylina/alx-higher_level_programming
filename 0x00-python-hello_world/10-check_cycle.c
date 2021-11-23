#include "lists.h"

/**
 * check_cycle - check if there is cycle in list
 * @list: point to head of the list
 *
 * Return: 0 if no cycle and 1 if there is
 */

int check_cycle(listint_t *list)
{
	listint_t *current_node, *previous_node;

	current_node = list->next;
	previous_node = list;
	while (current_node)
	{
		if (previous_node->next == current_node)
		{
			return (1);
		}
		else
		{
			previous_node = current_node;
			current_node = current_node->next;
		}
	}
	return (0);
}
