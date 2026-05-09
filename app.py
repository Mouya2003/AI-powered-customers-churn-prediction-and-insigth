import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Customer Churn Dashboard")

# Load Dataset
df = pd.read_csv(r"C:\mouya projects\CustomerID,Name,Gender,Age,City,Ten.txt")

# Remove duplicates
df = df.drop_duplicates()

# Fix Gender values
df['Gender'] = df['Gender'].str.lower()
df['Gender'] = df['Gender'].replace({
    'male': 'Male',
    'female': 'Female'
})

# Convert MonthlyCharges to numeric
df['MonthlyCharges'] = pd.to_numeric(
    df['MonthlyCharges'],
    errors='coerce'
)

# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['MonthlyCharges'] = df['MonthlyCharges'].fillna(df['MonthlyCharges'].median())

# Show dataset
st.subheader("Dataset")
st.dataframe(df)

# Churn Count
st.subheader("Churn Distribution")
st.bar_chart(df['Churn'].value_counts())

# Age vs Churn
st.subheader("Age vs Churn")

fig, ax = plt.subplots()

sns.boxplot(
    x='Churn',
    y='Age',
    data=df,
    ax=ax
)

st.pyplot(fig)

# Monthly Charges vs Churn
st.subheader("Monthly Charges vs Churn")

fig2, ax2 = plt.subplots()

sns.boxplot(
    x='Churn',
    y='MonthlyCharges',
    data=df,
    ax=ax2
)

st.pyplot(fig2)

# Insights
st.subheader("Business Insights")

st.write("✔ Customers with monthly contracts churn more.")
st.write("✔ High monthly charges increase churn chance.")
st.write("✔ Lower tenure customers churn more.")