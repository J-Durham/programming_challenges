# https://edabit.com/challenge/WXqH9qvvGkmx4dMvp

def fizzbuzz(num):
    retval = ""
    if((num % 3) == 0): retval += "Fizz"
    if((num % 5) == 0): retval += "Buzz"
    if(retval == ""): retval = str(num)
    return retval

def main():
    in_num = input("Enter a number: ")
    print(fizzbuzz(int(in_num)))

if __name__ == "__main__":
    main()