#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
import chardet

def detect_encoding(file_path):
    """Detect the encoding of a file using chardet."""
    with open(file_path, 'rb') as file:
        raw_data = file.read(10000)  # Read first 10000 bytes for detection
        result = chardet.detect(raw_data)
        return result['encoding'], result['confidence']

def convert_file_to_utf8(input_path, output_path=None):
    """Convert a file from its detected encoding to UTF-8."""
    if output_path is None:
        # If no output path provided, create one with _utf8 suffix
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_utf8{ext}"
    
    # Detect the encoding
    detected_encoding, confidence = detect_encoding(input_path)
    print(f"Detected encoding: {detected_encoding} with {confidence:.2%} confidence")
    
    # Try different encodings if detection confidence is low
    encodings_to_try = ['utf-8', 'latin1', 'cp1252', 'iso-8859-1']
    if detected_encoding and confidence > 0.5:
        encodings_to_try.insert(0, detected_encoding)
    
    # Read the file with the best encoding we can find
    content = None
    used_encoding = None
    
    for encoding in encodings_to_try:
        try:
            with codecs.open(input_path, 'r', encoding=encoding) as file:
                content = file.read()
                used_encoding = encoding
                print(f"Successfully read file with {encoding} encoding")
                break
        except UnicodeDecodeError:
            print(f"Failed to read with {encoding} encoding")
    
    if content is None:
        print("Could not read the file with any of the attempted encodings")
        return False
    
    # Write the content in UTF-8
    try:
        with codecs.open(output_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"File successfully converted from {used_encoding} to UTF-8")
        print(f"Saved as: {output_path}")
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

if __name__ == "__main__":
    input_file = "00 - INBOX/02 - LITERATURE/Yoga_R00_cleaned.md"
    convert_file_to_utf8(input_file) 