#Cleaning our job postings database

#Convert posting integer date to a timestamp
database_aggregated['original_listed_time'] = pd.to_datetime(database_aggregated['original_listed_time'], unit='ms')

#Convert 'remote_allowed' to string type
database_aggregated['remote_allowed'] = database_aggregated['remote_allowed'].astype(str)
# Replace '1.0' with 'Yes' and fill NaN with 'No'
database_aggregated['remote_allowed'] = database_aggregated['remote_allowed'].replace('1.0', 'Yes')
database_aggregated['remote_allowed'].replace('nan', 'No')

#For missing values, compute the median number of applications based on the common main skill required
median_applies = database_aggregated.groupby('skill_abr')['applies'].transform('median')
database_aggregated['applies'].fillna(median_applies, inplace=True)

#Replace null values with 0 in the 'views' column
database_aggregated['views'].fillna(0, inplace=True)
# Ensure 'views' >= 'applies' where 'views' < 'applies', by replacing 'views' with the corresponding value of 'applies'
database_aggregated.loc[database_aggregated['views'] < database_aggregated['applies'], 'views'] = database_aggregated['applies']

#Set 0 in the 'applies' column where 'views' are 0
database_aggregated.loc[database_aggregated['views'] == 0, 'applies'] = 0

#Replace missing 'application_url' values with 'Not available'
database_aggregated['application_url'].fillna('Not available', inplace=True)

#Convert expiry integer date to a timestamp
database_aggregated['expiry'] = pd.to_datetime(database_aggregated['expiry'], unit='ms')

#Convert closed_time integer date to a timestamp
database_aggregated['closed_time'] = pd.to_datetime(database_aggregated['closed_time'], unit='ms')
# Replace null values with 'Unknown'
database_aggregated['closed_time'].fillna('2023-12-31 23:59:59', inplace=True)

#Replace missing values with "Not specified" in the 'formatted_experience_level' column
database_aggregated['formatted_experience_level'].fillna('Not specified', inplace=True)

#Trim 'skills_desc' to first 50 characters
database_aggregated['skills_desc'] = database_aggregated['skills_desc'].str[:50]
# Replace missing values with 'No information'
database_aggregated['skills_desc'].fillna('No information', inplace=True)

#Convert listing time date to a timestamp
database_aggregated['listed_time'] = pd.to_datetime(database_aggregated['listed_time'], unit='ms')

#Replace missing values with "Not specified" in the 'posting_domain' column
database_aggregated['posting_domain'].fillna('Not specified', inplace=True)

#For the 'sponsored' column, change 0 into "No", 1 into "Yes"
database_aggregated['sponsored'] = database_aggregated['sponsored'].astype(str)
database_aggregated['sponsored'] = database_aggregated['sponsored'].replace('1', 'Yes').replace('0', 'No')

#Change null values into "USD" in the 'currency_x'
database_aggregated['currency_x'].fillna('USD', inplace=True)

#Replace missing values with "OTHER" in the 'compensation_type_x' column
database_aggregated['compensation_type_x'].fillna('OTHER', inplace=True)

#Change null values into "NONE" in the 'skill_abr'
database_aggregated['skill_abr'].fillna('NONE', inplace=True)

# Subset of data with the specified condition
subset_data = database_aggregated.query('industry_id.isna() and med_salary_x.isna()==False')
# Define the values you want to set for the 'industry_id' column
industry_id_values = [39, 11, 13, 56, 44, 32, 3197, 110, 3213]
# Set specific values for the 'industry_id' column in each row
for i, value in zip(subset_data.index, industry_id_values):
    database_aggregated.loc[i, 'industry_id'] = value

# Subset of data with the specified condition
subset_data = database_aggregated.query('industry_name.isna() and med_salary_x.isna()==False')
# Define the values you want to set for the 'industry_name' column
industry_name_values = ['Performing Arts', 'Business Consulting and Services', 'Medical Practices', 'Mining', 'Real Estate', 'Restaurants', 'Building Materials', 'Events Services', 'Renewables & Environment']
# Set specific values for the 'industry_name' column in each row
for i, value in zip(subset_data.index, industry_name_values):
    database_aggregated.loc[i, 'industry_name'] = value

#Set 'Not listed' for the records with company 'name' missing
database_aggregated['name'].fillna('Not listed', inplace=True)

#Set 'No information' for the records with 'description_x' missing
database_aggregated['description_x'].fillna('No information', inplace=True)

#Set 'No information' for the records with 'description_y' missing
database_aggregated['description_y'].fillna('No information', inplace=True)

#Fill null values with 0 in the 'company_size' column
database_aggregated['company_size'].fillna(0, inplace=True)

#Set 0 where values in 'zip_code' and 'address' are null
database_aggregated['zip_code'].fillna(0, inplace=True)
database_aggregated['address'].fillna(0, inplace=True)

#Fill null values with 'Not listed' in the 'url' column
database_aggregated['url'].fillna('Not listed', inplace=True)

#Set 0 where 'type' is null
database_aggregated['type'].fillna(0, inplace=True)

# Subset of data 'state'
database_aggregated['state'].fillna('none', inplace=True)

#Remove rows with location information missing
database_aggregated.dropna(subset=['city'], inplace=True)
