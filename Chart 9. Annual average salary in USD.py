mean_salaries_sorted = merged_data.sort_values('med_salary_overall', ascending=False)

plt.figure(figsize=(9, 8))
sns.barplot(x='skill_name', y='med_salary_overall', data=mean_salaries_sorted, palette='viridis')
plt.title('Average annual salary by occupation', fontsize=16)
plt.xlabel('Occupation', fontsize=12)
plt.xticks(rotation=85)
plt.ylabel('Annual average salary in USD', fontsize=12)
plt.grid(True, which="both", axis='y', ls="--", lw=0.5, c="gray")  # Add grid lines
plt.show()
