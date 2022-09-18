#!/usr/bin/env python3
# Path: py-cloudflare-ddns.py
# Parameters: --help, --zoneid, --recordid, --apikey, --email, --recordname, --type, --insecure, --verbose, --protocol

import argparse
import requests
from json import dumps as dict_to_str


def fetch_ip(protocol, verbose):
    '''
    fetches the ip address of the machine running the script from ipify.org
    return: ipv4 address as a string; returns None if the request fails
    '''
    if protocol == 'ipv4':
        openapi_ip_lst = ['https://api.ipify.org/',
                      'https://api4.my-ip.io/ip', 'https://ip4.seeip.org/']
    else:
        openapi_ip_lst = ['https://api6.ipify.org/',
                      'https://api6.my-ip.io/ip', 'https://ip6.seeip.org/']
    for url in openapi_ip_lst:
        try:
            response = requests.get(url)
            if verbose: print(f'[INFO] IP from {url} [{response.status_code}]: {response.text}')
            if response.status_code == 200:
                return response.text
        except:
            pass
    return None


def main(zonid, recordid, apikey, email, recordname, recordtype, insecure, verbose, protocol):
    '''
    update dynamic dns record on cloudflare
    updates the ip address of a cloudflare dns record
    '''
    if protocol == 'ipv6' and recordtype != 'AAAA':
        print('[ERROR] IPv6 protocol specified but record type is not AAAA;')
        return False
    ip_str = fetch_ip(protocol, verbose)
    if ip_str is None:
        return False
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Email": email,
    }

    data = {
        "type": recordtype,
        "name": recordname,
        "content": ip_str
    }
    if verbose: print('[INFO] Data: ', data)


    if 'Bearer' in apikey:
        if verbose: print('[INFO] Using Bearer token')
        headers['Authorization'] = apikey
    else:
        if verbose: print('[INFO] Attempting CloudFlare Global API key')
        if insecure:
            if verbose: print('[INFO] CloudFlare Global API key enabled and insecure connections permitted; this is not recommended.')
            headers['X-Auth-Key'] = apikey
        else:
            if verbose: print('[INFO] Failed CloudFlare Global API key; --insecure mode not enabled')
            print('[ERROR] API key must be a Bearer token or --insecure must be set')
            return False
    if verbose: print('[INFO] Headers: ', headers)

    response = requests.patch(
        f"https://api.cloudflare.com/client/v4/zones/{zonid}/dns_records/{recordid}", headers=headers, data=dict_to_str(data))
    if verbose: print('[INFO] Response [{response.status_code}]: ', response.json())
    if response.status_code == 200:
        if verbose: print('[INFO] Successfully updated DNS record')
        return True
    else:
        print('[ERROR] Failed to update DNS record')
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--zoneid', help='CloudFlare Zone ID; https://developers.cloudflare.com/fundamentals/get-started/basic-tasks/find-account-and-zone-ids/', type=str, required=True)
    parser.add_argument(
        '--recordid', help='Cloudflare Record ID; https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records', type=str, required=True)
    parser.add_argument(
        '--apikey', help='Cloudflare API Key; https://dash.cloudflare.com/profile/api-tokens', type=str, required=True)
    parser.add_argument('--email', help='Email', type=str, required=True)
    parser.add_argument('--recordname', help='Record Name',
                        type=str, required=True)
    parser.add_argument('--recordtype', help='DNS record type (default: "A")', type=str, default='A', required=False)
    parser.add_argument(
        '--insecure', help='allow insecure Global API Key access', type=bool, default=False, required=False)
    parser.add_argument('--verbose', help='Verbose output (default: False)',
                        type=bool, default=False, required=False)
    parser.add_argument('--protocol', help='DNS record protocol (default: "ipv4")',
                        type=str, default='ipv4', required=False)
    args = parser.parse_args()
    main(args.zoneid, args.recordid, args.apikey, args.email, args.recordname, args.recordtype, args.insecure, args.verbose, args.protocol.lower())
