top10_titles = database_aggregated['title'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top10_titles.values, y=top10_titles.index, palette='viridis')
plt.title('Top 10 Popular Job Titles', fontsize=16)
plt.xlabel('Count', fontsize=12)
plt.ylabel('Job Title', fontsize=12)
plt.grid(True, which="both", axis='x', ls="--", lw=0.5, c="gray")  # Add grid lines
plt.show()
