#! /usr/bin/env python3
import os
from pprint import pprint
import json
from templates import *

from urllib.parse import parse_qs
import sys

def main():
    print("Content-Type: text/html")
    print()
    
    print("<!doctype html>")
    print("<head>")
    print("<title>Hello</title>")
    print("<style>pre {white-space: pre-wrap; word-wrap: break-word;}</style>")
    print("</head>")
    print("<h2>Hello</h2>")

    print("<dl>")
    print("<dt>QUERY_STRING:</dt>")
    print("<dd>")
    print(parse_qs(os.environ.get("QUERY_STRING")))
    print("</dd>")
    print("<dt>HTTP_USER_AGENT:</dt>")
    HTTP_USER_AGENT = os.environ.get("HTTP_USER_AGENT", None)
    print("<dd>" + HTTP_USER_AGENT + "</dd>")
    print("</dl>")

    print("<pre>")
    env = {}
    for key, value in os.environ.items():
        env[key] = value
    print(json.dumps(env))
    print("</pre>")
    

main()
