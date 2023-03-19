'''The data have been modified to contain some missing values, identified by NaN.
Using pandas should make this exercise easier, in particular for the bonus question.

You should be able to perform all of these operations without using a for loop or other looping construct.'''

'''The data in 'wind.data' has the following format:'''

'''The first three columns are year, month and day. The remaining 12 columns are average windspeeds in knots at 12 locations in Ireland on that day.'''

'''Step 1. Import the necessary libraries'''
import pandas as pd
from datetime import datetime


'''Step 2. Import the dataset from this address'''

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data'
wind_data = pd.read_csv(url, sep='\s+', parse_dates=[[0,1,2]]) # Combine first three columns as dates

wind_data = wind_data.replace(-9999.9, pd.NA)

'''Step 4. Year 2061? Do we really have data from this year? Create a function to fix it and apply it.'''

def fix_year(date):
    if date.year >= 2061:
        return datetime(date.year - 100, date.month, date.day)
    else:
        return date
wind_data['Yr_Mo_Dy'] = wind_data['Yr_Mo_Dy'].apply(fix_year)

'''Step 3. Assign it to a variable called data and replace the first 3 columns by a proper datetime index.'''

wind_data.rename(columns={'Yr_Mo_Dy': 'date'}, inplace=True)

'''Step 5. Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns].'''

wind_data['date'] = pd.to_datetime(wind_data['date'], format='%Y-%m-%d')
# print(wind_data.dtypes)
# print(wind_data)

wind_data.set_index('date', inplace=True)

'''Step 6. Compute how many values are missing for each location over the entire record.'''

# print(wind_data.isna().sum())

'''Step 7. Compute how many non-missing values there are in total.'''

# print(wind_data.count().sum())

'''Step 8. Calculate the mean windspeeds of the windspeeds over all the locations and all the times.
    A single number for the entire dataset.'''

# print(wind_data.mean().mean())

'''Step 9. Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations 
    of the windspeeds at each location over all the days. A different set of numbers for each location.'''

# print(wind_data.agg(['min', 'max', 'mean', 'std']).T)

'''Step 10. Create a DataFrame called day_stats and calculate the min, max and mean windspeed and standard deviations of the 
    windspeeds across all the locations at each day.'''

day_stats = pd.DataFrame()
day_stats['min'] = wind_data.min(axis=1)
day_stats['max'] = wind_data.max(axis=1)
day_stats['mean'] = wind_data.mean(axis=1)
day_stats['std'] = wind_data.std(axis=1)
# print(day_stats)

'''Step 11. Find the average windspeed in January for each location. Treat January 1961 and January 1962 both as January.'''

january_data = wind_data.resample('M').get_group('1961-01-31').append(wind_data.resample('M').get_group('1962-01-31'))
january_means = january_data.mean()
# print(january_means)

'''Step 12. Downsample the record to a yearly frequency for each location.'''
yearly_data = wind_data.resample('Y').mean()
# print(yearly_data)

'''Step 13. Downsample the record to a monthly frequency for each location.'''
monthly_data = wind_data.resample('M').mean()
# print(monthly_data)

'''Step 14. Downsample the record to a weekly frequency for each location.'''
weekly_data = wind_data.resample('W').mean()
# print(weekly_data)

'''Step 15. Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations 
    for each week (assume that the first week starts on January 2 1961) for the first 52 weeks.'''

weekly_data_1961 = wind_data.resample('W', label='left', closed='left').first().head(52)
weekly_stats = weekly_data.agg(['min', 'max', 'mean', 'std'], axis=1)
print(weekly_stats)