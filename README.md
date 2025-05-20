# Preswald-project2


# Job Dataset Explorer

This project is a data exploration app built with the Preswald platform. It analyzes a real-world job dataset to uncover trends in education, training effort, experience, and city-level job seeker distribution. The application includes data cleaning, SQL querying, and rich visualizations powered by Plotly.

## 🚀 Features

- **Data Loading**: Connects to and reads from a CSV-based job dataset.
- **Data Cleaning**:
  - Handles missing values for categorical fields like `gender`, `company_type`, `education_level`, etc.
  - Cleans and converts experience ranges (e.g., `<1`, `>20`) to numeric form.
- **Exploratory Analysis**:
  - Null value summaries
  - Training hour distributions
  - Filtering by education level
- **SQL Insights**:
  - Most common education levels
  - Average training hours by experience
  - Top cities by job seeker count
- **Visualizations (Plotly)**:
  - Histogram of training hours
  - Bar chart of average training hours by education level
  - Scatter plot: training hours vs. city development index
  - Bar chart: top cities by number of enrollees

## 🧰 Tech Stack

- **Preswald SDK**: for app composition, data querying, and UI components
- **Pandas**: for data manipulation and aggregation
- **SQL-like queries**: via Preswald’s `query()` interface
- **Plotly Express**: for clean and interactive charts

## 📂 Folder Structure

