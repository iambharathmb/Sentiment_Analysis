import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def sentiment_analysis(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)
    return sentiment_score

def main():
    st.title("Sentiment Analysis App")
    text = st.text_input("Enter text:")
    if st.button("Analyze"):
        sentiment_score = sentiment_analysis(text)
        st.write(sentiment_score)

if __name__ == '__main__':
    main()