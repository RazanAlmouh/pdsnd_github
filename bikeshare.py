import time
import pandas as pd
import numpy as np

CITY_DATA = {'Chicago': 'chicago.csv',
             'New York City': 'new_york_city.csv',
             'Washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHi! Let\'s explore US bike-share dataset!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
        city = input('\nWhich city would you like to filter by? New York City, Chicago or Washington? \n').title()
        if city not in CITY_DATA.keys():
            print('Sorry, I can\'t catch this. Try again please.')
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input('\nWhich month would you like to filter by? January, February, March, April, May, June or enter \'all\' if you do not have any preference?\n').title()
        if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
            print('Sorry, I can\'t catch that. Try again please.')
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('\nAre you looking for a particular day? If so, enter the day as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or enter \'all\' if you do not have any preference.\n' ).title()
        if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
            print('Sorry, I can\'t catch that. Try again.')
            continue
        else:
            break

    print('-'*40)

    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.day)

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'All':
        # use the index of the days list to get the corresponding int
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        day = days.index(day) + 1

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time() 
   # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('the most common month:', most_common_month)
    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('the most common day of week:',most_common_day_of_week)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('the most common hour:',most_common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
     
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station :", most_common_start_station)
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station :",most_common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    frequent_stations = df.groupby(['Start Station'])['End Station'].value_counts().mode
    print("Most frequent start and end stations:", frequent_stations)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('the total travel time:',total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('the mean travel time:',mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user = df["User Type"].value_counts()
    print("Counts Of User Types:\n{}".format(counts_of_user))
    # TO DO: Display counts of gender
    if "Gender" in df:
        counts_of_gender= df["Gender"].value_counts()
        print("\nCounts Of Gender:\n{}".format(counts_of_gender))

    else:
        print("\nThere is no column for 'Gender' data")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest=int(df['Birth Year'].min())
        recent=int(df['Birth Year'].max())
        common=int(df['Birth Year'].mode())
        print("Oldest subscriber year of birth is: ",earliest)
        print("Youngest subscriber year of birth is: ",recent)
        print("Most common subscriber year of birth is: ",common)
    except:
        print('\nSorry, Whasington has no "year of birth" informations')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(data):
    choice = input('\nDo you want to see the first 5 rows of data? YES OR NO \n').lower()
    records = 0
    while (choice != 'no'):
        records += 5
        print(data.head(records))
        choice = input('\nWould you like to see five more rows? YES OR NO\n').lower()
        print('-'*30) 
        
def main():
    while True:
        city, month, day = get_filters()  
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
    main()