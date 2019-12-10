# Overview
## Specific Aims
This paper aims to predict housing sale prices using machine learning in San Francisco. The hypothesis states that the machine learning models will outperform simple regression models for the same given dataset. Furthermore, the hypothesis states that feature additions including crime, school, and transportation will lead to better predictions. The San Francisco dataset is used as a preliminary example for the UAE dataset. The aim of the overall capstone project is to build a series of machine learning models to better predict housing sale prices. This will include a data preparation library for fine tuning inputs to the provided models. The models will be adaptable to both San Francisco and the UAE and thus would assumedly generalize to most city housing datasets.

## Background
draw from previous research

## Data
### Ideal Dataset
The ideal data set includes all housing sales in a recent time frame. Within the dataset the column space includes: hedonistic features (number of rooms, number of bath, square footage, number of bedrooms, etc.), location data (latitude, longitude, neighborhood, zip code, etc.), important features (number of crimes in the neighborhood, school ratings in the neighborhood, number of blocks to public transportation, etc.)

### Neighborhoods and Spatial Join
There are 104 realtor neighborhoods that were represented in the dataset. These neighborhoods are used by real estate regions to subdivide the zip coded areas of San Francisco. Thus, the paper assumes that these neighborhoods encode a non-linear transformation of the location data in San Francisco. For this reason, the neighborhoods were added to each housing sale in the dataset. Furthermore, schooling and crime data was spatially joined to the dataset by aggregating on each neighborhood. This technique was employed for both ease and accuracy. However, better methods are possible and could be employed in future iterations of the project. One possible extension could be approximating the density of the given indicator at each location of the housing sale using GPU programming.

### Great Schools API & Data
Schooling data is a known indicator of housing prices in the US. This is often due to the nature of US public school zoning laws and large discrepancies in the quality of public school between neighborhoods. Thus, housing prices can be deeply influenced by school data. To incorporate this type of data in my models, I utilized Great Schools API to get data on all schools in San Francisco. The data included the location (latitude and longitude), a great schools rating (made by Great Schools themselves, explanation can be found here https://www.greatschools.org/gk/ratings/), the number of public, private, and charter schools, the number of enrolled students, and the public school district the school was located in. Some of the data was missing or incomplete. About 40% of the schools did not have a Great schools rating. About 25% did not have the number of enrolled students. The average value for each respective indicator was used to fill the missing columns. This was the technique employed for its ease, further discussion can be found in the filling empty data section. There was 32 neighborhoods that did not have any school data and thus about 3000 housing sales that did not have any school data.

#### Spatial Binning of School Data
The school data was spatially binned by realtor neighborhoods using a GeoJson file of San Francisco realtor neighborhoods provided by OpenSF [https://data.sfgov.org/Geographic-Locations-and-Boundaries/SF-Find-Neighborhoods/pty2-tcw4]. The average enrollment and Great Schools rating and the total number of private, public, and charter schools per neighborhood were generated. This data can be viewed in the repository under "ENG_DATA/CLEANED/school-data-by-neighborhood.csv".

### Crime Data
Crime is another known indicator of housing prices in the US. One can imagine that houses in relatively safe areas will be more likely to be higher priced than houses in relatively unsafe areas. To test this assumption and include such indicator in the models, the San Francisco police crime data set was gathered. The data set is publicly available at [https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry]. The data contains all crimes from 2003 to 2018. This is over 2 million rows of individual crime data. A 20 percent random sample of the entire dataset was used for simplicity and easier processing.

#### Spatial Binning of Crime Data
The crime data was spatially binned by realtor neighborhoods using a GeoJson file of San Francisco realtor neighborhoods provided by OpenSF [https://data.sfgov.org/Geographic-Locations-and-Boundaries/SF-Find-Neighborhoods/pty2-tcw4].  
The crime data included over 50 different types of crimes. To distinguish between crimes, the number of incidents of each type of crime was included in the spatially binned dataset in addition to the total number of incidents per neighborhood. The data can be viewed in the repository under "ENG_DATA/CLEANED/crime-data-by-neighborhood.csv".

## Filling Empty Data
Empty data was filled using the average value for the given indicator. This is a common technique. However, it often leads to inaccuracies and incorrect assumptions in the dataset. A better methodology, which could be employed in the next iteration, would be to build a prior distribution on the empty data. This could be done by training a bayesian model to predict the empty data indicator. Then, when an empty piece of data is encountered, the trained distribution's MAP or MLE on the empty data column for the given data row is used.

### Feature Visualization

### Feature Encoding

### Feature Selection


## Approach
The approach begins with research and collection of the ideal dataset, specified in the `Data` section under the `Ideal Dataset`. This type of dataset was unattainable within semester's timeline. For this reason, the San Francisco dataset and example has been used. Once the dataset is collected, the first step is to understand and clean the dataset. This may involve filling missing data, finding missing data, identifying outliers, removing outliers. The next step is to pull in important features. This is heavily bias to the city in focus. For the US, crime and school quality are two crucial aspects to understanding housing prices. In Singapore, proximity to public transportation is crucial to understanding housing prices. In Abu Dhabi and Dubai, proximity to Sheik Zayed Road may be critical to housing prices. Next, visualizing the dataset is performed. Reference to methodology can be found under the `Data` and `Feature Visualization` section. Visualization is important for fine tuning models and understanding failure. Finally, feature encoding is performed to allow categorical data to be interpreted by the models used. Feature selection is optionally performed to reduce the dimensionality of the data space. This is critical for one-hot encoded data as the dimensionality can grow exponentially. This can prove ruinous for the models accuracy.
Once data cleaning is complete, the dataset is split by training, validation, and test data. The split is generally: 0.7, 0.1, 0.2, respectively. The models ingest the training data, perform cross-validation on the validation data, and output the score based on the test data.
Finally, model performance is conducted to evaluate the results and impact. R-squared values are used as a primary indicator for model performance as the target variable is continuous. Percent test error is also used to identify outliers in the test error. Finally, percent test error is visualized spatially across the city. 

## Objectives

## Hypothesis

# Results
## H20 Models
The AutoML H20 models were used to evaluate the data collected. The models set a benchmark for the best in class predictors in out of the box machine learning. The top AutoML model was an ensemble method which compiles the best individual regressors (Decision Trees, Neural Networks, Random Forests, etc...). The model had a cross-validation R squared of 0.81. The test R squared was 0.79.
