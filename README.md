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

### How to Run the Project
#### Prerequisites
- Python 3.x installed with Pandas and Matplotlib libraries.
- Python IDLE (version 3.x).
- SQL environment (e.g., SQLite, PostgreSQL).
  
#### Steps
1. Clone the repository:
```
git clone https://github.com/Ignacy98/linkedin_jobs_2023.git
cd linkedin_jobs_2023
```
2. Data Setup:
   - The dataset can be downloaded from [this external link](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings/data);
   - Place the dataset in the ```data/``` directory of the repository.
3. Run .py files:
   - Execute the Python files (end with .py) starting from ```Step 1...``` to clean and prepare data for analysis, in the ```main/``` directory of the repository.
   - Execute the Python files (end with .py) having ```Chart...``` in the title, better in the respective order.
4. View Visualizations:
   - Alternatively, you can view visualisations by opening ```.png``` files having ```Chart...``` in the title.

### Key Insights
#### General observations

- ***Sales being in-demand industry***: 4 out of 5 most common job titles involve various roles in Sales;
- ***Unfriendly job market for starters***: just 25% of jobs are suitable for recent graduates and career changers (incl. internships and entry-level positions);
- ***Small companies post few jobs***: companies with 50 employees or less posted only 11% of total number of jobs;
- ***Most of jobs struggle to get enough applicants***: roughly half of all jobs received 3 or fewer applications through LinkedIn, 75% - 8 or fewer candidates applied;
- ***City with the highest number of open positions***: New York City Metropolitan Area had 1,042 openings (3.37% of jobs);

#### Salaries

- ***Best-paid occupations***: Legal, Advertising, and Product Management, ranging from 149,800 to 127,400 USD per year, are the best-paid occupations on average;
- ***The industry with highest paid jobs***: the top 5 highest paid jobs all come from the tech industry;
- ***Locations with the highest median salary***: San Francisco median salary of 125,000 USD is the highest, followed by New York City (112,500 USD) and Seattle (109,872.5 USD);

#### Competition level

- ***Bigger compensation leads to more applicants***: in big locations, the average number of applications is associated with the median salary;
- ***Locations with the highest competition***: jobs located in New York City and San Francisco get 28 and 20 applications on average, respectively;
- ***Remote vs on-site jobs***: remote jobs attract 5 times as many applicants as on-site positions;
- ***Complex vs simple application procedure***: counterintuitively, a complex application procedure leads to twice as many candidates as simple applications;
- ***Associate positions have the highest competition***: on average, the one would need to compete with 15 other candidates for an associate-level job;

### Next Steps

- Analyze the relationship between the number of times a posting has been viewed (views) and applications it received. Aggregate by occupation and industry.
- Investigate how the job market changes throughout the year by analyzing the most popular titles and the number of applicants in different months.
- Find out the average time between publishing and closing the job posting. Aggregate by industry and experience level.

### Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

### License
This project is licensed under the Data License Agreement. Click [here](https://creativecommons.org/licenses/by-sa/4.0/) to see details.
