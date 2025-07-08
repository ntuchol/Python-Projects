 import nltk
    from nltk.corpus import brown

    nltk.download('brown')
    news_categories = brown.categories(categories='news')
    news_files = brown.fileids(categories=news_categories)
    news_text = [brown.words(fileid) for fileid in news_files]