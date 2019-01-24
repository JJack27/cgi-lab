#!/usr/bin/env python3
import os

def main():
    length = os.environ['CONTENT_LENGTH']
    cookie = os.environ['HTTP_COOKIE']

    print(length)

main()