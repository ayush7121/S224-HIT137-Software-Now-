
def decryptor(ciphertext, shift):
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha(): 
            ascii_offset = 65 if char.isupper() else 97
            
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char) 
    return ''.join(decrypted_text)

# Sample Input
ciphered_quote = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY"\
                 " NAQNG GVZR UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF"\
                 " URYYQBAQ QRFRER ZR NG ZL ORFG ZNEVYLA ZBAEBR"

shift_key = 7  # Initial value for decryption key
original_quote = decryptor(ciphered_quote, shift_key)

original_quote  # Priniting decrypted text
print(original_quote)