// https://www.hackerrank.com/challenges/small-triangles-large-triangles/problem

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
void swap(triangle *trA, triangle *trB) {
    triangle temp = *trA;
    *trA = *trB;
    *trB = temp;
}

float getArea(triangle tr) {
    float p = ((float)tr.a + (float)tr.b + (float)tr.c) / 2;
    return sqrt(p * (p - (float)tr.a) * (p - (float)tr.b) * (p - (float)tr.c));
}
void sort_by_area(triangle* tr, int n) {
    for (int i = 0; i < n - 1; i++) 
        for (int j = 0; j < n - i - 1; j++)
            if (getArea(*(tr + j)) > getArea(*(tr + j + 1)))
                swap(tr + j, tr + j + 1);
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
