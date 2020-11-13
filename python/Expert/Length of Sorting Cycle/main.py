# https://edabit.com/challenge/K9MuSPs9W4zCJq6EM
import sys


def cycle_length(num_list, sorted_list, change_index, itera):
  if num_list[change_index] == sorted_list[change_index]:
    return itera
  mod_list = num_list
  passed_val = mod_list[change_index]
  bitch_index = sorted_list.index(passed_val)
  bitch_val = mod_list[bitch_index]
  mod_list[bitch_index] = passed_val
  mod_list[change_index] = bitch_val
  return cycle_length(mod_list, sorted_list, change_index, itera + 1)


def main():
  in_list = []
  while 1:
    in_num = input("Enter an int to be added to the list, enter q to stop: ")
    if in_num == "q":
      break
    try:
      in_list.append(int(in_num))
    except ValueError:
      print("Enter integers only")
  if len(in_list) == 0:
    sys.exit("Enter some values")
  change_val = int(input("Enter the value of the number to change: "))
  try:
    in_list.index(change_val)
  except ValueError:
    sys.exit("Entered value doesn't exist in list")
  print(in_list)
  print(cycle_length(in_list, sorted(in_list), in_list.index(change_val), 0))


if __name__ == "__main__":
  main()
