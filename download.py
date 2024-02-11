# Run this file to download the zillow-prize-1 directory
# Download your kaggle.json file and place it in the GitHub directory from your Kaggle account page under API: https://www.kaggle.com/settings
import opendatasets as od
dataset_url = 'https://www.kaggle.com/c/zillow-prize-1/data'
od.download(dataset_url)
