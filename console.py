import pdb
from models.albums import Album
from models.artists import Artist
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository


album_1 = Album("Now 100", 2010, "Pop")
album_repository.save(album_1)
album_2 = Album("Now 101", 2011, "Pop")
album_repository.save(album_2)


# results = album_repository.select_all()


# result = album_repository.select(5)


# artist_1 = Artist("Taylor", 27)
# artist_repository.save(artist_1)


# results = artist_repository.select_all()
# pdb.set_trace()

# results = artist_repository.select(2)
# pdb.set_trace()

# artist_repository.delete_all()

new_artist = Artist("Brian", 55)
artist_repository.update(new_artist)

# results = artist_repository.delete(5)
