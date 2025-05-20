from preswald import connect, get_df, table, text, query, plotly
import plotly.express as px

connect()
df = get_df("aug_test")

text("# Job Dataset Explorer")
text("Welcome! Let's start with null value analysis and cleaning.")

text("## 🔍 Initial Null Value Summary")
null_summary = df.isnull().sum().reset_index()
null_summary.columns = ["Column", "Null Count"]
table(null_summary)

text("## Cleaning Missing Values")

df["gender"] = df["gender"].fillna("Unknown")
df["company_type"] = df["company_type"].fillna("Unknown")
df["company_size"] = df["company_size"].fillna("Unknown")
df["major_discipline"] = df["major_discipline"].fillna("Other")

df["education_level"] = df["education_level"].fillna(df["education_level"].mode()[0])
df["enrolled_university"] = df["enrolled_university"].fillna(df["enrolled_university"].mode()[0])
df["last_new_job"] = df["last_new_job"].fillna(df["last_new_job"].mode()[0])

df["experience"] = df["experience"].replace({'>20': '21', '<1': '0'})
df["experience"] = df["experience"].fillna(df["experience"].mode()[0])
df["experience"] = df["experience"].astype(int)

text("###  Sample of Cleaned Data")
table(df.head(5))

text("##  Post-Cleaning Null Check")
null_summary = df.isnull().sum().reset_index()
null_summary.columns = ["Column", "Null Count"]
table(null_summary)

text("## Filtered View: Only 'Graduate' Education Level")
sql_filter = "SELECT * FROM aug_test WHERE education_level = 'Graduate'"
filtered_df = query(sql_filter, "aug_test")
table(filtered_df.head(10))



text("##  Insight 1: Most Common Education Level")
sql1 = """
SELECT education_level, COUNT(*) AS count
FROM aug_test
GROUP BY education_level
ORDER BY count DESC
"""
result1 = query(sql1, "aug_test")
table(result1)



text("##  Insight 2: Top 10 Cities by Enrollee Count")
sql2 = """
SELECT city, COUNT(*) AS enrollee_count
FROM aug_test
GROUP BY city
ORDER BY enrollee_count DESC
LIMIT 10
"""
result3 = query(sql2, "aug_test")
table(result3)




text("##  Distribution of Training Hours")
fig1 = px.histogram(
    df,
    x="training_hours",
    nbins=30,
    labels={"training_hours": "Training Hours"},
    color_discrete_sequence=["#007BFF"]
)
fig1.update_layout(template="plotly_white")
plotly(fig1)



text("## Top 10 Cities by Enrollee Count")

top_cities = df["city"].value_counts().nlargest(10).reset_index()
top_cities.columns = ["City", "Number of Enrollees"]

fig3 = px.bar(
    top_cities,
    x="City",
    y="Number of Enrollees",
    title="",
    labels={"City": "City", "Number of Enrollees": "Enrollees"},
    color="Number of Enrollees"
)
fig3.update_layout(template="plotly_white", showlegend=False, xaxis_tickangle=45)
plotly(fig3)
