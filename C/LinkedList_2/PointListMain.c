#include <stdio.h>
#include <stdlib.h>
#include "DLinkedList.h"
#include "Point.h"

int WhoIsPrecede(Point * d1, Point * d2)
{
	if (d1->xpos < d2->xpos)
		return 0;
	else if (d1->xpos == d2->xpos)
	{
		if (d1->ypos < d2->ypos)
			return 0;
		else
			return 1;
	}
	else
		return 1;

}

int main(void)
{
	List list;
	Point compPos;
	Point * ppos;
	int cnt;
	ListInit(&list);

	SetSortRule(&list, WhoIsPrecede);

	printf("Enter Number :");
	scanf("%d", &cnt);

	for (int i = 0; i < cnt; i++)
	{
		int x, y;
		printf("[x, y] input :");
		scanf("%d %d", &x, &y);
		ppos = (Point*)malloc(sizeof(Point));
		SetPointPos(ppos, x, y);
		LInsert(&list, ppos);
	}

	printf("\nNumber of current data: %d \n", LCount(&list));

	int num = 0;

	if (LFirst(&list, &ppos))
	{
		printf("# %d", ++num);
		ShowPointPos(ppos);

		while (LNext(&list, &ppos))
		{
			printf("# %d", ++num);
			ShowPointPos(ppos);
		}
	}
	printf("\n");

	int xp, yp;
	printf("Enter [xpos, ypos] to delete :");
	scanf("%d %d", &xp, &yp);
	compPos.xpos = xp;
	compPos.ypos = yp;

	if (LFirst(&list, &ppos))
	{
		if (PointComp(ppos, &compPos) == 1)
		{
			ppos = LRemove(&list);
			free(ppos);
		}

		while (LNext(&list, &ppos))
		{
			if (PointComp(ppos, &compPos) == 1)
			{
				ppos = LRemove(&list);
				free(ppos);
			}
		}
	}

	printf("Number of current data: %d \n", LCount(&list));

	num = 0;

	if (LFirst(&list, &ppos))
	{
		printf("# %d", ++num);
		ShowPointPos(ppos);

		while (LNext(&list, &ppos))
		{
			printf("# %d", ++num);
			ShowPointPos(ppos);
		}
	}
	printf("\n");

	return 0;
}