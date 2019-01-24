#! /usr/bin/env python3
import os
from pprint import pprint
import json
from templates import *
from secret import *
import cgi
from urllib.parse import parse_qs
import sys

authorized = False

def main():
    global authorized

    form = cgi.FieldStorage()
    username_in = form.getvalue('username')
    password_in  = form.getvalue('password')
    
    if username_in == username and password_in == password:
        authorized = True

    if not authorized:
        print("Content-Type: text/html")
        print()
        print(login_page())
        print(username_in)

    else:
        print("Content-Type: text/html")
        print()
        print(secret_page(username_in, password_in))
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

        print("<dt>Data from POST:</dt>")
        print("<dd>")
        print(username_in, password_in)
        print("</dd>")

        print("</dl>")
        

        print("<pre>")
        env = {}
        for key, value in os.environ.items():
            env[key] = value
        print(json.dumps(env))
        print("</pre>")
    

main()
