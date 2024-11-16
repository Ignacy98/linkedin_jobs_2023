#Get top 20 titles with most applications
applies_title = database_aggregated.groupby('title')['applies'].mean().reset_index()
applies_title_sorted_top20 = applies_title.sort_values('applies', ascending=False).head(20)

plt.figure(figsize=(9, 7))
sns.barplot(x='title', y='applies', data=applies_title_sorted_top20, palette='viridis')
plt.title('Job titles that received the most applications', fontsize=16)
plt.xlabel('Title', fontsize=12)
plt.xticks(rotation=90)
plt.ylabel('Number of applications', fontsize=12)
plt.grid(True, which="both", axis='y', ls="--", lw=0.5, c="gray")  # Add grid lines
plt.show()
