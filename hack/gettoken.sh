#!/bin/bash
if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
	echo "usage: $0 user pass engine_url"
	exit 1
fi
exec curl -k --data "grant_type=password&scope=ovirt-app-api&username=${1}&password=${2}" -H "Accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" "${3}/ovirt-engine/sso/oauth/token"
