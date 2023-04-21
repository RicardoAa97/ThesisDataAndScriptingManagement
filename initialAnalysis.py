import pandas as pd
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt

filePath = "Data/CustomerHubspotData.xlsx"

customerData = pd.read_excel(filePath)

#################### REVENUE #####################

customerData["Log10 Annual Revenue"] = np.log10(customerData["Annual Revenue"])

customerData.loc[customerData["Log10 Annual Revenue"] == -np.inf, "Log10 Annual Revenue"] = np.nan

customerData[['Log10 Annual Revenue']].hist(bins = 30, grid=False)

pl.title('Histogram of Base 10 Logarithm of the Annual Revenue')
pl.ylabel('Frequency')
pl.xlabel('Log10 Annual Revenue')

customerData[['Annual Revenue Category']] = np.nan

customerData.loc[
    pd.isna(customerData['Annual Revenue']),
    'Annual Revenue Category'
] = '0'
customerData.loc[
    customerData['Annual Revenue'] >= 50000000, 'Annual Revenue Category'
] = '7'
customerData.loc[
    ((customerData['Annual Revenue'] < 50000000) & (customerData['Annual Revenue'] >= 10000000)),
    'Annual Revenue Category'
] = '6'
customerData.loc[
    ((customerData['Annual Revenue'] < 10000000) & (customerData['Annual Revenue'] >= 2500000)),
    'Annual Revenue Category'
] = '5'
customerData.loc[
    ((customerData['Annual Revenue'] < 2500000) & (customerData['Annual Revenue'] >= 1000000)),
    'Annual Revenue Category'
] = '4'
customerData.loc[
    ((customerData['Annual Revenue'] < 1000000) & (customerData['Annual Revenue'] >= 250000)),
    'Annual Revenue Category'
] = '3'
customerData.loc[
    ((customerData['Annual Revenue'] < 250000) & (customerData['Annual Revenue'] >= 100000)),
    'Annual Revenue Category'
] = '2'
customerData.loc[
    ((customerData['Annual Revenue'] < 100000) & (customerData['Annual Revenue'] >= 0)),
    'Annual Revenue Category'
] = '1'

print(customerData["Annual Revenue Category"].value_counts())


################# REVIEWS ###################3

customerData[["Log10 Reviews"]] = np.log10(customerData["Reviews"])

customerData[['Log10 Reviews']].hist(bins = 30, grid=False)

pl.title('Histogram of Base 10 Logarithm of the Review Amount')
pl.ylabel('Frequency')
pl.xlabel('Log10 Review Amount')

customerData[['Review Amount Category']] = np.nan

customerData.loc[
    pd.isna(customerData['Reviews']),
    'Review Amount Category'
] = '0'
customerData.loc[
    customerData['Reviews'] >= 5000, 'Review Amount Category'
] = '5'
customerData.loc[
    ((customerData['Reviews'] < 5000) & (customerData['Reviews'] >= 1500)),
    'Review Amount Category'
] = '4'
customerData.loc[
    ((customerData['Reviews'] < 1500) & (customerData['Reviews'] >= 750)),
    'Review Amount Category'
] = '3'
customerData.loc[
    ((customerData['Reviews'] < 750) & (customerData['Reviews'] >= 250)),
    'Review Amount Category'
] = '2'
customerData.loc[
    ((customerData['Reviews'] < 250) & (customerData['Reviews'] >= 0)),
    'Review Amount Category'
] = '1'

print(customerData["Review Amount Category"].value_counts())

#################### SKUs ########################

customerData['SKU Amount'] = customerData["Products (SKU's)"]

# removeDataBoolean = (
#     customerData["SKU Amount"] == 0
# )

# customerData = customerData[~removeDataBoolean]

customerData[["Log10 SKU Amount"]] = np.log10(customerData["SKU Amount"])

customerData.loc[customerData["Log10 SKU Amount"] == -np.inf, "Log10 SKU Amount"] = np.nan

customerData[['Log10 SKU Amount']].hist(bins = 30, grid=False)

pl.title('Histogram of Base 10 Logarithm of the SKU Amount')
pl.ylabel('Frequency')
pl.xlabel('Log10 SKU Amount')

customerData[['SKU Amount Category']] = np.nan

customerData.loc[
    pd.isna(customerData['SKU Amount']),
    'SKU Amount Category'
] = '0'
customerData.loc[
    customerData['SKU Amount'] >= 10000, 'SKU Amount Category'
] = '6'
customerData.loc[
    ((customerData['SKU Amount'] < 10000) & (customerData['SKU Amount'] >= 2500)),
    'SKU Amount Category'
] = '5'
customerData.loc[
    ((customerData['SKU Amount'] < 2500) & (customerData['SKU Amount'] >= 1000)),
    'SKU Amount Category'
] = '4'
customerData.loc[
    ((customerData['SKU Amount'] < 1000) & (customerData['SKU Amount'] >= 250)),
    'SKU Amount Category'
] = '3'
customerData.loc[
    ((customerData['SKU Amount'] < 250) & (customerData['SKU Amount'] >= 100)),
    'SKU Amount Category'
] = '2'
customerData.loc[
    ((customerData['SKU Amount'] < 100) & (customerData['SKU Amount'] >= 0)),
    'SKU Amount Category'
] = '1'

print(customerData["SKU Amount Category"].value_counts())

