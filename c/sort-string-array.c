#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int lexicographic_sort(const char* a, const char* b) {
	int c = strcmp(*(char**)a,*(char**)b);
/*printf("comparing '%s' and '%s' -> %d\n",*(char**)a,*(char**)b,c);*/
	return c;
}

int lexicographic_sort_reverse(const char* a, const char* b) {
	return lexicographic_sort(a,b) * -1;
}

int count_distinct_letters(const char* a) {
	char *aa = *(char**)a;
	short found[26],c;
	
	c = 0;
	for(int i=0;i<26;i++) found[i] = 0;
	
	for(int i=0;aa[i] != '\0';i++) {
		if(found[aa[i]-'a'] == 0)
			c++;
		found[aa[i]-'a']++;
	}

	return c;
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    int c = count_distinct_letters(a) - count_distinct_letters(b);
    if(c==0) return lexicographic_sort(a,b);
    return c;
}

int sort_by_length(const char* a, const char* b) {
	int c = strlen(*(char**)a) - strlen(*(char**)b);
	if(c==0) return lexicographic_sort(a,b);
	return c;
}

void string_sort(char** arr,const int len,int (*cmp_func)(const char* a, const char* b)){
	qsort((void *)arr,len,sizeof(char *),(int (*)(const void*,const void*))cmp_func);
}


int main() 
{
    int n;
    scanf("%d", &n);
  
    char** arr;
	arr = (char**)malloc(n * sizeof(char*));
  
    for(int i = 0; i < n; i++){
        *(arr + i) = malloc(1024 * sizeof(char));
        scanf("%s", *(arr + i));
        *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
    }
  
    string_sort(arr, n, lexicographic_sort);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, lexicographic_sort_reverse);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");

    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);    
    printf("\n");

    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");
}