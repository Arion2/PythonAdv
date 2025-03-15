import streamlit as st
import pandas as pd
import plotly.express as px

books_df = pd.read_csv('bestsellers_books_amazon.csv')
st.title("BestSelling books analysis")
st.write("This app analyzes the Amazon top selling books from 2009 to 2022")

st.subheader("Summary Statistics")
total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
average_rating = books_df['user rating'].mean()
average_price = books_df['Price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total books", total_books)
col2.metric("Unique titles", unique_titles)
col3.metric("Average rating", average_rating)
col4.metric("Average prices", average_price)