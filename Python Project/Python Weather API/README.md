<h1>Weather API Client (Python CLI)</h1>

<p>
A simple Python script that fetches real-time weather data using the OpenWeatherMap API 
and displays it in a clean, formatted table in the terminal.
</p>

<hr>

<h2>Features</h2>
<ul>
  <li>Fetch live weather data using REST API</li>
  <li>Display formatted output in terminal</li>
  <li>Shows temperature, humidity, wind, pressure, and more</li>
  <li>Convert into a web API (Flask)</li>
</ul>

<hr>

<h2>Tech Stack</h2>
<ul>
  <li>Python</li>
  <li>Requests</li>
  <li>python-dotenv</li>
</ul>

<hr>

<h2>Project Structure</h2>

<pre>
project-folder/
│── weather_script.py
│── .env
│── .gitignore
│── README.md
</pre>

<hr>

<h2>Setup Instructions</h2>

<h3>1. Clone the repository</h3>
<pre>
git clone &lt;your-repo-link&gt;
cd &lt;repo-folder&gt;
</pre>

<h3>2. Install dependencies</h3>
<pre>
pip install requests python-dotenv
</pre>

<h3>3. Create .env file</h3>
<pre>
WEATHER_KEY=your_api_key_here
</pre>

<p><b>Do NOT upload .env to GitHub; Rather add .env file in .gitignore file</b></p>

<hr>

<h2>Run the Script</h2>

<pre>
python weather_script.py
</pre>

<p>Enter city name when prompted</p>

<hr>

<h2> Sample Output</h2>

<pre>

==========================================
************   Weather Info   ************
==========================================
City                 | Bhopal
Temperature (°C)     | 28
Feel Like (°C)       | 30
Min.Temperature (°C) | 27
Max.Temperature (°C) | 30
Condition            | Clear Sky
Humidity (%)         | 60%
Atm. Pressure (hPa)  | 1012
Wind Speed (m/s)     | 3.5
Wind Degree          | 120°
Sunrise Time         | 06:20
Sunset Time          | 18:35
==========================================
</pre>

<hr>

<h2>Notes</h2>
<ul>
  <li>Uses metric units (°C)</li>
  <li>API key is stored securely using environment variables</li>
  <li>Simple CLI-based application</li>
</ul>

<hr>

<h2>Future Improvements</h2>
<ul>
  <li>Add support for multiple cities</li>
  <li>Save output to CSV/JSON</li>
</ul>

<hr>

<h2>Learning Outcome</h2>
<ul>
  <li>Working with REST APIs</li>
  <li>Parsing JSON data</li>
  <li>Handling environment variables</li>
  <li>Building CLI-based Python applications</li>
  <li>Convert into a web API (Flask)</li>
</ul>

<hr>

<h2>Author</h2>
<p>Rohan Prasad</p>