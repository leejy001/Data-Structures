#include <stdio.h>
#include <stdlib.h>

typedef struct _node
{
	int data;
	struct _node * next;
} Node;

int main(void)
{
	Node * head = NULL;
	Node * tail = NULL;
	Node * cur = NULL;

	Node * newNode = NULL;
	int readData;
	// Add Dummy node
	head = (Node*)malloc(sizeof(Node));
	tail = head;
	// Data input
	while (1)
	{
		printf("input (exit:0): ");
		scanf("%d", &readData);
		if (readData < 1)
			break;

		// Add Node
		newNode = (Node*)malloc(sizeof(Node));
		newNode->data = readData;
		newNode->next = NULL;

		tail->next = newNode;
		tail = newNode;
	}
	printf("\n");

	// output Node
	printf("Full output of data entered \n");
	if (head == NULL)
	{
		printf("Saved number does not exist... \n");
	}
	else
	{
		cur = head;

		while (cur->next != NULL) 
		{
			cur = cur->next;
			printf("%d  ", cur->data);
		}
	}
	printf("\n\n");

	// Delete Node
	if (head == NULL)
	{
		return 0; 
	}
	else
	{
		Node * delNode = head;
		Node * delNextNode = head->next;   

		while (delNextNode != NULL)   
		{
			delNode = delNextNode;
			delNextNode = delNextNode->next;

			printf("%d delete.. \n", delNode->data);
			free(delNode); 
		}
	}

	return 0;
}