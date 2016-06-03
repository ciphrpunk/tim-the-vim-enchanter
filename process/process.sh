#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
  cd ../bundle; git submodule add $line ; git submodule init ; git submodule update
done < "./plugin-list"
