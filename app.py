import streamlit as st
import nltk
import pickle
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            if i not in stopwords.words('english'):
                y.append(ps.stem(i))

    return ' '.join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")
input_text = st.text_area("Enter the message")

if st.button('Predict'):
    transformed_sms = transform_text(input_text)
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input)[0]

    if result ==1:
        st.header('Spam')
    else:
        st.header("Not Spam")

