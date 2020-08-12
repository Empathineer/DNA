# course: CS50
# problem set: 6
# date: 08/07/2020
# username: Empathineer
# name: Carissa Chan
# description: identifies a person based on their DNA


"""
This program determines a match through the following process:
1) open the csv file containing the DNA sequence and read contents
  into memory.
2) For each STR, compute longest run of consecutive repeates in
  sequence
3) Compare STR against each row of the csv file to find a match.
4) Print the match if there is a perfect match. Otherwise,
  print "No match."

CSV format Ex.

name   |AGATC  |AATG   |TATC   |
-------|-------|-------|-------|
Alice     2       8       3
Bob,      4       1       5
Charlie   3       2       5

"""

import pandas as pd
import numpy as np
from collections import defaultdict
import csv
import re
from sys import argv, exit


def reset_cnt():
    counter = 1


# Validate command-line arguments.
if len(argv) != 3:
    print(f"Error there should be 2 argv, you have {argv}")
    exit(1)


database = pd.read_csv(argv[1])
# database = database.drop(['name'], axis = 1) #remove name column
data_str_list = list(database)  # STR's to be searched
num_strs = len(data_str_list)

sequence = pd.read_csv(argv[2])
seq_list = list(sequence)[0]  # sequence to be searched as list

# initialize dictionary to store STR max counts
dict_str_max = {i: 0 for i in data_str_list}

# print("\nDatabase Entries:\n{}\n".format(database))
# print("{} STR's in Database:\n{}\n".format(num_strs, data_str_list))
# print("Sequence:\n{}\n".format(seq_list))

# print STR max count dictionary
# for pair in dict_str_max.items():
#     print(pair)

str_max_cnts = []  # array to store max counts from search


# for each STR in the database, search the sequence
for rp in range(num_strs):

  target = data_str_list[rp]
  # print("\nTarget: {} is {} bases long".format(target, len(target)))

  # check for any occurence of the STR in sequnce
  if (seq_list.find(target) > -1):

      # find all occurrences of the substring and break if none found
      matches = re.finditer(target, seq_list)
      match_positions = [match.start() for match in matches]
      # print("\nMatched positions:\n", match_positions)

      # create an array of the same size as the sequence to
      # store the counters for the matched positions
      match_cnt_arr = [1] * len(match_positions)

      if (len(match_positions) == 1):
        dict_str_max[target] = 1

      else:

        counter = 1

        for idx, match in enumerate(match_positions[1:], 1):
            # print("Index: {}, Match Position: {}".format(idx, match)) #DEBUGGING

            #counts as consecutive if the matched positions are the target STR length apart
            if (match - match_positions[idx - 1] == len(target)):
              match_cnt_arr[idx] = counter + 1
              counter = counter + 1
            else:
              # reset_cnt()
              counter = 1
              # reset_cnt()


      # print("Match Count Array: \n {}".format(match_cnt_arr))

      str_max_cnts.append(max(match_cnt_arr))

# display final max consecutive counts for each STR searched
# print("\nFinal Search Max Counts:\n{}\n ".format(str_max_cnts))


# print("\nMatching Values in Database...\n")
# row1 = database.iloc[10] #TESTER
# suspect = list(row1)

# print("Entry:{}\n".format(suspect))

not_found = True

# iterate through database by name to find a match against str_max_cnts
for i in range(len(database)):

  row = list(database.iloc[i][1:])

  # print("{} : {}.".format(database.iloc[i, 0], row))

  if (str_max_cnts == row):
      # print("\nCULPRIT FOUND: ", database.iloc[i, 0])
      print(database.iloc[i, 0])
      not_found = False
      break

  # else:
  #     print("SUSPECT IS NOT HERE!")

# print('NO MATCH' if not_found == True)

print((' ', 'No Match')[not_found])

