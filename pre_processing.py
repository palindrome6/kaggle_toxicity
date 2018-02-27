import pandas as pd
import nltk
from nltk.corpus import stopwords

df = pd.read_csv('data/train.csv')

try:
    stop = stopwords.words('english')
except LookupError:
    nltk.download('stopwords')
    stop = stopwords.words('english')

df['comment_text_without_stopwords'] = df['comment_text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
print(df.head(5))
