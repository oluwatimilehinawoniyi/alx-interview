#!/usr/bin/python3

"""
a method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Helper function to check if a byte is a valid continuation byte
    """
    def isContinuation(byte):
        return (byte & 0b11000000) == 0b10000000
    i = 0
    while i < len(data):
        """
        Get the number of bytes for the current UTF-8 character
        """
        num_bytes = 0
        if (data[i] & 0b10000000) == 0:
            num_bytes = 1
        elif (data[i] & 0b11100000) == 0b11000000:
            num_bytes = 2
        elif (data[i] & 0b11110000) == 0b11100000:
            num_bytes = 3
        elif (data[i] & 0b11111000) == 0b11110000:
            num_bytes = 4
        else:
            return False

        if i + num_bytes > len(data):
            return False

        """
        Check if subsequent bytes are valid continuation bytes
        """
        for j in range(1, num_bytes):
            if not isContinuation(data[i + j]):
                return False
        i += num_bytes
    return True
