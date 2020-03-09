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

print(product_name.title() + " rating stars distribution by specific word ('great'/'bad') statistics (every 2 count 1)\n")

# two list for storing star numbers for 'great', 'bad'
star_list = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]    
for i in scope_list:
    if not pd.isna(body[i]):
        great = [w for w in nltk.word_tokenize(body[i]) if w.lower() == 'great']
        bad   = [w for w in nltk.word_tokenize(body[i]) if w.lower() == 'bad']      

    if great:
        for j in range(5):
            if df.star_rating[i] == j+1:
                star_list[0][j] += 1
                break            
    if bad:
        for j in range(5):
            if df.star_rating[i] == j+1:
                star_list[1][j] += 1
                break



## borrowed from <matplotlib.org>
labels = ['1 star', '2 stars', '3 stars', '4 stars', '5 stars']

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, star_list[0], width, label="'great'")
rects2 = ax.bar(x + width/2, star_list[1], width, label="'bad'")

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Review Count')
ax.set_title(product_name.title() + " rating stars distribution by specific word ('great'/'bad')")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()

        

