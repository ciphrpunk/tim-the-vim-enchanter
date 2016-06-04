PLUGINS=$(wildcard bundle/*.vim)

all: ./process/process.sh
	echo "Entering process/" &&\
		cd process &&\
		echo "Running process.sh" &&\
		./process.sh

clean: ${PLUGINS}
	echo "Entering process/" &&\
		cd process &&\
		echo "Running process.sh" &&\
		./clean.sh


