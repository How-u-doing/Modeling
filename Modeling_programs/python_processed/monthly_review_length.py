import nltk
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime

product_name = "microwave"
#product_name = "pacifier"
#product_name = "hair_dryer"
file_name = product_name + ".tsv"

df = pd.read_csv(file_name, sep="\t")
scope_list = list(range(0,len(df.review_body),2))   ## use half data
#scope_list = list(range(0,len(df)))                ## use all data
body = df.review_body[scope_list]

punc = [',','.','...','!','$','?','(',')',"'",'"',';',':','/','<','br','>',
      '+','&','#','@','-','=','~','`','*','%','^','{','}','[',']','|','\\']

print(product_name.title() + ' monthly average review length statistics (every 2 count 1)\n')

#length_list = []           # review words length of each item in scope_list
monthly_length_list = []    # monthly average review words length
monthly_date_list = []
monthly_total_length = 0
monthly_day_no = 0
date_0 = datetime.strptime(df.review_date[0],'%m/%d/%Y')
for i in scope_list:
    words_no = 0
    if not pd.isna(body[i]):
        words_no = len([w for w in nltk.word_tokenize(body[i]) if w not in punc])

    
    date = datetime.strptime(df.review_date[i],'%m/%d/%Y')
    if date.month == date_0.month and date.year == date_0.year:
        monthly_total_length += words_no
        monthly_day_no += 1
    else:
        monthly_length_list.append(monthly_total_length/monthly_day_no)
        monthly_date_list.append(datetime(date_0.year, date_0.month, 15))
        monthly_total_length = 0
        monthly_day_no = 1

    date_0 = date

plt.plot(monthly_date_list, monthly_length_list, '-b')
plt.title(product_name.title() + ' monthly average review_body words length')
plt.xlabel('Year, Month (y, m)')
plt.ylabel('Monthly Average Length (words)')
plt.show()

        

