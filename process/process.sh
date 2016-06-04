#!/bin/bash
Here=`pwd`
while IFS='' read -r line || [[ -n "$line" ]]; do
  cd $Here
  if [[ $line =~ url[[:space:]]=[[:space:]](.+) ]]
  then
    url=${BASH_REMATCH[1]}
  fi
  cd ../bundle && git clone $url
  if [[ $url =~ vimproc ]]
  then
    cd ../bundle/vimproc.vim && make
  fi
done < "./plugin-list"
