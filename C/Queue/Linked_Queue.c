#include <stdio.h>
#include <malloc.h>


typedef char element;
typedef struct QNode{
	element data;
	struct QNode *link;
}QNode;

typedef struct {
	QNode *front, *rear;
}LQueueType;

LQueueType *createLinkedQueue()
{
	LQueueType *LQ;
	LQ = (LQueueType*)malloc(sizeof(LQueueType));
	LQ->front = NULL;
	LQ->rear = NULL;
	return LQ;
}

int isEmpty(LQueueType *LQ)
{
	if (LQ->front == NULL)
	{
		printf("\n Linked Queue is empty! \n");
		return 1;
	}
	else
		return 0;
}

void enQueue(LQueueType *LQ, element item)
{
	QNode *newNode = (QNode*)malloc(sizeof(QNode));
	newNode->data = item;
	newNode->link = NULL;
	if (LQ->front == NULL)
	{
		LQ->front = newNode;
		LQ->rear = newNode;
	}
	else
	{
		LQ->rear->link = newNode;
		LQ->rear = newNode;
	}
}

element deQueue(LQueueType *LQ)
{
	QNode *old = LQ->front;
	element item;
	if (isEmpty(LQ))
		return 0;
	else
	{
		item = old->data;
		LQ->front = LQ->front->link;
		if (LQ->front == NULL)
			LQ->rear = NULL;
		free(old);
		return item;
	}
}

element peek(LQueueType *LQ)
{
	element item;
	if (isEmpty(LQ))
		return 0;
	else
	{
		item = LQ->front->data;
		return item;
	}
}

void printQ(LQueueType *LQ)
{
	QNode *temp = LQ->front;
	printf("\n Linked Queue : [");
	while (temp)
	{
		printf("%3c", temp->data);
		temp = temp->link;
	}
	printf(" ]");
}

int main(void)
{
	LQueueType *Q1 = createLinkedQueue();
	element data;
	enQueue(Q1, 'A');
	printQ(Q1);
	enQueue(Q1, 'B');
	printQ(Q1);
	deQueue(Q1);
	printQ(Q1);
	enQueue(Q1, 'C');
	printQ(Q1);
	data = peek(Q1);
	printf("\n peek item : %c", data);
	deQueue(Q1);
	printQ(Q1);
	deQueue(Q1);
	printQ(Q1);

	getchar();
	return 0;
}