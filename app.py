import streamlit as st
import pandas as pd
import joblib

model = joblib.load('taxi_model.pkl')
scaler = joblib.load('taxi_scaler.pkl')
columns = joblib.load('taxi_columns.pkl')

st.title('🚕 NEWYORK TAXE FARE PREDICTION')


distance = st.number_input('DISTANCE(MILE)', min_value=0.1, max_value=50.0, value=2.0, step=0.5)
passengers = st.number_input('PASSENGER COUNT', min_value=1, max_value=6, value=1)
payment = st.selectbox('PAYMENT METHOD', ['credit card', 'cash'])
pickup = st.selectbox('THE PICKUP', ['Manhattan', 'Queens', 'Brooklyn', 'Bronx', 'Unknown'])


if st.button('FARE PREDICT'):
    
    input_data = pd.DataFrame(0, index=[0], columns=columns)
    input_data[['distance', 'passengers']] = scaler.transform([[distance, passengers]])
    
    if f'payment_{payment}' in columns:
        input_data[f'payment_{payment}'] = 1
        
    if f'pickup_borough_{pickup}' in columns:
        input_data[f'pickup_borough_{pickup}'] = 1
        
    prediction = model.predict(input_data)[0]
    st.success(f'YOUR PREDICTED FARE: ${prediction:.2f}')
