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

### How to do cross-validation

This will be filled once we know.

