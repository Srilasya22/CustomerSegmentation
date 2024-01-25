
# import streamlit as st
# import pandas as pd
# from sklearn.preprocessing import StandardScaler
# import joblib

# # Load the pre-trained model
# model = joblib.load('model.pkl')

# # Function to preprocess input data
# def preprocess_input(data):
#     # Create a DataFrame
#     input_data = pd.DataFrame([data])

#     # Feature scaling
#     scaler = StandardScaler()

#     # Update feature names to match those used during training
#     scaled_input = scaler.fit_transform(input_data[['Age', 'Annual Income', 'Spending Score']])
    
#     input_data[['0', '1', '2']] = scaled_input
   
#     return input_data

# # Streamlit App
# def main():
#     st.title("Customer Prediction App")

#     # User inputs
#     st.sidebar.subheader("Enter Customer Information:")
#     customer_id = st.sidebar.number_input("Customer ID", min_value=1)
#     age = st.sidebar.number_input("Age", min_value=0)
#     annual_income = st.sidebar.number_input("Annual Income (k$)", min_value=0)
#     spending_score = st.sidebar.number_input("Spending Score (1-100)", min_value=0, max_value=100)

#     # "Predict" button
#     if st.sidebar.button("Predict"):
#         # Make predictions
#         input_data = {'Customer ID': customer_id, 'Age': age, 'Annual Income': annual_income, 'Spending Score': spending_score}
#         processed_input = preprocess_input(input_data)
        
#         # Ensure feature names match those used during training
#         processed_input = processed_input[['0', '1', '2']]
        
#         cluster = model.predict(processed_input)[0]

#         # Display predictions
#         st.subheader("Predictions:")
#         st.write(f"Predicted Cluster: {cluster}")

# if __name__ == "__main__":
#     main()

import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

# Load the pre-trained model
model = joblib.load('model.pkl')

# Function to preprocess input data
def preprocess_input(data):
    # Create a DataFrame
    input_data = pd.DataFrame([data])

    # Map gender categories to numerical values
    gender_mapping = {'Male': 0, 'Female': 1}
    input_data['Gender'] = input_data['Gender'].map(gender_mapping)

    # Feature scaling
    scaler = StandardScaler()

    # Update feature names to match those used during training
    input_features = ['Age', 'Annual Income', 'Spending Score', 'Gender']
    scaled_input = scaler.fit_transform(input_data[input_features])

    return scaled_input

# Streamlit App
def main():
    st.title("Customer Prediction App")

    # User inputs
    st.sidebar.subheader("Enter Customer Information:")
    customer_id = st.sidebar.number_input("Customer ID", min_value=1)
    age = st.sidebar.number_input("Age", min_value=0)
    annual_income = st.sidebar.number_input("Annual Income (k$)", min_value=0)
    spending_score = st.sidebar.number_input("Spending Score (1-100)", min_value=0, max_value=100)
    gender = st.sidebar.selectbox("Gender", ['Male', 'Female'])

    # "Predict" button
    if st.sidebar.button("Predict"):
        # Make predictions
        input_data = {'Customer ID': customer_id, 'Age': age, 'Annual Income': annual_income, 'Spending Score': spending_score, 'Gender': gender}
        processed_input = preprocess_input(input_data)

        # Use only the first three features as the model expects 3 features
        cluster = model.predict(processed_input[:, :3])[0]

        # Display predictions
        st.subheader("Predictions:")
        st.write(f"Predicted Cluster: {cluster}")

if __name__ == "__main__":
    main()
