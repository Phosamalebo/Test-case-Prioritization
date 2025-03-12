## Test Case Prioritazation

### Project Overview

This project is an AI-powered system for prioritizing test cases based on their likelihood of passing or failing. It leverages Natural Language Processing (NLP) and Machine Learning (ML) models to predict and prioritize software test cases, helping teams focus on the most critical tests first.

### Features

-Data Preprocessing: Cleans and prepares test case descriptions.

-Imbalanced Data Handling: Uses SMOTE to balance pass/fail distributions.

-Model Training: Trains Logistic Regression and Naive Bayes classifiers.

-Prediction & Probability: Predicts pass/fail outcomes with associated probabilities.

-Visualization: Graphically displays dataset distributions and class balancing.

-Streamlit App: Interactive web interface for real-time test case analysis.

-Model & Vectorizer Persistence: Saves models and vectorizers for reuse.

### Models & Techniques

-TF-IDF Vectorizer: Converts text to feature vectors.

-SMOTE: Synthetic Minority Oversampling Technique to balance class distribution.

-Logistic Regression: With class weights to handle imbalances.

-Multinomial Naive Bayes: Suitable for text classification tasks.

### Visualizations

-Test case execution distribution (Pass/Fail).

-Class distribution post-SMOTE (balancing demonstration).

-Top keywords for Pass/Fail outcomes.

### Saving and Loading Models

-Trained model saved as model.pkl

-Vectorizer saved as vectorizer.pkl

-Automatically loaded in Streamlit app for real-time predictions.

 ### IDE

-Developed and tested using Visual Studio Code (VSCode).

-Recommended extensions for smooth experience:

-Python

-Jupyter (for notebooks)

-Pylance for IntelliSense

-Streamlit for web app development and preview
