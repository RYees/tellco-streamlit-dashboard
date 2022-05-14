import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def app():
    st.header("model")
    # df = pd.read_csv('tellco_data.csv', index_col=0)
    # st.title('Modelling')
    # model, accuracy = train_model(df)
    # st.write('Accuracy: ' + str(accuracy))
    # st.markdown('### Make prediction')
    # st.dataframe(df)
    # row_number = st.number_input('Select row', min_value=0, max_value=len(df)-1, value=0)
    # st.markdown('#### Predicted')
    # st.text(model.predict(df.drop(['alcohol'], axis=1).loc[row_number].values.reshape(1, -1))[0])


# def train_model(df):
#     X = np.array(df.drop(['alcohol'], axis=1))
#     y= np.array(df['alcohol'])

#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#     model = RandomForestClassifier()
#     model.fit(X_train, y_train)

#     return model, model.score(X_test, y_test)
