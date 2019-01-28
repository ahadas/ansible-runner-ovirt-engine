#!/usr/bin/env python

# Copyright (c) 2019 Red Hat, Inc.
# All Rights Reserved.

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="ansible-runner-ovirt-engine",
    version="1.0.0",
    author="oVirt",
    url="https://github.com/fromanirh/ansible-runner-ovirt-engine",
    license='Apache',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'requests',
        'requests-unixsocket',
    ],
    entry_points={'ansible_runner.plugins': 'ovirt_engine = ansible_runner_ovirt_engine'},
    zip_safe=False,
)
