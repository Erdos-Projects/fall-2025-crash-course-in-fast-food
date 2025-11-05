# fall-2025-crash-course-in-fast-food
Team project: fall-2025-crash-course-in-fast-food

This project has been developed during the Erdos Institute Data Science Boot Camp Fall 2025.

Team: [Larissa Boie](https://github.com/larissaboie) & [Ann-Kathrin Raab](https://github.com/anka-raab)


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

