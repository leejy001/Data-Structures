#ifndef __D_LINKED_LIST_H__
#define __D_LINKED_LIST_H__

#include "Point.h"

#define TRUE  1
#define FALSE 0

typedef Point * LData;

typedef struct _node	// typedef int LData
{
	LData data;
	struct _node * next;
} Node;

typedef struct _linkedList
{
	Node * head;	// pointing to a dummy node
	Node * cur;		// Reference and Delete
	Node * before;	// Delete
	int numOfData;	// Record the number of stored data
	int(*comp)(LData d1, LData d2); // Register criteria for alignment
} LinkedList;

typedef LinkedList List;

void ListInit(List * plist);
void LInsert(List * plist, LData data);

int LFirst(List * plist, LData * pdata);
int LNext(List * plist, LData * pdata);

LData LRemove(List * plist);
int LCount(List * plist);

void SetSortRule(List * plist, int(*comp)(LData d1, LData d2));

#endif