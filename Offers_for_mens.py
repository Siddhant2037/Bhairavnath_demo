import streamlit as st
from streamlit_lottie import st_lottie
import json
st.sidebar.markdown("Site created by Siddhant....")
# Load Lottie animations
def load_lottie_json(path: str):
    with open(path, "r") as f:
        return json.load(f)

# Layout and Lottie animations
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
        button1=st.button("Click to get all latest offers related to jeans")

    with col2:
        st_lottie(animation_2, height=200, key="animation2")
        button2 = st.button("Click to get all latest offers related to Hoodies")

    with col3:
        st_lottie(animation_3, height=200, key="animation3")
        button3= st.button("Click to get all latest offers related to Shirts")


    if button1:
        video_file = open('WhatsApp Video 2024-09-14 at 21.47.02_06f81cbd.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    if button2:
        video_file1 = open('WhatsApp Video 2024-09-14 at 22.51.51_16df28e3.mp4', 'rb')
        video_bytes1 = video_file1.read()
        st.video(video_bytes1)




def main2():

    # Load your JSON animations
    animation_4 = load_lottie_json("Animation - 1726314484672.json")
    animation_5 = load_lottie_json("Animation - 1726314461844.json")
    animation_6 = load_lottie_json("Animation - 1726314484672 (1).json")

    # Arrange animations using Streamlit columns
    col4, col5, col6 = st.columns(3)

    with col4:
        st_lottie(animation_4, height=200,key="animation4")
        button=st.button("Click to get all latest offers related to Undergarments")
        if button:
             st.image("1629362802-Neeraj Chopra.jpg")


    with col5:
        st_lottie(animation_5, height=200, key="animation5")
        button1 = st.button("Click to get all latest offers related to Sando")
        if button1:
            st.image("1629362802-Neeraj Chopra.jpg")

    #with col6:
        #button2 = st.button("Click to get all latest offers related to Sirts")
        #if button2:
         #   st.image("1629362802-Neeraj Chopra.jpg")


if __name__ == "__main__":
    main()
    main2()

# if button:
#     st.image("1629362802-Neeraj Chopra.jpg")