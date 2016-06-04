PLUGINS = $(sort $(dir $(wildcard ../Test/*/)))
process: ./process/process.sh
	@mkdir bundle &&\
		cd process &&\
		./process.sh
.PHONY: process
all: $(process)
clean: $(PLUGINS)
	@rm -rf bundle/$(PLUGINS) &&\
		echo "All plugins have been erased"
