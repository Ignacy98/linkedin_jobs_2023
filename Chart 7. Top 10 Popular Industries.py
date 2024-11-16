top10_industries = database_aggregated['industry_name'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top10_industries.values, y=top10_industries.index, palette='viridis')
plt.title('Top 10 Popular Industries', fontsize=16)
plt.xlabel('Count', fontsize=12)
plt.ylabel('Industry Name', fontsize=12)
plt.grid(True, which="both", axis='x', ls="--", lw=0.5, c="gray")  # Add grid lines
plt.show()
