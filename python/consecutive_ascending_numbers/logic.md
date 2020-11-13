# logic
- make 5 functions
  - one of them gets all clean divisors to get grouping numbers
    - if number is 9 digits long, get 1, 3
    - if number is 8 long, get 1, 2, 4
    - input: the number to check
    - output: the array of clean divisors
      - if array length is 0, no clean divisors
  - one takes in the array of clean divisors
    - calls the function that groups by divisor number and acts as handler for that
  - one that groups by divisor number and checks for ascending
    - input: array of clean divisors, number to check
    - output: bool of if ascending or not
  - one that groups by divisor number to check for descending
    - same as before but descending
  - one that will return an array of the split numbers

# prototype shit
  - `divisor_check(in_num)`                 1
  - `validation_handler(in_num)`            5
  - `ascention_check(split_list)`           3
  - `descention_check(split_list)`          4
  - `grouping_handler(in_num, divisor)`     2

