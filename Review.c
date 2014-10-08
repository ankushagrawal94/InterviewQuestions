"Brushing up C programming language for those who still know programming."

"Every program starts with a main function:"

#include <stdio.h>							//A directive is the #include that imports header files
int main() {								//Main can calls other functions
	printf("Long Tran");
	return 0;
}

"This is a declaration. Declaration must come before other types of statements in a block."
int add() {
	int result;
	result = 812 % 37;
	return result;
}

"Dynamic memory allocation: handle any amount of data on the fly. No need to specify how much memory is needed when writing the program."

"This is a pointer declaration. Always declare pointers before using them. Dynamic memory allocation is useful for structures like BST and lists beause 
you don't know how much memory needed at compilation."
int *pointer;

"Request for (free) memory."
int *ptr = malloc(sizeof(int));				//malloc returns a pointer to a block of free memory 

"Remember to free pointers or set them to null after using them."

"This is a structure declaration."
struct family {
	int dad;
	int mom;
	int son;
};

"This is an array declaration."
int array[100];

"Strings always end with a null character \0"

"Memory allocation in C:
There are 2 ways to allocate memory: declare variables or explicitly request space.
	stdlib.malloc and stdlib.calloc reserve space
	stdlib.realloc moves a reserved block of memory to another location of different dimensions
	stdlib.free releases space

	malloc retruns a pointer to a block of memory
	calloc returns a pointer to an array of zero-value initialized blocks

	
