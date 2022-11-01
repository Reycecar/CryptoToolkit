# CryptoToolkit
Explanations for each program below
## ex_gcd.py
## Extended Euclidean Algorithm Calculator
### Takes in two arguments (a and b) and computes the following:
#### Greatest Common Divisor of a and b
#### Multiplicative inverse of a (mod b)
#### Multiplicative inverse of b (mod a)
#### Calibrated (non-negative) multiplicative inverses

## gcd.py
## Greatest Common Divisor calculator
### Takes in two arguments (a and b) and computes the gcd of a and b

## lfsr.py
## LFSR Calculator
### Takes in the exponent values of an LFSR polynomial and responds with  data about the polynomial (not 0 inclusive)
#### ie: for (x^8 + x^4 + x^3 + x + 1) you would run: lfsr.py 8 4 3 1

## modtabs.py
## Order calculator
### Computes and displays all elements of (x^y mod n) where: x ∈ {1, 2, ... (n-1), n} and y ∈ {0, 1, ... (n-1)}
### order = number of elements of a finite field
### Runs with an integer argument (n) and ___optional___ integer argument (m).

### With 1 argument:
#### Will create a table with the powers of each value from (1 to n)^(0 to n) mod n
#### as well as the order of each value in that table.
#### Table will indicate where the order starts to repeat.

### With 2 arguments:
#### Shows m^x mod n (where x is 0-n) as well as the order for m in Zn

## subCipherInfo.py
## Get info about a ciphertext that is encrypted with a substitution cipher + caesar cipher cracking

### Information gathering of a ciphertext

### Arg 1 can be a file path or a ciphertext.

### if argument 1 is a path to a file:
#### subCiperInfo will use the file to build the ciphertext

### if arg 1 is ciphertext:
#### subCipherInfo will use the given ciphertext
    
(you can also run without any arguments, the program will simply ask you for the ciphertext in the form of a filename or the text itself)

## multiply_poly.py
## Multiply two polynomials that are represented as 8-bit hexadecimal values within Galois Field 2^8
### Argument 1 is the hexadecimal representation of polynomial A
### Argument 2 is the hexadecimal representation of polynomial B
### Program computes A * B in GF(2^8)

GF(2^8) uses the AES Irreducable Polynomial (x^8 + x^4 + x^3 + x + 1) 
(Bitwise, this is 1 0001 1011 or 0x11B)
