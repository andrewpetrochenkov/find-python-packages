#!/usr/bin/env bash
{ set +x; } 2>/dev/null

set -- "long/key" "value1" "value2" "value3"
( set -x; shell-cache "$@" ) && ( set -x; shell-cache "$1" )
