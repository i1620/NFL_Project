def predictor(a,b,c,d):
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import os
    
    data = 'finaldata.csv'
    data_df = pd.read_csv(data, encoding="ISO-8859-1")
    original_df = data_df

    data_df['Type'] = np.where(data_df['PlayType'] == "PASS", 0, 1)
    data_df = data_df.drop(columns = ['Yards','PlayType', "OffenseTeam"])

    # Assign X (data) and y (target)
    X = data_df.drop("sucess", axis=1)
    y = data_df["sucess"]

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)
    training_score = classifier.score(X_train, y_train)
    testing_score = classifier.score(X_test, y_test)

    down = int(a)
    togo = int(b)
    yardline = int(c)
    playtype = d

    if playtype == "pass":
        play = 0
    elif playtype == "rush":
        play = 1

    new_input = [[down, togo, yardline, int(play)]]

    successful = classifier.predict(new_input)

    if successful == "yes":
        success = "your play was successful"
    elif successful == "no":
        success = "your play was not successful"

    return success

# a = input('What down is it? ')
# b = input("How many yards to go? ")
# c = input("What yardline are you on? ")
# d = input("Are you going to pass or rush? ")

# test = predictor(a,b,c,d)
# print(test)
