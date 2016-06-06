PROCESS = process/process.sh
BUNDLE  = bundle/
PLUGINS = ${sort ${dir ${wildcard ${BUNDLE}/*/}}}
PLUGINNAMES = ${basename ${basename $(PLUGINS)}}

install: $(PROCESS)
	@$(PROCESS)
process:  
	@cd process &&\
		./$(PROCESS)
.PHONY: process
clean: $(PLUGINS)
	@echo "Removing $(PLUGINNAMES) plugins" &&\
		rm -rf $(PLUGINS)  
