#!/usr/bin/env python3
"""
CSCI 5471 Homework 4 Problem 4a
INSTRUCTIONS : run 'python3 hw4_problem4a.py' in terminal

RSA Key Generation for username: CHEN7790
"""

import hashlib

def open_encoded_from_file(filename):
  with open(filename, 'rb') as f:
      data = f.read()
  return int.from_bytes(data, 'big')

def main():
    username = "CHEN7790"
    
    # get the encoded 1024-bit primes p and q
    p = open_encoded_from_file("p")
    q = open_encoded_from_file("q")
    
    # calculate n the rsa mod
    n = p * q
    #phi(n)
    phi_n = (p - 1) * (q - 1)
    
    username_hash = hashlib.sha256(username.encode()).digest()
    e = int.from_bytes(username_hash, 'big')
    if e % 2 == 0:
        e += 1
    
    if e >= phi_n:
        e = e % phi_n
    if e <= 1:
        e = 65537 #standard RSA exponent
    
    # Compute d = e^(-1) mod phi(n)
    inverse = pow(e, -1, phi_n)
    
    print(f"e = {e:x}")
    print(f"d = {inverse:x}")

if __name__ == "__main__":
    main()