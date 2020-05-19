#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef char element;

typedef struct stackNode
{
	element data;
	struct stackNode *link;
}stackNode;

stackNode* top;

int isEmpty()
{
	if (top == NULL)
		return 1;
	else
		return 0;
}

void push(element data)
{
	stackNode* temp = (stackNode*)malloc(sizeof(stackNode));
	temp->data = data;
	temp->link = top;
	top = temp;
}

element pop()
{
	element data;
	stackNode* temp = top;
	if (top == NULL)
	{
		printf("\n\n Stack is empty \n");
		return 0;
	}
	else
	{
		data = temp->data;
		top = temp->link;
		free(temp);
		return data;
	}
}

int testPair(char *exp)
{
	char symbol, open_pair;
	int length = strlen(exp); //char형 포인터 매개변수로 받은 수식 exp의 길이를 계산
	top = NULL;
	for (int i = 0; i < length; i++)
	{
		symbol = exp[i];
		switch (symbol)
		{
		case '(':
		case '[':
		case '{':
			push(symbol);
			break;
		// 오른쪽 괄호
		case ')':
		case ']':
		case '}':
			if (top == NULL)
				return 0;
			else
			{
				open_pair = pop(); // top 호출
				if ((open_pair == '(' && symbol != ')') || (open_pair == '[' && symbol != ']') || (open_pair == '{' && symbol != '}'))
					return 0; // 수식 오류
				else
					break; // 다음 검사 계속
			}
		}
	}
	if (top == NULL)
		return 1;
	else
		return 0;
}

void main()
{
	char* express = "{(A+B)-3}*5+[{cos(x+y)+7}-1]*4";
	printf("%s", express);
	if (testPair(express) == 1)
		printf("\n\n done! \n");
	else
		printf("\n\n error! \n");
	
	getchar();
}