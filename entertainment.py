import fresh_tomatoes
import media


# This section is used to initialize the values in the Movie Class in the Media
# Module for each movie

Aravindha_Sametha = media.Movie("Aravindha Sametha",
                        "Get ready to witness the #RageOfTiger this Dussehra",
                        "https://upload.wikimedia.org/wikipedia/commons/2/2b/Aravinda_Sametha_Veera_Raghava_Poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=dNMe5oRfsCE&t=2s")


Robo = media.Movie("2.0",
                     "2.0 is an upcoming Indian science fiction film ",
                     "https://upload.wikimedia.org/wikipedia/en/c/cf/2.0_film_poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=2wvq8hdGdAw")


Thugs_Of_Hindostan = media.Movie("Thugs Of  Hindostan",
                             "Thugs of Hindostan is an upcoming 2018 Flim",
                             "https://upload.wikimedia.org/wikipedia/en/1/15/Thugs_Of_Hindostan_Poster.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=hoKPLMqIztw")


Sye_Raa_Narasimha_Reddy = media.Movie("Sye Raa Narasimha Reddy",
                     "Sye Raa Narasimha Reddy is an Indian period film.",
                     "https://upload.wikimedia.org/wikipedia/en/a/ac/Sye_Raa_Narasimha_Reddy_film_poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=NMRJTTMMmZw")


Saakshyam = media.Movie("Saakshyam",
                                "Saakshyam is a Telugu action romantic Flim",
                                "https://upload.wikimedia.org/wikipedia/en/c/c1/Saakshyam.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=VEEWvlCvLNY")


Pantham = media.Movie("Pantham",
                           "Pantham is an Indian action film",
                           "https://upload.wikimedia.org/wikipedia/en/6/65/Pantham.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=kawW_8S6r60")


Geetha_Govindam = media.Movie("Geetha Govindam",
                           "Geetha Govindam is an Telugu romantic comedy  ",
                           "https://upload.wikimedia.org/wikipedia/en/5/50/GeethaGovindamramp.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=U3dqoAHqagk")


# "import fresh_tomatoes" allows to turn this code
# into a movie website by using function "open_movies_page"
# The "open_movies_page" function takes a list or array of movies,
# then outputs or creates and opens
# an html webpage or website that shows those movies
movies = [Aravindha_Sametha, Robo, Thugs_Of_Hindostan,
          Sye_Raa_Narasimha_Reddy, Saakshyam, Pantham, Geetha_Govindam]
fresh_tomatoes.open_movies_page(movies)
