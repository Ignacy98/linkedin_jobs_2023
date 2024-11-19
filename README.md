# Winning the Job Hunt: Data-Driven Strategies

## Project Overview
In this project I analyzed over 30,000 job postings on LinkedIn to see the job market trends. Analysis supported by charts digs deeper into general job postings insights, salary wise distributions, and the number of application per job patterns. Recommendations are given for both job seekers and people who are hiring.

## Table of Contents

1. Project Overview
2. Dataset
3. Objectives
4. Technologies Used
5. How to Run the Project
6. Key Insights
7. Next Steps
8. Contributing
9. License

### Dataset
- ***Source***: [LinkedIn Job Postings](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings/data)
- ***Date Range***: January 2023 - December 2023  
- ***Size***: ~142MB (full dataset - 10 tables)

The dataset used in this project contains 10 different tables with certain relationships based on key fields:
- ***job_postings***: each row represents one job posting with date, title, company, salary, description, number of applications etc.;
- ***companies***: more detailed information about each company represented in ```job_postings``` table. The key field is ```company_id```;
- ***job_skills***: information about each job and a skill abbreviation associated with it. The key field is ```job_id```;
- ***benefits***: information about a benefit that applies to a specific job. The key field is ```job_id```;
- ***salaries***: salary information for jobs including range from minimum to maximum, and a base (hourly, monthly, annualy etc.). The key field is ```job_id```;
- ***job_industries***: information about each job and an ```industry_id``` associated with it. The key field is ```job_id```;
- ***employee_counts***: indicates the size of each company represented in the database by employee number. The key field is ```company_id```;
- ***company_industries***: information about a company and an industry name it belongs to. The key field is ```company_id```;
- ***industries***: contains information about ```industry_id```, followed by the name. The key field is ```industry_id```;
- ***skills***: information about a skill abbreviation and name. The key field is ```skill_abr```.

### Objectives

- Identify the most in-demand job roles across various industries.
- Find the highest concentrations of job postings geographically located.
- Compare the median salary across job titles, industries and locations.
- Explore remote and on-site positions in terms of compensation and applicants volume.
- Find out which postings get many applications and which few, and why.

### Technologies Used
- ***Python***:    
  ***Pandas***, ***NumPy*** libraries for appending data and cleaning, performing aggregations and addressing outliers.    
  ***Matplotlib*** and ***Seaborn*** libraries for creating visualizations.
- ***Git & GitHub***: For version control and sharing the project.
