✉️ Spam Detection System

A Python-based spam detection project that combines data handling, feature extraction, and machine learning to classify messages as spam or ham (not spam). 🚀

- 🛠️ Features
  
Data Handling 🧹

Verify and remove missing values.

Create a numerical label column for classification.

Count the occurrences of spam and ham in the dataset.

Feature Extraction 🔍

Bag of Words (BoW) and TF-IDF vectorization for textual data.

- Machine Learning 🤖

Logistic Regression for spam classification.

Train and test data split with accuracy evaluation.

- 🧰 Prerequisites
  
Python 3.8+ 🐍

Libraries:

Pandas (pip install pandas)

Scikit-learn (pip install scikit-learn)

- 🚀 How It Works
  
1. Data Handling
   
The DataHandler class is responsible for:

Detecting missing values.

Cleaning the dataset by removing columns with missing values.

Creating a new label column where:

spam = 0

ham = 1

2. Feature Extraction
3. 
The ExtractionFeatures class supports:

Bag of Words (BoW): Encodes text into a sparse matrix of token counts.

TF-IDF: Encodes text into a sparse matrix of term frequency-inverse document frequency.

3. Model Training
   
The spam_detector class:

Splits the data into training and testing sets.

Trains a Logistic Regression model.

Evaluates the accuracy of the model.

- 📦 Project Structure

├── DataHandler.py           # Data cleaning and preprocessing class

├── ExtractionFeatures.py    # Feature extraction utilities

├── SpamDetector.py          # Machine learning model class

├── main.py                  # Main script for execution

├── spam.csv                 # Example dataset

- ✨ Future Enhancements
  
Add support for additional machine learning models (e.g., SVM, Random Forest).

Incorporate real-time prediction for incoming messages.

Provide visualizations of the dataset and model performance.

Let me know if you'd like any adjustments or additional sections! 🚀

Reach out to us:

📩 Email: aymenkacem2019@gmail.com

💻 GitHub: aymen-kacem


