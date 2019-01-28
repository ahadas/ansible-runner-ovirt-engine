#!/bin/bash
exec docker run --rm -v $(pwd)/playbooks/:/root:z -e RUNNER_PLAYBOOK=/root/test.yml ansible-runner-engine
