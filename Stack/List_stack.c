#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef int element;

typedef struct Node
{
	element data;
	struct Node *next;
} Node;

Node* top;

void push(element data)
{
	Node *cur = (Node *)malloc(sizeof(Node));
	cur->data = data;
	cur->next = top;
	top = cur;
}

element pop()
{
	Node* cur = top;
	element re;
	if (top == NULL)
	{
		printf("\n\n Stack is empty! \n");
		return 0;
	}
	else
	{
		re = cur->data;
		top = cur->next;
		free(cur);
		return re;
	}
}

element peek()
{
	element data;
	if (top == NULL)
	{
		printf("\n\n Stack is Empty!\n");
		return 0;
	}
	else
	{
		data = top->data;
		return data;
	}
}

void del()
{
	Node* cur;
	if (top == NULL)
	{
		printf("\n\n Stack is empty! \n");
	}
	else
	{
		cur = top;
		top = top->next;
		free(cur);
	}
}

void printStack()
{
	Node *ptr = top;
	printf("\n Stack [");
	while (ptr)
	{
		printf(" %d", ptr->data);
		ptr = ptr->next;
	}
	printf("]\n");
}

void main()
{
	element item;
	top = NULL;
	printf("\n** 순차 스택 연산 **\n");
	printStack();
	push(1);
	printStack();
	push(2);
	printStack();
	push(3);
	printStack();

	item = peek();
	printStack();
	printf("\t peek top => %d", item);

	del();
	printStack();

	item = pop();
	printStack();
	printf("\t pop top => %d", item);

	item = pop();
	printStack();
	printf("\t pop top => %d", item);

	pop();

	getchar();
}