################### INTEGRATION ####################

customerData["Integration Category"] = np.nan

customerData.loc[
    customerData.Integration.isin(["Picqer", "Picqer Fulfilment", "Goedgepickt"]),
    "Integration Category"
] = "WMS/Fulfilment"
customerData.loc[
    customerData.Integration.isin(["Unit4", "Logic4", "AFAS", "Exact Globe", "Exact Online voor Handel", "Navision Dynamic"]),
    "Integration Category"
] = "ERP"
customerData.loc[
    customerData.Integration.isin(["Magento 2.0", "Shopify", "Woocommerce", "Lightspeed"]),
    "Integration Category"
] = "CMS/Webshop System"
customerData.loc[
    customerData.Integration.isin(["Custom Made"]),
    "Integration Category"
] = "Custom Made"

customerData["Integration"].value_counts()

print(customerData["Integration Category"].value_counts())

#################### INDUSTRY ##################

customerData["Industry"] = customerData["Webshop Business (new)"]

customerData["Industry Category"] = np.nan

customerData.loc[
    customerData.Industry.isin(["Fashion/Clothing", "Shoes", "Fashion accessories", "Beauty Products"]),
    "Industry Category"
] = "Fashion & Accessories"
customerData.loc[
    customerData.Industry.isin(["Gardening/Plants", "Furniture/Accessories", "Lighting", "Bed and bath", "Home improvement", "Kitchen suppliers", "Paper and Packaging"]),
    "Industry Category"
] = "Home & Garden"
customerData.loc[
    customerData.Industry.isin(["Electronics/Accessories", "Phone/Phone Accessories", "Audio/Music", "Gaming/Gaming Accessories"]),
    "Industry Category"
] = "Electronics & Accessories"
customerData.loc[
    customerData.Industry.isin(["Toys", "Party consumables", "Gaming/Gaming Accessories"]),
    "Industry Category"
] = "Toys & Games"
customerData.loc[
    customerData.Industry.isin(["Food & Beverages", "Food/Health supplements"]),
    "Industry Category"
] = "Food & Beverages"
customerData.loc[
    customerData.Industry.isin(["Pets"]),
    "Industry Category"
] = "Pet Supplies"
customerData.loc[
    customerData.Industry.isin(["Tools", "DIY material/products", "Building materials"]),
    "Industry Category"
] = "Tools & Materials"
customerData.loc[
    customerData.Industry.isin(["Other", "Agency", "Baby products", "Faping/smoking goods", "Automotive parts/accessories", "Bicycle/cycle accessories", "Industrial components", "Printing/Print shop", "Multi-seller", "Travel", "Fashion accessories", "Office supplies", "Sport gear"]),
    "Industry Category"
] = "Miscellaneous"

customerData["Industry"].value_counts()

print(customerData["Industry Category"].value_counts())

################## Scatter Matrix #################

scatterData = customerData[["Annual Revenue", "Reviews", "SKU Amount"]]

pd.plotting.scatter_matrix(scatterData)

scatterDataLog = customerData[["Log10 Annual Revenue", "Log10 Reviews", "Log10 SKU Amount"]]

axarr = pd.plotting.scatter_matrix(scatterDataLog, hist_kwds={'bins': 20})

plt.suptitle("Scatter Matrix of Logarithmic Numerical ICP Features")

for i, ax in enumerate(axarr.flatten()):
    if i%3==0:
        ax.set_xlabel('Annual Revenue \n (Log10)')
    if i%3==1:
        ax.set_xlabel('Review Amount \n (Log10)')
    if i%3==2:
        ax.set_xlabel('SKU Amount \n (Log10)')
    if i<=2:
        ax.set_ylabel('Annual Revenue \n (Log10)')
    elif i<=5:
        ax.set_ylabel('Review Amount \n (Log10)')
    elif i<=8:
        ax.set_ylabel('SKU Amount \n (Log10)')
        
        
################### Scatter Matrix Including EMPLOYEES #######################

customerData["Log10 Number of Employees"] = np.log10(customerData["Number of Employees"])

customerData.loc[customerData["Log10 Number of Employees"] == -np.inf, "Log10 Number of Employees"] = np.nan

customerData["Log10 Number of Employees"].hist(bins=30, grid=False)

scatterDataLog = customerData[["Log10 Annual Revenue", "Log10 Reviews", "Log10 SKU Amount", "Log10 Number of Employees"]]

axarr = pd.plotting.scatter_matrix(scatterDataLog, hist_kwds={'bins': 20})

plt.suptitle("Scatter Matrix of Logarithmic Numerical ICP Features")

for i, ax in enumerate(axarr.flatten()):
    if i%4==0:
        ax.set_xlabel('Annual Revenue \n (Log10)')
    if i%4==1:
        ax.set_xlabel('Review Amount \n (Log10)')
    if i%4==2:
        ax.set_xlabel('SKU Amount \n (Log10)')
    if i%4==3:
        ax.set_xlabel('Employee Count \n (Log10)')
    if i<=3:
        ax.set_ylabel('Annual Revenue \n (Log10)')
    elif i<=7:
        ax.set_ylabel('Review Amount \n (Log10)')
    elif i<=11:
        ax.set_ylabel('SKU Amount \n (Log10)')
    elif i<=15:
        ax.set_ylabel('Employee Count \n (Log10)')
