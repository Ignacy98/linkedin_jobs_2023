top10_locations = database_aggregated['location'].value_counts().head(11)
top10_locations_notus = top10_locations.iloc[1:]
plt.figure(figsize=(10, 6))
sns.barplot(x=top10_locations_notus.values, y=top10_locations_notus.index, palette='viridis')
plt.title('Top 10 Popular Locations', fontsize=16)
plt.xlabel('Count', fontsize=12)
plt.ylabel('Location', fontsize=12)
plt.grid(True, which="both", axis='x', ls="--", lw=0.5, c="gray")  # Add grid lines
plt.show()
