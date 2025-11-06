# fall-2025-crash-course-in-fast-food
Team project: fall-2025-crash-course-in-fast-food

This project has been developed during the Erdos Institute Data Science Boot Camp Fall 2025.

Team: [Larissa Boie](https://github.com/larissaboie) & [Ann-Kathrin Raab](https://github.com/anka-raab)

[Jump to Description of Repository](#description-of-repository)

### The goal

As frequent pedestrians and cyclists, the city of Columbus, OH, does not always feel safe to us. This is especially true during rush hours on weekdays, where many cars are on the road. Living in a busy area where lots of fast food chains are located conveniently for people driving in and out of town, anecdotal evidence seems to indicate that our most dangerous near misses happen when people drive in and out the drive through areas of the fast food restaurants. We believe that the large speed difference between cars on the road and cars entering the road leads to many dangerous situations. Understanding if and how the surrounding environment (traffic lights nearby, blind corners etc.) influences the possibility of accidents can help improving road safety for all participants. As the city of Columbus is growing, the information can be useful when developing new neighborhoods with a mix of residential and commercial areas. Understanding if certain commercial vendors need extra signage, more space, or maybe even a redesign of the entrance and exit driveways will help plan the development of mixed resident/commercial areas.

The information can help developers, road planning offices, and the franchise owners alike, making the restaurant experience not only pleasant, but also safe.

We will not focus on general accident causes or general road improvements. Our analysis should only correrlate locations of fast food restaurants, as these are places where we understand incoming and outgoing traffic and these places can be easily located on online maps, as all restaurant chains have marked their locations online


### The data

We requested the Crash Statistics from the state of Ohio for the longest available period, which is 9/23/2020 until 9/22/2025. This falls in the Covid-19 pandemic, which we should keep in mind, as many behaviors have been drastically different to usual routines and data might vary more than what one could expect from usual annual fluctuations. This data was obtained via e-mail from the Ohio Department of Public Safety and contained a README file with the following information:

```
Crash Statistics was Generated on the Following Criteria::
----------------------------------------------------------

Generated On : 9/23/2025 6:59:37 AM
Order Number : OH250922102523426ZELSFG
From Date    : 9/23/2020
To Date      : 9/22/2025
Total Records : 41404
```

While this data contains the data from the whole state of Ohio, we will only use the part of Franklin county, where the city of Columbus is located. We will furthermore focus on weekdays and exclude public holidays, as routines often differ which could blurr any patterns we detect.



### The workflow

We use the [crash dashboard](https://statepatrol.ohio.gov/dashboards-statistics/ostats-dashboards/crash-dashboard) and connect it to location details via the [Google Maps API](https://developers.google.com/maps/apis-by-platform) which not only tells us the location of the relevant restaurants, but also reveals information on pedestrian crossings, lights, and sharp corners. To have a large enough dataset, we use information from the years 20xx - 20xx.

Open Street Maps (OSM) contains tags for landmarks, sights and also restaurants. If they are properly categorized, we can use a certain geographic unit (in our case the state of 
Ohio) and look for amenities with the label "fast food". To verify that the extraction of locations with their latidude and longitude coorinates works as expected, we plot all "fast food" marks:

<img width="547" height="450" alt="overview_fast_food_locations_Columbus" src="https://github.com/user-attachments/assets/35f1d87e-8de9-4439-823b-5e6801cd2039" />


### What we compare

Our assumption of drive-throughs being specifically prone to accidents and near misses will be tested against a very similar type of restaurant involving easily accessible food, but almost never a drive through: pizza restaurants. Take-out is still very common, but as pizza is considered an item that takes too long to prepare for a drive-through workflow to work efficiently, people call ahead and pick up their order. This might be a more intentional action than the drive-through, where you don't really stop the car, you don't get out of the car etc.

Filtering for restaurants with the cuisine labeled "pizza" shows these locations:

<img width="535" height="450" alt="overview_pizza_locations_Columbus" src="https://github.com/user-attachments/assets/c7e35ad3-7779-453e-9dc9-30692cc9243a" />


### Our modeling approach

We employ a regression model to connect the density of car crashes with the density of fast food restaurant chains. More precisely, we model the spatial distribution of car crashes as a function of fast-food restaurant proximity. Using the model, we want to identify a potential correlation between crash incidents and fastfood locations deviating from random spatial distribution.

The geographically weighted regression (GWR) model takes into account that loacal coefficients can very spatially, identifying regional differences in the strength and direction of the observables. Applying this model, we want to identify potential hotspots with above-average correlation between crash sites and fastfood chain locations.

Our model thus takes the following form:

$$
D_{\text{Crash}}(x,y) = a(x,y) + b(x,y) \cdot D_{\text{Fastfood}}(x,y) + c
$$

with the densities $D$ for crash events and fastfood restaurant locations, the spatial coordinates $(x,y)$, represented by longitude and latitude values, and $a(x,y)$ the intercept term of the regression giving us the expected value for no correlation at a specific location $(x,y)$. With $a(x,y)$ we can describe naturally occurring higher densities in the crash map (e.g. a narrow curve, a blind turn), that have nothing to do with the location of fastfood restaurants. Parameter $b(x,y)$ hints at the strength of the relationship between car crash location and fastfood restaurant location. 

With the residual $c$ we can identify weaknesses of the model or other irregularities.

### Results

The GWR gives the following parameters:
```
Optimal bandwidth: 51.0
===========================================================================
Model type                                                         Gaussian
Number of observations:                                                 292
Number of covariates:                                                     2

Global Regression Results
---------------------------------------------------------------------------
Residual sum of squares:                                         744856.084
Log-likelihood:                                                   -1559.582
AIC:                                                               3123.164
AICc:                                                              3125.248
BIC:                                                             743209.825
R2:                                                                   0.079
Adj. R2:                                                              0.076

Variable                              Est.         SE  t(Est/SE)    p-value
------------------------------- ---------- ---------- ---------- ----------
X0                                  35.681      5.042      7.077      0.000
X1                                  11.659      2.335      4.994      0.000

Geographically Weighted Regression (GWR) Results
---------------------------------------------------------------------------
Spatial kernel:                                           Adaptive bisquare
Bandwidth used:                                                      51.000

Diagnostic information
---------------------------------------------------------------------------
Residual sum of squares:                                         556601.790
Effective number of parameters (trace(S)):                           30.347
Degree of freedom (n - trace(S)):                                   261.653
Sigma estimate:                                                      46.122
Log-likelihood:                                                   -1517.046
AIC:                                                               3096.786
AICc:                                                              3104.596
BIC:                                                               3212.040
R2:                                                                   0.312
Adjusted R2:                                                          0.232
Adj. alpha (95%):                                                     0.003
Adj. critical t value (95%):                                          2.963

Summary Statistics For GWR Parameter Estimates
---------------------------------------------------------------------------
Variable                   Mean        STD        Min     Median        Max
-------------------- ---------- ---------- ---------- ---------- ----------
X0                       37.911     20.938     -6.478     34.259     90.050
X1                       11.792      8.699     -3.350     11.644     43.793
===========================================================================
```
A spatical correlogram using Moran's $I$ statistical analysis shows clustering and outliers in the correlation between crash site and fastfood restaurant location.

<img width="545" height="391" alt="spatial_correlogram" src="https://github.com/user-attachments/assets/994d5118-6d25-4173-b7b7-41f41d1d0a1b" />

While the spatial correlogram shows a decreasing trend for a larger number of nearest neighbors, indicating that the autocorrelation weakens for increasing distances. The high positive Moran's $I$ number for short distances hints at strong spatial clustering. To further evaluate the clustering, we apply the geographically weighted regression to search for hotspots of correlation between fastfood location proximity and crash report density.

The GWR on a map (which only fits roughly because of the grid to perform the regression) looks like this:

<img width="869" height="450" alt="grid_map_GWR_statistics" src="https://github.com/user-attachments/assets/11ae9dd0-fbb2-40bf-879c-0ab410ace9b3" />

For comparison, the same analysis is performed for the locations of pizza restaurants.
```
Optimal bandwidth: 129.0
===========================================================================
Model type                                                         Gaussian
Number of observations:                                                 134
Number of covariates:                                                     2

Global Regression Results
---------------------------------------------------------------------------
Residual sum of squares:                                         318108.051
Log-likelihood:                                                    -710.882
AIC:                                                               1425.765
AICc:                                                              1427.949
BIC:                                                             317461.536
R2:                                                                   0.001
Adj. R2:                                                             -0.007

Variable                              Est.         SE  t(Est/SE)    p-value
------------------------------- ---------- ---------- ---------- ----------
X0                                  41.804     11.201      3.732      0.000
X1                                   3.220      8.905      0.362      0.718

Geographically Weighted Regression (GWR) Results
---------------------------------------------------------------------------
Spatial kernel:                                           Adaptive bisquare
Bandwidth used:                                                     129.000

Diagnostic information
---------------------------------------------------------------------------
Residual sum of squares:                                         304816.932
Effective number of parameters (trace(S)):                            4.316
Degree of freedom (n - trace(S)):                                   129.684
Sigma estimate:                                                      48.481
Log-likelihood:                                                    -708.023
AIC:                                                               1426.677
AICc:                                                              1427.203
BIC:                                                               1442.081
R2:                                                                   0.043
Adjusted R2:                                                          0.011
Adj. alpha (95%):                                                     0.023
Adj. critical t value (95%):                                          2.297

Summary Statistics For GWR Parameter Estimates
---------------------------------------------------------------------------
Variable                   Mean        STD        Min     Median        Max
-------------------- ---------- ---------- ---------- ---------- ----------
X0                       40.725     10.181     29.067     36.398     62.444
X1                        5.730      5.869     -8.084      8.850     11.054
===========================================================================
```



### Discussion

We observe very little to no negative 

# Description of Repository

The content is presented in the following folders:

### Data
Contains partial and filtered csv that have been generated from the main file received via download link from the Ohio Department of Public Safety. Furthermore, there are .gpkg files where location coordinates have been transformed to geospatial dataframes for plotting.

### executive summary
Contains both the .tex file and the pdf generated from the file. The file has been created using Overleaf. While Overleaf allows for zip file export to include all connected files, we believed that this was not necessary for the goal of the report.

### presentation
Contains the .tex and pdf of the presentation. As the executive summary, the file has been created using Overleaf. The recording is not included due to file size restrictions.

### Notebooks
Contains the Jupyter notebooks that were used for data exploration, modeling, visualization and further analysis.

1. statistics_fastfood.ipynb and statistics_pizza.ipnb
   
   We use the esda module for a Moran analysis and the mgwr module to perform the correlation with a grid coordinate system.

3. export_XX_locations_from_osm.py
   
   There are three python scripts that obtain the data of a certain type of location from the OSM (OpenStreetMap) overpass API. The data extraction is refined using the boundaries of the state of Ohio. Furthermore, depending on the category, certain name adjustments are implemented to account for inconsistent naming conventions and heterogeneous tags/keywords regarding cuisine.


