Weather Forecast Console App
A simple Python console application that fetches and displays weather data using the OpenWeatherMap API. The app allows users to check the current weather or a 5-day forecast for any city.
Features

Retrieve current weather details (temperature, humidity, pressure, wind speed, and description).
Fetch a 5-day weather forecast with noon-time updates for simplicity.
User-friendly console interface with a menu-driven system.
Error handling for invalid inputs and API request failures.

Technologies Used

Python: Core programming language.
Requests: Library for making HTTP requests to the OpenWeatherMap API.
OpenWeatherMap API: Provides weather data in JSON format.

Prerequisites

Python 3.6 or higher.
An OpenWeatherMap API key (free tier available).

Installation

Clone the repository:
git clone https://github.com/yourusername/weather-forecast-app.git
cd weather-forecast-app


Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Configure the API key:

Sign up at OpenWeatherMap to get a free API key.
Open weather_app.py and replace YOUR_API_KEY with your actual API key:API_KEY = "your_actual_api_key_here"




Run the application:
python weather_app.py



Usage

Launch the app with python weather_app.py.
Choose from the menu:
1. Get Current Weather: Enter a city name to view current weather details.
2. Get 5-Day Forecast: Enter a city name to see a 5-day forecast (noon updates only).
3. Exit: Close the application.


Example:Weather Forecast App
1. Get Current Weather
2. Get 5-Day Forecast
3. Exit
Enter your choice (1-3): 1
Enter city name: London
Current Weather in London:
Temperature: 15.2°C
Feels Like: 14.8°C
Humidity: 72%
Pressure: 1012 hPa
Weather: Broken clouds
Wind Speed: 3.6 m/s



Project Structure
weather-forecast-app/
├── weather_app.py          # Main application script
├── requirements.txt        # Project dependencies
└── README.md               # This file

Requirements
The requirements.txt file includes:
requests==2.28.1

Install dependencies using:
pip install -r requirements.txt

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit (git commit -m "Add feature").
Push to the branch (git push origin feature-branch).
Open a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

Thanks to OpenWeatherMap for providing a free weather API.
Inspired by practical Python projects for learning API integration.

Contact
For questions or feedback, open an issue or contact the maintainer at [your.email@example.com].
