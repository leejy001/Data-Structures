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

typedef struct sNode {
	int data;
	struct sNode *link;
} sNode;

sNode* top;

void push(int item)
{
	sNode *temp = (sNode*)malloc(sizeof(sNode));
	temp->data = item;
	temp->link = top;
	top = temp;
}

int pop()
{
	int item;
	sNode* temp = top;

	if (top == NULL)
	{
		printf("\n\n Stack is empty! \n");
		return 0;
	}
	else
	{
		item = temp->data;
		top = temp->link;
		free(temp);
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

void DFS_adjList(graph* g, int v)
{
	graphNode* w;
	top = NULL;		// 스택 top
	push(v);
	g->visited[v] = TRUE;
	printf(" %c", v + 65);
	while (top != NULL) {
		w = g->list[v];
		while (w) {   // 인접정점이 있는 동안 수행
			if (!g->visited[w->vertex]) { // 방문안한 인접정점에 대해서 수행
				push(w->vertex);
				g->visited[w->vertex] = TRUE;
				printf(" %c", w->vertex + 65);  // 정점 0~6을 A~G로 바꾸어서 출력
				v = w->vertex;
				w = g->list[v];
			}
			else w = w->link;
		}
		v = pop();	// 방문안한 인접정점이 없으면 스택 pop !
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

	printf("\n\n///////////////\n\n깊이우선탐색 >> ");
	DFS_adjList(G9, 0);

	getchar();
}