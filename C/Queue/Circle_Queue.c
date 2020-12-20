#include <stdio.h>
#include <stdlib.h>
#define Q_SIZE 4


typedef char element;
typedef struct {
	element queue[Q_SIZE];
	int front, rear;
}QueueType;

QueueType *createQueue()
{
	QueueType *Q;
	Q = (QueueType*)malloc(sizeof(QueueType));
	Q->front = 0;
	Q->rear = 0;
	return Q;
}

int isEmpty(QueueType *Q)
{
	if (Q->front == Q->rear)
	{
		printf("\n Queue is empty! \n");
		return 1;
	}
	else
		return 0;
}

int isFull(QueueType *Q)
{
	if (((Q->rear + 1) % Q_SIZE) == Q->front)
	{
		printf("\n Queue is full! \n");
		return 1;
	}
	else
		return 0;
}

void enQueue(QueueType *Q, element item)
{
	if (isFull(Q))
		exit(1);
	else
	{
		Q->rear = (Q->rear + 1) % Q_SIZE;
		Q->queue[Q->rear] = item;
	}
}

void deQueue(QueueType *Q)
{
	if (isEmpty(Q))
		exit(1);
	else
	{
		Q->front = (Q->front + 1) % Q_SIZE;
		return Q->queue[Q->front];
	}
}

int del(QueueType *Q)
{
	if (isEmpty(Q))
		exit(1);
	else
		Q->front = (Q->front + 1) % Q_SIZE;
}

element peek(QueueType *Q)
{
	if (isEmpty(Q))
		exit(1);
	else
		return Q->queue[(Q->front + 1) % Q_SIZE];
}

void printQ(QueueType *Q)
{
	int i, first, last;
	first = (Q->front + 1) % Q_SIZE;
	last = (Q->rear + 1) % Q_SIZE;
	printf("\n Circular Queue : [");
	i = first;
	while (i != last)
	{
		printf("%3c", Q->queue[i]);
		i = (i + 1) % Q_SIZE;
	}
	printf(" ]");
}

int main(void)
{
	QueueType *Q1 = createQueue();
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