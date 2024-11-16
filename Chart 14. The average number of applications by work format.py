applies_work_type = database_aggregated.groupby('formatted_work_type')['applies'].mean()

plt.figure(figsize=(9, 5))
sns.barplot(x=applies_work_type.index, y=applies_work_type.values, palette='viridis')
plt.title('The average number of applications by work format', fontsize=16)
plt.xlabel('Work format', fontsize=12)
plt.xticks(rotation=80)
plt.ylabel('Average number of applications', fontsize=12)
plt.grid(True, which="both", axis='y', ls="--", lw=0.5, c="gray")  # Add grid lines
plt.show()
