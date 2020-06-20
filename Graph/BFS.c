#include <stdio.h>
#include <memory.h>
#include <stdlib.h>
#define MAX 10
#define FALSE 0
#define TRUE 1

typedef struct graphNode {
	int vertex;
	struct graphNode* link;
} graphNode;

typedef struct graph {
	int n;
	graphNode* list[MAX];
	int visited[MAX];
} graph;

typedef struct QNode {
	int data;
	struct QNode *link;
} QNode;

typedef struct {
	QNode *front, *rear;
} LQueue;

LQueue *createLinkedQueue()
{
	LQueue *LQ;
	LQ = (LQueue *)malloc(sizeof(LQueue));
	LQ->front = NULL;
	LQ->rear = NULL;
	return LQ;
}

int isEmpty(LQueue *LQ)
{
	if (LQ->front == NULL) {
		printf("\n Linked Queue is empty! \n");
		return 1;
	}
	else return 0;
}

void enQueue(LQueue *lq, int item)
{
	QNode *newNode = (QNode *)malloc(sizeof(QNode));
	newNode->data = item;
	newNode->link = NULL;
	if (lq->front == NULL) 
	{
		lq->front = newNode;
		lq->rear = newNode;
	}
	else
	{
		lq->rear->link = newNode;
		lq->rear = newNode;
	}
}

int deQueue(LQueue *lq)
{
	QNode *old = lq->front;
	int item;
	if (isEmpty(lq))
		return 0;
	else
	{
		item = old->data;
		lq->front = lq->front->link;
		if (lq->front == NULL)
			lq->rear = NULL;
		free(old);
		return item;
	}
}

void createGraph(graph* g)
{
	int v;
	g->n = 0;
	for (v = 0; v < MAX; v++)
	{
		g->visited[v] = FALSE;
		g->list[v] = NULL;
	}
}

void insertVertex(graph* g, int v)
{
	if (((g->n) + 1) > MAX)
	{
		printf("\n 그래프 정점의 개수를 초과하였습니다!");
		return;
	}
	g->n++;
}

void insertEdge(graph* g, int u, int v)
{
	graphNode* node;
	if (u >= g->n || v >= g->n) {
		printf("\n 그래프에 없는 정점입니다!");
		return;
	}
	node = (graphNode *)malloc(sizeof(graphNode));
	node->vertex = v;
	node->link = g->list[u];
	g->list[u] = node;
}

void print_adjList(graph* g)
{
	int i;
	graphNode* p;
	for (i = 0; i < g->n; i++) {
		printf("\n\t\t정점%c의 인접리스트", i + 65);
		p = g->list[i];
		while (p) {
			printf(" -> %c", p->vertex + 65);
			p = p->link;
		}
	}
}

void BFS_adjList(graph* g, int v)
{
	graphNode* w;
	LQueue* Q;		// 큐
	Q = createLinkedQueue();
	g->visited[v] = TRUE;
	printf(" %c", v + 65);
	enQueue(Q, v);
	while (!isEmpty(Q)) {
		v = deQueue(Q);
		for (w = g->list[v]; w; w = w->link)   // 인접정점이 있는 동안 수행
			if (!g->visited[w->vertex]) {      // 방문안한 인접정점에 대해서 수행
				g->visited[w->vertex] = TRUE;
				printf(" %c", w->vertex + 65);  // 정점 0~6을 A~G로 바꾸어서 출력
				enQueue(Q, w->vertex);
			}
	}
}

void main()
{
	int i;
	graph *G9;
	G9 = (graph *)malloc(sizeof(graph));

	createGraph(G9);
	for (i = 0; i < 7; i++)
		insertVertex(G9, i);
	insertEdge(G9, 0, 2);
	insertEdge(G9, 0, 1);
	insertEdge(G9, 1, 4);
	insertEdge(G9, 1, 3);
	insertEdge(G9, 1, 0);
	insertEdge(G9, 2, 4);
	insertEdge(G9, 2, 0);
	insertEdge(G9, 3, 6);
	insertEdge(G9, 3, 1);
	insertEdge(G9, 4, 6);
	insertEdge(G9, 4, 2);
	insertEdge(G9, 4, 1);
	insertEdge(G9, 5, 6);
	insertEdge(G9, 6, 5);
	insertEdge(G9, 6, 4);
	insertEdge(G9, 6, 3);
	printf("\n G9의 인접 리스트 ");
	print_adjList(G9);

	printf("\n\n///////////////\n\n너비우선탐색 >> ");
	BFS_adjList(G9, 0);

	getchar();
}