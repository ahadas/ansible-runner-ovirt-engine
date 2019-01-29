#!/bin/bash
exec docker run --rm -v $(pwd)/ansible-runner-ovirt-engine:/usr/lib/python2.7/site-packages/ansible-runner-ovirt-engine:z -v $(pwd)/playbooks/:/root:z  -v $(pwd)/env/settings:/runner/env/settings:z -e RUNNER_PLAYBOOK=/root/test.yml ansible/ansible-runner
