import numpy as np

def generate_hamming_code(data_bits):
    # Number of parity bits needed for 11 data bits
    p_bits = 4
    
    # Total bits (data + parity)
    total_bits = 15
    
    # Initialize array to hold the coded bits
    coded_bits = np.zeros(total_bits, dtype=int)
    
    # Position of parity bits (1-indexed)
    p_positions = [1, 2, 4, 8]
    
    # Place the data bits in the correct positions
    j = 0
    for i in range(1, total_bits + 1):
        if i not in p_positions:
            coded_bits[i-1] = data_bits[j]
            j += 1
    
    # Calculate parity bits
    for p in p_positions:
        # XOR of bits whose position has the pth bit set in its binary representation
        xor = 0
        for i in range(1, total_bits + 1):
            if i & p:
                xor ^= coded_bits[i-1]
        coded_bits[p-1] = xor
    
    return coded_bits

# Example usage
data_bits = np.array([1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1])  # 11 data bits
hamming_code = generate_hamming_code(data_bits)

print(f"Data bits: {data_bits}")
print(f"Hamming code: {hamming_code}")
