#Remove columns
database_aggregated.drop(columns=['scraped'], inplace=True)
database_aggregated.drop(columns=['max_salary_y'], inplace=True)
database_aggregated.drop(columns=['med_salary_y'], inplace=True)
database_aggregated.drop(columns=['min_salary_y'], inplace=True)
database_aggregated.drop(columns=['pay_period_y'], inplace=True)
database_aggregated.drop(columns=['currency_y'], inplace=True)
database_aggregated.drop(columns=['compensation_type_y'], inplace=True)
#Change column's name
database_aggregated.rename(columns = {'type':'no_of_benefits'}, inplace = True)
