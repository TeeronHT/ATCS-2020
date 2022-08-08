import random
import math

def alphabet_wrap(startchar, shiftvalue):
	start_offset = ord(startchar) - ord("A")
	final_offset = (start_offset + shiftvalue) % 26
	return chr(final_offset + ord("A"))

# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
	encrypted = []  
	if len(plaintext) == 0:
		return ""
	for char in plaintext:
		if(ord("A") <= ord(char) <= ord("Z")):
			encrypted.append(alphabet_wrap(char, offset))
		else:
			encrypted.append(char)
	return ("".join(encrypted)).strip()
			
# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
	decrypted = []  
	if len(ciphertext) == 0:
		return ""
	for char in ciphertext:
		if(ord("A") <= ord(char) <= ord("Z")):
			decrypted.append(alphabet_wrap(char, -1 * offset))
		else:
			decrypted.append(char)
	return ("".join(decrypted)).strip()

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
	encrypted = []
	##making the key
	fittedkey = ""
	for i in range((len(plaintext) // len(keyword)) + 1):
		fittedkey += keyword
	fittedkey = fittedkey[: len(plaintext)]
	for index in range(len(plaintext)):
			encrypted.append(alphabet_wrap(plaintext[index], ord(fittedkey[index]) - ord("A")))
	return ("".join(encrypted)).strip()

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
	decrypted = []
	fittedkey = ""
	for i in range((len(ciphertext) // len(keyword)) + 1):
		fittedkey += keyword
	fittedkey = fittedkey[: len(ciphertext)]
	for index in range(len(ciphertext)):
			decrypted.append(alphabet_wrap(ciphertext[index], -1 * ord(fittedkey[index]) - ord("A")))
	return ("".join(decrypted)).strip()

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
	private_key = []
	for i in range(n):
		sumofprevious = 1
		for j in range(i):
			sumofprevious += private_key[j]
		private_key.append(random.randint(sumofprevious + 1, 2*sumofprevious))
	sum = 0
	for i in range(n):
		sum += private_key[i]
	q = random.randint(sum + 1, 2 * sum)
	r = random.randint(2, q - 1)
	while math.gcd(r, q) != 1:
		r = random.randint(2, q - 1)
	return private_key,q,r

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: B - a length-n tuple of integers
def create_public_key(private_key):
	w, q, r = private_key
	b = []
	for i in w:
		b.append(r*i % q)
	return tuple(b)
def bytetobit(ordval):
	bitlist = [0,0,0,0,0,0,0,0]
	if ordval >= 128:
		bitlist[0] = 1
		ordval = ordval - 128
	if ordval >= 64:
		bitlist[1] = 1
		ordval = ordval - 64
	if ordval >= 32:
		bitlist[2] = 1
		ordval = ordval - 32
	if ordval >= 16:
		bitlist[3] = 1
		ordval = ordval - 16
	if ordval >= 8:
		bitlist[4] = 1
		ordval = ordval - 8
	if ordval >= 4:
		bitlist[5] = 1
		ordval = ordval - 4
	if ordval >= 2:
		bitlist[6] = 1
		ordval = ordval - 2
	if ordval >= 1:
		bitlist[7] = 1
		ordval = ordval - 1
	return bitlist

# Arguments: string, tuple B
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
	encrypted = []
	for char in plaintext:
		asciival = ord(char)
		bitlist = bytetobit(asciival)
		encrypted_byte = []
		for j in range(len(public_key)):
			encrypted_byte.append(public_key[j] * bitlist[j])
		encrypted.append(sum(encrypted_byte))
	return encrypted
def bittobyte(bitlist):
	return bitlist[0]*128 + bitlist[1]*64 + bitlist[2]*32 + bitlist[3]*16 + bitlist[4]*8 + bitlist[5]*4 + bitlist[6]*2 + bitlist[7]
def getS(q, r):
	s = 0
	while (r*s)%q != 1:
		s += 1
	return s

# Arguments: list of integers, private key (W, Q, R) with W a tuple.
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
	w, q, r = private_key
	s = getS(q,r)
	c_prime = 69
	decrypted = ""
	for c in ciphertext:
		c_prime = c * s%q
		c_decrypted = []
		for i in reversed(w):
			if i <= c_prime:
				c_decrypted.append(1)
				c_prime -= i
			else:
				c_decrypted.append(0)
		decrypted += chr(bittobyte(list(reversed(c_decrypted))))


	return decrypted


def main():
	# Choose which function you'd like to call

if __name__ == "__main__": 
	main() 