import streamlit as st

def main():
    st.title('Hello World!')

if __name__ == '__main__':
    main()


if st.button("Click me"):
    st.write("Button Clicked")

st.checkbox("Check me!")

if st.checkbox("Check me to show some text"):
    st.write("You are seeing this text because you checked the button!!!! :) ")

user_input = st.text_input("Enter text", "Shenoni nje text")
st.write("You entered:", user_input)

age = st.number_input("Enter you age", min_value=1, max_value=100)
st.write(f"Your age: {age}")

message = st.text_area("Enter a message")
st.write(f"Your message: {message}")

choice = st.radio("Pick one", ['Choice 1','Choice 2','Choice 3'])
st.write(f"You chose: {choice}")

if st.button("Success"):
    st.success("It was sent successfully")

try:
    1 / 0
except Exception as e:
    st.exception(e)