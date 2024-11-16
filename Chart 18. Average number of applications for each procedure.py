applies_procedure = database_aggregated.groupby('application_type')['applies'].mean().reset_index()

plt.figure(figsize=(8, 4))
sns.barplot(x='application_type', y='applies', data=applies_procedure, palette='viridis', width=0.5)
plt.title('Average number of applications for each procedure', fontsize=16)
plt.xticks(rotation=80)
plt.xlabel('Procedure', fontsize=12)
plt.ylabel('Average number of applications', fontsize=12)
plt.grid(True, which="both", axis='y', ls="--", lw=0.5, c="gray")  # Add grid lines
plt.show()
