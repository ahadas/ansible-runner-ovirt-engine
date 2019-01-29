#!/bin/bash
exec docker run --rm -v $(pwd)/playbooks/:/root:z  -v $(pwd)/env/settings:/runner/env/settings:z -e RUNNER_PLAYBOOK=/root/test.yml ansible-runner-engine
