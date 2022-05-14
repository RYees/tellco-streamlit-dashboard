import streamlit as st
import pandas as pd
from multiapp import MultiApp
from pages import User_Overview_Analysis, User_Engagement_Analysis, User_Experience_Analysis , User_Satisfaction_Analysis, Model_Implementation
# import numpy as np
# import plotly.express as px

st.header("Analysis for Telecommunication Industry")

# st.write(df)

# st.set_page_config(page_title="TellCo Telecom Analytics", layout="wide")

app = MultiApp()

PAGES = {
    "User Overview Analysis": User_Overview_Analysis,
    "User Engagement Analysis": User_Engagement_Analysis,
    "User Experience Analysis": User_Experience_Analysis,
    "User Satisfaction Analysis": User_Satisfaction_Analysis,
    "Predict Satisfaction": Model_Implementation
}

st.sidebar.markdown("""
# TellCo's User Analytics
### Explore
""")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

# Add all your application here
# app.add_app("User Overview Analysis", User_Overview_Analysis.app)
# app.add_app("User Engagement Analysis", User_Engagement_Analysis.app)
# app.add_app("User Experience Analysis", User_Experience_Analysis.app)
# app.add_app("User Satisfaction Analysis", User_Satisfaction_Analysis.app)
# app.add_app("Predict Satisfaction", Model_Implementation.app)

# # The main app
# app.run()