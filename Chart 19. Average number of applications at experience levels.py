applies_experience = database_aggregated.groupby('formatted_experience_level')['applies'].mean().reset_index()

plt.figure(figsize=(8, 4))
sns.barplot(x='formatted_experience_level', y='applies', data=applies_experience, palette='viridis', width=0.5)
plt.title('Average number of applications at experience levels', fontsize=16)
plt.xticks(rotation=80)
plt.xlabel('Experience level', fontsize=12)
plt.ylabel('Average number of applications', fontsize=12)
plt.grid(True, which="both", axis='y', ls="--", lw=0.5, c="gray")  # Add grid lines
plt.show()
