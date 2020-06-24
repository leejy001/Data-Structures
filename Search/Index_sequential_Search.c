#include <stdio.h>
#define SIZE 3

typedef struct {
	int index;
	int key;
} btable;

btable indexTable[SIZE];

void sequentialSearch(int a[], int begin, int end, int key)
{
	int i = begin;
	printf("\n %d를 검색하여라! ->", key);
	while (i < end && a[i] < key)
		i++;
	if (a[i] == key)
		printf("%d번째에 검색 성공!\n\n", (i - begin) + 1);
	else
		printf("%d번째에 검색 실패!\n\n", (i - begin) + 1);
}

void makeIndexTable(int a[], int size)
{
	int i, n;
	n = size / SIZE;	// 인덱스 테이블에 들어가는 배열 원소의 간격 계산
	if (size%SIZE > 0)
		n = n + 1;

	for (i = 0; i < SIZE; i++) {	// 인덱스 테이블 채우기
		indexTable[i].index = i * n;
		indexTable[i].key = a[i*n];
	}
}

int indexSearch(int a[], int n, int key)
{
	int i, begin, end;
	if (key < a[0] || key > a[n - 1])
		return -1;

	// 해당 키를 포함하는 범위에 위치한 인덱스 테이블을 구함
	for (i = 0; i < SIZE; i++)
	{
		// 키 값이 포함하는 인덱스 테이블의 범위가 존재할 경우
		if ((indexTable[i].key <= key) && (indexTable[i + 1].key > key)) {
			begin = indexTable[i].index;
			end = indexTable[i + 1].index;
			break;
		}
	}
	//인덱스 테이블이 없다면
	if (i == SIZE) {
		begin = indexTable[i - 1].index;
		end = n;
	}
	sequentialSearch(a, begin, end, key);
}

void main()
{
	int a[] = { 1,2,8,9,11,19,29 };
	int n = 7;
	printf("\n\t<< 색인 순차 검색 >> \n");
	makeIndexTable(a, n);
	indexSearch(a, n, 9);
	indexSearch(a, n, 6);
}