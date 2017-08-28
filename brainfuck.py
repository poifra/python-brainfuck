"""
>	increment the data pointer (to point to the next cell to the right).
<	decrement the data pointer (to point to the next cell to the left).
+	increment (increase by one) the byte at the data pointer.
-	decrement (decrease by one) the byte at the data pointer.
.	output the byte at the data pointer.
,	accept one byte of input, storing its value in the byte at the data pointer.
[	if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.
]	if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.
"""

import sys

SYMBOLS = ['>','<','+','-','.',',','[',']']
MEMORY = [0 for i in range (1024)]
PTR = 0
IP = 0
program = list(filter(lambda x: x in SYMBOLS, open(sys.argv[1],'r').read()))

tempStack, brackets = [], {}

for pos, s in enumerate(program):
	if s == '[':
		tempStack.append(pos)
	if s == ']':
		start = tempStack.pop()
		brackets[start] = pos
		brackets[pos] = start


while IP < len(program):
	s = program[IP]
	if s == '>':
		PTR += 1
	if s =='<':
		PTR -= 1
	if s == '+':
		MEMORY[PTR] += 1
	if s == '-':
		MEMORY[PTR] -= 1
	if s == '.':
		print(chr(MEMORY[PTR]),end='')
	if s == ',':
		MEMORY[PTR] = int(input())

	if s == '[':
		if not MEMORY[PTR]:
			IP = brackets[IP]
	if s == ']':
		if MEMORY[PTR]:
			IP = brackets[IP]

	IP += 1