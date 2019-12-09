## Neighborhoods and Spatial Join
There are 104 neighborhoods that were represented in the dataset.

## Great Schools API & Data
Schooling data is a known indicator of housing prices in the US. This is often due to the nature of US public school zoning laws and large discrepancies in the quality of public school between neighborhoods. Thus, housing prices can be deeply influenced by school data. To incorporate this type of data in my models, I utilized Great Schools API to get data on all schools in San Francisco. The data included the location (latitude and longitude), a great schools rating (made by Great Schools themselves, explanation can be found here https://www.greatschools.org/gk/ratings/), the number of public, private, and charter schools, the number of enrolled students, and the public school district the school was located in. Some of the data was missing or incomplete. About 40% of the schools did not have a Great schools rating. About 25% did not have the number of enrolled students. The average value for each respective indicator was used to fill the missing columns. This was the technique employed as regression and machine learning models will not be influenced by those missing data pieces. There was 32 neighborhoods that did not have any school data and thus about 3000 housing sales that did not have any housing data.

### Spatial Binning of School Data
The school data was spatially binned by realtor neighborhoods using a GeoJson file of San Francisco realtor neighborhoods provided by OpenSF [https://data.sfgov.org/Geographic-Locations-and-Boundaries/SF-Find-Neighborhoods/pty2-tcw4]. The average enrollment and Great Schools rating and the total number of private, public, and charter schools per neighborhood were generated. This data can be viewed in the repository under "ENG_DATA/CLEANED/school-data-by-neighborhood.csv".


## Crime Data
Crime is another known indicator of housing prices in the US. One can imagine that houses in relatively safe areas will be more likely to be higher priced than houses in relatively unsafe areas. To test this assumption and include such indicator in the models, the San Francisco police crime data set was gathered. The data set is publicly available at [https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry]. The data contains all crimes from 2003 to 2018. This is over 2 million rows of individual crime data. A 20 percent random sample of the entire dataset was used for simplicity and easier processing.

### Spatial Binning of Crime Data
The crime data was spatially binned by realtor neighborhoods using a GeoJson file of San Francisco realtor neighborhoods provided by OpenSF [https://data.sfgov.org/Geographic-Locations-and-Boundaries/SF-Find-Neighborhoods/pty2-tcw4].  
The crime data included over 50 different types of crimes. To distinguish between crimes, the number of incidents of each type of crime was included in the spatially binned dataset in addition to the total number of incidents per neighborhood. The data can be viewed in the repository under "ENG_DATA/CLEANED/crime-data-by-neighborhood.csv".





###
- Train a bayesian model to predict missing data.
- Test a ada boost tree and shallow forest (low variance) (ensemble method)
- Boosting - predict error, add it back to the model
- Contour plot
- Visualize areas that are under or overpriced

- Can I submit this to a workshop or conference in CS (or close to CS)? 
