    P(Class|Features) = (P(Features|Class) * P(Class)) / P(Features)
    from sklearn.naive_bayes import GaussianNB # or MultinomialNB, BernoulliNB
    model = GaussianNB()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

