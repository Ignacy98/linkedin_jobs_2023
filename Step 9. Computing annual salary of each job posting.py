# Additional salaries validation & cleaning
# Define a function to apply the conditions
def update_pay_period(row):
    if row['pay_period_x'] == 'YEARLY':
        if (row['med_salary_x'] < 13500) and (row['med_salary_x'] > 1000):
            return 'MONTHLY'
        elif row['med_salary_x'] <= 1000:
            return 'HOURLY'
    elif row['pay_period_x'] == 'MONTHLY':
        if row['med_salary_x'] >= 13500:
            return 'YEARLY'
        elif row['med_salary_x'] <= 1000:
            return 'HOURLY'
    elif row['pay_period_x'] == 'HOURLY':
        if (row['med_salary_x'] > 1000) and (row['med_salary_x'] < 13500):
            return 'MONTHLY'
        elif row['med_salary_x'] >= 13500:
            return 'YEARLY'
    return row['pay_period_x']  # Return the original value if none of the conditions are met

# Apply the function to each row
database_aggregated['pay_period_x'] = database_aggregated.apply(update_pay_period, axis=1)

# Add a new column with a unified salary
def calculate_unified_med_salary(row):
    if row['pay_period_x'] == 'YEARLY':
        return row['med_salary_x']
    elif row['pay_period_x'] == 'MONTHLY':
        return row['med_salary_x'] * 12
    elif row['pay_period_x'] == 'WEEKLY':
        return row['med_salary_x'] * 52
    elif row['pay_period_x'] == 'HOURLY':
        return row['med_salary_x'] * 40 * 52
    return row['med_salary_x'] * 40 * 52

database_aggregated['unified_med_salary'] = database_aggregated.apply(calculate_unified_med_salary, axis=1)
