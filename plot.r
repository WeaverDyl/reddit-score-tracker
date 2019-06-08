library(tidyverse)

# Read the csv from the python script
data <- read_csv("score_history.csv")

first <- data$Time[1] # The time of the first piece of data

# time constants
minute <- 60
hour <- minute * 60
day <- hour * 24

# Adds a new column quantifying the time elapsed since the 
# first data point.Change to [minute,hour,day] depending on 
# how you want the graph to be produced. Don't forget to 
# change the x-label below
data <- data %>%
  mutate(TimeSinceFirst = (Time - first) / hour)


# Creates the plot. Change x-label to match units of TimeSinceFirst
data %>%
  ggplot(aes(x=TimeSinceFirst, y=Score)) +
  geom_point() + 
  labs(x="Hours Since Data Collection Began", y="Score", 
        title="Reddit Score Over Time")