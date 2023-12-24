#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_WORDS 100
#define MAX_WORD_SIZE 50
#define MAX_DEF_SIZE 200

struct dictionary {
    char words[MAX_WORD_SIZE];
    char defin[MAX_DEF_SIZE];
};

typedef struct dictionary WordDef;

WordDef book[MAX_WORDS];
int i = 0;

int load_dictionary(char *fl) {
    FILE *f;
    char line[250];

    f = fopen(fl, "r");

    if (f == NULL) {
        printf("Error: %s file does not exist\n", fl);
        return 0;
    } else {
        while (fgets(line, sizeof(line), f) != NULL) {
            if (i < MAX_WORDS) {
                strcpy(book[i].words, strtok(line, "    "));
                strcpy(book[i].defin, strtok(NULL, "\n"));
                i++;
            } else {
                printf("Error: Dictionary is full. Increase MAX_WORDS to add more words.\n");
                break;
            }
        }

        fclose(f);
        return 1;
    }
}

int lookup(char *word) {
    int j;
    for (j = 0; j < i; j++) 
        if (!strcmp(book[j].words, word)) 
            return j;
    return -1;
}
