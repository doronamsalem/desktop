#!/bin/bash

objects = foo_test.o foo.o demo.o
CC = gcc
CFLAGS = -ansi -pedantic-errors -Wall -Wextra -g

all : $(objects)
	@$(CC) $(CFLAGS) $(objects)
#%.o : %.c
#	@$(CC) $(CFLAGS) -c $^
foo_test.o : foo_test.c foo.h
	@$(CC) $(CFLAGS) -c foo_test.c
foo.o : foo.c foo.h
	@$(CC) $(CFLAGS) -c foo.c
demo.o : demo.c foo.c
	@$(CC) $(CFLAGS) -c demo.c

.PHONY : cl
cl :
	rm $(objects)
