#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        url = sys.argv[1]

        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            headers = response.info()
            x_request_id = headers.get('X-Request-Id')
            if x_request_id:
                print(x_request_id)
# or print(response.info().['X-Request-Id'])
