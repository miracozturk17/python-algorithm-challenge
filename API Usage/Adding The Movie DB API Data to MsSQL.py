import requests
import pyodbc

API_KEY = "The Movie DB üzerinden edindiginiz key."

server = 'server' 
#PORT:1433
database = 'database' 
username = 'username' 
password = 'password' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

page = 1
while True:
    response = requests.get(
        "https://api.themoviedb.org/3/movie/popular",
        params={"api_key": API_KEY, "page": page}
    )

    movies_data = response.json()["results"]

    if not movies_data or page==500:
        break

    for movie_data in movies_data:
        image_response = requests.get(
            f"https://api.themoviedb.org/3/movie/{movie_data['id']}/images",
            params={"api_key": API_KEY}
        )
        image_path = image_response.json()["posters"][0]["file_path"]
        image_url = f"https://image.tmdb.org/t/p/w500{image_path}"

        imdb_response = requests.get(
            f"https://api.themoviedb.org/3/movie/{movie_data['id']}/external_ids",
            params={"api_key": API_KEY}
        )
        imdb_id = imdb_response.json()["imdb_id"]

        cursor.execute(
            "INSERT INTO MovieDetail (title, release_date, overview, image_url, imdb_id) VALUES (?, ?, ?, ?, ?)",
            (movie_data["title"], movie_data["release_date"], movie_data["overview"], image_url, imdb_id)
        )

    cnxn.commit()
    page += 1

cursor.close()
cnxn.close()