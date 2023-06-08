'''
By ID or Title
Parameter 	Required 	Valid Options 	            Default Value 	Description
i 	        Optional* 		                            <empty> 	A valid IMDb ID (e.g. tt1285016)
t 	        Optional* 		                            <empty> 	Movie title to search for.
type 	    No 	            movie, series, episode 	    <empty> 	Type of result to return.
y 	        No 		                                    <empty> 	Year of release.
plot 	    No 	            short, full 	            short 	    Return short or full plot.
r 	        No 	            json, xml 	                json 	    The data type to return.
callback 	No 		                                    <empty> 	JSONP callback name.
v 	        No 		                                    1 	        API version (reserved for future use).
*Please note while both "i" and "t" are optional at least one argument is required.

By Search
Parameter 	Required 	Valid options 	        Default Value 	Description
s 	        Yes 		                        <empty> 	    Movie title to search for.
type 	    No 	        movie, series, episode 	<empty> 	    Type of result to return.
y 	        No 		                            <empty> 	    Year of release.
r 	        No 	        json, xml 	            json 	        The data type to return.
page  	    No 	        1-100 	                1 	            Page number to return.
callback 	No 		                            <empty> 	    JSONP callback name.
v 	        No 		                            1 	            API version (reserved for future use).
'''

import requests
from myapp import de_en_crypter
import json
import socket


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False


def api(movie_name: str): # -> str of html
    # if not is_connected():
    try:
        url= f"http://www.omdbapi.com/?i=tt3896198&apikey={de_en_crypter.decrypter('101336-97512-91776-105160-103248-193112-195024-107072')}"
        params = {
            't': movie_name # input()
        }
        r = requests.get(url = url, params = params)
        data = r.json()
        html = create_html_representation(data)
        return data, html, r.status_code
    except Exception as e:
        return {"message": str(e)}, None, 404
        # main.main()
        



def create_html_representation(data):
    html = f'''
    <html>
    <head>
        <style>
            /* Add your CSS styles here */
            body {{
                font-family: Arial, sans-serif;
            }}
            h1 {{
                color: #333;
                font-size: 24px;
            }}
            /* Add more styles as needed */
        </style>
    </head>
    <body>
        <h1>{data['Title']}</h1>
        <p><strong>Rated:</strong> {data['Rated']}</p>
        <p><strong>Released:</strong> {data['Released']}</p>
        <p><strong>Runtime:</strong> {data['Runtime']}</p>
        <p><strong>Genre:</strong> {data['Genre']}</p>
        <p><strong>Director:</strong> {data['Director']}</p>
        <p><strong>Actors:</strong> {data['Actors']}</p>
        <p><strong>Plot:</strong> {data['Plot']}</p>
        <img src="{data['Poster']}" alt="Movie Poster" width="200">
        <p><strong>Ratings:</strong></p>
        <ul>
    '''

    for rating in data['Ratings']:
        html += f'<li>{rating["Source"]}: {rating["Value"]}</li>'

    html += f'''
        </ul>
        <p><strong>IMDb Rating:</strong> {data['imdbRating']}</p>
        <p><strong>Type:</strong> {data['Type']}</p>
    </body>
    </html>
    '''

    return html