import data_processing
import ui_testing
import csv
import random

x = True
while x == True:
    print("Type 'quit' if you want to exit the program\n")
    user_input = input("Please type the genre(s) you want to watch\nExample: action,drama,comedy\n")
    if user_input == 'quit':
        x = False
    else:
        print('')
        print('Here are some recommendations assorted by their rating',"COMMENT")
        print('')
        ui_testing.titles(data_processing.main_reco(user_input))
        print('')
        user_input2 = input("Select a movie to see more information ")
        print('')
        ui_testing.get_info(data_processing.main_reco(user_input),int(user_input2))
