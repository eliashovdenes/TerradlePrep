import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Elias's website!", page_icon=":shark:", layout="wide")


#Assets


def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# lottie_coding = load_lottie_url("")








with st.container():
    
    st.subheader("Skibidi bop mm dada!", anchor=False)
    st.title("Gaming is fun! :video_game:", anchor=False)
    st.write("[My proudest achievement!](https://www.youtube.com/watch?v=G1RnhpIMQFI)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec nulla ac justo aliquet ultricies. Nullam nec metus nec nisi tincidunt ultrices. Nulla facilisi.")

    with left_column:
        #show the cat gif
        url = "cat.gif"
        st.image(url, use_column_width=True, caption="A cat gif")

        hide_img_fs = '''
        <style>
        button[title="View fullscreen"]{
            visibility: hidden;}
        </style>
        '''

        st.markdown(hide_img_fs, unsafe_allow_html=True)
