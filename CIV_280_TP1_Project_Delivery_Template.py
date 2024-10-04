from tabulate import tabulate
import pandas as pd

# Project - Project Delivery Methods Evaluation Matrix

# Updated data with new scores and methods
data = {
    'Goals / Criteria': ['Time', 'Quality', 'Risk', 'Cost'],
    'Criteria Weight': [65 , 20, 10, 5],  # Example scores (These must sum up to 100)
    'DB-TurnKey Score': [95, 80, 20, 20],  # Updated scores
    'IPD Score': [80, 90, 95, 90],   # New method with scores
    'CM at Risk Score': [85, 85, 10, 85],  # Updated scores
}

# Create the DataFrame
evaluation_matrix = pd.DataFrame(data)

# Calculate Weighted Scores for each method
# Weighted score is calculated as (Score * Criteria Weight) / 100
for method in ['DB-TurnKey', 'IPD', 'CM at Risk']:
    evaluation_matrix[f'{method} Weighted Score'] = (
        evaluation_matrix[f'{method} Score'] * evaluation_matrix['Criteria Weight'] / 100
    )

columns_order = [
    'Goals / Criteria', 'Criteria Weight',
    'DB-TurnKey Score', 'DB-TurnKey Weighted Score',
    'IPD Score', 'IPD Weighted Score',
    'CM at Risk Score', 'CM at Risk Weighted Score',
]

# Reordering the DataFrame according to specified column order
evaluation_matrix = evaluation_matrix[columns_order]

# Calculate the total weighted scores for each method and create a summary row
summary = {
    'Goals / Criteria': 'Total Weighted Score',
    'Criteria Weight': '',
    'DB-TurnKey Score': '',
    'DB-TurnKey Weighted Score': evaluation_matrix['DB-TurnKey Weighted Score'].sum(),
    'IPD Score': '',
    'IPD Weighted Score': evaluation_matrix['IPD Weighted Score'].sum(),
    'CM at Risk Score': '',
    'CM at Risk Weighted Score': evaluation_matrix['CM at Risk Weighted Score'].sum(),
}

# Create a summary DataFrame
summary_df = pd.DataFrame([summary])

# Append summary DataFrame to the main DataFrame
evaluation_matrix = pd.concat([evaluation_matrix, summary_df], ignore_index=True)

# Display the complete matrix
print(tabulate(evaluation_matrix, headers='keys', tablefmt='pretty'))
