import streamlit as st
from streamlit_lottie import st_lottie
import json
st.sidebar.markdown("Site created by Siddhant....")
# Load Lottie animations
def app():

    def load_lottie_json(path: str):
        with open(path, "r") as f:
            return json.load(f)


    def main():
        st.title("Select one ot the following catogrires")

        # Load your JSON animations
        animation_1 = load_lottie_json("Animation - 1726314383121.json")
        animation_2 = load_lottie_json("Animation - 1726314407127.json")
        animation_3 = load_lottie_json("Animation - 1726314282958.json")

        # Arrange animations using Streamlit columns
        col1, col2, col3 = st.columns(3)

        with col1:
            st_lottie(animation_1, height=200,key="animation1")
            button=st.button("Click to get all latest offers related to jeans")
            if button:
                st.video

        with col2:
            st_lottie(animation_2, height=200, key="animation2")
            button = st.button("Click to get all latest offers related to Hoodies")
            if button:
                st.image("1629362802-Neeraj Chopra.jpg")

        with col3:
            st_lottie(animation_3, height=200, key="animation3")
            button = st.button("Click to get all latest offers related to Shirts")
            if button:
                st.image("1629362802-Neeraj Chopra.jpg")
