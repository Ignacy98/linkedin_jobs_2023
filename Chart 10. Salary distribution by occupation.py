#Get the skills description
unified_med_salary_skill = database_aggregated.merge(skills, on='skill_abr', how='left')

skill_name_sorted = ['Legal', 'Advertising', 'Product Management', 'Engineering', 'Information Technology', 'Project Management', 'Strategy/Planning', 'Finance', 'Supply Chain', 'Science', 'Consulting', 'Writing/Editing', 'Business Development', 'Research', 'Design', 'Art/Creative', 'Accounting/Auditing', 'Quality Assurance', 'Human Resources', 'Sales', 'Health Care Provider', 'Purchasing', 'General Business', 'Analyst', 'Marketing', 'Manufacturing', 'Public Relations', 'Administrative', 'Other', 'Management', 'Distribution', 'Production', 'Education', 'Training', 'Customer Service']

# Define the custom order as a categorical data type
custom_order = pd.CategoricalDtype(categories=skill_name_sorted, ordered=True)

# Convert the 'skill_name' column to the categorical data type with the custom order
unified_med_salary_skill['skill_name'] = unified_med_salary_skill['skill_name'].astype(custom_order)

# Sort the DataFrame by the 'skill_name' column
unified_med_salary_skill_sorted = unified_med_salary_skill.sort_values('skill_name')

plt.figure(figsize=(9, 10))
sns.boxplot(data=unified_med_salary_skill_sorted, x='skill_name', y='unified_med_salary', whis=(0,99), showfliers=True, palette='viridis')
plt.title('Salary distribution by occupation', fontsize=16)
plt.xlabel('Occupation', fontsize=12)
plt.xticks(rotation=85)
plt.yticks([0, 50000, 100000, 200000, 300000, 400000, 500000, 1000000], ['0', '50K', '100K', '200K', '300K', '400K', '500K', '1M'])
plt.ylabel('Annual salary in USD', fontsize=12)
plt.ylim(top=1100000)
plt.grid(True, which="both", axis='y', ls="--", lw=0.5, c="gray")  # Add grid lines
plt.show()
