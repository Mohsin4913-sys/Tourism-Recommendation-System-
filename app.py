from flask import Flask, render_template, request
import pandas as pd
from geopy.distance import geodesic
import folium
import os
from geopy.distance import geodesic
from time import time

app = Flask(__name__)

CATEGORIES = {
    "parks": "park",
    "museums": "museum",
    "waterfalls": "waterfall",
    "beaches": "beach",
    "zoos": "zoo",
    "temples": "temple",
    "hills": "hill",
    "attractions": "tourist attraction",
    "all": "all"
}

def load_data():
    try:
        data = pd.read_csv("indianspots.csv")
        data.dropna(subset=['Latitude', 'Longitude', 'Categories', 'Name'], inplace=True)
        data['Latitude'] = pd.to_numeric(data['Latitude'], errors='coerce')
        data['Longitude'] = pd.to_numeric(data['Longitude'], errors='coerce')
        data.dropna(inplace=True)
        return data
    except:
        return pd.DataFrame()

dataset = load_data()

from geopy.distance import geodesic

def recommend_spots(user_location, radius, category_filter, data_df):
    print(f"User location: {user_location}, Radius: {radius}, Category: {category_filter}")
    print(f"Dataset size: {len(data_df)}")
    recommended = []

    for _, row in data_df.iterrows():
        try:
            spot_location = (row['Latitude'], row['Longitude'])
            distance = geodesic(user_location, spot_location).km
            if distance <= radius:
                print(f"Found nearby spot: {row['Name']} at distance {distance} km")
                # Convert category fields to lowercase for case-insensitive partial match
                spot_categories = str(row['Categories']).lower()
                user_filter = category_filter.lower().strip()

                if user_filter == "all" or user_filter in spot_categories:
                    recommended.append({
                        'Name': row['Name'],
                        'Category': row['Categories'],
                        'Latitude': row['Latitude'],
                        'Longitude': row['Longitude'],
                        'Distance': round(distance, 2)
                    })
        except Exception as e:
            print(f"Error on row: {e}")
    
    print(f"Total recommendations: {len(recommended)}")
    return recommended



def create_map(user_location, spots):
    m = folium.Map(location=user_location, zoom_start=12)
    folium.Marker(user_location, tooltip="Your Location", icon=folium.Icon(color='red')).add_to(m)

    for spot in spots:
        folium.Marker(
            location=(spot['Latitude'], spot['Longitude']),
            tooltip=f"{spot['Name']} ({spot['Distance']} km)",
            icon=folium.Icon(color='blue')
        ).add_to(m)

    map_path = os.path.join("static", "map.html")
    m.save(map_path)
    return map_path

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    map_path = None
    cache_buster = int(time())  # Generate version number for cache busting

    if request.method == "POST":
        try:
            lat = float(request.form["latitude"])
            lon = float(request.form["longitude"])
            radius = float(request.form["radius"])
            category = request.form["category"]

            user_location = (lat, lon)
            recommendations = recommend_spots(user_location, radius, CATEGORIES[category], dataset)

            if recommendations:
                map_path = create_map(user_location, recommendations)
        except Exception as e:
            return render_template("index.html", error=str(e), categories=CATEGORIES.keys())

    return render_template(
        "index.html",
        recommendations=recommendations,
        map_path=map_path,
        categories=CATEGORIES.keys(),
        cache_buster=cache_buster  # ✅ Now this is passed to HTML
    )

@app.route("/map")
def show_map():
    # For demo, a fixed location or you can pass real spots if you want
    user_location = (12.833815, 77.65645)
    spots = []  # you can fill spots if you want to add markers here
    
    m = folium.Map(location=user_location, zoom_start=12)
    
    # Optionally add markers from spots list
    for spot in spots:
        folium.Marker(
            location=(spot['Latitude'], spot['Longitude']),
            tooltip=f"{spot['Name']} ({spot['Distance']} km)",
            icon=folium.Icon(color='blue')
        ).add_to(m)

    # Generate raw HTML of the map
    map_html = m._repr_html_()
    return map_html

if __name__ == "__main__":
    app.run(debug=True)
