CC = cc
OBJECT = out

main in2post postfix_parser score:
	@${CC} -lm -o ${OBJECT} c/$@.c
	@./${OBJECT}

list queue stack:
	@${CC} -lm -o ${OBJECT} c/dsa/$@.c
	@./${OBJECT}

insertion:
	@${CC} -lm -o ${OBJECT} c/sort/$@.c
	@./${OBJECT}

ja1: java/assignment_1.java
	@echo $@
	@java java/assignment_1.java

ja2: java/assignment_2.java
	@java java/assignment_2.java

test:
	@echo ${SHELL}

clean:
	rm c/${OBJECT}
