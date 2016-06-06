#!/bin/bash
Here=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )
i=0
declare -a Urls
declare -a Names
while IFS='' read -r line || [[ -n "$line" ]]; do
  if [[ $line =~ url[[:space:]]=[[:space:]](.+) ]]
  then
    Urls[i]=${BASH_REMATCH[1]}
    Names[i]=$(echo "${Urls[i]##*/}" | sed -e 's/[\.\-]\(vim\.\)*git$//g' | sed -e 's/\b\(.\)/\u\1/g')
  fi
  #len=${#name} ch='='
  #cd ../bundle                         &&\
  #  printf '%*s' "$len" | tr ' ' "$ch" &&\
  #  printf '%s\n' ==========           &&\
  #  printf "${name}"                   &&\
  #  printf '\n'                        &&\
  #  printf '%*s' "$len" | tr ' ' "$ch" &&\
  #  printf '%s\n' ==========           &&\
  #  git clone $url                     &&\
  #  printf '\n\n' 
  #if [[ $url =~ vimproc ]]
  #then
  #  cd ../bundle/vimproc.vim && make
  #fi
  ((i++))
done < "${Here}/plugin-list"
for url in "${Urls[@]}"
do 
  echo $url
done
