"""

n0-venv
rle enoder in python
provides rle sizes from 8 bit to 16 bit

"""
import struct

def rle(b_str : bytes, max_bits ):
    
    """
    
        b_str : byte string
        max_bits : either 8 or 16, defaults to 8 if nothing is passed

    """
    
    buffer = b""
    last_char = b""

    count = 0 

    max_bits = not max_bits and 8 or max_bits
    bit_sig = max_bits == 8 and "B" or "H"
    max_count = max_bits == 8 and (2**8)-1 or (2**16)-1

    for i in range(b_str.__len__()):
    
       
        char = b_str[i:i+1]

        if not last_char: last_char = char; count +=1; continue

        if not char == last_char or count >= max_count: 


            buffer += last_char + struct.pack(bit_sig,count)

            count = 0

        last_char = char

        count +=1

    buffer += last_char + struct.pack(bit_sig,count)
    return buffer

