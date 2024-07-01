import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men_total = df[df['sex'] == 'Male']
    average_age_men = men_total['age'].mean().round(1)

    #clean data
    def cleaned_salary(df):
        def clean_salary(salary):
            if salary == '<=50K':
                return 50000
            elif salary == '<50K':
                return 49999
            elif salary == '>50k':
                return 50001
            elif salary == '>50K':
                return 50001    
            else:
                return salary

        df['salary'] = df['salary'].apply(clean_salary)

        return df

    df = cleaned_salary(df)
    
    # What is the percentage of people who have a Bachelor's degree?
    bachelors_people = ['Bachelors']
    total_Certificates = df['education'].value_counts()
    bachelors_people_total = df[df['education'].isin(bachelors_people)].value_counts()
    percentage_bachelors = round(((sum(bachelors_people_total) / sum(total_Certificates))*100),1)



    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advanced_education = ['Bachelors','Masters','Doctorate']
    advanced_educated_rich = df[(df['education'].isin(advanced_education)) & (df['salary'] > 50000)]
    advanced_educated_poor = df[(df['education'].isin(advanced_education)) & (df['salary'] <= 50000)]
    advanced_educatedpoor_total = advanced_educated_poor['education'].value_counts()
    advanced_educated_number = df[df['education'].isin(advanced_education)]
    advanced_education_total = advanced_educated_number['education'].value_counts()
    
    # What percentage of people without advanced education make more than 50K?
    without_advanced_edu = df[(~df['education'].isin(advanced_education)) & (df['salary'] > 50000)]
    without_adv_edu_num = df[(~df['education'].isin(advanced_education))]
    without_adv_edu_total = without_adv_edu_num['education'].value_counts()


    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = advanced_educated_rich['education'].value_counts()
    lower_education = without_advanced_edu['education'].value_counts()

    # percentage with salary >50K
    higher_education_rich = round(((sum(higher_education) / sum(advanced_education_total))*100),1)
    lower_education_rich = round(((sum(lower_education) / sum(without_adv_edu_total))*100),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[(df['hours-per-week'] == min_work_hours)  & (df['salary'] > 50000)]
    min_total_num = df[df['hours-per-week'] == min_work_hours]
    min_workers_num_total = min_total_num['hours-per-week'].value_counts()
    num_min_workers = min_workers['hours-per-week'].value_counts()

    rich_percentage = (sum(num_min_workers) / sum(min_workers_num_total))*100

    # What country has the highest percentage of people that earn >50K?
    rich_people_total = df[df['salary'] > 50000]
    rich_country = rich_people_total['native-country'].value_counts()
    countries_populations_total = df['native-country'].value_counts()
    percentage_rich_people = round(((rich_country / countries_populations_total)*100),1)
    highest_earning_country = percentage_rich_people.idxmax()


    highest_earning_country_percentage = percentage_rich_people.max()

    # Identify the most popular occupation for those who earn >50K in India.
    india_stats = df[(df['native-country'] == 'India') & (df['salary'] > 50000)]
    india_stats_total = india_stats['occupation'].value_counts()
    top_IN_occupation = india_stats_total.idxmax() 

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)


    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
calculate_demographic_data()