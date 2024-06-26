"""
SPDX-FileCopyrightText: Copyright (c) 2024 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
SPDX-FileType: SOURCE
SPDX-License-Identifier: Apache-2.0
"""

default_max = 100
default_min = 0


MAX_VALUES = {
    "longitude": 180,
    "latitude": 90,
    "radius": 1000,
    "length": 1000,
    "width": 1000,
    "height": 1000,
    "expiration_duration": 100,
    "idle_duration": 16777215,
    "running_duration": 16777215,
    "temperature": 50,
    "current_sequence": 7,
    "total_sequences": 7,
    "priority": 255,
    "pressure": 20460,
    "time_to_flat": 2097151,
    "light_intensity": 1275,
    "hours": 24,
    "minutes": 59,
    "seconds": 59,
    "nanos": 999999999,
    "token": 10000,
}

MIN_VALUES = {
    "longitude": -180,
    "latitude": -90,
    "expiration_duration": -1,
}
