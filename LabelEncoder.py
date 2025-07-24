    from sklearn.preprocessing import LabelEncoder
    import pandas as pd
      data = {'Category': ['Red', 'Green', 'Blue', 'Red', 'Green']}
      df = pd.DataFrame(data)
      le = LabelEncoder()
      df['Category_Encoded'] = le.fit_transform(df['Category'])
    print(df)