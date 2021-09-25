from faker import Faker
fake = Faker("pl_PL")

movies_and_series = []

class Movies_library:
    def __init__(self, title, publication_year,film_genre, number_of_plays):
        self.title=title
        self.publication_year = publication_year
        self.film_genre = film_genre
        self.number_of_plays = number_of_plays
    def play(self, play_number=1):
        self.number_of_plays += play_number
    def __str__(self):
        return f"{self.title} {self.publication_year}"
    def __repr__(self):
        return f"{self.title} {self.publication_year}"

class Series_library(Movies_library):
    def __init__(self, episode_number, season_number, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number =episode_number
        self.season_number =season_number
    def __str__(self):
      return f"{self.title} S{self.season_number:02d}E{self.episode_number:02d}"
    def __repr__(self):
        return f"{self.title} S{self.season_number:02d}E{self.episode_number:02d}"


for x in range(15):
    movie = Movies_library(title=fake.word().title(), publication_year = fake.year(),film_genre=fake.word(), number_of_plays=fake.random_int(0,40))
    movies_and_series.append(movie)
    series = Series_library(title=fake.word().title(), publication_year = fake.year(),film_genre=fake.word(), number_of_plays=fake.random_int(0,40), episode_number = fake.random_int(1,20), season_number=fake.random_digit_not_null())
    movies_and_series.append(series)

print(movies_and_series)

def get_movies():
    movies = [i for i in movies_and_series if not isinstance(i,Series_library)]
    sorted_movies = sorted(movies, key=lambda x: x.title)
    print(sorted_movies)
    return sorted_movies

print("Filmy:")
get_movies()

def get_series():
    series = [i for i in movies_and_series if isinstance(i,Series_library)]
    sorted_series=sorted(series,key=lambda x: x.title)
    print(sorted_series)
    return sorted_series

print("Serale:")
get_series()

def search(title):
    for i in range(len(movies_and_series)):
        if movies_and_series[i].title == title:
            return movies_and_series[i]
        else:
            return "This title does not appear in the Movies and Series Library"
'''
Przykład do sprawdzenia funkcji search oraz top_titles, bez użycia fakera,
znajduje się w pliku Search_function

'''
by_number =  sorted(movies_and_series, key=lambda i: i.number_of_plays)
by_number_reversed= list(reversed(by_number))

print("Top movies and series:")

def top_titles(quantity):
   for i in range(quantity):
       print(by_number_reversed[i])
   return ""

print(top_titles(4))

import random
def generate_views():
    for i in range(len(movies_and_series)):
        random.shuffle(movies_and_series)
        movies_and_series[i].play(random.randint(1,100))
    return f"{movies_and_series[i].title} {movies_and_series[i].number_of_plays}"

print(generate_views())

print("10 razy:")
def multiple():
    for a in range(9):
        print(generate_views())
    return generate_views()
print(multiple())
