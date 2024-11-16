work_type_counts = database_aggregated['formatted_work_type'].value_counts(normalize=True)

# Set the Seaborn style
palette_color = sns.color_palette("viridis")
# declaring exploding pie 
explode = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

# Create a pie chart using Matplotlib
plt.figure(figsize=(8, 8))
plt.pie(work_type_counts, labels=work_type_counts.index, explode=explode, colors=palette_color, autopct='%1.2f%%', startangle=45)
plt.title('Distribution of Work Types', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
