import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
# sets list of available answers to check input against
months = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6}
reverse_months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
days_of_week = {0: "sunday", 1: "monday", 2: "tuesday", 3: "wednesday", 4: "thursday", 5: "friday", 6: "saturday"}

def month_data():
    month_name = ''
    month = ''
    months = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6}
    while True:
        print('-' * 40)
        y = input("Please enter a month. (E.g. January)\nData is only available for January-June.\n")
        if y.lower() in months.keys():
            month = months[y.lower()]
            month_name = y.title()
            break
        else:
            print("\nMonth not recognized.\n")
            continue
    return month

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no month filter
        (str) day - name of the day of week to filter by, or "none" to apply no day filter
    """
    # Prints header
    print('\n')
    print('Hello! Let\'s explore some US bike sharing data!')
    print('-' * 40)
    print('\n')

    # gets user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    month = ''
    day = ''
    day_name = ''
    month_name = ''
    while True:
        print('Data is available for Chicago, New York City, and Washington.')
        x = input("Please enter a city.\n")
        if x.lower() in CITY_DATA.keys():
            city = x
            break
        else:
            print("\nCity not recognized.\n")
            continue

    # spacing
    print('\n' * 2)
    print('-' * 40)

    # gets user to input desire to filter data
    print("Data is available for January-June 2017.\nYou can choose to see all data, or filter the data by a specific "
          "month and/or the day of the week.\n")
    while True:
        x = input("Would you like to filter the data?\nType yes or no.\n")
        filter_choice = ''
        if x.lower() == 'yes':
            filter_choice = x
            break
        elif x.lower() == 'no':
            filter_choice = x
            break
        else:
            print("\nFilter choice not recognized.\n")
            continue

    # spacing
    print('\n' * 2)

    # No filter assignments
    if filter_choice.lower() == 'no':
        month = "none"
        day = "none"

    # secondary filtering
    elif filter_choice.lower() == 'yes':
        # gets user to input degree of data filtering
        while True:
            print('-' * 40)
            x = input('Would you like to filter data by month, day, or both?\n')
            second_filter = ''
            if x.lower() == 'month':
                month = month_data()
                month_name = reverse_months[month]
                day = 'none'
                second_filter = 'month'
                break
            elif x.lower() == 'day':
                second_filter = x
                month = 'none'
                break
            elif x.lower() == 'both':
                second_filter = x
                break
            else:
                print("\nChoice not recognized\n")
                continue

        # spacing
        print('\n' * 2)

        # gets user input when only filtering for month
        if second_filter == 'month':
            # month filter
            # get user input for month (all, january, february, ... , june)
            print('Getting data')

        # gets user input when only filtering for day
        elif second_filter == 'day':
            # day filter
            # get user input for day of week (all, monday, tuesday, ... sunday)
            while True:
                print('-' * 40)
                try:
                    z = int(input("Please enter the day of the week, in integer form, for which you would like data."
                                  "\n(E.g. 0 for Sunday, 1 for Monday, ...)\n"))
                    if int(z) in days_of_week.keys():
                        day = z
                        month = 'none'
                        day_name = days_of_week[z]
                        break
                    else:
                        print("\nDay not recognized.\n")
                        continue
                except ValueError:
                    print('\nDay not recognized.')
                    print('\n')

        # gets user input when filtering for both month and day
        else:
            # month filter
            # get user input for month (all, january, february, ... , june)
            month = month_data()
            month_name = reverse_months[month]

            # spacing
            print('\n')

            # day filter
            # get user input for day of week (all, monday, tuesday, ... sunday)
            while True:
                print('-' * 40)
                try:
                    z = int(input("Please enter the day of the week, in integer form, for which you would like data."
                                  "\n(E.g. 0 for Sunday, 1 for Monday, ...)\n"))
                    if int(z) in days_of_week.keys():
                        day = z
                        month = 'none'
                        day_name = days_of_week[z]
                        break
                    else:
                        print("\nDay not recognized.\n")
                        continue
                except ValueError:
                    print('\nDay not recognized.')
                    print('\n')

    # spacing
    print('\n')
    print('-' * 40)

    # returns final statement of filters
    print('\n' * 2)
    # no filters
    if month == 'none' and day == 'none':
        print('Thank you.\n\nHere is all the data available for {}'.format(city.title()))
    # day filter statement
    elif month == 'none' and day != 'none':
        print('Thank you.\n\nHere is all the data available for every {} in {}.'.format(day_name, city.title()))
    # month filter statement
    elif month != 'none' and day == 'none':
        print('Thank you.\n\nHere is all the data available for {} in {}.'.format(month_name, city.title()))
    # both filter statement
    else:
        print('Thank you.\n\nHere is all the data available for every {} in {} for {}.'.format(day_name, month_name,
                                                                                               city.title()))
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no month filter
        (str) day - name of the day of week to filter by, or "none" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    with open(CITY_DATA[city], 'r') as f:
        file = pd.read_csv(f)
        file['Start Time'] = pd.to_datetime(file['Start Time'])
        file['End Time'] = pd.to_datetime(file['End Time'])
        file['month'] = file['Start Time'].dt.month
        file['dow'] = file['Start Time'].dt.dayofweek
        file['Trip Duration'] = pd.to_numeric(file['Trip Duration'])
        # no filters chosen
        if month == 'none' and day == 'none':
            df = file
        # filters by day
        elif month == 'none' and day != 'none':
            file = file[file['dow'] == day]
            df = file
        # filters by month
        elif month != 'none' and day == 'none':
            file = file[file['month'] == month]
            df = file
        # filters by day and month
        else:
            file = file[file['dow'] == day]
            file = file[file['month'] == month]
            df = file
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == 'none':
        max_month = df.month.mode()
        print('The month with the most rides is', reverse_months[max_month[0]])

    # display the most common day of week
    if day == 'none':
        max_day = df.dow.mode()
        print('The day with the most rides is', days_of_week[max_day[0]].title())

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df.hour.mode()
    if common_hour[0] < 10:
        print('The most common hour is 0' + str(common_hour[0]) + ':00')
    else:
        print('The most common hour is ' + str(common_hour[0]) + ':00')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    fav_start = df['Start Station'].mode()
    print('The most popular starting station - ' + fav_start[0])

    # display most commonly used end station
    fav_end = df['End Station'].mode()
    print('The most popular ending station - ' + fav_end[0])
    print('\n')
    # display most frequent combination of start station and end station trip
    df['Round Trip'] = df['Start Station'] + ' : ' + df['End Station']
    top_combo = df['Round Trip'].mode()
    top_combo = top_combo[0].split(' : ')
    print('The most popular starting/ending station combination:\nStart Station - ' + top_combo[
        0] + '\nEnd Station - ' + top_combo[1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_dur = int(sum(df['Trip Duration']))
    if total_dur >= 86400:
        day, rem = total_dur // 86400, total_dur % 86400
        hr, rem = rem // 3600, rem % 3600
        minutes, sec = rem // 60, rem % 60
        print('Bikes were rented for a total time of {} days, {} hours, {} minutes, and {} seconds.'.format(day, hr,
                                                                                                            minutes,
                                                                                                            sec))

    elif total_dur >= 3600:
        hr, rem = total_dur // 3600, total_dur % 3600
        minutes, sec = rem // 60, rem % 60
        print('Bikes were rented for a total time of {} hours, {} minutes, and {} seconds.'.format(hr, minutes, sec))
    elif total_dur >= 60:
        minutes, sec = total_dur // 60, total_dur % 60
        print('Bikes were rented for a total time of {} minutes, and {} seconds.'.format(minutes, sec))
    else:
        sec = total_dur
        print('Bikes were rented for a total time of {} seconds.'.format(sec))

    # display mean travel time
    total_trips = df['Trip Duration'].count()
    ave_dur = int(total_dur / total_trips)
    if ave_dur >= 86400:
        ave_day, rem = ave_dur // 86400, ave_dur % 86400
        ave_hr, rem = rem // 3600, rem % 3600
        ave_min, ave_sec = rem // 60, rem % 60
        print('The average length of a rental was {} days, {} hours, {} minutes, and {} seconds.'.format(ave_day,
                                                                                                         ave_hr,
                                                                                                         ave_min,
                                                                                                         ave_sec))

    elif ave_dur >= 3600:
        ave_hr, rem = ave_dur // 3600, ave_dur % 3600
        ave_min, ave_sec = rem // 60, rem % 60
        print('The average length of a rental was {} hours, {} minutes, and {} seconds.'.format(ave_hr, ave_min,
                                                                                                ave_sec))
    elif ave_dur >= 60:
        ave_min, ave_sec = ave_dur // 60, ave_dur % 60
        print('The average length of a rental was {} minutes, and {} seconds.'.format(ave_min, ave_sec))
    else:
        ave_sec = ave_dur
        print('The average length of a rental was {} seconds.'.format(ave_sec))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bike share users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df.groupby('User Type')['Start Time'].count()
    print('Breakdown of user types:')
    for i in range(len(user_types)):
        print(user_types.index[i], '-', user_types[i])

    print('\n')

    # Display counts of gender
    print('Distribution of rider sexes:')
    if city != 'washington':
        gen_df = df.groupby('Gender')['Start Time'].count()
        for i in range(len(gen_df)):
            print(gen_df.index[i], '-', gen_df[i])

        print('\n')
    else:
        print('There is no gender data available for Washington.\n')

    # Display earliest, most recent, and most common year of birth
    # oldest rider
    print('Distribution of rider birth years:')
    if city != 'washington':
        print('The oldest rider to rent a bike was born in {}.'.format(int(min(df['Birth Year']))))
        print('The youngest rider to rent a bike was born in {}.'.format(int(max(df['Birth Year']))))
        print('The highest number of riders were born in {}.'.format(int(df['Birth Year'].mode())))
    else:
        print('There is no birth year data available for Washington.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def see_data(df):
    while True:
        see_data_ans = input('\nWould you like to see a sample of the raw data? Enter yes or no.\n')
        if see_data_ans.lower() == 'yes':
            print('\n')
            print(df.head())
            print('\n')
            break
        elif see_data_ans.lower() == 'no':
            break
        else:
            print('Input not recognized.')


def restart():
    while True:
        restart_ans = input('\nWould you like to restart the program? Enter yes or no.\n')
        if restart_ans.lower() == 'yes':
            answer = 'yes'
            return answer
        elif restart_ans.lower() == 'no':
            answer = 'no'
            return answer
        else:
            print('Input not recognized.')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        see_data(df)
        if restart() != 'yes':
            break


if __name__ == "__main__":
    main()
