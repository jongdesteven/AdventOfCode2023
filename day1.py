file = open("input.txt", "r")
#file = open("test.txt", "r")
totalValue = 0

def findFirstNumber( line ):
  english_digits = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9 
  }

  first_digit_position = -1

  first_word_position = -1
  number_found = -1
  word_found = -1

  #print(line)

  # find first number location, if any.
  for index, char in enumerate(line):
    if char.isalpha() == False and char != '\n':
      first_digit_position = index
      #print("digit: ", index, "char: ", char)
      number_found = int(char)
  #    print("Number found: ", number_found)
      break

  # find first written character, if any
  for digits in english_digits:
    found = line.find(digits)
    #print("digit: ", digits, "\tfound: ", found)
    if found != -1:
      if first_word_position == -1:
        first_word_position = found
        word_found= english_digits[digits]
      elif found < first_word_position:
        first_word_position = found
        word_found= english_digits[digits]
  #    print("Word Found: ", word_found)

  #print("digit_pos: ", first_digit_position," word_pos: ", first_word_position)
  if first_digit_position == -1 and first_word_position == -1:
    return None
  elif first_word_position == -1:
    return number_found
  elif first_digit_position == -1:
    return word_found
  else:
    if first_digit_position < first_word_position:
      return number_found
    else:
      return word_found
  
def findLastNumber( line ):
  english_digits = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9 
  }

  last_digit_position = -1

  last_word_position = -1
  number_found = -1
  word_found = -1

 # print(line)

  # find first number location, if any.
 # for index, char in enumerate(reversed(line)):
  for index, char in reversed(list(enumerate(line))):
    if char.isalpha() == False and char != '\n':
      last_digit_position = index
      #print("digit: ", index, "char: ", char)
      number_found = int(char)
    #  print("Number found: ", number_found)
      break

  # find first written character, if any
  for digits in english_digits:

    found = line.rfind(digits)
    print("digit: ", digits, "\tfound: ", found)
    if found != -1:
      if last_word_position == -1:
        last_word_position = found
        word_found= english_digits[digits]
      elif found > last_word_position:
        last_word_position = found
        word_found= english_digits[digits]
  #    print("Word Found: ", word_found)

  print("digit: ", last_digit_position," word: ", last_word_position)
  if last_digit_position == -1 and last_word_position == -1:
    return None
  elif last_word_position == -1:
    return number_found
  elif last_digit_position == -1:
    return word_found
  else:
    if last_digit_position > last_word_position:
      return number_found
    else:
      return word_found
  

for line in file:
  print(line)
  firstDigit = findFirstNumber(line)
  lastDigit = findLastNumber(line)

  print("First: ", firstDigit, "\tLast: ", lastDigit)

  if firstDigit is not None and lastDigit is not None:
    totalValue += (firstDigit*10) + lastDigit

print(totalValue)