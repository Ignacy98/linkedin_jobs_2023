#Appending data altogether based on key fields to the main job openings table
database_plus_job_id = database_raw.merge(job_skills, on='job_id', how='left').merge(salaries, on='job_id', how='left').merge(job_industries, on='job_id', how='left')
database_plus_industries = database_plus_job_id.merge(industries, on='industry_id', how='left')
database_plus_companies = database_plus_industries.merge(companies, on='company_id', how='left')
database_aggregated = database_plus_companies.merge(benefits_pivoted, on='job_id',how='left')
database_aggregated.head()
