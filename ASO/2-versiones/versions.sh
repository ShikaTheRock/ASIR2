#!/bin/bash

for op in $(find / -perm -u=s 2>/dev/null); do
    echo "$op"
done