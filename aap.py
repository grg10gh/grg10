import requests
import streamlit as st
from streamlit_lottie import st_lottie



st.set_page_config(page_title="manishggrg", page_icon=":🤙:", layout="wide")

def load_lottieur1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieur1("https://lottie.host/bf8cec61-6595-4553-91bb-9816c4bfc12e/xDKUlWw2be.json")


with st.container():

    st.header("Hi! I am Manish :wave:")
    st.subheader("Welcome to my webpage! I hope you like my creation.")
    st.write("""I love programming and I find it very interesting!! """)

    st.write("[Do follow me on my social media :camera:](https://www.instagram.com/manishggrg/#)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Thank you for visiting my web page!!")
        st.write(
            " I will try to improve my programming skills day by day"
        )

        with right_column:
            st_lottie(lottie_coding, height = 300, key="coding")

        with st.container():
            st.write("""The web page will be updated once every week.
                     So, stay tuned!!""")
            
