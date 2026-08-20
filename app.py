import streamlit as st
from PIL import Image


st.title("HOLA! mi nombre es nicky")

st.header("Gata negra cool")
st.write("La gata tiene lentes")
image = Image.open('gatocool.jpg')
st.image(image, caption= 'Miawww')
