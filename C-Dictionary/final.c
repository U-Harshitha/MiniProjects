#include <stdio.h>
#include <stdlib.h>
#include "dict.c"

#define MAX_FILENAME_SIZE 50
#define MAX_WORD_SIZE 50

int main() {
  int j, k;
  char filename[MAX_FILENAME_SIZE];
  char word[MAX_WORD_SIZE];

  printf("Enter dictionary filename: ");
  scanf("%s", filename);

  int success = load_dictionary(filename);
  if (!success) {
    printf("Failed to load the dictionary.\n");
    exit(EXIT_FAILURE);
  } else {
    printf("Enter a word to know its definition (enter 'exit' to end):\n");

    while (1) {
      scanf("%s", word);

      if (strcmp(word, "exit") == 0) {
        break;
      }

      int flag = 0;
      k = lookup(word);

      for (j = 0; j < i; j++) {
        if (k == j) {
          printf("%s\t%s\n", book[k].words, book[k].defin);
          flag = 1;
          break;
        }
      }

      if (flag == 0) {
        printf("%s is not found in the uploaded dictionary\n", word);
      }
    }
  }

  return 0;
}
