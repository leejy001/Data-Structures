#include <stdio.h>
#include "ArrayList.h"

int main(void)
{
	List list;
	int data, sum = 0;
	ListInit(&list);

	for (int i = 1; i < 10; i++)
	{
		LInsert(&list, i);
	}

	if (LFirst(&list, &data))
	{
		sum += data;
		while (LNext(&list, &data))
			sum += data;
	}
	printf("Stored number sum : %d\n", sum);

	if (LFirst(&list, &data))
	{
		if (data % 2 == 0 || data % 3 == 0)
			LRemove(&list);
		while (LNext(&list, &data))
		{
			if (data % 2 == 0 || data % 3 == 0)
				LRemove(&list);
		}
	}

	printf("Total number :");
	if (LFirst(&list, &data))
	{
		printf("%d ", data);
		while (LNext(&list, &data))
		{
			printf("%d ", data);
		}
	}
	printf("\n\n");
}