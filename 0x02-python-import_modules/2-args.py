#!/usr/bin/python3

import sys

def print_arguments():
  """Prints the number of arguments and the list of arguments."""

  num_args = len(sys.argv) - 1  # Exclude the script name

  if num_args == 0:
    print("Number of argument(s): 0.")
  else:
    print(f"Number of argument(s): {num_args}")
    if num_args == 1:
      print("argument:")
    else:
      print("arguments:")

    for i, arg in enumerate(sys.argv[1:]):
      print(f"{i+1}: {arg}")

if __name__ == "__main__":
  print_arguments()
