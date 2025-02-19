#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
int check_cycle(listint_t *list){
    const listint_t *current;
    current = list;
    while (current != NULL && current->next != NULL){
        if (current->next == list){
            return 1;
            }
            current = current->next;
            }
            return 0;
}
