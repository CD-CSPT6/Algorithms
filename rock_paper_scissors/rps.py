#!/usr/bin/python

import sys


def rock_paper_scissors(n):
  final_arr = []
  string_list = ['rock', 'paper', 'scissors']
  def roshambo(n, arr=[]):
    if n == 0:
      return final_arr.append(arr)
    for words in string_list:
      rolshambo(n - 1, arr + [words])
  roshambo(n)
  return final_arr



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')