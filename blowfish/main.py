import matplotlib.pyplot as plt

# Define the stages of the literature research cycle
research_cycle = ["Task Understanding", "Library Search", "Identify Relevant Literature", "Create Table of Contents", "Writing", "Review and Revise"]

# Create a cycle diagram
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))
explode = (0.1, 0, 0, 0, 0, 0)  # To highlight the first stage, you can explode it a bit

# Plot the cycle as a pie chart
wedges, texts, autotexts = ax.pie([1] * len(research_cycle), labels=research_cycle, autopct='%1.1f%%',
                                  textprops=dict(color="w", weight="bold"))

# Add a circle in the center to make it look like a cycle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Add labels and title
ax.set_title("")

# Label each stage within the circle
for text in texts:
    text.set(size=8, ha='center', va='center', color='black', weight='bold')

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

# Show the plot
plt.show()
