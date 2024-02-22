from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        variance = float(request.form['variance'])
        skewness = float(request.form['skewness'])
        curtosis = float(request.form['curtosis'])
        entropy = float(request.form['entropy'])
        result = predict_note_authentication(variance, skewness, curtosis, entropy)
        return render_template('index.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
