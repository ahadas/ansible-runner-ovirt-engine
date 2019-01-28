FROM python:3
RUN pip install ansible-runner
ADD setup.py /
ADD ansible_runner_ovirt_engine /ansible_runner_ovirt_engine
ENTRYPOINT [ "python", "setup.py" ]
