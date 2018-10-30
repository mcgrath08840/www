import os
import json
from user import User



def menu():
    name = input("Enter your name: ")
    filename = "{}.txt".format(name)
    if file_exists(filename):
        with open(filename) as f:
            json_data = json.load(f)
            user = User.from_json(json_data)

    else:
        user = User(name)

    user_input = input("Enter 'a' to add a movie,\n"
          "'s' to see the list of movies\n"
          "'w' to set a movie as watched,\n"
          "'d' to delete a movie\n"
          "'l' to see a list of watched movies\n"
          "'f' to save file\n"
          "or 'q' to save and quit ")

    while user_input != 'q':
        if user_input == 'a':
            movie_name = input("Enter movie name: ")
            movie_genre = input("Enter movie genre: ")
            user.add_movie(movie_name, movie_genre)
        elif user_input == 's':
            for movie in user.movies:
                print('Name: {}  Genre: {}  Watched: {}'.format(movie.name, movie.genre, movie.watched))
        elif user_input == 'w':
            movie_name = input("Enter the movie name to set as watched: ")
            user.set_watched(movie_name)
        elif user_input == 'd':
            movie_name = input("Enter the movie name to delete: ")
            user.delete_movie(movie_name)
        elif user_input == 'l':
            for movie in user.watched_movies():
                print('Name: {}  Genre: {}  Watched: {}'.format(movie.name, movie.genre, movie.watched))
        elif user_input == 'f':
            with open(filename, 'w') as f:
                json.dump(user.json(), f)

        user_input = input("Enter 'a' to add a movie,\n"
                           "'s' to see the list of movies\n"
                           "'w' to set a movie as watched,\n"
                           "'d' to delete a movie\n"
                           "'l' to see a list of watched movies\n"
                           "'f' to save file\n"
                           "or 'q' to save and quit ")


def file_exists(filename):
    return os.path.isfile(filename)

menu()
