#include <stdio.h>
#include <stdlib.h>
#define MAX_STRING_LENGTH 6

struct package
{
	char* id;
	int weight;
};

typedef struct package package;

struct post_office
{
	int min_weight;
	int max_weight;
	package* packages;
	int packages_count;
};

typedef struct post_office post_office;

struct town
{
	char* name;
	post_office* offices;
	int offices_count;
};

typedef struct town town;



void print_all_packages(town t) {
	printf("%s:\n",t.name);
	for(int i=0;i<t.offices_count;i++) {
		printf("\t%d:\n",i);
		for(int j=0;j<t.offices[i].packages_count;j++) {
			printf("\t\t%s\n",t.offices[i].packages[j].id);
		}
	}
}

void send_all_acceptable_packages(town* source, int source_office_index, town* target, int target_office_index) {
	int min,max,thisWeight,insertIdx;
	short remove[source->offices[source_office_index].packages_count];
	
	min = target->offices[target_office_index].min_weight;
	max = target->offices[target_office_index].max_weight;
/*printf("moving packages from %s.%d to %s.%d\n",source->name,source_office_index,target->name,target_office_index);*/
	
	for(int i=0;i<source->offices[source_office_index].packages_count;i++) {
		remove[i] = 0;
		thisWeight = source->offices[source_office_index].packages[i].weight;
		/* if package is within allowable weight range */
		if(thisWeight >= min && thisWeight <= max) {
/*printf("\tmoving: %s\n",source->offices[source_office_index].packages[i].id);*/
			/* add to end of queue at destination */
			
			target->offices[target_office_index].packages =
					realloc(
						target->offices[target_office_index].packages,
						sizeof(package)*(target->offices[target_office_index].packages_count+1));
						
			target->offices[target_office_index].packages[target->offices[target_office_index].packages_count++] =
					source->offices[source_office_index].packages[i];
			
			/* mark to remove, so that we can loop once to remove everything we've marked */
			remove[i] = 1;
		}
	}
	/* now we shift everything up to cover what we want to remove */
	insertIdx = 0;
	for(int i=0;i<source->offices[source_office_index].packages_count;i++) {
		if(insertIdx < i)
			source->offices[source_office_index].packages[insertIdx] = 
				source->offices[source_office_index].packages[i];
		if(!remove[i])
			insertIdx++;
	}
	source->offices[source_office_index].packages_count = insertIdx;
	/* and adjust size of memory (probably not necessary) */
	/*source->offices[source_office_index].packages =
			realloc(
				source->offices[source_office_index].packages,
				sizeof(package)*source->offices[source_office_index].packages_count);*/
		
}

town town_with_most_packages(town* towns, int towns_count) {
	int packageCount,maxId,maxCount;
	
	maxCount = 0;
	maxId = -1;
	
	/* loop over towns */
	for(int i=0;i<towns_count;i++) {
		packageCount = 0;
		/* loop over post offices in town */
		for(int j=0;j<towns[i].offices_count;j++)
			packageCount += towns[i].offices[j].packages_count;
		if(packageCount > maxCount) {
			maxCount = packageCount;
			maxId = i;
		}
	}
	return(towns[maxId]);
}

town* find_town(town* towns, int towns_count, char* name) {
	int j;
	for(int i=0;i<towns_count;i++) {
		j = 0;
		while(towns[i].name[j] == name[j] && towns[i].name[j] && name[j])
			j++;
		if(towns[i].name[j] == '\0')
			return(&towns[i]);
	}
	return(NULL);
}

int main()
{
	int towns_count;
	scanf("%d", &towns_count);
	town* towns = malloc(sizeof(town)*towns_count);
	for (int i = 0; i < towns_count; i++) {
		towns[i].name = malloc(sizeof(char) * MAX_STRING_LENGTH);
		scanf("%s", towns[i].name);
		scanf("%d", &towns[i].offices_count);
		towns[i].offices = malloc(sizeof(post_office)*towns[i].offices_count);
		for (int j = 0; j < towns[i].offices_count; j++) {
			scanf("%d%d%d", &towns[i].offices[j].packages_count, &towns[i].offices[j].min_weight, &towns[i].offices[j].max_weight);
			towns[i].offices[j].packages = malloc(sizeof(package)*towns[i].offices[j].packages_count);
			for (int k = 0; k < towns[i].offices[j].packages_count; k++) {
				towns[i].offices[j].packages[k].id = malloc(sizeof(char) * MAX_STRING_LENGTH);
				scanf("%s", towns[i].offices[j].packages[k].id);
				scanf("%d", &towns[i].offices[j].packages[k].weight);
			}
		}
	}
	int queries;
	scanf("%d", &queries);
	char town_name[MAX_STRING_LENGTH];
	while (queries--) {
		int type;
		scanf("%d", &type);
		switch (type) {
		case 1:
			scanf("%s", town_name);
			town* t = find_town(towns, towns_count, town_name);
			print_all_packages(*t);
			break;
		case 2:
			scanf("%s", town_name);
			town* source = find_town(towns, towns_count, town_name);
			int source_index;
			scanf("%d", &source_index);
			scanf("%s", town_name);
			town* target = find_town(towns, towns_count, town_name);
			int target_index;
			scanf("%d", &target_index);
			send_all_acceptable_packages(source, source_index, target, target_index);
			break;
		case 3:
			printf("Town with the most number of packages is %s\n", town_with_most_packages(towns, towns_count).name);
			break;
		}
	}
	return 0;
}

