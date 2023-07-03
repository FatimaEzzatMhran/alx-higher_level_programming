#!/usr/bin/python3
"""
Python script that takes in a URL and an email address
Sends a POST request to the passed URL with the email as a parameter
And finally displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        url = sys.argv[1]
        email = sys.argv[2]
        data = {'email': email}

        r = requests.post(url, data=data)
        print(r.text)
