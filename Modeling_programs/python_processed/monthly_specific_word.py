import nltk
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime

#product_name = "microwave"
#product_name = "pacifier"
product_name = "hair_dryer"
file_name = product_name + ".tsv"

df = pd.read_csv(file_name, sep="\t")
scope_list = list(range(0,len(df.review_body),2))   ## use half data
#scope_list = list(range(0,len(df)))                ## use all data
body = df.review_body[scope_list]

print(product_name.title() + " monthly average rating stars whose review words contain specific word 'good'/'bad' (every 2 count 1)\n")

monthly_total_stars = [0, 0]             # monthly number of rating stars that have word 'good'/'bad'
monthly_day_no = [0, 0]                  # monthly number of reviews that have word 'good'/'bad'
monthly_star_list = [[], []]                   
monthly_date_list = []
date_0 = datetime.strptime(df.review_date[0],'%m/%d/%Y')
for i in scope_list:
    if not pd.isna(body[i]):
        good  = [w for w in nltk.word_tokenize(body[i]) if w.lower() == 'good']
        bad   = [w for w in nltk.word_tokenize(body[i]) if w.lower() == 'bad']
      
    date = datetime.strptime(df.review_date[i],'%m/%d/%Y')
    if date.month == date_0.month and date.year == date_0.year:
        if good:
            monthly_total_stars[0] += df.star_rating[i]
            monthly_day_no[0] += 1
        if bad:
            monthly_total_stars[1] += df.star_rating[i]
            monthly_day_no[1] += 1
    else:
        for k in range(2):
            if monthly_day_no[k]:
                monthly_star_list[k].append(monthly_total_stars[k]/monthly_day_no[k])
            else:
                monthly_star_list[k].append(0)           
        monthly_date_list.append(datetime(date_0.year, date_0.month, 15))
        monthly_total_stars = [0, 0]
        monthly_day_no = [0, 0]

    date_0 = date

plt.plot(monthly_date_list, monthly_star_list[0], label = "'good'")
plt.plot(monthly_date_list, monthly_star_list[1], label = "'bad'")
plt.title(product_name.title() + " reviews that contain specific word 'good'/'bad'")
plt.legend()
plt.xlabel('Year, Month (y, m)')
plt.ylabel('Monthly Average Star(s)')
plt.show()

        

