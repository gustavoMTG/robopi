.PHONY: build clean

build:
	python -m build

clean:
	rm -rf dist/ src/robopi.egg-info

motor.o: motor.c
	gcc -Wall -pthread -o src/robopi/motor src/robopi/motor.c -lpigpio -lrt