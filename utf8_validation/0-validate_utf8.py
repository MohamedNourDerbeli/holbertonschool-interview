#!/usr/bin/python3

def validUTF8(data):
	"""
	Determines if a given data set represents a valid UTF-8 encoding.

	UTF-8 is a variable-width character encoding that uses 1 to 4 bytes to represent
	each character. This function validates whether the input data adheres to the
	rules of UTF-8 encoding.

	Rules:
	- A 1-byte character starts with `0`.
	- A multi-byte character starts with `110`, `1110`, or `11110` for 2, 3, or 4-byte
	  characters respectively.
	- Continuation bytes in multi-byte characters start with `10`.

	Parameters:
	data (list of int): A list of integers representing bytes of data. Each integer
						should be in the range 0-255 (only the 8 least significant bits
						are considered).

	Returns:
	bool: True if the data is a valid UTF-8 encoding, False otherwise.
	"""
	# Number of bytes in the current UTF-8 character
	num_bytes = 0
	
	for byte in data:
		# Ensure we only consider the 8 least significant bits
		byte = byte & 0xFF
		
		if num_bytes == 0:
			# Determine the number of bytes in the UTF-8 character
			if (byte >> 5) == 0b110:
				# 2-byte character
				num_bytes = 1
			elif (byte >> 4) == 0b1110:
				# 3-byte character
				num_bytes = 2
			elif (byte >> 3) == 0b11110:
				# 4-byte character
				num_bytes = 3
			elif (byte >> 7):
				# If the byte starts with 1, it should be part of a multi-byte character
				return False
		else:
			# Check if the byte is a valid continuation byte (starts with 10)
			if (byte >> 6) != 0b10:
				return False
			num_bytes -= 1
	
	# If all characters are complete, num_bytes should be 0
	return num_bytes == 0
