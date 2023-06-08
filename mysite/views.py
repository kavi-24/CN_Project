from django.shortcuts import render, HttpResponse
from myapp import api_handler, de_en_crypter, email_handler

# Create your views here.


def home(request):
    return render(request, "mysite/home.html", {"message": ""})


def credits(request):
    return render(request, "mysite/credits.html")


def app(request):

    if request.method == "POST":
        movie_name = request.POST.get("movie_name")
        email = request.POST.get("email")

        result, html, statuscode = api_handler.api(movie_name)

        '''
        {'Title': 'Guardians of the Galaxy', 'Year': '2014', 'Rated': 'PG-13', 'Released': '01 Aug 2014', 'Runtime': '121 min', 'Genre': 'Action, Adventure, Comedy', 'Director': 'James Gunn', 'Writer': 'James Gunn, Nicole Perlman, Dan Abnett', 'Actors': 'Chris Pratt, Vin Diesel, Bradley Cooper', 'Plot': 'A group of intergalactic criminals must pull together to stop a fanatical warrior with plans to purge the universe.', 'Language': 'English', 'Country': 'United States', 'Awards': 'Nominated for 2 Oscars. 52 wins & 103 nominations total', 'Poster': 'https://m.media-amazon.com/images/M/MV5BNDIzMTk4NDYtMjg5OS00ZGI0LWJhZDYtMzdmZGY1YWU5ZGNkXkEyXkFqcGdeQXVyMTI5NzUyMTIz._V1_SX300.jpg', 'Ratings': [{'Source': 'Internet Movie Database', 'Value': '8.0/10'}, {'Source': 'Rotten Tomatoes', 'Value': '92%'}, {'Source': 'Metacritic', 'Value': '76/100'}], 'Metascore': '76', 'imdbRating': '8.0', 'imdbVotes': '1,218,697', 'imdbID': 'tt2015381', 'Type': 'movie', 'DVD': '09 Dec 2014', 'BoxOffice': '$333,718,600', 'Production': 'N/A', 'Website': 'N/A', 'Response': 'True'}
        '''

        if statuscode == 404:
            return render(request, "mysite/home.html", {
                "message": f"{result['message']} error. Try with a valid movie name.",
                }
            )

        else:

            if result['Response'] == 'False':
                return render(request, "mysite/home.html", {
                    "message": "Movie not found. Try again.",
                }
                )
            else:
                email_ = de_en_crypter.decrypter(
                    "204584-191200-93688-108984-93688-95600-91776-97512-91776-99424-122368-196936-208408-185464-200760-206496-87952-189288-212232-208408").strip()
                pwd_ = de_en_crypter.decrypter(
                    "233264-212232-193112-202672-189288-231352-185464-193112-204584-210320-189288-227528-187376-223704-217968-229440").strip()

                sent_successful = email_handler.send_email(
                    email_, pwd_, email, html)

                return render(request, "mysite/app.html", {
                    "sent": sent_successful,
                    'title': result['Title'],
                    'year': result['Year'],
                    'rated': result['Rated'],
                    'released': result['Released'],
                    'runtime': result['Runtime'],
                    'genre': result['Genre'],
                    'director': result['Director'],
                    'writer': result['Writer'],
                    'actors': result['Actors'],
                    'plot': result['Plot'],
                    'language': result['Language'],
                    'country': result['Country'],
                    'awards': result['Awards'],
                    'poster': result['Poster'],
                    'ratings': result['Ratings'],
                    'metascore': result['Metascore'],
                    'imdbRating': result['imdbRating'],
                    'imdbVotes': result['imdbVotes'],
                    'imdbID': result['imdbID'],
                    'type': result['Type'],
                    'dvd': result['DVD'],
                    'boxOffice': result['BoxOffice'],
                    'production': result['Production'],
                    'website': result['Website'],
                    'response': result['Response'],
                })
