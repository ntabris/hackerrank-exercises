#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;

int area_compare(triangle *, triangle *);

int area_compare(triangle *x, triangle *y) {
	/* we're actually going to compute the square of the area scaled by a const
	   so that we can do all the math with ints */
	int px = x->a + x->b + x->c;
	int py = y->a + y->b + y->c;
	int ax = px * (px - 2*x->a) * (px - 2*x->b) * (px - 2*x->c);
	int ay = py * (py - 2*y->a) * (py - 2*y->b) * (py - 2*y->c);
	if(ax<ay) return -1;
	else if(ax==ay) return 0;
	else return 1;
}

void sort_by_area(triangle* tr, int n) {
	/**
	* Sort an array a of the length n
	*/
	qsort(tr,n,sizeof(triangle),(int (*)(const void*,const void*))(area_compare));
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}