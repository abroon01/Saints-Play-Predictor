import streamlit as st
import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.ensemble import GradientBoostingClassifier


def yardLineCalc(yard, fieldPosition) : 
    if fieldPosition == "Saints":
        return yard
    else : 
       position = yard + (2*(50-yard))
       return position

def inputs() : 

    st.write("""
    # New Orlean Saints Play Predictor App
    """)


    down = st.selectbox(label = "Down", options = [1,2,3])
    toGo = st.number_input(label = "Yards to Go", min_value=1, max_value = 99, value = 10)
    fieldPosition = st.selectbox(label = "Side of the Field", options = ["Saints", "Opponents"])
    yardLine = st.number_input(label = "Yard Line", min_value = 1, max_value=99, value = 20)
    yard = yardLineCalc(yardLine, fieldPosition)
    

    quarter = st.selectbox(label = "Quarter", options = [1,2,3,4])
    minute = st.number_input(label = "Minutes Remaining", min_value=0, max_value=15, value = 15)
    second = st.number_input(label = "Seconds Remaining", min_value=0, max_value=59, value = 59)

    data = {'Quarter': quarter,
            'Minute': minute,
            'Second': second,
            'Down': down,
            'ToGo': toGo,
            'YardLine': yard}
    userInputs = pd.DataFrame(data, index = [0])
    return userInputs


df = inputs()


def model() :
    saintsDF = pd.read_csv("saints.csv")
    train = saintsDF.sample(frac=0.8, random_state = 24)
    test = saintsDF.drop(train.index)
    x_train = train[["Quarter", "Minute","Second", "Down", "ToGo", "YardLine"]]
    y_train = train[["PlayType"]]

    gbc = GradientBoostingClassifier()
    gbc.fit(x_train, y_train)
    return gbc

gbc = model()


def predictions(model, df) :
  if st.button("Predict") : 
    result = model.predict(df)
    if result[0] == "PASS" :
        prediction = "pass the ball"
    else :
        prediction = "run the ball"


    st.write("The Saints are predicted to " + prediction)

predictions(gbc, df)
        


    

