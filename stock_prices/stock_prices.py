#!/usr/bin/python

import argparse

def find_max_profit(prices):
  for i in range(0, len(prices) -1):
    cur_index = i 
    max_profit = cur_index
    min_profit = cur_index
    for el in range(cur_index, len(prices)):
      if el == 0:
        max_profit = el + 1
      elif prices[el] > prices[max_profit]:  
            max_profit = el
    for el in range(cur_index, len(prices[0:max_profit])):
      if prices[el] < prices[min_profit]:
        min_profit = el
    print(f'current max is:{prices[max_profit]} and current min is: {prices[min_profit]}')
    return prices[max_profit] - prices[min_profit]
  

    
    



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))