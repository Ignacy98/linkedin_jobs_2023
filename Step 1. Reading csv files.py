import pandas as pd
import numpy as np
database_raw = pd.read_csv("job_postings.csv")
companies = pd.read_csv("companies.csv", index_col=0)
job_skills = pd.read_csv("job_skills.csv", index_col=0)
job_industries = pd.read_csv("job_industries.csv", index_col=0)
company_industries = pd.read_csv("company_industries.csv", index_col=0)
employee_counts = pd.read_csv("employee_counts.csv", index_col=0)
salaries = pd.read_csv("salaries.csv", index_col=0)
benefits = pd.read_csv("benefits.csv", index_col=0)
benefits_pivoted = benefits.pivot_table(values='type', index='job_id', aggfunc=np.count_nonzero)
industries = pd.read_csv("industries.csv", index_col=0)
skills = pd.read_csv("skills.csv", index_col=0)
