from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from movies.models import *
import requests
from bs4 import BeautifulSoup
import json

class Command(BaseCommand):
    base_url = "https://www.rottentomatoes.com"
    opening_url = "/browse/opening/"
    movies = []
    max_critics_per_movie = 10

    def crawl(self):
        self.stdout.write(self.style.SUCCESS('1. Crawl: '+self.base_url+'/browse/opening/'))

        # Get schema from /browse/opening
        jsonLdSchema = self.get_schema(self.base_url+self.opening_url)

        # Get schema for each movie and then append to movies = []
        movieList = jsonLdSchema["itemListElement"]
        i = 1
        for movie_info in movieList:
            url = self.base_url+movie_info["url"]
            movie = self.crawl_movie(url, i)
            movie["position"] = movie_info["position"]
            self.movies.append(movie)
            i += 1

    def crawl_movie(self, url, counter):
        self.stdout.write(self.style.SUCCESS('1.'+str(counter)+'. Crawl movie: '+url))

        # Get schema from /m/?
        jsonLdSchema = self.get_schema(url)

        # Create movie from jsonLdSchema and return
        movie = {}
        movie["name"] = jsonLdSchema.get('name', "")
        movie["picture"] = jsonLdSchema.get("image", "")
        movie["score"] = jsonLdSchema["aggregateRating"].get('ratingValue', None)
        movie["description"] = jsonLdSchema.get('description', "")
        movie["production_company"] = jsonLdSchema["productionCompany"].get('name', None)
        movie["genre"] = jsonLdSchema.get('genre', "")
        movie["director"] = jsonLdSchema.get('director', "")
        movie["author"] = jsonLdSchema.get('author', "")
        movie["actor"] = jsonLdSchema.get('actor', "")
        movie["critic"] = jsonLdSchema.get('review', "")
    
        return movie

    def get_schema(self, url):
        # Return json schema from url
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        jsonLdSchema = soup.find('script', {'id': 'jsonLdSchema'}).get_text()
        jsonLdSchema = json.loads(jsonLdSchema)

        if(url != self.base_url+self.opening_url):
            jsonLdSchema["image"] = soup.select_one('.posterImage')['src']
            jsonLdSchema["description"] = soup.select_one('#movieSynopsis').text

        return jsonLdSchema

    def empty_db(self):
        # Empty database
        m = Movie.objects.all()
        m.delete()

        # Persons, genres and organizations can be related to many movies, so we are not going to delete them

        self.stdout.write(self.style.SUCCESS("2. Empty Database"))

    def get_reference(self, Object, name):
        if name == None:
            return None;

        objects = Object.objects.filter(name=name)
        # If Object exist
        if len(objects):
            # Get reference
            object = objects[0]
        else:
            # Create new and get reference
            object = Object(name=name)
            object.save()
        return object

    def save(self):
        # Save each movie = [] item to database
        i = 1
        for movie in self.movies:

            # Save production company
            new_production_company = self.get_reference(Organization, movie["production_company"])

            # Save movie
            new_movie = Movie(name=movie["name"], position=movie["position"], picture=movie["picture"], score=movie["score"], description=movie["description"], production_company=new_production_company)
            new_movie.save()   

            # Save other fields
            for genre_name in movie["genre"]:
                new_genre = self.get_reference(Genre, genre_name)
                new_movie.genre.add(new_genre)

            for director in movie["director"]:
                new_director = self.get_reference(Person, director["person"]["name"])
                new_movie.director.add(new_director)

            for author in movie["author"]:
                new_author = self.get_reference(Person, author["person"]["name"])
                new_movie.author.add(new_author)

            for actor in movie["actor"]:
                new_actor = self.get_reference(Person, actor["person"]["name"])
                new_movie.actor.add(new_actor)

            y = 1
            for critic in movie["critic"]:
                if y > self.max_critics_per_movie:
                    break
                text = critic["reviewBody"]
                url = critic["url"]
                author = self.get_reference(Person, critic["author"]["name"])
                publisher = self.get_reference(Organization, critic["publisher"]["name"])
                new_critic = Critic(text=text, url=url, author=author, publisher=publisher, movie=new_movie)
                new_critic.save()
                y += 1

            self.stdout.write(self.style.SUCCESS('3.'+str(i)+'. Movie saved to database'))
            i += 1

    def handle(self, *args, **options):
        self.crawl()
        self.empty_db()
        self.save()
        self.stdout.write(self.style.SUCCESS('Done'))