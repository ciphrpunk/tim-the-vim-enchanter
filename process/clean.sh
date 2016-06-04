#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
  if [[ $line =~ path[[:space:]]=[[:space:]]bundle/(.+)[\.vim]* ]]
  then
    name=${BASH_REMATCH[1]}
  fi
  cd ../bundle &&\
  git submodule deinit  -f $name &&\
  git rm --cached $name  &&\
  rm -r $name
done < "./plugin-list"
cd ../ && mv .gitmodules process/plugin-list 
