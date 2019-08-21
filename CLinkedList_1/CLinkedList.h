#ifndef __C__LINKED_LIST_H__
#define __C__LINKED_LIST_H__

#include "Employee.h"

#define TRUE 1
#define FALSE 0

typedef Employee * LData;

typedef struct _node
{
	LData data;
	struct _node * next;
} Node;

typedef struct _CLL
{
	Node * tail;
	Node * cur;
	Node * before;
	int numOfData;
} CList;

typedef CList List;

void ListInit(List * plist);
void LInsert(List * plist, LData data); //Add nodes to tail 
void LInsertFront(List * plist, LData data); //Add nodes to head

int LFirst(List * plist, LData *pdata);
int LNext(List * plist, LData *pdata);
LData LRemove(List * plist);
int LCount(List * plist);

#endif