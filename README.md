# 🧭 Tourist & Hotel Recommendation System

A Flask-based web application that helps users discover **recommended tourist spots and nearby hotels** based on their **current location** or **planned travel destination**. This project uses **content-based filtering** and **geospatial proximity** to suggest personalized experiences.

---

## 🌟 Features

- ✅ **Tourist Spot Recommendation** using content-based filtering (TF-IDF)
- 📍 **Location-based Filtering** using latitude, longitude, radius
- 🏨 **Nearby Hotel Suggestions** using Haversine formula
- 🌐 **Folium Interactive Maps** for visualizing spots and hotels
- 🧭 **User Preference Options**: current location or plan a trip
- 🖼️ Attractive **Welcome Page** with images of famous destinations
- 🗂️ Categorized recommendations (e.g., Adventure, Heritage, Nature)
- 🔗 **Hotel Detail Popups** with direct booking links

---

## 📁 Project Structure
project/
│
├── app.py # Flask backend
├── static/
│ ├── css/ # Custom stylesheets
│ └── images/ # Welcome page images
├── templates/
│ ├── welcome.html # Landing page with destination images
│ ├── preferences.html # Choose current location or trip plan
│ ├── index.html # Main recommendation page
├── data/
│ ├── tourist_spots.csv # Dataset of tourist spots in India
│ └── hotels.csv # Dataset of hotels with geo-coordinates
├── recommender.py # TF-IDF based recommendation engine

# 1. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

#2. Install Dependencies
pip install -r requirements.txt

#3. Run the App
python app.py


# 📌 Screenshots

## 🖼️ Screenshots

### Welcome Page
![Welcome Page]("C:\Users\HP\Pictures\Screenshots\Screenshot (181).png")

### Recommendations Page
![Recommendations](C:\users\hp\Pictures\Screenshots\Screenshot (182).png)

### Interactive Map 
![Interactive Map](C:\users\hp\Pictures\Screenshots\Screenshot (184).png)



