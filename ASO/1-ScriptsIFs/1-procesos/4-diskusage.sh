#!/bin/bash

find / -user $USER -type f -printf '%s\n' 2>/dev/null | awk '{sum += $1} END {print sum/1024/1024/1024 " GB"}'
