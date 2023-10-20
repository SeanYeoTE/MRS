import csv
import random
import os

data1=[]
# Open the CSV file
filename = os.path.join(os.path.dirname(__file__),'data.csv')
with open(filename) as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    # Read each row and print its contents
    for row in reader:
        data1+=[row]

#a bunch of getter functions for easier access
def get_title(data):
    return data[0]

def get_yearofrelease(data):
    return data[1]

def get_runtime(data):
    return data[2]

def get_genre(data):
    return data[3]

def get_subgenre(data):
    return data[4]

def get_mainactor(data):
    return data[5]

def get_score(data):
    return data[6]

def get_rating(data):
    return data[7]

 
#print(get_genre(data1[5]))
#print(get_genre(data1[50]))

class BagOfWords:
    def __init__(self):
        self.vocab = {}
        self.docs = []

    def add_doc(self, data):
        # split str by , into individual words
        words = data.lower().split(',')
        # add words to vocabulary
        for word in words:
            if word not in self.vocab:
                self.vocab[word] = len(self.vocab)
                #print(self.vocab)
        # add document to document list
        self.docs.append(words)

    def get_vectors(self, doc):
        # init doc vector for indiv data
        doc_vector = [0] * len(self.vocab)
        # split data to 
        words = doc.lower().split()
        # count occurrences of each word in document
        for word in words:
            if word in self.vocab:
                doc_vector[self.vocab[word]] += 1
        return doc_vector

    def get_matrix(self):
        # init matrix
        matrix = []
        # loop over all documents
        for doc in self.docs:
            # get indiv document vectors
            doc_vector = self.get_vectors(' '.join(doc))
            # add to matrix
            matrix.append(doc_vector)
        return matrix
    


genre_process1=[]
for i in data1:
    genre_process1.append(get_genre(i))
bow=BagOfWords()

for i in genre_process1:
    bow.add_doc(i)
    bow.get_vectors(i)

print(bow.get_matrix())

def cosine_similarity(a, b):
    dot_product = 0
    norm_a = 0
    norm_b = 0
    for i in range(len(a)):
        dot_product += a[i] * b[i]
        norm_a += a[i] ** 2
        norm_b += b[i] ** 2
    norm_a = norm_a ** 0.5
    norm_b = norm_b ** 0.5
    return dot_product / (norm_a * norm_b)

#print(bow.get_matrix()[2])
#print(bow.get_matrix()[50])
#similarity = cosine_similarity(bow.get_matrix()[2], bow.get_matrix()[50])
#print(similarity)
#print(bow.docs)


def convert(x):
    uservec= [0] * len(bow.vocab)
    #converting user input into vector
    indivgenre= x.lower().split(',')
    for i in indivgenre:
        uservec[bow.vocab[i]] = 1
    return uservec

        
def testing(x):
    total= len(bow.get_matrix())
    a,b=0,0
    for i in range(x):
        a = random.randint(0,total-1)
        b = random.randint(0,total-1)
        similarity = cosine_similarity(bow.get_matrix()[a],bow.get_matrix()[b])
        print(similarity)


#print(user_input('drama,biography'))

def sort_sim(simvalue, movie_index):
    #bubble sort in order of similarity values
    for i in range(len(simvalue)-1):
        for y in range(len(simvalue)-i-1):
            if simvalue[y]<simvalue[y+1]:
                simvalue[y], simvalue[y+1] = simvalue[y+1], simvalue[y]
                movie_index[y], movie_index[y+1] = movie_index[y+1], movie_index[y]       
    return simvalue, movie_index


def main_reco(user_genre):
    # vectorizing user input
    user= convert(user_genre)
    recommend = []
    movie_index=[]
    # find similar movies
    for i in range(0,len(bow.get_matrix())-1):
        #print("user", user)
        #print("i   ",i)
        #print("mat",bow.get_matrix()[i])
        check = cosine_similarity(user,bow.get_matrix()[i])
        #print(check)
        if check >=0.5:
            #print("success",i)
            recommend.append(check)
            movie_index.append(i)
    return sort_sim(recommend,movie_index)


        

#print(main_reco('drama'))
#print(main_reco('drama,action,mystery'))
#print(main_reco('drama,action,comedy'))