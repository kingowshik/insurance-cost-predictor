💰 Insurance Cost Prediction

A Machine Learning project that predicts Medical Insurance Cost (₹) based on personal and health information using Linear Regression, with an interactive Streamlit web application.

📖 Overview

Medical insurance costs vary depending on factors such as age, BMI, smoking status, and region. This project builds a Linear Regression model to predict insurance charges based on these features.

This project demonstrates a complete Machine Learning workflow:

Data loading and preprocessing

Exploratory Data Analysis (EDA)

Feature encoding

Model training using Linear Regression

Model evaluation

Saving the trained model

Building a web app using Streamlit

🧠 Model Details

Algorithm: Linear Regression

Input Features:

Age

BMI

Number of Children

Sex

Smoker Status

Region

Output:

Predicted Medical Insurance Cost

Performance:

R² Score: 0.78

Mean Absolute Error: ₹4176

Root Mean Squared Error: ₹5793

📁 Project Structure
insurance-cost-predictor
│
├── insurance_prediction.ipynb
├── insurance.csv
├── insurance_model.pkl
├── app.py
├── requirements.txt
└── README.md
🚀 Streamlit Application

This project includes a web application where users can:

Enter personal and health details

Get instant insurance cost prediction

▶️ How to Run the Project
Step 1: Clone the repository
git clone https://github.com/yourusername/insurance-cost-predictor.git
Step 2: Open project folder
cd insurance-cost-predictor
Step 3: Install libraries
pip install -r requirements.txt
Step 4: Run Streamlit app
streamlit run app.py
🛠️ Technologies Used

Python

Pandas

NumPy

Scikit-learn

Streamlit

Matplotlib

Seaborn

Pickle

📊 Example

Input:

Age = 40
BMI = 30
Smoker = Yes

Output:

Predicted Insurance Cost ≈ ₹42000
🎯 Project Purpose

This project was created to learn:

Linear Regression

Data Analysis and Visualization

Machine Learning Model Deployment

Building ML Web Applications

⚠️ Disclaimer

This project is for educational purposes only and should not be used for real insurance decisions.

👨‍💻 Author

Gowshik Subramaniyan

⭐ If you like this project

Please give it a ⭐ on GitHub.
