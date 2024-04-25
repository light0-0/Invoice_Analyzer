from dotenv import load_dotenv

load_dotenv()

import streamlit as s
import os
from PIL import Image
import google.generativeai as gen

gen.configure(api_key=os.getenv("key"))

def get_gemeni_resposne(input,image,prompt):
    model = gen.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input],image[0],prompt)
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]   
        return image_parts
    else:
        raise FileNotFoundError("No file Uploaded")

s.set_page_config(page_title="Invoice App")

s.header("Invoice Reader")
input=s.text_input("Ask Questions: ",key="input")
uploaded_file = s.file_uploader("Choose an Image...",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    s.image(image,caption="Image Uploaded.",use_column_width=True)

submit = s.button("Find Answer")

prompt = """
You are an expert in understaing invoices.You will 
receive input images as invoices and you will have to 
answer question based on the input image.
"""

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemeni_resposne(prompt,image_data,input)

    s.subheader("Your Answer is ")
    s.write(response)