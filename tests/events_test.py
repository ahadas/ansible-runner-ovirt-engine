#
# ansible runner ovirt engine plugin -- send ansible events to oVirt Engine
# Copyright (C) 2019 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from ansible_runner_ovirt_engine import events

ansible_event = {
  "uuid": "8c164553-8573-b1e0-76e1-000000000008",
  "counter": 5,
  "stdout": "\r\nTASK [debug] *******************************************************************",
  "start_line": 5,
  "end_line": 7,
  "event": "playbook_on_task_start",
  "event_data": {
    "playbook": "test.yml",
    "playbook_uuid": "34437b34-addd-45ae-819a-4d8c9711e191",
    "play": "all",
    "play_uuid": "8c164553-8573-b1e0-76e1-000000000006",
    "play_pattern": "all",
    "task": "debug",
    "task_uuid": "8c164553-8573-b1e0-76e1-000000000008",
    "task_action": "debug",
    "task_path": "\/home\/mjones\/ansible\/ansible-runner\/demo\/project\/test.yml:3",
    "task_args": "msg=Test!",
    "name": "debug",
    "is_conditional": False,
    "pid": 10640
  },
  "pid": 10640,
  "created": "2018-06-07T14:54:58.410605"
}

def test_make_event():
    correlation_id = "a455c644-9d2b-40db-9498-1fd2ef18365c"
    event_data = ansible_event["event_data"]
    ovirt_event = {
        "code": 0, # FIXME,
        # "comment"
        "correlation_id": correlation_id,
        # custom_data
        "custom_id": ansible_event["counter"],
        # description
        # flood_rate
        "id": ansible_event["uuid"],
        "index": ansible_event["counter"],
        "name": event_data["playbook"],
        "origin": "%s-%s" % (event_data["playbook"], event_data["play_uuid"]),
        "severity": "normal", # FIXME
        # "time"
    }
    assert events.make_ovirt_event(ansible_event, correlation_id) == ovirt_event
