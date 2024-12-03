#!/usr/bin/env bash
day=$1
echo ${day}

mkdir -p ${day}
touch ${day}/small.txt
touch ${day}/big.txt
touch ${day}/${day}.py