# simple nmap scanner with python

import threading
import socket
import argparse
import time
import sys
import ipaddress

def portScan(target, portNums):
    for x in portNums:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect(target, x)
            print(f"Port({x}) is open on target {target}\n")
        except:
            pass
            s.close()
    return
        
            
def serviceDetection(target, portNums):
    return

def main():
    
    if len(sys.argv) < 3:
        print("Usage: python3 scanner.py <targetIP> <portRange>")
        sys.exit(1)
        
    print(f"Nmap Scanner with Python Version 1.0\n")
    print(f"Starting scan on target: {sys.argv[1]} with port range: {sys.argv[2]}\n")
    
    target = sys.argv[1]
    portNums = sys.argv[2]
    
    try:
        ipaddress.ip_address(target)
    except KeyboardInterrupt:
        print("\n Caught Keyboard Interrupt, exiting...")
        sys.exit(0)
    except ValueError:
        print("Invalid IP address")
        sys.exit(1)
    
    portScan(target, portNums)
    #serviceDetection(target, portNums)
    
    sys.exit(0)
    
        
if __name__ == "__main__":
    main()
