import de_en_crypter
import email_handler
import api_handler

def main():

    email = de_en_crypter.decrypter("204584-191200-93688-108984-93688-95600-91776-97512-91776-99424-122368-196936-208408-185464-200760-206496-87952-189288-212232-208408").strip()
    pwd = de_en_crypter.decrypter("233264-212232-193112-202672-189288-231352-185464-193112-204584-210320-189288-227528-187376-223704-217968-229440").strip()

    movie_name = input("Enter the movie name: ")
    receiver = input("Enter the receiver email ID: ")

    html = api_handler.api(movie_name)
    email_handler.send_email(email, pwd, receiver, html)

if __name__ == "__main__":
    main()