applies_company_size = database_aggregated.groupby('company_size')['applies'].mean()

# Map the values in company_size_counts index to their corresponding descriptions
applies_company_size.index = applies_company_size.index.map(company_size_description)

applies_company_size = applies_company_size.reset_index()
applies_company_size.columns = ['company_size', 'applies']

plt.figure(figsize=(8, 4))
sns.barplot(x='company_size', y='applies', data=applies_company_size, palette='viridis', width=0.5)
plt.title('Average number of applications depending on a company size', fontsize=16)
plt.xticks(rotation=80)
plt.xlabel('Company size', fontsize=12)
plt.ylabel('Average number of applications', fontsize=12)
plt.grid(True, which="both", axis='y', ls="--", lw=0.5, c="gray")  # Add grid lines
plt.show()
