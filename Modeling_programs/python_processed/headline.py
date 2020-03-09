import nltk
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

product_name = "microwave"
#product_name = "pacifier"
#product_name = "hair_dryer"
file_name = product_name + ".tsv"

df = pd.read_csv(file_name, sep="\t")
scope_list = list(range(0,len(df.review_headline),2))
headline = df.review_headline[scope_list]

print(product_name.title() + ' review headline words statistics (every 2 count 1)\n')

all_words = []
dump = [',','.','...','!','$','?','(',')',"'",'"',';',':','/','<','br','>',
      '+','&','#','@','-','=','~','`','*','%','^','{','}','[',']','|','\\']
dump_words = ['the','it','a','and','is','of','for','to','on','in','or','i']
dump += dump_words
print('Dumped words in list dump\n',dump,'\n\n')

for i in scope_list:
    all_words += [w.lower() for w in nltk.word_tokenize(headline[i]) if w.lower() not in dump]

#sorted_words = sorted(all_words,key=all_words.count,reverse=True)

freq_words = nltk.FreqDist(all_words)
freq_words_50 = freq_words.most_common(50)
print('Top 50 frequent words (excepting words in dump)\n',freq_words_50,'\n\n')
plt.figure(1)
plt.title('Top 20 frequent words in ' + product_name + ' review headlines')
freq_words.plot(20, cumulative=False)   # close the plot window to continue execution

# use tag to find only adj
tagged_words = nltk.pos_tag(all_words)
adj_words = [word for (word, tag) in tagged_words if tag == 'JJ']
freq_adj = nltk.FreqDist(adj_words)
freq_adj_50 = freq_adj.most_common(50)
print('Top 50 frequent adjectives (excepting words in dump)\n',freq_adj_50)
plt.figure(2)
plt.title('Top 20 frequent adjectives in ' + product_name + ' review headlines')
freq_adj.plot(20, cumulative=False)

