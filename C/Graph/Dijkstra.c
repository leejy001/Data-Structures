#include<stdio.h>
#include<limits.h>

#define TRUE 1
#define FALSE 0
#define MAX 5
#define INF 10000

int weight[MAX][MAX] = {
	{0,10,5,INF,INF},
	{INF,0,2,1,INF},
	{INF,3,0,9,2},
	{INF,INF,INF,0,4},
	{7,INF,INF,6,0}
};

int distance[MAX];	// 시작 정점으로부터 최단경로 거리
int found[MAX];		// 방문 정점 표시

//최소 거리 같는 다음 정점 찾기
int next(int n)
{
	int i, min, minPos;
	min = INT_MAX;
	minPos = -1;
	for (i = 0; i < n; i++) {
		if ((distance[i] < min) && !found[i]) {
			min = distance[i];
			minPos = i;
		}
	}
	return minPos;
}

int printStep(int step)
{
	int i;
	printf("\n %3d 단계 : S={", step);
	for (i = 0; i < MAX; i++) 
		if (found[i] == TRUE)
			printf("%3c", i + 65);
	
	if (step < 1)
		printf(" } \t\t\t");
	else if (step < 4)
		printf(" } \t\t");
	else
		printf(" } \t");

	printf(" distance :[ ");
	for (i = 0; i < MAX; i++)
	{
		if (distance[i] == 10000)
			printf("%4c", '*');
		else
			printf("%4d", distance[i]);
	}
	printf("%4c", ']');
	return ++step;
}


void shortestPath(int start, int n)
{
	int i, u, w, step = 0;
	for (i = 1; i < n; i++) {
		distance[i] = weight[start][i];
		found[i] = FALSE;
	}

	found[start] = TRUE;	// 시작 정점 방문 표시
	distance[start] = 0;	// 시작 정점 최단 경로 0으로 설정
	step = printStep(0);	// 0단계 상태를 출력

	for (i = 0; i < n - 1; i++) {
		u = next(n);		// 최단 경로를 만드는 다음 정점 u 찾기
		found[u] = TRUE;	// 정점 u를 집합 S에 추가
		for (w = 0; w < n; w++)
		{
			if (!found[w])	// u에 인접하며 집합 found에 포함되지 않은 경우
			{
				if (distance[u] + weight[u][w] < distance[w])
					distance[w] = distance[u] + weight[u][w];	// 경로 길이 수정
			}
		}
		step = printStep(step);
	}
}

void main()
{
	int i, j;
	printf("\n ********** 가중치 인접 행렬 **********\n\n");
	for (i = 0; i < MAX; i++) { 
		for (j = 0; j < MAX; j++) { 
			if (weight[i][j] == 10000) 
				printf("%4c", '*'); 
			else 
				printf("%4d", weight[i][j]); 
		} 
		printf("\n\n"); 
	}
	printf("\n ********** 다익스트라 최단 경로 구하기 **********\n\n"); 
	shortestPath(0, MAX);
	getchar();
}