import data_processing
#print(data_processing.main_reco('romance'))
import csv
import os

data1=[]
filename = os.path.join(os.path.dirname(__file__),'data.csv')
# Open the CSV file
with open(filename) as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    # Read each row and print its contents
    for row in reader:
        data1+=[row]


def titles(data):
    for i in range(len(data[1])):
        if i > 10:
            pass
        else:
            print(str(i) + ' ' + data_processing.get_title(data1[data[1][i]]))
#titles(data_processing.main_reco('drama,action,comedy'))


def release(data):
    for i in range(len(data[1])):
        print(data_processing.get_yearofrelease(data1[data[1][i]]))
#release(data_processing.main_reco('drama,action,comedy'))

def genre(data):
    for i in range(len(data[1])):
        print(data_processing.get_genre(data1[data[1][i]]))
#genre(data_processing.main_reco('drama,action,comedy'))

def sub_genre(data):
    for i in range(len(data[1])):
        print(data_processing.get_subgenre(data1[data[1][i]]))
#sub_genre(data_processing.main_reco('drama,action,comedy'))

def actor(data):
    for i in range(len(data[1])):
        print(data_processing.get_mainactor(data1[data[1][i]]))
#actor(data_processing.main_reco('drama,action,comedy'))

def score(data):
    for i in range(len(data[1])):
        print(data_processing.get_score(data1[data[1][i]]))
#score(data_processing.main_reco('drama,action,comedy'))

def rating(data):
    for i in range(len(data[1])):
        print(data_processing.get_rating(data1[data[1][i]]))
#rating(data_processing.main_reco('drama,action,comedy'))

def get_info(data,index):
    print('Name: ' + data_processing.get_title(data1[data[1][index]]))
    print('Year of Release: ' + data_processing.get_yearofrelease(data1[data[1][index]]))
    print('Main Genre: ' + data_processing.get_genre(data1[data[1][index]]))
    print('Subgenres: ' + data_processing.get_subgenre(data1[data[1][index]]))
    print('Main actor: ' + data_processing.get_mainactor(data1[data[1][index]]))
    print('Score: ' + data_processing.get_score(data1[data[1][index]]))
    print('Rating: ' + data_processing.get_rating(data1[data[1][index]]))
    print('')

#get_info(data_processing.main_reco('drama,action,comedy'),0)
