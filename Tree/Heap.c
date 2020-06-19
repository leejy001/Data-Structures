#include <stdio.h>
#include <stdlib.h>
#define MAX 100

typedef struct Heap {
	int heap[MAX];
	int heap_size;
} heap;

heap *createHeap()
{
	heap *h = (heap *)malloc(sizeof(heap));
	h->heap_size = 0;
	return h;
}

void insertHeap(heap *h, int item)
{
	int i;
	h->heap_size = h->heap_size + 1; // 힙 크기를 하나 증가
	i = h->heap_size;
	// i가 루트 노드가 아니고, 삽입할 item의 값이 i의 부모 노드보다 크면
	while ((i != 1) && (item > h->heap[i / 2])) {
		//i번째 노드와 부모 노드를 교환한다.
		h->heap[i] = h->heap[i / 2];
		//한 레벨 위로 올라간다.
		i /= 2;
	}
	h->heap[i] = item; //새로운 노드를 삽입
}

int deleteHeap(heap *h)
{
	int parent, child;
	int item, temp;
	item = h->heap[1]; // 루트 노드 값 반환 위해 item 할당
	temp = h->heap[h->heap_size]; // 마지막 노드를 temp에 할당
	h->heap_size = h->heap_size - 1; //힙 크기를 하나 감소
	parent = 1;
	child = 2;
	while (child <= h->heap_size) {
		// 현재 노드의 자식 노드 중 더 큰 자식 노드를 찾는다. 
		//(루트 노드의 왼쪽 자식 노드(index: 2)부터 비교 시작)
		if ((child < h->heap_size) && h->heap[child] < h->heap[child + 1])
			child++;
		// 더 큰 자식 노드보다 마지막 노드가 크면, 반복문 중지
		if (temp >= h->heap[child])
			break;

		// 더 큰 자식 노드보다 마지막 노드가 작으면, 부모 노드와 더 큰 자식 노드를 교환
		h->heap[parent] = h->heap[child];
		parent = child; // 한 단계 아래로 이동
		child = child * 2;
	}
	h->heap[parent] = temp; // 마지막 노드를 재구성한 위치에 삽입
	return item; // 최대값을 반환
}

printHeap(heap *h)
{
	int i;
	printf("Heap : ");
	for (i = 1; i <= h->heap_size; i++)
		printf("[%d] ", h->heap[i]);
}

void main()
{
	int i, n, item;
	heap *h = createHeap();
	insertHeap(h, 10);
	insertHeap(h, 45);
	insertHeap(h, 19);
	insertHeap(h, 11);
	insertHeap(h, 96);

	printHeap(h);

	n = h->heap_size;

	for (i = 1; i <= n; i++)
	{
		item = deleteHeap(h);
		printf("\n delete : [%d] ", item);
	}
	getchar();
}