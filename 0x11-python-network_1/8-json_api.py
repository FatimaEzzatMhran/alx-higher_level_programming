#!/usr/bin/python3
"""
Use requests package to make a post request to given URL with argument
set in variable `q`, defaulting to empty string. If response body is properly
JSON formatted and not empty, display `id` and `name` as given format.
Otherwise display error message.
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
