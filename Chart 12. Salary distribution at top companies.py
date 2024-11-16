#Subset data to top 20 companies
largest_companies = database_aggregated.query('company_size==7')
top20_companies = largest_companies['name'].value_counts().head(20)
filtered_data_companies = largest_companies[largest_companies['name'].isin(top20_companies.index)]

plt.figure(figsize=(9, 10))
sns.boxplot(data=filtered_data_companies, x='name', y='unified_med_salary', whis=(0,99), showfliers=True, palette='viridis')
plt.title('Salary distribution at top companies', fontsize=16)
plt.xlabel('Company name', fontsize=12)
plt.xticks(rotation=85)
plt.yticks([0, 100000, 200000, 300000, 400000, 500000], ['0', '100K', '200K', '300K', '400K', '500K'])
plt.ylabel('Annual salary in USD', fontsize=12)
plt.grid(True, which="both", axis='y', ls="--", lw=0.5, c="gray")  # Add grid lines
plt.show()
