import pandas as pd
import csv
from textblob import TextBlob
#Read csv file
df=pd.read_csv('toxicity_train.csv')
Y=df['comment_text'].tolist()
for x in Y:
    print(x)
    t=TextBlob(x)
    j=t.sentiment
    print(j)

