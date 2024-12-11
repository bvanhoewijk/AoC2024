#!/usr/bin/env bash
day=$1
echo ${day}

mkdir -p ${day}
touch ${day}/small.txt
touch ${day}/big.txt

cp ./util/init.py ${day}/${day}.py
cd ${day}