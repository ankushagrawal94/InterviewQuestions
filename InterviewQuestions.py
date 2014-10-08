''' Implement a queue using 2 stacks.
	
	Label 2 stacks inStack and outStack:
		To enqueue an item, push it onto inStack. Done.
		To dequeue:
			If outStack empty, push everything on inStack to outStack. Pop outStack. Done.
			If outStack not empty, pop outStack. Done. '''

def enqueue(item):
	inStack.push(item)

def dequeue():
	if outStack.empty():
		while not inStack.empty():
			outStack.push(inStack.pop())
	return outStack.pop()

-----------------------------------------------------------------------------------------------------------------------

''' Check if parantheses openners and closers match. Ex: (()) returns true, (() returns false. 

	Traverse the string to check.
	If character at index is (, push it on a stack.
	If character at index is ), pop the stack.
	At the end of the string, if stack is empty, then return true, else false. '''

def parantheses_validator(string):
	for each_char in string:
		if each_char == '(':
			stack.push('(')
		if each_char == ')':
			stack.pop()
	return stack.empty()

-----------------------------------------------------------------------------------------------------------------------

''' Extend a stack class to find the largest element in the stack. 

	Keep another stack, L, of all the largest values. 
	When push an item, check to see if it's larger than the current largest (i.e top of stack L).
		If so, push this new value onto L in addition to pushing it on the normal stack.
	When pop an item, check to see if it's the same as top of L.
		If so, pop L. '''

class Stack:
	stack = Stack()
	L = Stack()

	def push(item):
		if item >= L.top():
			L.push(item)
		stack.push(item)

	def pop():
		if stack.top() == L.top():
			L.pop()
		stack.pop()

	def largest():
		return L.pop()

-----------------------------------------------------------------------------------------------------------------------	

''' Find the first non-repeating character in a string. 

	Worst case is O(n) since you have to traverse the entire string at least once.
	Traverse through each character and make a dictionary element for each new character, along with its count. '''

def first_non_repeat(string):
	dictionary = {}
	for char in string:
		if char in dictionary:
			dictionary[char] = dictionary[char] + 1
		else:
			dictionary[char] = 1

	for key in dictionary:
		if dictionary[key] == 1
			return key

	return '' 

-----------------------------------------------------------------------------------------------------------------------

''' Check if a string is a palindrome. 

	Worst case is O(n) since you have to traverse the entire thing at least once. 
	Check each index with its corresponding palindromic index. Return false immediately if found an unmatch. '''

def is_palin(string):
	for index in range(len(string)/2):
		if string[index] != string[len(string) - index]:
			return false
	return true

-----------------------------------------------------------------------------------------------------------------------

''' Solely based on a collection of Yelp reviews, determine the most popular dish. You do not have access to a 
	collection of all the menu items. Just the text of the reviews.'''

-----------------------------------------------------------------------------------------------------------------------

''' Create a 50-item cache. 
	Kush, please elaborate on this question and answer here.'''

-----------------------------------------------------------------------------------------------------------------------

''' Given a string "ABC DEF GHIJK", reverse the substrings that are separated by the spaces. The output of the given 
	string should be "CBA FED KJIHG". You do not have access to any split by space library function.'''

