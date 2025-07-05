import pandas as pd

# float to datetime conversion
def fractional_year_to_datetime(fractional_year):
    year = int(fractional_year)
    fraction = fractional_year - year
    
    if year % 4 == 0:
        # Leap year adjustment
        days = int(fraction * 366)
    else:
        days = int(fraction * 365)
        
    base_date = pd.to_datetime(f'{year}-01-01')
    return base_date + pd.Timedelta(days=days)

# Apply the conversion
# df['Transaction date'] = df['Transaction date'].apply(fractional_year_to_datetime)
# df