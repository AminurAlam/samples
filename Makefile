CC = cc
OBJECT = out

array main in2post list postfix queue score stack:
	@${CC} -lm -o ${OBJECT} c/$@.c
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
