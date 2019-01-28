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

import os
import requests
import requests_unixsocket
import logging

logger = logging.getLogger('ansible-runner')

def make_ovirt_event(data):
    return data

def send_request(url, data, headers={}, urlpath=None):
    if os.path.exists(url):
        url_actual = "http+unix://{}".format(url.replace("/", "%2F"))
        if urlpath is not None:
            url_actual += urlpath
        session = requests_unixsocket.Session()
    else:
        url_actual = url
        session = requests.Session()
    logger.debug("Sending payload to {}".format(url_actual))
    event_data = make_ovirt_event(data)
    logger.debug("Sending event {}".format(event_data)
    return session.post(url_actual, headers=headers, json=(event_data))


def get_configuration(runner_config):
    runner_url = runner_config.settings.get("runner_http_url", None)
    runner_url = os.getenv("RUNNER_HTTP_URL", runner_url)
    runner_path = runner_config.settings.get("runner_http_path", None)
    runner_path = os.getenv("RUNNER_HTTP_PATH", runner_path)
    runner_headers = runner_config.settings.get("runner_http_headers", None)
    return dict(runner_url=runner_url,
                runner_path=runner_path,
                runner_headers=runner_headers)


def status_handler(runner_config, data):
    plugin_config = get_configuration(runner_config)
    if plugin_config['runner_url'] is not None:
        status = send_request(plugin_config['runner_url'],
                              data=data,
                              headers=plugin_config['runner_headers'],
                              urlpath=plugin_config['runner_path'])
        logger.debug("POST Response {}".format(status))
    else:
        logger.info("HTTP Plugin Skipped")


def event_handler(runner_config, data):
    status_handler(runner_config, data)
