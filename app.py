import streamlit as st
from PIL import Image


st.title("HOLA! mi nombre es nicky")

st.header("Gata negra cool")
st.write("Miawww Miawwwww Miawwww")
image = Image.open('gatocool.jpg')
st.image(image, caption= 'Miawww')
