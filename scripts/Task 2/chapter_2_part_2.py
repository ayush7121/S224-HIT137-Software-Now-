def decipher_text(cipher_text, shift):
    result = []

    for ch in cipher_text:
        if ch.isalpha():
            # Shift character
            shift_start = ord('A') if ch.isupper() else ord('a')
            decrypted_char = chr((ord(ch) - shift_start - shift) % 26 + shift_start)
            result.append(decrypted_char)
        else:
            result.append(ch)

    return ''.join(result)


cipher_text = input("Enter ur ciphered quote : ")
shift = int(input("Enter ur shift value : "))
decrypted_message = decipher_text(cipher_text, shift)
print(f"if ciphered quote is {cipher_text} and Shift: {shift} \n then original quote is: {decrypted_message}")
