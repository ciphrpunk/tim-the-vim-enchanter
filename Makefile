#!/bin/bash

THIS_DIR =$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
TIM_DIR =${THIS_DIR}/tim-the-vim-enchanter/
BUNDLE  = ${HOME}/.vim/bundle/
# PLUGINS = ${sort ${dir ${wildcard ${BUNDLE}/*/}}}
all:
	@cd ${HOME} &&\
		mkdir -p .vim/bundle &&\
		cd ${THIS_DIR}

install:
	@cd ${TIM_DIR} &&\
		python tim-the-vim-enchanter.py --all &&\
		cd ${THIS_DIR}
		
clean: 	
	@printf "Removing: \n" &&\
		for i in `find ${BUNDLE} -maxdepth 1 -mindepth 1 -type d`;do printf "\t"; basename $$i; rm -rf $$i; done &&\
		printf "All plugins removed\n";

