#Drop duplicate job records
database_aggregated.drop_duplicates(subset=['job_id'], inplace=True)
#Remove rows with company information missing
database_aggregated.dropna(subset=['company_id'], inplace=True)
