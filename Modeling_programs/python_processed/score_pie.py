import nltk
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

product_name = "microwave"
#product_name = "pacifier"
#product_name = "hair_dryer"
file_name = product_name + ".tsv"

df = pd.read_csv(file_name, sep="\t")
scope_list = list(range(0,len(df.review_body),2))   ## use half data
#scope_list = list(range(0,len(df)))                ## use all data
body = df.review_body[scope_list]
score_list = []

grade_words = ['great','happy','perfect','old','bad']

def word_to_grade(word):
    switcher = {        
        'great' :3 ,
        'perfect':3,
        'happy':2,
        'old':-1,
        'bad':-2
    }
    return switcher.get(word, 0)

print(product_name.title() + ' cumstomer scores statistics (every 2 count 1)\n')

def clac_star_score(i):
    if df.total_votes[i] <= 5:
        votes = df.total_votes[i]               
    elif df.total_votes[i] <= 50:
        votes = 5 + 0.1 * (df.total_votes[i] - 5)
    else:
        votes = 5 + 0.1 * 45 + 0.01 * (df.total_votes[i] - 50)
        
    votes -= 1.0*(df.total_votes[i]-df.helpful_votes[i])
    if votes < 0:
        votes = 0

    score = 0.1 * df.star_rating[i] * votes 
    return score

             
for i in scope_list:
    score = clac_star_score(i)
    #score = 0
    if not pd.isna(body[i]):
        tokens = [w.lower() for w in nltk.word_tokenize(body[i]) if w.lower() in grade_words]
    
    review_score = 0
    if tokens:
        for w in tokens:
            review_score += word_to_grade(w)
        if review_score < 0:
            review_score = 0            
        review_score /= len(tokens)

    score += review_score
    score_list.append(score)
    

max_score = max(score_list)
print(product_name.title() + ' maximum score is: ',max_score)

partition = np.linspace(0,max_score,6)
partition_no = [0, 0, 0, 0, 0]

for i in range(5):
    for score in score_list:
        if partition[i] <= score and score < partition[i+1]:
            partition_no[i] += 1
            score_list.remove(score)


# plot pie chart
intervals = ['0~1/5', '1/5~2/5', '2/5~3/5', '3/5~4/5', '4/5~1'] # labels 
colors = ['r', 'y', 'g', 'b', 'c']  # color for each label
plt.pie(partition_no, labels = intervals, colors=colors, autopct = '%1.1f%%')

plt.title(product_name.title() + ' maximum score %f' %max_score)
plt.legend() 
plt.show()


