// https://edabit.com/challenge/cPu9k4bBimoKHc9zD
#include <iostream>
#include <string>

using namespace std;

string concat(int digits, int concat_num)
{
  string cat_val = to_string(digits);
  string appendee = to_string(digits);
  for(int i = 0; i < concat_num - 1; i++)
  {
    cat_val.append(appendee);
  }
  return cat_val;
}

int superDigit(string digits)
{
  int total = 0;
  for(int k = 0; k < digits.length(); k++)
  {
    total += ((int)(digits[k]) - 48);
  }
  if(total > 9)
  {
    return superDigit(to_string(total));
  }
  return total;
}

int main()
{
  int digits;         //number to concatenate with
  int concat_num;     //number of times to concatnate

  // get user input
  cout << "Enter the number to calculate with: ";
  cin >> digits;
  cout << endl << "Enter the number of times to concatnate: ";
  cin >> concat_num;
  cout << endl;

  // do the concatnations
  string cat_num = concat(digits, concat_num);

  // start the recursive thing
  cout << "pre-recursion" << endl;
  int s_digit = superDigit(cat_num);

  // handle output
  cout << "Super digit is " << to_string(s_digit) << endl;
}