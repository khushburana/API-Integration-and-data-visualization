# 🌤️ Weather Forecast Dashboard

This Python project generates a **5-day weather dashboard** for any given city using the OpenWeatherMap API. It fetches, processes, and visualizes weather data in a clean image dashboard containing:

- 📈 Temperature trend over time  
- 📊 Daily average temperature  
- 🥧 Weather condition distribution

## 📁 Features

- Uses **OpenWeatherMap API** to fetch 5-day weather forecast.
- **Matplotlib** for data visualization with line, bar, and pie charts.
- Saves dashboard as an image file.

## 📦 Requirements

Install the dependencies using pip:

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```txt
requests
pandas
matplotlib
python-dotenv
```

## 🔐 Setup

1. Create a `.env` file in the project root:

```
OPENWEATHER_API_KEY=your_api_key_here
```

> Replace `your_api_key_here` with your OpenWeatherMap API key.

2. Ensure this file is in the same directory as the script:
   ```
   weather_dashboard.py
   .env
   ```

## 🚀 How to Run

```bash
python weather_dashboard.py
```

You'll be prompted to enter a city name. The script will fetch the weather, process it, and save a dashboard image like `london_dashboard.png`.

## 📊 Output

The output image includes:
- A line chart of temperature changes throughout the forecast period.
- A bar chart of average daily temperatures.
- A pie chart showing the proportion of different weather conditions.

## 🛠️ File Structure

```
.
├── weather_dashboard.py
├── .env
├── london_dashboard.png  # Example output
└── README.md
```

## 💡 Example

```bash
Enter city name: London

✅ Dashboard saved as: london_dashboard.png
```
