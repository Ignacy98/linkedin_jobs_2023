remote_applies = database_aggregated.groupby('remote_allowed')['applies'].mean().reset_index()

plt.figure(figsize=(8, 4))
sns.barplot(x='remote_allowed', y='applies', data=remote_applies, palette='viridis', width=0.5)
plt.title('Remote and on-site jobs: number of applications', fontsize=16)
plt.xticks(['Yes', 'nan'], ['Yes', 'No'], rotation=80)
plt.xlabel('Remote allowed', fontsize=12)
plt.ylabel('Average number of applications', fontsize=12)
plt.grid(True, which="both", axis='y', ls="--", lw=0.5, c="gray")  # Add grid lines
plt.show()
