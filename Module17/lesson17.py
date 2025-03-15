import streamlit as st

"""col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="center")

with col1:
    st.header("Column 1")
    st.write("Content for column 1")

with col2:
    st.header("Column 2")
    st.write("Content for column 2")

with col3:
    st.header("Column 3")
    st.write("Content for column 3")

with col4:
    st.header("Column 4")
    st.write("Content for column 4")

with col5:
    st.header("Column 5")
    st.write("Content for column 5")"""


with st.form("my_form", clear_on_submit=True):
    name = st.text_input('Name')
    age = st.slider('Age', min_value=0, max_value=100)
    email = st.text_input('Email')
    biography = st.text_area('Short bio')
    terms = st.checkbox('I agree to the terms and conditions')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Email: {email}")
    st.write(f"Short Bio: {biography}")

    if terms:
        st.write('Your agreed to the terms and condition!')
    else:
        st.write('You did not agree to the terms and conditions!')


tab1, tab2, tab3 = st.tabs(["Tab1", "Tab2", "Tab3"])

with tab1:
    st.header('Content for tab1')
    st.write('This is content for tab 1')

with tab2:
    st.header('Content for tab2')
    st.write('This is content for tab 2')

with tab3:
    st.header('Content for tab3')
    st.write('This is content for tab 3')