# Filter out rows where 'applies' is zero
non_zero_counts = database_aggregated[database_aggregated['applies'] > 0]

# Create the histogram with logarithmic scale for the count axis using Matplotlib
plt.figure(figsize=(10, 6))
plt.hist(non_zero_counts['applies'], bins=16, color='#492C68', log=True)
plt.title('The Number of Applications Distribution', fontsize=16)
plt.xlabel('Number of Applications', fontsize=12)
plt.ylabel('Count (logarithmic scale)', fontsize=12)
plt.grid(True, which="both", ls="--", lw=0.5, c="gray")  # Add grid lines
plt.yticks([1, 10, 100, 1000, 10000], ['1', '10', '100', '1000', '10000'])
plt.show()
