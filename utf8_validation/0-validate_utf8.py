#!/usr/bin/python3
def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    
    for byte in data:
        # Ensure we only consider the 8 least significant bits
        byte = byte & 0xFF
        
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                # If the byte starts with 1, it should be part of a multi-byte character
                return False
        else:
            # Check if the byte is a valid continuation byte (starts with 10)
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1
    return num_bytes == 0
