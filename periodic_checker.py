#!/usr/bin/env python3

import json
import ssl
import sys

from send_email import send_email

from bs4 import BeautifulSoup
from urllib.request import urlopen

def main():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except:
        print('The data.json file was not found. Please refer to the README on how to get setup')
        exit(1)

    try:
        with open('baseline-values.json', 'r') as f:
            baseline_data = json.load(f)
    except:
        baseline_data = {}

    # Loop through interested url and selector pairs
    for url, selector in data.items():
        context = ssl._create_unverified_context()
        with urlopen(url, context=context) as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc, 'html.parser')
        # Extract contents to compare with baseline
        html_element = soup.select(selector)
        try:
            contents = html_element.pop().get_text()
        except:
            print('selector element was not found')
            exit(1)

        # Send email if contents differs from baseline
        # Store contents if there is no existing baseline
        baseline_key = f'{url} {selector}'

        if baseline_key in baseline_data and baseline_data[baseline_key] != contents:
            subject = f'{url} contents have changed'
            body = f'Content in {url} with selector {selector} has changed from \'{baseline_data[baseline_key]}\' TO \'{contents}\''
            send_email(subject, body)

        baseline_data[baseline_key] = contents


    # Remove baseline values no longer in interested data items
    baseline_data = { k: v for k, v in baseline_data.items() if k.split(' ')[0] in data }

    # Write updated base line values back out to file
    with open('baseline-values.json', 'w+') as f:
        f.write(json.dumps(baseline_data, sort_keys=True, indent=4))

main()