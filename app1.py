import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import pandas as pd
import numpy as np


import nltk
from gtts import gTTS
import os
import tempfile


# Download necessary NLTK resources
nltk.download('punkt')

def text_to_speech(text, language='en'):
    """Converts text to speech and plays it in the web page."""
    # Tokenize the text into sentences
    sentences = nltk.sent_tokenize(text)

    # Create a temporary directory for audio files
    with tempfile.TemporaryDirectory() as tmpdir:
        audio_files = []

        # Convert each sentence to speech and save to temporary files
        for idx, sentence in enumerate(sentences):
            tts = gTTS(text=sentence, lang=language, slow=False)
            filename = f"output_{idx}.mp3"
            filepath = os.path.join(tmpdir, filename)
            tts.save(filepath)
            audio_files.append(filepath)

        # Play the audio files
        for file in audio_files:
            st.audio(file, format='audio/mp3')

        # Clean up temporary audio files (not strictly necessary in this case)
        for file in audio_files:
            os.remove(file)

    st.success("Text-to-speech conversion complete.")




# Create a Streamlit app interface



def home():
    
    st.write("Welcome to the Text to Speech App")
    imageha = mpimg.imread('t_to_s.png')     
    st.image(imageha)  
    st.header('Sentiment')
    st.title("Text to Speech Converter")

    input_text = st.text_area("Enter text to convert to speech")

    if st.button("Convert to Speech"):
        if input_text:
            text_to_speech(input_text)
        else:
            st.warning("Please enter some text to convert.")
    


def prediction():
    
    st.subheader("Sentiment Prediction")

    imagehb = mpimg.imread('sentiment2.jpg')     
    st.image(imagehb)
    # Upload audio file
    comment = st.text_input('Enter your comment:')
    if st.button('Predict Sentiment'):
        # Predict sentiment
        sentiment = predict_sentiment(comment)
        if sentiment == 0:
            st.write('Sentiment: Negative')
        elif sentiment == 1:
            st.write('Sentiment: Neutral')
        else:
            st.write('Sentiment: Positive')

       

    



def main():
    st.set_page_config(layout="wide")
    st.title("Sentiment Analysis App")
# Create the tab layout
    tabs = ["Home"]
    page = st.sidebar.selectbox("Select a page", tabs)

# Show the appropriate page based on the user selection
    home()
    
   
main()
