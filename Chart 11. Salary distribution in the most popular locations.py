#Subset data to top 20 locaions
top20_locations = database_aggregated['location'].value_counts().head(21)
top20_locations_notus = top20_locations.iloc[1:]
filtered_data_locations = database_aggregated[database_aggregated['location'].isin(top20_locations_notus.index)]

plt.figure(figsize=(9, 10))
sns.boxplot(data=filtered_data_locations, x='location', y='unified_med_salary', whis=(0,99), showfliers=True, palette='viridis')
plt.title('Salary distribution in the most popular locations', fontsize=16)
plt.xlabel('Location', fontsize=12)
plt.xticks(rotation=85)
plt.yticks([0, 100000, 200000, 300000, 400000, 500000, 600000], ['0', '100K', '200K', '300K', '400K', '500K', '600K'])
plt.ylabel('Annual salary in USD', fontsize=12)
plt.grid(True, which="both", axis='y', ls="--", lw=0.5, c="gray")  # Add grid lines
plt.show()
