#Subset data to top 20 locaions
#filtered_data_locations

applies_location = database_aggregated.groupby('location')['applies'].mean().reset_index()
applies_location_sorted = applies_location.sort_values('applies', ascending=False)

plt.figure(figsize=(9, 7))
sns.barplot(x='location', y='applies', data=filtered_data_locations, ci=None, palette='viridis')
plt.title('Top 20 location vs number of applications', fontsize=16)
plt.xlabel('Location', fontsize=12)
plt.xticks(rotation=90)
plt.ylabel('Average number of applications', fontsize=12)
plt.grid(True, which="both", axis='y', ls="--", lw=0.5, c="gray")  # Add grid lines
plt.show()
