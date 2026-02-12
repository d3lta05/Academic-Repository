#!/usr/bin/env python3 
# calculates the checksum of a file in python
# added some minimum safeguards for extended personal use

import sys

def validateFilename(filename):
                                                    # verify input isn't blank / whitespace
    if not filename or not filename.strip():
        sys.stderr.write("Error: Filename cannot be empty\n")
        sys.exit(1)
    if '..' in filename:
        sys.stderr.write(f"Error: Invalid filename '{filename}'\n")
        sys.exit(1)
    
    return filename
        
def validateChecksumSize(size_str):
   
    try:
        size = int(size_str)
        if size not in [8, 16, 32]:
            sys.stderr.write("Valid checksum sizes are 8, 16, or 32\n")
            sys.exit(1)
        return size
    except ValueError:
        sys.stderr.write("Valid checksum sizes are 8, 16, or 32\n")
        sys.exit(1)

def readFileContents(filename):
    
    try:
        with open(filename, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        sys.stderr.write(f"Error: File '{filename}' not found\n")
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"Error reading file: {e}\n")
        sys.exit(1)

def echoFileContents(data):
    
    print()  # intentional blank line 
    text = data.decode('ascii', errors='replace')
    
    # 80-char chunks
    for i in range(0, len(text), 80):
        chunk = text[i:i+80]
        if i + 80 < len(text):  
            print(chunk)  
        else:  
            print(chunk)  

def padData(data, checksum_size): # heavily modified standard padding functions to generate correct output in line with pa01test.sh
    bytes_per_chunk = checksum_size // 8
    remainder = len(data) % bytes_per_chunk
    
    if remainder != 0:
        padding_needed = bytes_per_chunk - remainder
        data = data + b'X' * padding_needed
    
    return data

def calculateChecksum(data, checksum_size):
  
    bytes_per_chunk = checksum_size // 8
    checksum = 0
    
    # proc in chunks
    for i in range(0, len(data), bytes_per_chunk):
        chunk = data[i:i+bytes_per_chunk]
        chunk_value = 0
        for byte in chunk:
            chunk_value = (chunk_value << 8) | byte
        
        checksum += chunk_value
    
    mask = (1 << checksum_size) - 1
    checksum = checksum & mask
    
    return checksum

def formatChecksumOutput(checksum, checksum_size, char_count): 
    
    hex_width = checksum_size // 4
    
    # "%2d bit checksum is %8lx for all %4d chars\n"
    print(f"{checksum_size:2d} bit checksum is {checksum:8x} for all {char_count:4d} chars")      
    


def main():

    if len(sys.argv) != 3:
        sys.stderr.write("Usage: python3 pa01.py <input_file> <checksum_size>\n")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    checksum_size = validateChecksumSize(sys.argv[2])
    
    validateFilename(input_filename)

    file_data = readFileContents(input_filename)
    padded_data = padData(file_data, checksum_size)
    
    echoFileContents(padded_data)
    checksum = calculateChecksum(padded_data, checksum_size)
    formatChecksumOutput(checksum, checksum_size, len(padded_data))

if __name__ == "__main__":
    main()
