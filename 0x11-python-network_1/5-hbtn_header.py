#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        url = sys.argv[1]

        r = requests.get(url)
        x_request_id = r.headers.get('X-Request-Id')
        print(x_request_id)
