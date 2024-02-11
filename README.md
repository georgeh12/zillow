# Datasheet for dataset "Housing"

Questions from the [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) paper, v7.

Jump to section:

- [Motivation](#motivation)
- [Composition](#composition)
- [Collection process](#collection-process)
- [Preprocessing/cleaning/labeling](#preprocessingcleaninglabeling)
- [Uses](#uses)
- [Distribution](#distribution)
- [Maintenance](#maintenance)

## Motivation

The related project is an attempt to recreate machine learning models to use in the [Zillow Prize: Zillow’s Home Value Prediction (Zestimate)](https://www.kaggle.com/c/zillow-prize-1/).

### For what purpose was the dataset created? 

Testing house price prediction using regression models with machine learning.

### Who created the dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)?
This dataset was collected from [Kaggle Housing Prices Dataset](https://www.kaggle.com/code/yasserh/housing-price-prediction-best-ml-algorithms/input) by M Yasser H.

### Who funded the creation of the dataset? 

Kaggle

## Composition

Data is licensed under [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/).

### What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)?

Housing prices and features.

### How many instances are there in total (of each type, if appropriate)?

504 house entries

### Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set?

The dataset may represent a sample of extremely expensive houses, houses in a different currency than USD, or neglected a decimal point in the housing prices to indicate 00 fractional dollars.

### What data does each instance consist of? 

The following feature data is available for each house: price (positive integer), area (positive integer), bedrooms (positive integer), bathrooms (positive integer), stories (positive integer), mainroad (yes/no), guestroom (yes/no), basement (yes/no), hotwaterheating (yes/no), airconditioning (yes/no), parking (0-3), prefarea (yes/no), furnishingstatus (furnished/semi-furnished/unfurnished).

### Is there a label or target associated with each instance?

No

### Is any information missing from individual instances?

No

### Are relationships between individual instances made explicit (e.g., users’ movie ratings, social network links)?

No relationships observed.

### Are there recommended data splits (e.g., training, development/validation, testing)?

No. I used a 50-50 split of training and testing data.

### Are there any errors, sources of noise, or redundancies in the dataset?

The price of the houses seems rather high. It is possible that the author did not include the decimal point to indicate a fractional dollar, or the prices are in a different denomination than USD.

### Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)?

Self-contained.

### Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals’ non-public communications)?

No, public housing data only.

### Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?

No

### Does the dataset relate to people? 

No

### Does the dataset identify any subpopulations (e.g., by age, gender)?

No

### Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset?

No

### Does the dataset contain data that might be considered sensitive in any way (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)?

No

## Collection process

It is unclear how the author collected this data or if it was generated.

## Preprocessing/cleaning/labeling

Data was not manipulated from the original sample.

## Uses

Other users of Kaggle reported that the data is useful for Learning (64), Research (12), and Application (6).

## Distribution

Data will be distributed to Carnegie Mellon University.

## Maintenance

Kaggle is supporting the dataset. The author has not made changes to the dataset after it was first uploaded January 12, 2022.
