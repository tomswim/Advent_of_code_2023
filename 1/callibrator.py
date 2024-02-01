import json

def get_number(line):
  wordNumber = ''
  possibleNumber= ''
  found_first_digit = False
  for char in line:
    if char.isnumeric():
      if (found_first_digit == False):
        found_first_digit = True
        first_digit = char
        last_digit = char
      else:
        last_digit = char
      possibleNumber = ''
    else:
      possibleNumber = str(possibleNumber) + str(char)
      if possibleNumber in list(doublesJson.keys()):
        possibleNumber = doublesJson[possibleNumber]
      # print(possibleNumber)
      if possibleNumber in numberWords:
        if (found_first_digit == False):
          found_first_digit = True
          first_digit = numbersJson[possibleNumber]
          last_digit = numbersJson[possibleNumber]
        else:
          last_digit =numbersJson[possibleNumber]
        possibleNumber = ''
      if possibleNumber not in starts:
        possibleNumber = ''

  return int(first_digit+last_digit)


with open('numbers.txt', 'r') as numberFile:
  numbersData = numberFile.read()

numbersJson = json.loads(numbersData)

numberWords = list(numbersJson.keys())
print(numberWords)

with open('input.txt', 'r') as file:
  lines = file.readlines()

with open('starters.txt', 'r') as startsFile:
  starters = startsFile.readlines()

with open('doubles.txt', 'r') as doublesFile:
  doublesData = doublesFile.read()

doublesJson = json.loads(doublesData)

starts = []
for start in starters:
  start = start.replace('\n', '')
  starts.append(start)

print(starts)

# print(lines[0])
count = 0
total = 0
for line in lines:
  count += 1
  number = get_number(line)
  # if (count < 20):
  print(count, line, number)
  total += number
  
print(total)
print(count)