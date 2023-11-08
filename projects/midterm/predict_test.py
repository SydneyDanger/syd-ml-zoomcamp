import requests

url = "http://localhost:9696/predict"

# Randomized customer with 1 as a y value
customer = {'job': 'admin.', 'marital': 'married', 'education': 'university.degree', 'default': 'no', 'housing': 'no', 'loan': 'yes', 'contact': 'cellular', 'month': 'dec', 'day_of_week': 'tue', 'poutcome': 'success', 'age': 34, 'duration': 196, 'campaign': 2, 'pdays': 6, 'previous': 2, 'emp_var_rate': -3.0, 'cons_price_idx': 92.713, 'cons_conf_idx': -33.0, 'euribor3m': 0.707, 'nr_employed': 5023.5}
response = requests.post(url, json=customer).json()

print(response)
if response['deposit'] == True:
    print("Customer is predicted to make a deposit!")
else:
    print("Customer is not predicted to make a deposit.")