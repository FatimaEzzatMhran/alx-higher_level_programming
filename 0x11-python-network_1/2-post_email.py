#!/usr/bin/python3
"""
Script that takes in a URL and an email
Sends a POST request to the passed URL with the email as a parameter
Displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.parse
import urllib.request


if __name__ = "__main__":
    if len(sys.argv) >= 3:
        url = sys.argv[1]
        email = sys.argv[2]
        value = {'email': email}
        data = urllib.parse.urlencode(value).encode('ascii')

        request = urllib.request.Request(url, data)
        with urllib.request.urlopen(request) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')
        print(utf8_content)
