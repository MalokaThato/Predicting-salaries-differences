import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("salary.csv")

# Get the number of responders

print("Responses in each column: \n" + str(df.count()))


# After seeing the responses we can not that there is one value mising from the salary column

# Number of responders
responders = int(df["exprior"].count())


# Number of missing values

df_missing_va = responders - int(df["salary"].count())

print(" Number of responders: " + str(responders) + "\n Number of missing responses: " + str(df_missing_va))


# Now we must start cleaning the data

# first we get the position of the null value

print("Printing null value: \n" + str(df["salary"].loc[df["salary"].isnull() == True]))

# After printing the above we can confirm that the missing value is at position 208


# Removing the missing position

df_clean = df.drop(208)

# From this point we will be using the clean df

# Getting the lowest and hightest salary

print("The lowest salary is: " + str(df_clean["salary"].min()))
print("The heighest salary is: " +  str(df_clean["salary"].max()))

# Getting the mean and the standard error

print("The mean for the salaries is: " + str(df_clean["salary"].mean()))
print("The standard error is: " + str(stats.sem(df_clean["salary"])))

#Getting the stantard deviation for the years worked and the median salary

print("The standard deviation for the years worked is: " + str(df_clean["yearsworked"].std()))
print("The median salary is: " +  str(df_clean["salary"].median()))

# Getting the interquartile range
i_range = stats.iqr(df_clean['salary'])
print('The salary interquartile range is: ' +str(i_range))


#This secetion gets the number of men and women in the sample

# Getting the number of males
df_clean_males =  df_clean.loc[df_clean["male"] == 1]
print("The number of males in the sample is: " + str(df_clean_males["male"].count()))

# Getting the number of females in the sample
df_clean_females = df_clean.loc[df_clean["male"] == 0]
print("The number of females in the sample is: " + str(df_clean_females["male"].count()))

# Getting the number of women who are executives compared to men
print("The number of male executives is: " + str(df_clean_males["position"].loc[df_clean_males["position"] == 3].count()))

print("The number of female executives is: " + str(df_clean_females["position"].loc[df_clean_females["position"] == 3].count()))

# Ploting a histograme to display the salaries
df_clean["salary"].plot(kind="hist", bins = 100)
plt.xlabel("Salary")
plt.show()

# Different average salaries of men and women
avg_men_salary = df_clean_males["salary"].mean()
avg_females_salary = df_clean_females["salary"].mean()

avg_salaries = [avg_men_salary, avg_females_salary]
label = ["male", "female"]

x = np.arange(len(label))

plt.bar(x,avg_salaries)
plt.ylabel("Salary")
plt.xlabel("Gender")
plt.show()

# Scatter plot between the years worked and salary

sns.regplot(df_clean['yearsworked'], df_clean['salary'])
plt.xlabel('Year Worked')
plt.ylabel('Salary')
plt.show()

print("If we take a look at the above we can clearly see there is a positive relationship between the years worked and the salary one gets.")
print("Although the are some extreme cases, where one has worked for more than 41 years but yet they earn less than 70 000 and one \n where 3 people(males) have worked less than 24 years but they earn more than 90 000")

# Getting the identities of the extreme individuels on our Scatter Plot
df_salary_heigh = df_clean.loc[df_clean["salary"] > 90000]
print("Extreme cases where people earn more but have worked less years: \n" + str(df_salary_heigh))

# Gettig the individual that earns less but hs worked for over 40 yearsworked

df_low_salary_moreyears = df_clean.loc[df_clean["salary"] < 70000]
extreme_low_individual = df_low_salary_moreyears.loc[df_low_salary_moreyears["yearsworked"] > 40]
print("Extreme case where one earns less but yet they have worked for more years: \n" + str(extreme_low_individual))


# Pearson correlation coefficient for therelationship between Years Worked and Salary
Pearson_c_c = stats.stats.pearsonr(df_clean['yearsworked'], df_clean['salary'])
print("The Pearson correlation coefficient for our sample is: \n" + str(Pearson_c_c))
