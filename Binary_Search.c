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
		printf("input number (input 100 exit) :");
		scanf("%d", &num);
		if (num != 100)
		{
			idx = BSearch(arr, sizeof(arr) / sizeof(int), num);
			if (idx == -1)
				printf("Search fail...\n");
			else
				printf("Target save index: %d\n", idx);
		}
		else
		{
			printf("End...");
			break;
		}
	}
	return 0;
}