all: c js

c: main array

main: c/main.c
	cc -lm -o c/main c/main.c

array: c/array.c
	cc -lm -o c/array c/array.c

postfix:
	cc -lm -o out c/postfix_parser.c
	./out

js:
	node javascript/index.js

test:
	@echo ${SHELL}

clean:
	rm out c/main c/array c/out
