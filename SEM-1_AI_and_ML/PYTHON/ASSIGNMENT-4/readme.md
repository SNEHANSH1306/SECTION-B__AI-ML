🌦️ Weather Analyzer & Visualizer

A Python-based project that loads, cleans, analyzes, and visualizes weather data using Pandas, NumPy, and Matplotlib.

📁 Project Structure
├── main.py
├── data_analysis
│   ├── loader.py
│   └── stats.py
├── visualization
│   └── plots.py
├── weather_data.csv
└── my_cleaned_data.csv (generated after running)

🚀 Features
✅ 1. Data Loading & Cleaning

Reads raw CSV data.

Converts date strings to datetime objects.

Handles missing values:

Missing temperature → replaced with mean temperature

Missing rainfall → replaced with 0

✅ 2. Statistical Analysis

Using NumPy:

Mean temperature

Maximum temperature

Minimum temperature

Standard deviation

Using Pandas:

Monthly averages (Temperature & Rainfall)

Proper month ordering using Categorical data type

✅ 3. Visualizations

Generated using Matplotlib:

📈 Daily Temperature Trend (Line Plot)

🌧️ Total Monthly Rainfall (Bar Chart)

🔵 Temp vs Humidity (Scatter Plot)

🟦 Combined Subplots (Temp + Humidity Trends)

Output files include:

1_temp_trend.png
2_rain_bar.png
3_scatter.png
4_combined.png

✅ 4. Exporting Cleaned Data

Saves processed dataset as my_cleaned_data.csv

🏃 How to Run

Make sure you have Python installed (3.8+ recommended).

1️⃣ Install Required Libraries
pip install pandas numpy matplotlib

2️⃣ Run the Project
python main.py

📜 Code Overview
main.py

Entry point for executing the full pipeline

Loads data → computes stats → generates plots → saves cleaned file

loader.py

Handles importing and cleaning the dataset

Applies missing value rules

stats.py

Computes NumPy statistics

Groups and calculates monthly averages

plots.py

Generates all required visualizations and saves them as PNG files

📊 Sample Output (Console)

You will see:

Data loading info

Cleaning results

NumPy statistics

Monthly average table

Plot saved confirmations

🧪 Input Data

Place your weather_data.csv file in the root directory.

Example CSV columns:

Date, Temperature_C, Humidity_Pct, Rainfall_mm

✨ Author

Snehansh Jangir
B.Tech CSE (AI & ML) — Section B
Roll No. 2501730140
