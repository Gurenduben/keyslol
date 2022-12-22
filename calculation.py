from cryptography.hazmat.primitives.asymmetric import ec

# Load the secp256k1 curve
curve = ec.SECP256K1()

# Convert the hexadecimal number to a decimal integer
num = int('79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8', 16)

# Calculate the result of the division
result = num / curve.g % 1

print(result)
