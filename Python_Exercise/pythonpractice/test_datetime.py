'''
Created on 3 Dec 2017

@author: marashid
'''
from _datetime import datetime
from datetime import date, time
from datetime import timedelta
'''
1 <= month <= 12,
1 <= day <= number of days in the given month and year,
0 <= hour < 24,
0 <= minute < 60,
0 <= second < 60,
0 <= microsecond < 1000000,
fold in [0, 1]
'''
def manipulate_using_replace(orig_time):
    print("="*5+"before manipulating using replace"+"="*5)
    print(orig_time.year)
    print(orig_time.month)
    print(orig_time.day)
    print(orig_time.hour)
    print(orig_time.minute)
    print(orig_time.second)
    
    ## let's add 1 hour to orig_time
    new_orig_time = orig_time.replace(hour=orig_time.hour + 1) ## will throw exception if 'new hour' > 23
                                                            ## also, this doesn't alter the orig_time
                                                            ## to add hours surpassing 23 use timedelta function
    print("="*5+"after manipulating using replace"+"="*5)
    print(new_orig_time.year)
    print(new_orig_time.month)
    print(new_orig_time.day)
    print(new_orig_time.hour)
    print(new_orig_time.minute)
    print(new_orig_time.second)

'''
A timedelta object represents a duration, the difference between two dates or times.
ex: timedelta(weeks=40|days=84|hours=23|minutes=50|seconds=600)
'''   
def manipulate_using_timedelta(orig_time):
    print("="*5+"before manipulating using timedelta"+"="*5)
    print(orig_time.year)
    print(orig_time.month)
    print(orig_time.day)
    print(orig_time.hour)
    print(orig_time.minute)
    print(orig_time.second)
    
    ## let's add 23 hours to orig_time
    new_orig_time = orig_time + timedelta(hours=23)
    print("="*5+"after manipulating using timedelta"+"="*5)
    print(new_orig_time.year)
    print(new_orig_time.month)
    print(new_orig_time.day)
    print(new_orig_time.hour)
    print(new_orig_time.minute)
    print(new_orig_time.second)

### source: https://docs.python.org/3.6/library/datetime.html?highlight=datetime#datetime.datetime    
def birthday_example():
    today = date.today()
    print(today.__str__)
    
    print(today == date.fromtimestamp(time.time()))

    my_birthday = date(today.year, 6, 24)
    if my_birthday < today:
        my_birthday = my_birthday.replace(year=today.year + 1)
        print(my_birthday)

    time_to_birthday = abs(my_birthday - today)
    print(time_to_birthday.days)

### source: https://docs.python.org/3.6/library/datetime.html?highlight=datetime#datetime.datetime
def timedelta_example():
    year = timedelta(days=365)
    another_year = timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)  # adds up to 365 days
    print(year.total_seconds())
    print(year == another_year)

    ten_years = 10 * year
    print(ten_years, ten_years.days // 365)

    nine_years = ten_years - year
    print(nine_years, nine_years.days // 365)

    three_years = nine_years // 3;
    print(three_years, three_years.days // 365)
    
    print(abs(three_years - ten_years) == 2 * three_years + year)
    
# manipulate_using_replace(datetime.today())
manipulate_using_timedelta(datetime.today())
# birthday_example()
# timedelta_example()