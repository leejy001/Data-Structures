#include <stdio.h>
#include <stdlib.h>
#include "NameCard.h"
#include "ArrayList.h"

int main(void)
{
	List list;
	NameCard * pcard;
	ListInit(&list);

	pcard = MakeNameCard("James", "000-0000-0000");
	LInsert(&list, pcard);

	pcard = MakeNameCard("Tom", "000-0000-0000");
	LInsert(&list, pcard);

	pcard = MakeNameCard("Lena", "000-0000-0000");
	LInsert(&list, pcard);

	printf("[Show James Info]\n");

	if (LFirst(&list, &pcard))
	{
		if (!NameCompare(pcard, "James"))
			ShowNameCardInfo(pcard);
		else
		{
			while (LNext(&list, &pcard))
			{
				if (!NameCompare(pcard, "James"))
				{
					ShowNameCardInfo(pcard);
					break;
				}
			}
		}
	}

	printf("\n\n");

	if (LFirst(&list, &pcard))
	{
		if (!NameCompare(pcard, "Lena"))
			ChangePhoneNum(pcard, "010-1111-1111");
		else
		{
			while (LNext(&list, &pcard))
			{
				if (!NameCompare(pcard, "Lena"))
				{
					ChangePhoneNum(pcard, "010-1111-1111");
					break;
				}
			}
		}
	}

	if (LFirst(&list, &pcard))
	{
		if (!NameCompare(pcard, "Tom"))
		{
			pcard = LRemove(&list);
			free(pcard);
		}
		else
		{
			while (LNext(&list, &pcard))
			{
				if (!NameCompare(pcard, "Tom"))
				{
					pcard = LRemove(&list);
					free(pcard);
					break;
				}
			}
		}
	}

	printf("[Output all user information]\n");
	if (LFirst(&list, &pcard))
	{
		ShowNameCardInfo(pcard);

		while (LNext(&list, &pcard))
			ShowNameCardInfo(pcard);
	}
	return 0;
}