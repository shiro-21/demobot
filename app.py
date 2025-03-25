import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Function to input data
def user_input_features():
    st.sidebar.header('Enter your data manually:')
    company_name = st.sidebar.text_input('Company Name', 'My Company')
    company_size = st.sidebar.number_input('Company Size', min_value=10, max_value=10000, step=10)
    mean_salary = st.sidebar.number_input('Mean Salary', min_value=20000, max_value=200000, step=1000)
    productivity = st.sidebar.number_input('Productivity Metric', min_value=1, max_value=100, step=1)
    revenue = st.sidebar.number_input('Revenue', min_value=10000, max_value=100000000, step=10000)
    return {
        'Company Name': company_name,
        'Company Size': company_size,
        'Mean Salary': mean_salary,
        'Productivity': productivity,
        'Revenue': revenue
    }

# Generate random data for visualization
def generate_random_data(size, salary, productivity, revenue):
    np.random.seed(42)  # For reproducibility
    data = {
        'Company Size': np.random.randint(10, size*2, size=10),
        'Mean Salary': np.random.randint(20000, salary*2, size=10),
        'Productivity': np.random.randint(1, productivity*2, size=10),
        'Revenue': np.random.randint(1000, revenue*2, size=10)
    }
    return pd.DataFrame(data)

# Streamlit application
st.title('Enterprise Data Visualization Models')

data = user_input_features()

# Display entered data
st.write('### Entered Data:')
st.write(pd.DataFrame(data, index=[0]))

# Generate random data
random_data = generate_random_data(data['Company Size'], data['Mean Salary'], data['Productivity'], data['Revenue'])

# Model 1: Mean Salary vs. Company Size
st.write('### Model 1: Mean Salary vs. Company Size')
fig1 = px.scatter(random_data, x='Company Size', y='Mean Salary', title='Mean Salary vs. Company Size')
st.plotly_chart(fig1)

# Model 2: Productivity vs. Revenue
st.write('### Model 2: Productivity vs. Revenue')
fig2 = px.scatter(random_data, x='Productivity', y='Revenue', title='Productivity vs. Revenue')
st.plotly_chart(fig2)

