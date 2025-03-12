import streamlit as st
import pickle

# Load the model and vectorizer
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

def predict(text):
    # Preprocess the text
    text_vectorized = vectorizer.transform([text])
    # Get prediction and probability
    probabilities = model.predict_proba(text_vectorized)[0]  # Probability array for both classes
    prediction = model.predict(text_vectorized)[0]  # Predicted label
    probability = probabilities[1] if prediction == 1 else probabilities[0]  # Probability of predicted class
    return prediction, probability

def main():
    st.title("Test Case Prioritization")
    text_input = st.text_area("Enter your test case description here")
    if st.button("Predict"):
        if text_input:
            prediction, probability = predict(text_input)
            # Update labels for pass/fail
            label = "Pass" if prediction == 1 else "Fail"
            st.write(f"Predicted Label: **{label}**")
            st.write(f"Probability of **{label}**: **{probability:.2f}**")
        else:
            st.warning("Please enter some text for analysis.")

if __name__ == '__main__':
    main()
