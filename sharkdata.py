# 1.HYPOTHESIS: Activity & Fatality
# Define the activity grouping function


def activity_grouping(x):
    if isinstance(x, str):
        act = x.lower()
        if "fish" in act:
            return "Fishing"
        if "board" in act or "surf" in act:
            return "Surfing"
        if "swim" in act:
            return "Swimming"
    return "Other"

# Apply the function to create a new column for Activity Type
shark_df['Activity Type'] = shark_df['Activity'].apply(activity_grouping)

# Calculate fatal and non-fatal counts by activity type
shark_df['Is Fatal'] = shark_df['Injury'].str.contains(r'Fatal', regex=True, case=False, na=False)

activity_counts = shark_df.groupby(['Activity Type', 'Is Fatal']).size().unstack(fill_value=0).reset_index()

activity_counts.columns = ['Activity Type', 'Non-Fatal', 'Fatal']

activity_counts = activity_counts.melt(id_vars='Activity Type', var_name='Injury Type', value_name='Count')

plt.figure(figsize=(10, 6))
sns.barplot(x='Activity Type', y='Count', hue='Injury Type', data=activity_counts, palette='pastel')

plt.title("Counts of Fatal and Non-Fatal Shark Incidents by Activity", fontsize=16)
plt.xlabel("Activity Type", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.legend(title='Injury Type')

plt.show()

#2. HYPOTHESIS: Frequency & Time




#3. HYPOTHESIS: Attacks & Season