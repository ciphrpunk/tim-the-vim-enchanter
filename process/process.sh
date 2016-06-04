#!/bin/bash
Here=`pwd`
while IFS='' read -r line || [[ -n "$line" ]]; do
  cd $Here
  if [[ $line =~ url[[:space:]]=[[:space:]](.+) ]]
  then
    url=${BASH_REMATCH[1]}
    name=$(echo "${url##*/}")
    name=$(echo "${name%.git}")
  fi
  len=${#name} ch='='
  cd ../bundle &&\
    printf '%*s' "$len" | tr ' ' "$ch" &&\
    printf '%s\n' ==========           &&\
    printf "${name}"                   &&\
    printf '%s\n' __________           &&\
    printf '%*s' "$len" | tr ' ' "$ch" &&\
    printf '%s\n' ==========           &&\
    git clone $url                     &&\    
    printf '\n\n' 
  if [[ $url =~ vimproc ]]
  then
    cd ../bundle/vimproc.vim && make
  fi
done < "./plugin-list"
