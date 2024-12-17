import streamlit as st 
import pickle as pkl
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
import string
ps = PorterStemmer()

st.title('Email Spam CLassifier')
text = st.text_area('Paste your message')
vectorizer = pkl.load(open("vectorizer.pkl",'rb'))
model = pkl.load(open("model.pkl",'rb'))



def tranform_text(text):
    text = text.lower() # lowering
    text = nltk.word_tokenize(text) # tokenization
    
    y = [] # removing special characters
    for i in text:
        if i.isalnum():
            y.append(i)
            
    text = y[:] # to copy the list..we gotta do cloning
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
            
    return " ".join(y)

if st.button('predict'):
    tranform_msg = tranform_text(text)
    vectorize = vectorizer.transform([tranform_msg])
    result = model.predict(vectorize)[0]
    if result == 1:
        st.header('Spam')
    else:
        st.header("Not Spam")