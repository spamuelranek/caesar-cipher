import re

def encrypt(text, shift):

  split_text_into_words = text.split(' ')

  encrypted_words = ''

  for word in split_text_into_words:

    encrypted_string = ''
    
    for char in word:
      
      regex_letter = r"[a-zA-Z]"
      regex_lower = r"[a-z]"
      regex_upper = r"[A-Z]"
      letter_check = re.match(regex_letter,char)
      if letter_check:
       
        before_encryption_value = ord(char)
        after_encryption_value = before_encryption_value + shift
        
        lower_case_check = re.match(regex_lower, char)
        upper_case_check = re.match(regex_upper,char)

        if lower_case_check and after_encryption_value > 122:
          after_encryption_value -= 26
        elif upper_case_check and after_encryption_value > 90:
          after_encryption_value -= 26

        shifted_char = chr(after_encryption_value)
        encrypted_string += shifted_char
      
      else:
        encrypted_string += char
    
    if len(encrypted_words) > 0:
      encrypted_words +=f" {encrypted_string}"
    else:
      encrypted_words = encrypted_string
  
  return encrypted_words


def decrypt(text, shift):
  decrypted = encrypt(text, -shift)
  return decrypted

def crack(text):
  pass

