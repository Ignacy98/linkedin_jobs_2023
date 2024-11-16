experience_level_counts = database_aggregated['formatted_experience_level'].value_counts(normalize=True)

# Set the Seaborn style
palette_color = sns.color_palette("viridis")
# declaring exploding pie 
explode = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]

# Create a pie chart using Matplotlib
plt.figure(figsize=(8, 8))
plt.pie(experience_level_counts, labels=experience_level_counts.index, explode=explode, colors=palette_color, autopct='%1.2f%%', startangle=45)
plt.title('The experience level distribution', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
