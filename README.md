<!--
SPDX-FileCopyrightText: 2022 Greg Back <git@gregback.net>
SPDX-License-Identifier: CC-BY-SA-4.0
-->
# unicode-web

Get Information on Unicode characters

## Installation

```shell
mkvirtualenv unicode-web
python -m pip install -r requirements.txt
```

## Usage

```shell
python app.py
```

Open a browser to <http://127.0.0.1:5000>.

To get  a string, paste it at end of the, like
<http://127.0.0.1:5000/3%EF%B8%8F%E2%83%A3,%202%EF%B8%8F%E2%83%A3,%201%EF%B8%8F%E2%83%A3,%20it's%20running!%20%F0%9F%9A%80%E2%9C%85>
