# Economic Trends in Balkan Countries: GDP Growth, Inflation, and Government Expenses

## Introduction

The Balkan region has experienced significant economic changes in recent decades. After periods of political transition, economic restructuring, and integration with global markets, several countries in the region have shown different economic trajectories. Some economies have grown rapidly due to tourism, foreign investment, and lower operating costs, while others have experienced slower growth despite having more developed economies.

This analysis focuses on several Balkan countries and examines three key economic indicators: **GDP growth, inflation, and government expenses**. The goal is to explore how these indicators relate to one another and how economic trends differ across the region. By combining geographical visualization with economic data analysis, it becomes possible to better understand the economic landscape of the Balkans.

---

## Data Sources

The data used in this analysis was obtained from two primary sources.

The geographical data was taken from the **Natural Earth dataset**, accessed through the GeoPandas library. Natural Earth provides publicly available geographic boundary data for countries around the world. These geographic boundaries were used to construct the regional map used in the analysis.

The economic indicators were retrieved from the **World Bank’s World Development Indicators database**. The World Bank provides a wide range of economic statistics for countries globally, including GDP growth, inflation rates, and government expenditures. These datasets contain yearly observations for each country and allow for comparative economic analysis across multiple years.

By combining these two data sources, it was possible to visualize economic indicators geographically and also analyze economic trends through additional charts.

---

## Methodology and Visualization Techniques

Several data visualization and data processing techniques were used to analyze the dataset.

### Geographical Choropleth Map

One of the primary techniques used was a **choropleth map**, which visualizes economic indicators using color intensity. In this analysis, GDP growth values were mapped onto the geographical boundaries of Balkan countries. Each country polygon was extracted from the Natural Earth shapefile and converted into Matplotlib patches. These patches were then colored according to GDP growth values using a continuous color scale.

A **color normalization technique** was applied so that lower GDP growth values appear as lighter shades of blue while higher growth values appear as darker shades. A colorbar was included to provide a legend indicating the scale of GDP growth values.

This technique allows economic differences between countries to be visualized spatially, making regional comparisons easier.

![GDP Growth Map](https://github.com/Jurgen12345/Economic-Trends-in-Balkan-Analysis/blob/main/images/GDP_Growth.png)

### Horizontal Bar Chart

To analyze government expenses, a **horizontal bar chart** was used. Each bar represents the government expenditure of a specific country. Since the values across the Balkan countries are relatively similar, a standard bar chart was used to allow clearer comparison between countries.

Countries are displayed in alphabetical order, allowing viewers to easily compare relative spending levels. This visualization helps highlight which countries have relatively higher or lower government expenses within the region.

![Expenses Plot](https://github.com/Jurgen12345/Economic-Trends-in-Balkan-Analysis/blob/main/images/Expenses.png)

### Time Series Line Chart

Inflation trends were visualized using a **multi-line time series chart**. Each country was represented as a separate line showing inflation values across multiple years. This type of chart is effective for identifying long-term trends, economic shocks, and periods of stabilization.

A legend was included to differentiate countries, and markers were used along the lines to highlight yearly observations.

![Time Series Line Plot](https://github.com/Jurgen12345/Economic-Trends-in-Balkan-Analysis/blob/main/images/Inflation_over_years.png)

## Results and Discussion

The analysis revealed several interesting patterns in the Balkan region.

Countries such as **Kosovo and Albania have experienced relatively strong GDP growth in recent years**, partly driven by tourism, foreign investment, and lower operational costs. These countries have become increasingly attractive destinations for businesses and tourists seeking lower costs compared to more expensive European locations.

Tourism appears to play an important role in economic growth across the region. As travel costs increase in traditional destinations, some tourists are choosing more affordable alternatives in Balkan countries. This shift can stimulate economic activity and contribute to higher GDP growth rates.

Inflation trends also provide insight into economic stability. While Albania experienced high inflation during the early post-communist transition period, inflation levels have stabilized significantly in recent years. Across the region, many Balkan countries now exhibit relatively similar inflation rates, suggesting a degree of macroeconomic convergence.

Government expenditure varies between countries. Greece and Italy show higher levels of government spending compared to some other countries in the region. Meanwhile, countries with lower public spending sometimes demonstrate stronger GDP growth. However, this relationship is not consistent across all cases. For example, Croatia has relatively high government expenditures while still maintaining strong economic performance. This indicates that government spending alone does not fully determine economic growth outcomes.

---

## Conclusion

The economic performance of Balkan countries varies significantly depending on several factors, including tourism, foreign investment, cost of living, and government policy. Smaller economies such as Albania and Kosovo have demonstrated strong growth in recent years, while larger economies such as Greece and Italy have experienced slower growth.

Inflation across the region has become relatively stable, suggesting improving macroeconomic conditions compared to earlier decades. At the same time, differences in government spending highlight that economic growth cannot be explained by a single factor.

Overall, the analysis shows that **economic development in the Balkans is influenced by multiple interconnected variables**, including tourism activity, investment patterns, and fiscal policy. Data visualization techniques such as choropleth maps, bar charts, and time-series line charts provide useful tools for understanding these economic patterns and comparing trends across countries.

---

## References

- Natural Earth Dataset: https://www.naturalearthdata.com  
- World Bank World Development Indicators: https://data.worldbank.org
