# -------------------------------------------------------------------------
#
# Copyright (c) 2023 General Motors GTO LLC
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# SPDX-FileType: SOURCE
# SPDX-FileCopyrightText: 2023 General Motors GTO LLC
# SPDX-License-Identifier: Apache-2.0
#
# -------------------------------------------------------------------------

import json
import os
import re

data = []


def process_proto(directory):
    for root, dirs, files in os.walk(directory):
        service_file_path = None
        topic_file_path = None
        for file in files:
            if file.endswith('_service.proto'):
                service_file_path = os.path.join(root, file)
            if file.endswith('_topics.proto'):
                topic_file_path = os.path.join(root, file)
        if service_file_path and topic_file_path:
            read_proto_file(service_file_path, topic_file_path)


def read_proto_file(service_file_path, topic_file_path):
    with open(service_file_path, 'r') as file:
        service_file_content = file.read()
    with open(topic_file_path, 'r') as file:
        topic_file_content = file.read()
    extract_proto_info(service_file_content, topic_file_content)


def extract_proto_info(service_file_content, topic_file_content):
    # Extract service name
    service_name_match = re.search(r'service\s+(\w+)\s*{', service_file_content)
    service_name = service_name_match.group(1) if service_name_match else None

    # Extract uprotocol name
    uprotocol_name_match = re.search(r'option\s+\(uprotocol\.name\)\s*=\s*"([^"]+)"', service_file_content)
    uprotocol_name = uprotocol_name_match.group(1) if uprotocol_name_match else None

    # Extract list of RPCs
    rpc_matches = re.findall(r'rpc\s+(\w+)\s*\(\s*[^)]*\s*\)', service_file_content)
    rpcs = rpc_matches if rpc_matches else None

    message_value_match = re.findall(r'message\s+(\w+)\s*{', topic_file_content)
    messages = message_value_match if message_value_match else None

    append_to_data(uprotocol_name, service_name, rpcs, messages)


def append_to_data(entity, display_name, rpcs, messages):
    json_obj = {"name": entity, "display_name": display_name, "rpc": rpcs, "message": messages}

    data.append(json_obj)


if __name__ == "__main__":
    process_proto('protos')
    resulting_json = json.dumps(data, indent=2)

    print(resulting_json)
