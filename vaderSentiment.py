from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# Sample text data
data = {'text': ["I love this product, it's amazing!", 
                 "This is a terrible experience.", 
                 "It's okay, not great but not bad either."]}
df = pd.DataFrame(data)

analyzer = SentimentIntensityAnalyzer()

# Function to get VADER scores
def get_vader_scores(text):
    return analyzer.polarity_scores(text)

# Apply the function to your text column
df['vader_scores'] = df['text'].apply(get_vader_scores)

# Expand the dictionary of scores into separate columns
df[['compound', 'neg', 'neu', 'pos']] = df['vader_scores'].apply(pd.Series)

print(df)