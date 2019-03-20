#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_array(char **s,int n) {
	for (int i = 0; i < n; i++)
		printf("%s%c", s[i], i == n - 1 ? '\n' : ' ');
}

void swap(char **s,int x,int y) {
	char *t = *(s+x);
	*(s+x) = *(s+y);
	*(s+y) = t;
}

int next_permutation(int n, char **s) {
    int tail,insIdx,t,i;

	/* find tail: longest sequence of ascending items from end */
    tail = n-1;
    while(tail > 0 && strcmp(s[tail-1],s[tail]) >= 0)
        tail -= 1;
    /* if tail is whole array, then we're already on final permutation */
    if(tail == 0)
		return(0);

    /* otherwise, swap item before tail with next larger item from tail */

    t = n-1;
    while(strcmp(s[t],s[tail-1]) <= 0) 
        t--;
    swap(s,tail-1,t);

    /* reverse order of tail */
    t = n-1;
    for(i=0;i<=(int)((t-tail)/2);i++)
        swap(s,tail+i,t-i);
    return(1);
}

int main()
{
	char **s;
	int n;
	scanf("%d", &n);
	s = calloc(n, sizeof(char*));
	for (int i = 0; i < n; i++)
	{
		s[i] = calloc(11, sizeof(char));
		scanf("%s", s[i]);
	}
	do
	{
		for (int i = 0; i < n; i++)
			printf("%s%c", s[i], i == n - 1 ? '\n' : ' ');
	} while (next_permutation(n, s));
	for (int i = 0; i < n; i++)
		free(s[i]);
	free(s);
	return 0;
}