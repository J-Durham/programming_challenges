# https://edabit.com/challenge/LMoP4Jhpm9kx4WQ3a
import sys


def input_validator(in_num):
  try:
    good_num = int(in_num)
    return(good_num)
  except ValueError:
    return(False)


def validation_handler(valid_num):
  # just call other functions as needed, and handle outputs with toggles
  divisor_list = divisor_check(valid_num)
  ascension_toggle = False
  working_divisor = 0
  working_split = []
  for divisor in divisor_list:
    split_numbers = grouping_handler(valid_num, divisor)
    if ascension_check(split_numbers):
      ascension_toggle = True
      working_divisor = divisor
      working_split = split_numbers
      break
  if ascension_toggle:
    good_out = "If grouped into " + str(working_divisor)
    good_out += "'s : " + str(working_split)
    print("Contains a set of consecutive ascending numbers")
    print(good_out)
    sys.exit()
  descension_toggle = False
  for divisor in divisor_list:
    split_numbers = grouping_handler(valid_num, divisor)
    if descension_check(split_numbers):
      descension_toggle = True
      working_divisor = divisor
      working_split = split_numbers
      break
  if descension_toggle:
    good_out = "If grouped into " + str(working_divisor)
    good_out += "'s : " + str(working_split)
    print("Contains a set of consecutive descending numbers")
    print(good_out)
    sys.exit()
  print("Regardless of the grouping size, the numbers can't be consecutive.")


def divisor_check(valid_num):
  # iterate through the length of the number to get all nums in that % 0
  num_length = len(str(valid_num))
  divisors = []
  for i in range(1, num_length):
    if ((num_length % i) == 0):
      divisors.append(i)
  return divisors


def grouping_handler(valid_num, divisor):
  # turn the number into a list, and reset the holder after getting the groups
  num_list = list(str(valid_num))
  num_length = len(str(valid_num))
  split_numbers = []
  num_holder = ""
  for i in range(0, num_length):
    num_holder += num_list[i]
    if((i + 1) % divisor) == 0:
      split_numbers.append(num_holder)
      num_holder = ""
  return split_numbers


def ascension_check(split_numbers):
  # use abs to make sure negative numbers don't fuck it up
  diff = abs(int(split_numbers[1]) - int(split_numbers[0]))
  for i in range(0, len(split_numbers) - 1):
    if ((int(split_numbers[i]) + diff) != int(split_numbers[i + 1])):
      return False
  return True


def descension_check(split_numbers):
  # use abs to make sure negative numbers don't fuck it up
  diff = abs(int(split_numbers[1]) - int(split_numbers[0]))
  for i in range(0, len(split_numbers) - 1):
    if ((int(split_numbers[i]) - diff) != int(split_numbers[i + 1])):
      return False
  return True


def main():
  in_num = input("Enter the number to test: ")
  if not (input_validator(in_num)):
    sys.exit("ERROR: entered value was not an integer")
  validation_handler(int(in_num))


if __name__ == "__main__":
    main()
