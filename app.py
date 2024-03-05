
# # """
# # Created on Fri May 15 12:50:04 2020

# # @author: Arshad.Shaikh
# # """


# import numpy as np
# import pickle
# import pandas as pd
# #from flasgger import Swagger
# import streamlit as st 

# # from PIL import Image



# pickle_in = open("classifier.pkl","rb")
# classifier=pickle.load(pickle_in)


# # def welcome():
# #     return "Welcome All"


# def predict_note_authentication(variance,skewness,curtosis,entropy):
    
#     # """Let's Authenticate the Banks Note 
#     # This is using docstrings for specifications.
#     # ---
#     # parameters:  
#     #   - name: variance
#     #     in: query
#     #     type: number
#     #     required: true
#     #   - name: skewness
#     #     in: query
#     #     type: number
#     #     required: true
#     #   - name: curtosis
#     #     in: query
#     #     type: number
#     #     required: true
#     #   - name: entropy
#     #     in: query
#     #     type: number
#     #     required: true
#     # responses:
#     #     200:
#     #         description: The output values
        
#     # """
   
#     prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
#     # print(prediction)
#     if prediction==1:
#         declare='No'
#     else:
#         declare='Yes'
#     return declare




# def main():
#     st.title("Bank Authenticator")
#     html_temp = """
#     <div style="background-color:tomato;padding:10px">
#     <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
#     </div>
#     """
#     st.markdown(html_temp,unsafe_allow_html=True)
#     variance = st.text_input("Variance")
#     skewness = st.text_input("skewness")
#     curtosis = st.text_input("curtosis")
#     entropy = st.text_input("entropy")
#     result=""
#     if st.button("Predict"):
#         result=predict_note_authentication(variance,skewness,curtosis,entropy)
#     st.success('The output is {}'.format(result))
#     # if st.button("About"):
#     #     st.text("Lets LEarn")
#     #     st.text("Built with Streamlit")




# if __name__=='__main__':
#     main()



import streamlit as st
import pickle

# Load the pre-trained classifier model
with open('classifier.pkl', 'rb') as model_file:
    classifier = pickle.load(model_file)

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
        background-color: olive;
        color: white;
        padding: 10px;
        font-size: 24px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="header">Samrat Consultancy</p>', unsafe_allow_html=True)

st.sidebar.title('Input Features')
variance = st.sidebar.number_input('Variance', value=0.0)
skewness = st.sidebar.number_input('Skewness', value=0.0)
curtosis = st.sidebar.number_input('Curtosis', value=0.0)
entropy = st.sidebar.number_input('Entropy', value=0.0)

if st.sidebar.button('Predict'):
    result = predict_note_authentication(variance, skewness, curtosis, entropy)
    st.write(result)





    
