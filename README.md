# py-cloudflare-ddns
<!-- [![Build Status](https://travis-ci.org/0x46616c6b/py-cloudflare-ddns.svg?branch=master)](https://travis-ci.org/0x46616c6b/py-cloudflare-ddns)
[![PyPI version](https://badge.fury.io/py/py-cloudflare-ddns.svg)](https://badge.fury.io/py/py-cloudflare-ddns)
[![PyPI](https://img.shields.io/pypi/pyversions/py-cloudflare-ddns.svg)](https://pypi.python.org/pypi/py-cloudflare-ddns)
[![PyPI](https://img.shields.io/pypi/l/py-cloudflare-ddns.svg)](https://pypi.python.org/pypi/py-cloudflare-ddns)

----- -->

**Table of Contents**

- [Installation](#installation)
- [Operation](#Operation)
- [Acknowledgements](#Acknowledgements)

## Installation

```console
git clone https://github.com/dmoruzzi/py-cloudflare-ddns.git
```

## Operation

`py-cloudflare-ddns` is a command line tool. It has the following operations:


```console
usage: py-cloudflare-ddns.py [-h] --zoneid ZONEID --recordid RECORDID --apikey APIKEY --email EMAIL --recordname
                             RECORDNAME [--recordtype RECORDTYPE] [--insecure INSECURE] [--verbose VERBOSE]
                             [--protocol PROTOCOL]

options:
  -h, --help            show this help message and exit
  --zoneid ZONEID       CloudFlare Zone ID; https://developers.cloudflare.com/fundamentals/get-started/basic-
                        tasks/find-account-and-zone-ids/
  --recordid RECORDID   Cloudflare Record ID; https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records
  --apikey APIKEY       Cloudflare API Key; https://dash.cloudflare.com/profile/api-tokens
  --email EMAIL         Email
  --recordname RECORDNAME
                        Record Name
  --recordtype RECORDTYPE
                        DNS record type (default: "A")
  --insecure INSECURE   allow insecure Global API Key access
  --verbose VERBOSE     Verbose output (default: False)
  --protocol PROTOCOL   DNS record protocol (default: "ipv4")
```


This CLI application is best maintained through a cron job. For example, to run this script every 24 hours, add the following line to your crontab:

```console
0 0 * * * /path/to/py-cloudflare-ddns.py --zoneid <zoneid> --recordid <recordid> --apikey <apikey> --email <cloudflare_email> --recordname <recordname>
```

## Limitations

This script is currently limited to updating a single DNS record. If you would like to update multiple records, you can run this script multiple times with different arguments. You can also run this script multiple times with the same arguments, but this is not recommended :P

## Acknowledgements

The [CloudFlare API](https://api.cloudflare.com/) team is incredible for providing detailed and granular access to their REST API. This script is a wrapper for all the hardwork Cloudflare dedicated to the Internet. Thank you!
