#Import libraries
import streamlit as st
import joblib

# Load the pre-trained classifier model
classifier = joblib.load('classifier.pkl')

# Now you can use the loaded classifier object in your Streamlit app


# Function to predict if currency note is fake or not
def predict_note_authentication(variance, skewness, curtosis, entropy):
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    if prediction == 1:
        return "The currency note is authentic."
    else:
        return "The currency note is fake."

# Streamlit app layout
st.markdown(
    """
    <style>
    .header {
        background-color: Red;
        color: white;
        padding: 10px;
        font-size: 24px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="header">Currency Detector App</p>', unsafe_allow_html=True)

st.sidebar.title('Input Features')
variance = st.sidebar.number_input('Variance', value=0.0)
skewness = st.sidebar.number_input('Skewness', value=0.0)
curtosis = st.sidebar.number_input('Curtosis', value=0.0)
entropy = st.sidebar.number_input('Entropy', value=0.0)

if st.sidebar.button('Predict'):
    result = predict_note_authentication(variance, skewness, curtosis, entropy)
    st.write(result)





    
