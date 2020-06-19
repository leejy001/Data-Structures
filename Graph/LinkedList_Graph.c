#include <stdio.h>
#include <stdlib.h>
#define MAX 30

typedef struct graphNode {
	int vertex;
	struct graphNode* link;
} graphNode;

typedef struct graph {
	int n;
	graphNode* list[MAX];
} graph;

void createGraph(graph *g)
{
	int v;
	g->n = 0;
	for (v = 0; v < MAX; v++)
		g->list[v] = NULL;
}

void insertVertex(graph *g, int v)
{
	if (((g->n) + 1) > MAX)
	{
		printf("\n 그래프 정점의 개수를 초과하였습니다!");
		return;
	}
	g->n++;
}

void insertEdge(graph *g, int u, int v)
{
	graphNode* node;
	if (u >= g->n || v >= g->n)
	{
		printf("\n 그래프에 없는 정점입니다!");
		return;
	}
	node = (graphNode*)malloc(sizeof(graphNode));
	node->vertex = v;
	node->link = g->list[u];
	g->list[u] = node;
}

void print_adjList(graph* g)
{
	int i;
	graphNode *p;
	for (i = 0; i < g->n; i++)
	{
		printf("\n\t\t정점 %c의 인접리스트", i + 65);
		p = g->list[i];
		while (p) {
			printf(" -> %c", p->vertex + 65);
			p = p->link;
		}
	}
}

void main()
{
	int i;
	graph *G1, *G2, *G3, *G4;
	G1 = (graph *)malloc(sizeof(graph));
	G2 = (graph *)malloc(sizeof(graph));
	G3 = (graph *)malloc(sizeof(graph));
	G4 = (graph *)malloc(sizeof(graph));

	createGraph(G1);
	createGraph(G2);
	createGraph(G3);
	createGraph(G4);

	for (i = 0; i < 4; i++)
		insertVertex(G1, i);
	insertEdge(G1, 0, 3);
	insertEdge(G1, 0, 1);
	insertEdge(G1, 1, 3);
	insertEdge(G1, 1, 2);
	insertEdge(G1, 1, 0);
	insertEdge(G1, 2, 3);
	insertEdge(G1, 2, 1);
	insertEdge(G1, 3, 2);
	insertEdge(G1, 3, 1);
	insertEdge(G1, 3, 0);
	printf("\n G1의 인접 리스트");
	print_adjList(G1);

	for (i = 0; i < 3; i++)
		insertVertex(G2, i);
	insertEdge(G2, 0, 2);
	insertEdge(G2, 0, 1);
	insertEdge(G2, 1, 2);
	insertEdge(G2, 1, 0);
	insertEdge(G2, 2, 1);
	insertEdge(G2, 2, 0);
	printf("\n\n G2의 인접 리스트");
	print_adjList(G2);

	for (i = 0; i < 4; i++)
		insertVertex(G3, i);
	insertEdge(G3, 0, 3);
	insertEdge(G3, 0, 1);
	insertEdge(G3, 1, 3);
	insertEdge(G3, 1, 2);
	insertEdge(G3, 2, 3);
	printf("\n\n G3의 인접 리스트");
	print_adjList(G3);

	for (i = 0; i < 3; i++)
		insertVertex(G4, i);
	insertEdge(G4, 0, 2);
	insertEdge(G4, 0, 1);
	insertEdge(G4, 1, 2);
	insertEdge(G4, 1, 0);
	printf("\n\n G4의 인접 리스트");
	print_adjList(G4);

	getchar();
}