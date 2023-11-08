<h3>ML Zoomcamp - Midterm Project</h3>
<h1>Analyzing Banking Data to Determine Term Deposit Likelyhood</h1>

<h2>Table of Contents</h2>
<ol>
    <li>About</li>
    <li>Data Prep, EDA and Feature Importance</li>
    <li>Model Selection</li><ul>
        <li>Logistic Regression</li>
        <li>Decision Tree</li>
        <li>Random Forest</li>
        <li>Gradient Boost</li>
    </ul>
</ol>

<h2>1. About</h2>

This analysis uses data from the UC Irvine Machine Learning Repository. As per the datasets README:  
  
*The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to assess if the product (bank term deposit) would be ('yes') or not ('no') subscribed.*
  
The purpose of my analysis is to build a model that can predict the likelyhood a bank customer will make a term deposit, based on bank client data, information about contact with customer, and socio-economic context attributes. The full dataset includes 20 attributes and 41,188 customer instances. The final model will be trained and deployed as a webservice, allowing customer data to be sent as a JSON request and a prediction to be returned. **This solution would provide a way for the bank to analyze future customers when targeting their ad campaigns, thus increasing their relative percentage of customers who make a deposit.**
  
The data used in this analysis can be accessed here: https://archive.ics.uci.edu/ml/datasets/bank+marketing
  
This analysis will use "bank-additional-full.csv" to build the model. The file is included in this repository.
  
Attribute data, as outlined in dataset README:  
  
**bank client data:**  
1 - age (numeric)  
2 - job : type of job (categorical: 'admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown')  
3 - marital : marital status (categorical: 'divorced','married','single','unknown'; note: 'divorced' means divorced or widowed)  
4 - education (categorical: 'basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown')  
5 - default: has credit in default? (categorical: 'no','yes','unknown')  
6 - housing: has housing loan? (categorical: 'no','yes','unknown')  
7 - loan: has personal loan? (categorical: 'no','yes','unknown')  
**related with the last contact of the current campaign:**  
8 - contact: contact communication type (categorical: 'cellular','telephone')  
9 - month: last contact month of year (categorical: 'jan', 'feb', 'mar', ..., 'nov', 'dec')  
10 - day_of_week: last contact day of the week (categorical: 'mon','tue','wed','thu','fri')  
11 - duration: last contact duration, in seconds (numeric). *Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.*  
**other attributes:**  
12 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)  
13 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric; *999 means client was not previously contacted*)  
14 - previous: number of contacts performed before this campaign and for this client (numeric)  
15 - poutcome: outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success')  
**social and economic context attributes**  
16 - emp.var.rate: employment variation rate - quarterly indicator (numeric)  
17 - cons.price.idx: consumer price index - monthly indicator (numeric)  
18 - cons.conf.idx: consumer confidence index - monthly indicator (numeric)  
19 - euribor3m: euribor 3 month rate - daily indicator (numeric)  
20 - nr.employed: number of employees - quarterly indicator (numeric)  
  
**output variable**
21 - y - has the client subscribed a term deposit? (binary: 'yes','no')  
  
  
Citation: *[Moro et al., 2014] S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, Elsevier, 62:22-31, June 2014*


<h3> Instructions for Running the Project:</h3>