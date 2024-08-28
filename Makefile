CC = cc
OBJECT = out

test:
	@echo ${SHELL}

clean:
	@rm ${OBJECT} c/${OBJECT}

### misc
ja1 ja2 ja3 Stack Queue: java/
	@java java/$@.java

pya1 pya2 pya3 pya4 pya5 pya6: python/
	@python python/$@.py

rust: rust/main.rs
	@rustc -o ${OBJECT} rust/main.rs

### c
main in2post postfix_parser score: c/
	@${CC} -lm -o ${OBJECT} c/$@.c
	@./${OBJECT}

list queue stack: c/dsa/
	@${CC} -lm -o ${OBJECT} c/dsa/$@.c
	@./${OBJECT}

binary linear sequential: c/search/
	@${CC} -lm -o ${OBJECT} c/search/$@.c
	@./${OBJECT}

bubble insertion selection: c/sort/
	@${CC} -lm -o ${OBJECT} c/sort/$@.c
	@./${OBJECT}

fifo sjf rr: c/scheduling/
	@${CC} -lm -o ${OBJECT} c/scheduling/$@.c
	@./${OBJECT}
