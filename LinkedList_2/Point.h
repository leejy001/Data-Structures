#ifndef __POINT_H__
#define __POINT_H__

typedef struct _point
{
	int xpos;
	int ypos;
} Point;

// set the xpos, ypos value
void SetPointPos(Point * ppos, int xpos, int ypos);

// xpos, ypos information output
void ShowPointPos(Point * ppos);

// Comparison of two point variables
int PointComp(Point * pos1, Point * pos2);

#endif