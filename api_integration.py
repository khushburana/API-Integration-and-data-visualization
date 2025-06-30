import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from matplotlib.gridspec import GridSpec
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Load API Key from .env
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
API_URL = "https://api.openweathermap.org/data/2.5/forecast"

# Fetch 5-day weather forecast using city name
def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    res = requests.get(API_URL, params=params)
    res.raise_for_status()
    return res.json()

# Convert JSON response to DataFrame
def process_data(data):
    rows = []
    for entry in data["list"]:
        dt = entry["dt_txt"]
        temp = entry["main"]["temp"]
        weather = entry["weather"][0]["main"]
        rows.append([dt, temp, weather])
    
    df = pd.DataFrame(rows, columns=["DateTime", "Temp", "Weather"])
    df["DateTime"] = pd.to_datetime(df["DateTime"])
    df["Date"] = df["DateTime"].dt.date
    return df

# Plot all charts and save the dashboard image
def create_dashboard(df, city):
    plt.figure(figsize=(15, 10))
    gs = GridSpec(2, 2)

    # Line chart: Temperature trend
    ax1 = plt.subplot(gs[0, 0])
    ax1.plot(df["DateTime"], df["Temp"], marker='o', color='tab:blue')
    ax1.set_title("Temperature Trend")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Temp (°C)")
    ax1.tick_params(axis='x', rotation=45)

    # Bar chart: Daily average temperature
    ax2 = plt.subplot(gs[0, 1])
    avg_temp = df.groupby("Date")["Temp"].mean()
    ax2.bar(avg_temp.index.astype(str), avg_temp.values, color='orange')
    ax2.set_title("Average Daily Temperature")
    ax2.set_ylabel("Temp (°C)")
    ax2.tick_params(axis='x', rotation=45)

    # Pie chart: Weather condition distribution
    ax3 = plt.subplot(gs[1, :])
    weather_counts = df["Weather"].value_counts()
    ax3.pie(weather_counts, labels=weather_counts.index, autopct='%1.1f%%', startangle=140)
    ax3.set_title("Weather Condition Distribution")

    # Save dashboard image
    plt.suptitle(f"Weather Dashboard: {city.title()}", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    filename = f"{city.lower()}_dashboard.png"
    plt.savefig(filename)
    print(f"\n✅ Dashboard saved as: {filename}")

# Main function
def main():
    city = input("Enter city name: ").strip()
    try:
        data = fetch_weather(city)
        df = process_data(data)
        create_dashboard(df, city)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()