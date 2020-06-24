#include <stdio.h>

int BSearch(int arr[], int len, int target)
{
	int first = 0;
	int last = len - 1;
	int mid;

	while (first <= last)
	{
		mid = (first + last) / 2;

		if (target == arr[mid])
			return mid;
		else
		{
			if (target < arr[mid])
				last = mid - 1;
			else
				first = mid + 1;
		}
	}
	return -1;
}

int main(void)
{
	int arr[] = { 1,3,5,7,9 };
	int idx, num;
	while (1)
	{
		scanf("%d", &num);
		printf("를 검색하라! (100 일때 종료) ->> ");
		if (num != 100)
		{
			idx = BSearch(arr, sizeof(arr) / sizeof(int), num);
			if (idx == -1)
				printf("검색 실패...\n");
			else
				printf("%d번째에 검색 성공!\n", idx);
		}
		else
		{
			printf("End...");
			break;
		}
	}
	return 0;
}