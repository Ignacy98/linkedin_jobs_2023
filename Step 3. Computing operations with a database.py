#Computing operations with a database

# Filter the DataFrame to include only rows with 'pay_period_x' equal to 'YEARLY' or null
yearly_data = database_aggregated.query('(pay_period_x=="YEARLY" or pay_period_x.isna()) and max_salary_x.isna()')
# Calculate the median by industry for yearly data
med_by_industry_null_yearly = yearly_data.groupby('industry_id')['med_salary_x'].transform('median')
# Replace missing values in 'med_salary_x' with the calculated median values for yearly data
database_aggregated.loc[yearly_data.index, 'med_salary_x'] = med_by_industry_null_yearly

# Filter the DataFrame to include only rows with 'pay_period_x' equal to 'HOURLY'
hourly_data = database_aggregated.query('pay_period_x=="HOURLY" and max_salary_x.isna()')
# Calculate the median by industry for hourly data
med_by_industry_hourly = hourly_data.groupby('industry_id')['med_salary_x'].transform('median')
# Replace missing values in 'med_salary_x' with the calculated median values for hourly data
database_aggregated.loc[hourly_data.index, 'med_salary_x'] = med_by_industry_hourly

# Filter the DataFrame to include only rows with 'pay_period_x' equal to 'MONTHLY'
monthly_data = database_aggregated.query('pay_period_x=="MONTHLY" and max_salary_x.isna()')
# Calculate the median by industry for monthly data
med_by_industry_monthly = monthly_data.groupby('industry_id')['med_salary_x'].transform('median')
# Replace missing values in 'med_salary_x' with the calculated median values for monthly data
database_aggregated.loc[monthly_data.index, 'med_salary_x'] = med_by_industry_monthly

# Fill null values in 'max_salary_x' and 'min_salary_x' where 'med_salary_x' is not null
database_aggregated['max_salary_x'].fillna(database_aggregated['med_salary_x'] * 1.10, inplace=True)
database_aggregated['min_salary_x'].fillna(database_aggregated['med_salary_x'] * 0.90, inplace=True)
# Recalculate 'med_salary_x' where both 'max_salary_x' and 'min_salary_x' are not null
database_aggregated['med_salary_x'] = database_aggregated[['max_salary_x', 'min_salary_x']].mean(axis=1)

#For pay period information, first replace null values where salary is mentioned HOURLY
# Define the condition
condition = (database_aggregated['pay_period_x'].isna()) & (database_aggregated['med_salary_x'] < 10000)
# Fill null values in 'pay_period_x' with 'HOURLY' where the condition is True
database_aggregated.loc[condition, 'pay_period_x'] = 'HOURLY'
#Then replace remaining null values with YEARLY
database_aggregated['pay_period_x'].fillna('YEARLY', inplace=True)
