import sys # standard import to interact with system + args

def yap():
    print("Usage: python3 pa02.py <keytextfile.txt> <plaintextfile.txt>") # check for 2 args
    sys.exit(1) # proper exit call
    
def main(): 
    
    # check for oopsie doopsies
    if len(sys.argv) != 3: # if argument count is not script name + the 2 args
        yap()
    # check for more oopsie doopsies
    if sys.argv[1].endswith('.txt') == False or sys.argv[2].endswith('.txt') == False:
        yap()
    
# prereqs w/ 2 args and file check

    with open(sys.argv[1]) as f: # open key file, shorten to f
        n = int(f.readline()) # read key file's first line and append to n, shorten it to f for ease of use
        key = [[int(x) for x in f.readline().split()] for _ in range(n)] # read next lines and append to 2d list until all n lines read

    with open(sys.argv[2]) as f: # open plaintext file, shorten it to f for ease of use
        chars = [c.lower() for c in f.read() if c.isalpha()] # read plaintext file, converting to lowercase + kill non-alpha chars

    while len(chars) % n != 0: # while length of chars is NOT a multiple of n PAD X
        chars.append('x') # pad with x until multiple of n

    cipher = [] # initialize empty list 
    for i in range(0, len(chars), n): # loop through chars for every n 
        block = [ord(c) - ord('a') for c in chars[i:i+n]] # convert chars to 0-25 by subtraction
        for r in range(n): # Go through rows of key matrix for hill cipher mult
            cipher.append(chr(sum(key[r][c] * block[c] for c in range(n)) % 26 + ord('a'))) # hill cipher formula = hill cipher mult + mod -> converted into char then appended to cipher list
# most of the cipher formula done above
# formatting start |
    print("\nKey matrix:") # print key matrix with formatting
    for row in key: # formatting adjustment
        print(''.join(f'{v:4d}' for v in row)) # 4 spaces per value
    plainString = ''.join(chars) # convert chars to strings

    print("\nPlaintext:") # print plaintext | 80 chars a lien
    for i in range(0, len(plainString), 80): # loop through the string 
        print(plainString[i:i+80]) # print 80 chars at a time until end

    cipherString = ''.join(cipher) # convert list to string 
    print("\nCiphertext:") # required format
    for i in range(0, len(cipherString), 80): # loop through string
        print(cipherString[i:i+80]) # 80 chars until end
# formatting end |
if __name__ == "__main__": # call main function properly
    main()
