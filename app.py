import datetime
import os
import errno

import streamlit as st
import pandas as pd
from matplotlib import pyplot

import plotly.figure_factory as ff
import plotly.express as px

from PIL import Image

year = datetime.datetime.now().year  # TODO : season and year may be different
month = datetime.datetime.now().month
day = datetime.datetime.now().day


st.sidebar.markdown(
    """
**How does it work ?**

A statistical regression model is fitted on historical data; Using WR data from 2012-2022 season to train the model   
It is then used to predict this season TOP WR based on previous season snapcount data.  

"""
)
st.sidebar.markdown(
    """
*Made by [CZ](https://www.linkedin.com/in/cheng-zhang-8b329012/). Thanks to [FFDP](https://www.fantasyfootballdatapros.com/), [pauldes](https://github.com/pauldes). *
"""
)

st.title("🏈 Predicting Top NFL Fantasy WR")
st.markdown(
    f"""
*Predicting top NFL Fantasy WR for the {year}-{str(year+1)[-2:]} season using machine learning.*
"""
)

df = pd.read_csv("2021result.csv", index_col=False)
st.write(df)

top_3 = df[["player_name", "predicted_fp_per_game"]][:3].values.tolist()

emojis = ["🥇", "🥈", "🥉"]

col1, col2 = st.columns(2)
col1.subheader("Predicted top 3")
col2.subheader("Prediction parameters")

for n, player_name in enumerate(top_3):
    title_level = "###" + n * "#"
    col1.markdown(
        f"""
    #### {emojis[n]} **{player_name[0]}**

    *{player_name[1]} chance to be Top Fantasy WR*
    """
    )

col2.markdown("Current Accuracy is 3.29 loss for each game")
image = Image.open('ck.png')
col2.image(image)

st.title("Predictions history")

# data
df_wide = pd.read_csv('nfl_player_line_data.csv')
df_long=pd.melt(df_wide, id_vars=['Year'], value_vars=['Cooper Kupp','Diontae Johnson','Davante Adams'])

# Plot!
fig = px.line(df_long, x='Year', y='value', color='variable')

st.plotly_chart(fig, use_container_width=True)