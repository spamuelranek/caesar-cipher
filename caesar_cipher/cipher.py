import re
from caesar_cipher.corpus_loader import word_list, name_list

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
          shifted_char = chr(after_encryption_value - 26)

        
        elif lower_case_check and after_encryption_value < 97:
          shifted_char = chr(after_encryption_value + 26)
 
        elif upper_case_check and after_encryption_value > 90:
          shifted_char = chr(after_encryption_value - 26)
        
        elif upper_case_check and after_encryption_value < 65:
          shifted_char = chr(after_encryption_value + 26)
        
        else:

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

def create_possible_solutions(text):
  range_of_shifts = range(1,26)

  total_list_of_decryptions = []

  for shift in range_of_shifts:
    decrypt_attempt = decrypt(text,shift)
    total_list_of_decryptions.append(decrypt_attempt)

  return total_list_of_decryptions

def real_word_count(text):
  split_into_words = text.split(' ')

  word_count = 0

  for possible_word in split_into_words:
    regex = r"[^a-zA-Z]+"
    cleaned_word = re.sub(regex,'',possible_word)
    if cleaned_word.lower() in word_list:
      word_count += 1
    elif cleaned_word in name_list:
      word_count += 1

  return word_count



def crack(text):
  total_decryptions = create_possible_solutions(text)
  highest_percentage = 50
  best_solution = ""
  for decryption_attempt in total_decryptions:
    word_count = real_word_count(decryption_attempt)
    percentage = int(word_count/ len(decryption_attempt.split(" ")) * 100)
    print(decryption_attempt, percentage)
    if percentage > highest_percentage:
      highest_percentage = percentage
      best_solution = decryption_attempt

  return best_solution


if __name__ == "__main__":

  def test_crack_phrase():
    phrase = "It was the best of times, it was the worst of times."
    encrypted = encrypt(phrase, 10)
    actual = crack(encrypted)
    print(actual)
  
  test_crack_phrase()







