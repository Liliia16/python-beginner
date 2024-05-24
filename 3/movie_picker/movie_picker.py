import itertools

if __name__ == '__main__':
    print('Tasks 15-17. Movie picker.')
GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}

ACTORS = {
   'Robert De Niro': ['Meet the Parents'],
  'Ben Stiller': ['Meet the Parents'],
   'Adam Sandler': ['Anger Management'],
   'Jack Nicholson': ['Anger Management'],
   'Brendan Fraser': ['Mummy'],
  'Rachel Weisz': ['Mummy'],
  'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
  'Penelope Cruz': ['Vanilla Sky'],
  'Cameron Diaz': ['Vanilla Sky'],
  'Brad Pitt': ['Meet Joe Black'],
  'Anthony Hopkins': ['Meet Joe Black'],
  'Jeremy Renner': ['Mission Impossible']
}

# search_by_genre = input("Input: > Search by Genre: ")
# if search_by_genre == 'y':
#     available_genres = GENRES.keys()
#     print(f"Output: Available Genres: {available_genres}")
#
#     user_genre = input("Input: > Enter genre: ")
#     if user_genre in available_genres:
#         available_movies = GENRES[user_genre]
#         print(f"Output: Available Movies: {available_movies}")
#         user_movie = input("Input: > Enter movie: ")
#         if user_movie in available_movies:
#             print(f"Output: Movie to watch: {user_movie}. Genre: {user_genre}.")
#         else:
#             print("Movie not found. Please try again.")
#
#     else:
#         print('Genre not found. Please try again.')
#
#
# if search_by_genre == 'n':
#     search_by_actor = input("Input: > Search by Actor: ")
#     if search_by_actor == 'y':
#         available_actors = ACTORS.keys()
#         print(f"Output: Available Actors: {available_actors}")
#
#         actor = input("Input: > Enter actor: ")
#         if actor in available_actors:
#             movies = ACTORS[actor]
#             print(f"Output: Available Movies: {movies}")
#
#             user_movie = input("Input: > Enter movie: ")
#             if user_movie in movies:
#                 print(f"Output: Movie to watch: {user_movie}. Actor: {actor}.")

CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}

# if search_by_genre == 'n':
#     search_by_cast = input("Input: > Search by Actor: ")
#     if search_by_cast == 'y':
#         all_actors = []
#         for actors_list in CAST.values():
#             all_actors=all_actors+actors_list
#
#         print(f"Output: Available Actors: {all_actors}")
#
#         actor = input("Input: > Enter actor: ")
#         available_movies=[]
#         for movie, actors_list in CAST.items():
#             if actor in actors_list:
#                 available_movies.append(movie)
#
#         print(f"Available movies: {available_movies} with {actor}")
#         user_movie = input("Input: > Enter movie: ")
#         print(f"Available movies: {available_movies} with {actor}")
#         if user_movie in available_movies:
#             print(f"Output: Movie to watch: {user_movie}. Starring: {actor}.")



is_search_by_answer_incorrect = True
while is_search_by_answer_incorrect:
    search_by_genre = input("Input: > Search by Genre: ")
    if search_by_genre == 'y':
        is_search_by_answer_incorrect = False
        available_genres = list(GENRES.keys())
        print(f"Output: Available Genres: {available_genres}")
        is_genre_answer_incorrect = True
        while is_genre_answer_incorrect:
            user_genre = input("Input: > Enter genre: ")
            if user_genre in available_genres:
                is_genre_answer_incorrect = False
                available_movies = GENRES[user_genre]
                print(f"Output: Available Movies: {available_movies}")
                is_user_movie_answer_incorrect = True
                while is_user_movie_answer_incorrect:
                    user_movie = input("Input: > Enter movie: ")
                    if user_movie in available_movies:
                        is_user_movie_answer_incorrect = False
                        print(f"Output: Movie to watch: {user_movie}. Genre: {user_genre}.")
                    else:
                        is_user_movie_answer_incorrect = True
                        print(f"Movie [{user_movie}] not found. Please try again. Available Movies: {available_movies}.")
            else:
                is_genre_answer_incorrect = True
                print(f'Genre [{user_genre}] not found. Please try again. Available Genres: {available_genres}.')

    elif search_by_genre == 'n':
        is_search_by_answer_incorrect = False
        is_search_by_actor_answer_incorrect = True
        while is_search_by_actor_answer_incorrect:
            search_by_actor = input("Input: > Search by Actor: ")
            if search_by_actor == 'y':
                is_search_by_actor_answer_incorrect = False
                available_actors = list(ACTORS.keys())
                print(f"Output: Available Actors: {available_actors}")
                is_actor_answer_incorrect = True
                while is_actor_answer_incorrect:
                    actor = input("Input: > Enter actor: ")
                    if actor in available_actors:
                        is_actor_answer_incorrect = False
                        movies = ACTORS[actor]
                        print(f"Output: Available Movies: {movies}")

                        is_movie_answer_incorrect = True
                        while is_movie_answer_incorrect:
                            user_movie = input("Input: > Enter movie: ")
                            if user_movie in movies:
                                is_movie_answer_incorrect = False
                                print(f"Output: Movie to watch: {user_movie}. Actor: {actor}.")
                            else:
                                is_movie_answer_incorrect = True
                                print(f"Output: Actor movie [{user_movie}] not found! Available Actors: {available_actors}")
                    else:
                        is_actor_answer_incorrect = True
                        print(f"Output: Actor [{actor}] not found! Available Actors: {available_actors}")

            elif search_by_actor == 'n':
                is_search_by_answer_incorrect = True
                is_search_by_actor_answer_incorrect = False
            else:
                print(f'You entered [{search_by_actor}] which is wrong answer! Available answers are [y] or [n].')
                is_search_by_actor_answer_incorrect = True
    else:
        is_search_by_answer_incorrect = True
        print(f'You entered [{search_by_genre}] which is wrong answer! Available answers are [y] or [n].')
