#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

# Get the file path from the command line
file_path = "00 - INBOX/02 - LITERATURE/Yoga_R00_cleaned.md"

try:
    # Try to read with UTF-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print("File read successfully with UTF-8 encoding.")
        print("First 500 characters:")
        print(content[:500])
except UnicodeDecodeError:
    # If UTF-8 fails, try with different encodings
    encodings = ['latin1', 'cp1252', 'iso-8859-1']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
                print(f"File read successfully with {encoding} encoding.")
                print("First 500 characters:")
                print(content[:500])
                break
        except UnicodeDecodeError:
            continue
    else:
        print(f"Could not read the file with any of the attempted encodings.") 