FROM ansible/ansible-runner
ADD README.md /
ADD setup.py /
ADD ansible_runner_ovirt_engine /ansible_runner_ovirt_engine
RUN pip install requests
RUN pip install requests_unixsocket
RUN python setup.py install
ENTRYPOINT ["/tini", "--"]
WORKDIR /
ENV RUNNER_BASE_COMMAND=ansible-playbook
CMD /entrypoint.sh
