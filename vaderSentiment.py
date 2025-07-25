from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

data = {'text': ["I love this product, it's amazing!", 
                 "This is a terrible experience.", 
                 "It's okay, not great but not bad either."]}
df = pd.DataFrame(data)

analyzer = SentimentIntensityAnalyzer()

def get_vader_scores(text):
    return analyzer.polarity_scores(text)

df['vader_scores'] = df['text'].apply(get_vader_scores)

df[['compound', 'neg', 'neu', 'pos']] = df['vader_scores'].apply(pd.Series)

print(df)
