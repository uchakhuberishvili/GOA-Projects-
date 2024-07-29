def longest_palindrome(s):
    def is_palindrome(sub):
        return sub == sub[::-1]
    n = len(s)
    if n == 0:
        return 0
    max_length = 1
    for start in range(n):
        for end in range(start + 1, n + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                max_length = max(max_length, len(substring))
                
    return max_length

def binary_to_string(binary_str):
    if not binary_str:
        return ""
    decoded_text = ""
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        ascii_value = int(byte, 2)
        decoded_text += chr(ascii_value)
    return decoded_text

