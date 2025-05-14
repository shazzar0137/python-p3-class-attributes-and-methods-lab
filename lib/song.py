class Song:
    artists = set()
    genre_count = dict()
    artist_count = dict()
    count = 0
    genres = set()


    def __init__(self, name, artist, genre):
        Song.count_increment()
        self.name = name
        self.genre = genre
        self.artist = artist
        Song.get_genre(self.genre)
        Song.get_artist(self.artist)
        Song.add_genre(self.genre)
        Song.add_artist(self.artist)

    @classmethod
    def get_genre(cls, genre):
        cls.genres.add(genre)

    @classmethod
    def show_artist(cls):
        print(list(cls.genres))
 

    @classmethod
    def add_artist(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    @classmethod
    def add_genre(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def count_increment(cls, increment=1):
        cls.count += increment
    @classmethod
    def get_artist(cls, artist):
        cls.artists.add(artist)

    @classmethod
    def show_artist(cls):
        print(list(cls.artists))