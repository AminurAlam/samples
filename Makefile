all:

array: c/array.c
	cc -lm -o out c/array.c && ./out

main: c/main.c
	cc -lm -o out c/main.c && ./out

in2post: c/in2post.c
	cc -lm -o out c/in2post.c && ./out

postfix: c/postfix_parser.c
	cc -lm -o out c/postfix_parser.c && ./out

queue: c/queue.c
	cc -lm -o out c/queue.c && ./out

stack: c/stack.c
	cc -lm -o out c/stack.c && ./out

ja1: java/assignment_1.java
	java java/assignment_1.java

ja2: java/assignment_2.java
	java java/assignment_2.java

test:
	@echo ${SHELL}

clean:
	rm out
