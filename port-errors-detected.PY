from pprint import pprint
import re
from termcolor import colored
import sys

with open("ts-Nokia.show") as f:
    data_to_parse = f.readlines()

i = 0 # This counter is needed because we need to catch the line after where 'port error' errors captured. 
port error_counter = False # To inform user if there is any port error Errors in the TS or not. 

for line in data_to_parse:
    i = i + 1
    if "port" in line:
        port error_counter = True
        #print(f"{line} {data_to_parse[i]}")
        #print(data_to_parse[i])
        with open("port errors.txt", "a") as f:
            f.write(f"{line} {data_to_parse[i]} {data_to_parse[i-2]}")

if port error_counter == False:
    print(colored("\nThere is no port errors observed in this node.", "green"))
elif port error_counter == True:
    print(colored("\nThere are port errors observed in this node. Please check attached 'port error_errors.txt' file.", "red"))
