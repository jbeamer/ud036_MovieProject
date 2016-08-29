#!/usr/bin/env python
"""entertainment_center.py: Main entry point for the movie website project"""

# import statements for our required modules
import media
import fresh_tomatoes

# movie definitions:  Here is where we add all data for the movies we love
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://images.popmatters.com/film_art/a/avatar-poster.jpg",
    "https://www.youtube.com/watch?v=8KAtG68bIUc")

caddyshack = media.Movie(
    "Caddyshack",
    "An exclusive golf course has to deal with a brash new member and a"
    " destructive dancing gopher.",
    "https://images-na.ssl-images-amazon.com/images/I/51qVp-dXLgL.jpg",
    "https://www.youtube.com/watch?v=zrTqenN1SqQ")

school_of_rock = media.Movie(
    "School of Rock",
    "After being kicked out of a rock band, Dewey Finn becomes a substitute"
    " teacher of a strict elementary private school, only to try and turn it"
    " into a rock band.",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "While on a trip to Paris with his fiancee's family, a nostalgic"
    " screenwriter finds himself mysteriously going back to the 1920s"
    " everyday at midnight.",
    "http://www.impawards.com/2011/posters/midnight_in_paris.jpg",
    "https://www.youtube.com/watch?v=wuOUdZjuCIA")

ratatouille = media.Movie(
    "Ratatouille",
    "A rat who can cook makes an unusual alliance with a young kitchen worker"
    " at a famous restaurant.",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=ALUmKa_mpik")

# create the list of Movie objects
movies = [
    toy_story,
    avatar,
    caddyshack,
    school_of_rock,
    midnight_in_paris,
    ratatouille]

# pass the list of Moviews to the fresh_tomatoes module, which will do all
# of the heavy lifting of web page creation:
fresh_tomatoes.open_movies_page(movies)
