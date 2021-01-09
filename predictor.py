
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

down = int(input("down: "))
togo = int(input('togo: '))
yardline = int(input('yardline: '))
playtype = input('pass or rush: ')

if playtype == "pass":
    play = 0
elif playtype == "rush":
    play = 1

new_input = [[down, togo, yardline, int(play)]]

successful = classifier.predict(new_input)

if successful == "yes":
    print("your play was successful")
elif successful == "no":
    print("your play was not successful")
