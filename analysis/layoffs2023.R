# Layoffs 2023

install.packages("readxl")
install.packages("viridisLite")
install.packages("ggplot2")

library(readxl)
library(tidyverse)
library(dplyr)
library(knitr)
library(ggplot2)

Layoffs_Tracker <- read_excel("Layoffs_Tracker.xlsx")

view(Layoffs_Tracker)
head(Layoffs_Tracker)
str(Layoffs_Tracker)
colnames(Layoffs_Tracker)
class(Layoffs_Tracker)
glimpse(Layoffs_Tracker)


# Summary of the Country column
country_count <- Layoffs_Tracker %>% 
  count(Country)

country_count

continent_count <- Layoffs_Tracker %>% 
  count(Continent)

continent_count

country_count_desc <- country_count %>% 
  arrange(desc(n))

country_count_desc

top_10_countries <- head(country_count_desc, 10)
top_10_countries

# Filter for USA and count Location HQ
usa_locations_2023 <- Layoffs_Tracker %>%
  filter(Country == "USA") %>%
  count(`Location HQ`) %>%
  arrange(desc(n))

usa_locations_2023

Top_5_USA_locations <- head(usa_locations_2023, 5)
Top_5_USA_locations

north_america_locations_2023 <- Layoffs_Tracker %>%
  filter(Continent == "North America") %>%
  count(`Location HQ`) |> 
  arrange(desc(n))
north_america_locations_2023

Top_5_North_America_locations <- head(north_america_locations_2023, 5)
Top_5_North_America_locations

north_america_countries_2023 <- Layoffs_Tracker %>%
  filter(Continent == "North America") %>%
  count(`Country`) |> 
  arrange(desc(n))
north_america_countries_2023

south_america_locations_2023 <- Layoffs_Tracker %>%
  filter(Continent == "South America") %>%
  count(`Location HQ`) |> 
  arrange(desc(n))
south_america_locations_2023

Top_5_South_America_locations <- head(south_america_locations_2023, 5)
Top_5_South_America_locations

south_america_countries_2023 <- Layoffs_Tracker %>%
  filter(Continent == "South America") %>%
  count(`Country`) |> 
  arrange(desc(n))
south_america_countries_2023

europe_locations_2023 <- Layoffs_Tracker %>%
  filter(Continent == "Europe") %>%
  count(`Location HQ`) |> 
  arrange(desc(n))
europe_locations_2023

Top_5_Europe_locations <- head(europe_locations_2023, 5)
Top_5_Europe_locations

europe_countries_2023 <- Layoffs_Tracker %>%
  filter(Continent == "Europe") %>%
  count(`Country`) |> 
  arrange(desc(n))
europe_countries_2023

Top_5_Europe_countries <- head(europe_countries_2023, 5)
Top_5_Europe_countries

africa_locations_2023 <- Layoffs_Tracker %>%
  filter(Continent == "Africa") %>%
  count(`Location HQ`) |> 
  arrange(desc(n))
africa_locations_2023

Top_5_Africa_locations <- head(africa_locations_2023, 5)
Top_5_Africa_locations

africa_countries_2023 <- Layoffs_Tracker %>%
  filter(Continent == "Africa") %>%
  count(`Country`) |> 
  arrange(desc(n))
africa_countries_2023

asia_locations_2023 <- Layoffs_Tracker %>%
  filter(Continent == "Asia") %>%
  count(`Location HQ`) |> 
  arrange(desc(n))
asia_locations_2023

Top_5_Asia_locations <- head(asia_locations_2023, 5)
Top_5_Asia_locations

asia_countries_2023 <- Layoffs_Tracker %>%
  filter(Continent == "Asia") %>%
  count(`Country`) |> 
  arrange(desc(n))
asia_countries_2023

Top_5_Asia_countries <- head(asia_countries_2023, 5)
Top_5_Asia_countries

australia_locations_2023 <- Layoffs_Tracker %>%
  filter(Continent == "Australia") %>%
  count(`Location HQ`) |> 
  arrange(desc(n))
australia_locations_2023

Top_5_Australia_locations <- head(australia_locations_2023, 5)
Top_5_Australia_locations

australia_countries_2023 <- Layoffs_Tracker %>%
  filter(Continent == "Australia") %>%
  count(`Country`) |> 
  arrange(desc(n))
australia_countries_2023


# Create a table for country_count
kable(country_count)

# Create a table for usa_locations
kable(usa_locations_2023)

# Create a table for top 10 countries
kable(top_10_countries)


# Bar plot for country_count
ggplot(country_count, aes(x = Country, y = n)) +
  geom_bar(stat = "identity")

