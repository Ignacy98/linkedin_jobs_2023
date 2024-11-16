application_type_counts = database_aggregated['application_type'].value_counts(normalize=True)

# Set the Seaborn style
palette_color = sns.color_palette("viridis")
# declaring exploding pie 
explode = [0, 0.1, 0.2]

# Create a pie chart using Matplotlib
plt.figure(figsize=(8, 8))
plt.pie(application_type_counts, labels=application_type_counts.index, explode=explode, colors=palette_color, autopct='%1.2f%%', startangle=45)
plt.title('The application process type frequency', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
