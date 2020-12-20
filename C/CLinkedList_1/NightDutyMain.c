#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Employee.h"
#include "CLinkedList.h"

Employee * WhoNightDuty(List * plist, char * name, int day);
void ShowEmployeeInfo(Employee *emp);

int main(void)
{
	int num, select, day;
	char name[20];
	Employee * pemp;
	List list;
	ListInit(&list);
	
	while(1)
	{
		printf("\n[Select Number] (input 0 : exit)\n");
		printf("(1) Add empolyee  (2) Add employee in front  (3) Remove empolyee \n");
		printf("(4) Search for who nightduty  (5) Show info\n");
		scanf("%d", &select);
		if (select == 0)
			break;
		else
		{
			switch (select)
			{
			case 1:
				printf("Enter number and name :");
				scanf("%d %s", &num, &name);

				pemp = (Employee*)malloc(sizeof(Employee));
				pemp->emp_num = num;
				strcpy(pemp->name, name);
				LInsert(&list, pemp);
				break;
			case 2:
				printf("Enter number and name :");
				scanf("%d %s", &num, &name);

				pemp = (Employee*)malloc(sizeof(Employee));
				pemp->emp_num = num;
				strcpy(pemp->name, name);
				LInsertFront(&list, pemp);
				break;
			case 3:
				printf("Enter empolyee number:");
				scanf("%d", &num);
				if (num != 0)
				{
					LFirst(&list, &pemp);
					if (pemp->emp_num == num)
						LRemove(&list);
					for (int i = 0; i < LCount(&list); i++)
					{
						LNext(&list, &pemp);
						if (pemp->emp_num == num)
							LRemove(&list);
					}
				}
				break;
			case 4:
				printf("\nInput name and day :");
				scanf("%s %d", &name, &day);
				pemp = WhoNightDuty(&list, name, day);
				ShowEmployeeInfo(pemp);
				printf("----------------------\n");
				break;
			}
			if (num != 0)
			{
				LFirst(&list, &pemp);
				for (int i = 0; i < LCount(&list); i++)
				{
					LNext(&list, &pemp);
					ShowEmployeeInfo(pemp);
				}
			}
		}
	}
	return 0;
}

/* 어떤 사원으로 부터 몇 일 후에 누가 당직인지 확인 */
Employee * WhoNightDuty(List * plist, char * name, int day)
{
	int i, num;
	Employee *emp;

	num = LCount(plist);

	LFirst(plist, &emp);

	if (strcmp(emp->name, name) != 0)
	{
		for (i = 0; i < num - 1; i++)
		{
			LNext(plist, &emp);

			if (strcmp(emp->name, name) == 0)
				break;
		}
		if (i >= num - 1)
			return NULL;
	}

	for (i = 0; i < day; i++)
		LNext(plist, &emp);

	return emp;
}

void ShowEmployeeInfo(Employee *emp)
{
	printf("\nEmployee name: %s\n", emp->name);
	printf("Employee number: %d\n", emp->emp_num);
}
