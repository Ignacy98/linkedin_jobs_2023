# The average hourly salary based on skills
database_aggregated_hourly = database_aggregated.query('pay_period_x=="HOURLY"')

skill_mean_salary_h = database_aggregated_hourly.groupby('skill_abr')['med_salary_x'].mean().reset_index()
skill_mean_salary_h.rename(columns={'med_salary_x': 'med_salary_hourly'}, inplace=True)

skill_count_salary_h = database_aggregated_hourly.groupby('skill_abr')['med_salary_x'].count().reset_index()
skill_count_salary_h.rename(columns={'med_salary_x': 'count_hourly'}, inplace=True)
    
# The average weekly salary based on skills
database_aggregated_weekly = database_aggregated.query('pay_period_x=="WEEKLY"')

skill_mean_salary_w = database_aggregated_weekly.groupby('skill_abr')['med_salary_x'].mean().reset_index()
skill_mean_salary_w.rename(columns={'med_salary_x': 'med_salary_weekly'}, inplace=True)

skill_count_salary_w = database_aggregated_weekly.groupby('skill_abr')['med_salary_x'].count().reset_index()
skill_count_salary_w.rename(columns={'med_salary_x': 'count_weekly'}, inplace=True)
    
# The average monthly salary based on skills
database_aggregated_monthly = database_aggregated.query('pay_period_x=="MONTHLY"')

skill_mean_salary_m = database_aggregated_monthly.groupby('skill_abr')['med_salary_x'].mean().reset_index()
skill_mean_salary_m.rename(columns={'med_salary_x': 'med_salary_monthly'}, inplace=True)

skill_count_salary_m = database_aggregated_monthly.groupby('skill_abr')['med_salary_x'].count().reset_index()
skill_count_salary_m.rename(columns={'med_salary_x': 'count_monthly'}, inplace=True)

# The average yearly salary based on skills
database_aggregated_yearly = database_aggregated.query('pay_period_x=="YEARLY"')

skill_mean_salary_y = database_aggregated_yearly.groupby('skill_abr')['med_salary_x'].mean().reset_index()
skill_mean_salary_y.rename(columns={'med_salary_x': 'med_salary_yearly'}, inplace=True)

skill_count_salary_y = database_aggregated_yearly.groupby('skill_abr')['med_salary_x'].count().reset_index()
skill_count_salary_y.rename(columns={'med_salary_x': 'count_yearly'}, inplace=True)

# Merge all skill mean salaries and their correspondive counts, together will skill names
merged_data = skill_mean_salary_h.merge(skill_count_salary_h, on='skill_abr', how='left').merge(skill_mean_salary_w, on='skill_abr', how='left').merge(skill_count_salary_w, on='skill_abr', how='left').merge(skill_mean_salary_m, on='skill_abr', how='left').merge(skill_count_salary_m, on='skill_abr', how='left').merge(skill_mean_salary_y, on='skill_abr', how='left').merge(skill_count_salary_y, on='skill_abr', how='left').merge(skills, on='skill_abr', how='left')
indexnone = merged_data[merged_data['skill_abr']=='NONE'].index
merged_data.drop(indexnone, inplace=True)
merged_data.fillna(0, inplace=True)


#Add a new column with a total count
merged_data['total_count'] = merged_data['count_hourly'] + merged_data['count_weekly'] + merged_data['count_monthly'] + merged_data['count_yearly']

#Add a new column with an overall mean salary weighted
merged_data['med_salary_overall'] = round(((merged_data['med_salary_hourly']*40*52) * merged_data['count_hourly'] + (merged_data['med_salary_weekly']*52) * merged_data['count_weekly'] + (merged_data['med_salary_monthly']*12) * merged_data['count_monthly'] + merged_data['med_salary_yearly'] * merged_data['count_yearly']) / merged_data['total_count'],2)
