{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "53a7674b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0e428b7a",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"http://localhost:9696/predict\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d3e6d120",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Randomized customer with 1 as a y value\n",
    "customer = {\n",
    "    'job': 'blue-collar', \n",
    "    'marital': 'married', \n",
    "    'education': 'high.school', \n",
    "    'default': 'no', 'housing': 'no', \n",
    "    'loan': 'no', \n",
    "    'contact': 'cellular', \n",
    "    'month': 'mar', \n",
    "    'day_of_week': 'tue', \n",
    "    'poutcome': 'nonexistent', \n",
    "    'age': 30, 'duration': 658, \n",
    "    'campaign': 1, 'pdays': 999, \n",
    "    'previous': 0, \n",
    "    'emp_var_rate': -1.8, \n",
    "    'cons_price_idx': 93.369, \n",
    "    'cons_conf_idx': -34.8, \n",
    "    'euribor3m': 0.655,\n",
    "    'nr_employed': 5008.7\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "349a46d3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Response [200]>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "requests.post(url, json=customer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ed5c5203",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
