#Remove rows with no salary information
database_aggregated.dropna(subset=['med_salary_x'], inplace=True)

#Remove rows with no information about the number of applications
database_aggregated.dropna(subset=['applies'], inplace=True)

#Remove rows with no information about the industry
database_aggregated.dropna(subset=['industry_name'], inplace=True)
