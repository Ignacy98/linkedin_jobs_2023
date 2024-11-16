company_size_counts = database_aggregated['company_size'].value_counts(normalize=True)
company_size_description = {
    0: '1-10 employees',
    1: '11-50 employees',
    2: '51-200 employees',
    3: '201-500 employees',
    4: '501-1000 employees',
    5: '1001-5000 employees',
    6: '5001-10,000 employees',
    7: '10,001+ employees'
}

# Map the values in company_size_counts index to their corresponding descriptions
company_size_counts.index = company_size_counts.index.map(company_size_description)

company_size_counts = company_size_counts.reset_index()
company_size_counts.columns = ['description', 'count']

# Set the Seaborn style
palette_color = sns.color_palette("viridis")
# declaring exploding pie 
explode = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35]

# Create a pie chart using Matplotlib
plt.figure(figsize=(8, 8))
plt.pie(company_size_counts['count'], labels=company_size_counts['description'], explode=explode, colors=palette_color, autopct='%1.2f%%', startangle=45)
plt.title('The number of job postings by company size', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
