#Subset to all remote jobs
remote = database_aggregated[database_aggregated['remote_allowed']=='Yes']

#Subset to rows that contain 'Remote' in title
remote_in_title = remote['title'].str.contains('Remote', case=False, regex=False)
remote_title = remote[remote_in_title]
remote_title_mean = remote_title['applies'].mean()

#Subset to rows that don't contain 'Remote' in title
does_not_apply_remote = ~remote['title'].str.contains('Remote', case=False, regex=False)
non_remote_title = remote[does_not_apply_remote]
non_remote_title_mean = non_remote_title['applies'].mean()

data = [remote_title_mean, non_remote_title_mean]

plt.figure(figsize=(8, 4))
sns.barplot(data=data, palette='viridis', width=0.5)
plt.title('With or without "Remote" in a title (hybrid and remote jobs)', fontsize=16)
plt.xticks([0, 1], ['With', 'Without'], rotation=80)
plt.ylabel('Average number of applications', fontsize=12)
plt.grid(True, which="both", axis='y', ls="--", lw=0.5, c="gray")  # Add grid lines
plt.show()
