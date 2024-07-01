import cv2
import streamlit as st
from yolov10.utils import load_model, detect_helmet
from PIL import Image


# Load the model
model = load_model('app/yolov10/weights/best.pt')

st.title("Helmet Detection with YOLOv10")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Detecting...")

    result = detect_helmet(model, image)
    result = cv2.cvtColor(result.plot(), cv2.COLOR_BGR2RGB)
    st.image(result, caption='Processed Image.', use_column_width=True)
