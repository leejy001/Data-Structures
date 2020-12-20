#include <stdio.h>

int LSearch(int arr[], int len, int target)
{
	for (int i = 0; i < len; i++)
	{
		if (arr[i] == target)
			return i;
	}
	return -1;
}

int main(void)
{
	int arr[] = { 3,5,2,4,9 };
	int idx, num;
	while (1)
	{
		printf("input number (input 100 exit): ");
		scanf("%d", &num);
		if (num != 100)
		{
			idx = LSearch(arr, sizeof(arr) / sizeof(int), num);
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
}