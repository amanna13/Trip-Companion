from dotenv import load_dotenv
import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import streamlit as st
from PIL import Image
import time 


load_dotenv()


genai.configure(api_key = os.getenv('Gemini_Api_Key'))

def detect_images(prompt, uploaded_img):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content ([prompt, uploaded_img[0]], 
                                       safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE 
        }
        )
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
        raise FileNotFoundError("No File Uploaded")

#Safety settings
    
safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]


st.title("See, Snap, Learn !")
st.header(":orange[Upload Images of Historical Places]")
uploaded_file = st.file_uploader("", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)  
        st.image(image, caption="Uploaded Image", use_column_width=True)
    except Exception as e:  
        st.error(f"Error processing image: {e}")



submit=st.button("Discover🔎", type="primary")
prompt = """You are a tour guide. You have to see images and give informative descriptions on the same. The image may be of Historical landmarks, or nature scene from all over the world. It must be
            of some educational experiences. You must provide me the architectural features of it in tabular or buleted at the begining like height 
            area constructed by. And after this you must give me a description of it.
            Explain everything like a tourist guide, how to reach this place. Also provide the timings, entry fees etc. Provide me the exact google maps direction link only. Make seperate headings for each section.
           """


if submit:
    if uploaded_file is None:
        st.error("Please upload an image before submitting.")
    else:
        image_data = input_image_setup(uploaded_file)
        with st.spinner('Just a moment...'):
            time.sleep(25)
        response = detect_images(prompt, image_data)
        
        st.subheader("Here's what we found 👀")
        st.write(response)
        st.info('Information provided may be inaccurate. Kindly double-check its responses', icon="ℹ")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

footer="""<style>
a:link , a:visited{
color: #8EA8C3;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: #7AE7C7;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
# background-color:#071013;
# color: #8EA8C3;
background: rgba(7, 16, 19, 0.24);
border-radius: 16px;
box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
backdrop-filter: blur(6.6px);
-webkit-backdrop-filter: blur(6.6px);
border: 1px solid rgba(7, 16, 19, 0.44);
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a text-align: justify;' href="https://twitter.com/MannaAmbarish" target="_blank">Ambarish</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
