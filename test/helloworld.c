#include <stdio.h>

int AddOne(int a);

int AddOne(int a) {
	return a+1;
}

int main(void) {
	printf("Hello world!\n");
	printf("Calling AddOne with 2:\n");
	printf("%d\n", AddOne(2));
}
