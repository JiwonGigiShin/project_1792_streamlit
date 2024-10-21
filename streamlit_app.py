import streamlit as st
import pandas as pd
import plotly.express as px
#requirements.txt



st.title("Hello Jayan, Anuprita, Omar!")
st.markdown("this is streamlit website for le wagon")


df = pd.read_csv('moderation (1).csv')
df.drop(columns=['node_id'], inplace=True)



st.dataframe(df.head())




px.histogram(df, x='email', color='email')
