#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
  if [[ $line =~ url[[:space:]]=[[:space:]](.+) ]]
  then
    url=${BASH_REMATCH[1]}
  fi
  cd ../bundle&& git submodule add $url && git submodule init && git submodule update && cd ../process/
done < "./gitmodules"
cd ../bundle/vimproc.vim && make 
