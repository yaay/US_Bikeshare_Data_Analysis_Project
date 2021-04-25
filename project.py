import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Choose the City Name from the Following List: New York City, Chicago or Washington: ").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("Please Entre a Correct City Name from the Cities Listed Above.")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please Entre the Name of the Month You Want to Analyze it's Data from the Following List: All, January, February, March, April, May, June: ").lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("Please Entre the Correct Month from the Months Listed Above.")
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please Entre the Name of the Day You Want to Analyze it's Data from the Following List: All, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday: ").lower()
        if day not in ('all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
            print("Please Entre the Correct Day from the Days Listed Above.")
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
    df['Start Time'] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The Most Common Month Is: ', most_common_month)
    # TO DO: display the most common day of week
    most_common_day= df['day_of_week'].mode()[0]
    print('The Most Common Day is: ', most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The Most Common Hour is: ', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_comman_start_station = df['Start Station'].mode()[0]
    print('The Most Comman Start Station is: ', most_comman_start_station)



    # TO DO: display most commonly used end station
    most_comman_end_station = df['End Station'].mode()[0]
    print('The Most Comman End Station is: ', most_comman_end_station)


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The Total of Trave Time is: ", df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print("The Mean of Travel Time is: ", df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The User Types Count is: ', user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('The Gender Count is', gender)
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')


   # gender = df['Gender'].value_counts()
    #print('The Gender Count is: ', gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print('The Earliest Birth Year is: ', earliest)
        print('The Most Recent Birth Year is: ', most_recent)
        print('The Most Comman Birth Year is: ', most_common)
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    start_loc = 0
    while view_data =='yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
        else:
            break







def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
