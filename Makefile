PLUGINS=$(wildcard bundle/*.vim)

all: ./process/process.sh
	cd process &&\
	./process.sh

clean: ${PLUGINS}
	-rm -rf bundle/*