# Create a color palette for the bars
my_colors <- c("darkblue", "darkslategray4", "azure4", "aquamarine2", "cornflowerblue", "cadetblue2","blue1","cyan","deepskyblue1" , "deepskyblue4")

# Bar plot for top 10 countries with specified colors
ggplot(top_10_countries, aes(x = reorder(Country, -n), y = n, fill = Country)) +
  geom_bar(stat = "identity") +
  labs(x = "Country", y = "Count") +
  scale_fill_manual(values = my_colors)  +
  theme(legend.position = "bottom") +
  theme(panel.background = element_rect(fill = "black"))
  

# Bar plot for usa_locations
ggplot(usa_locations_2023, aes(x = `Location HQ`, y = n)) +
  geom_bar(stat = "identity")

ggplot(Top_5_USA_locations, aes(x = reorder(`Location HQ`, -n), y = n, fill = `Location HQ`)) +
  geom_bar(stat = "identity") +
  labs(x = "Location HQ", y = "Count") +
  scale_fill_manual(values = my_colors) +
  coord_flip() +
  theme(legend.position = "bottom") +
  theme(panel.background = element_rect(fill = "black"))


# Create a pie chart
ggplot(Top_5_USA_locations, aes(x = "", y = n, fill = `Location HQ`)) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar("y", start = 0) +
  labs(fill = "Location HQ") +
  scale_fill_manual(values = my_colors) +
  theme_void() +
  theme(panel.background = element_rect(fill = "black")) +
  theme(legend.position = "bottom")  # Adjust legend position if needed


# Bar plot for european_locations

ggplot(Top_5_Europe_locations, aes(x = reorder(`Location HQ`, -n), y = n, fill = `Location_HQ`)) +
  geom_bar(stat = "identity") +
  labs(x = "Location_HQ", y = "Count") +
  scale_fill_manual(values = my_colors) +
  coord_flip() +
  theme(legend.position = "bottom") +
  theme(panel.background = element_rect(fill = "black"),
        )

# Create a pie chart
pie_chart_continent_count <- ggplot(continent_count, aes(x = "", y = n, fill = Continent)) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar("y", start = 0) +
  labs(fill = "Continent") +
  scale_fill_manual(values = my_colors) +
  ggtitle("Pie chart - Reported Layoffs 2023 by continent") +
  theme_void() +
  theme(panel.background = element_rect(fill = "azure2"),
        legend.position = "bottom",
        plot.title = element_text(face = "bold", size = 16))


library(dplyr)

# Assuming your dataset is named 'layoffs_2023'
unique_countries <- Layoffs_Tracker %>%
  distinct(Country) %>%
  summarise(Count = n())

# View unique country counts
print(unique_countries)

# Assuming your dataset is named 'layoffs_2023'
unique_country_list <- unique(Layoffs_Tracker$Country)

# View the list of unique countries
print(unique_country_list)

library(skimr)
skim(Layoffs_Tracker)


# Description: Remove rows with missing values.
Layoffs_Tracker_without_na <- na.omit(Layoffs_Tracker)
skim(Layoffs_Tracker_without_na)


mean(Layoffs_Tracker_without_na$Company_Size_before_Layoffs)
median(Layoffs_Tracker_without_na$Company_Size_before_Layoffs)

mean(Layoffs_Tracker_without_na$Company_Size_after_layoffs)
median(Layoffs_Tracker_without_na$Company_Size_after_layoffs)

usa_locations_2023_without_na <- Layoffs_Tracker_without_na %>%
  filter(Country == "USA") %>%
  count(`Location HQ`) %>%
  arrange(desc(n))
print(usa_locations_2023_without_na)


country_count_na <- Layoffs_Tracker_without_na %>% 
  count(Country)

country_count_desc_na <- country_count_na %>% 
  arrange(desc(n))

country_count_desc_na

top_10_countries_na <- head(country_count_desc_na, 10)
top_10_countries_na

pie_chart_north_america_locations_2023 <- ggplot(north_america_locations_2023, aes(x = "", y = n, fill = Location_HQ)) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar("y", start = 0) +
  labs(fill = "Location_HQ") +
  scale_fill_manual(values = my_colors) +
  ggtitle("Pie chart - Reported Layoffs 2023 by Location HQ in North America") +
  theme_void() +
  theme(panel.background = element_rect(fill = "azure2"),
        legend.position = "bottom",
        plot.title = element_text(face = "bold", size = 16))

install.packages("colorspace")
library(colorspace)
install.packages("viridisLite")
