# ========= Your classes ==========
import random

class Settings:
    def __init__(self, shuffle, repeat):
        self.shuffle = shuffle
        self.repeat = repeat

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __eq__(self, other):
        return isinstance(other, Song) \
               and self.title == other.title \
               and self.artist == other.artist \
               and self.duration == other.duration

    def __str__():
        return "%s - %s: %ds" %(title, artist, duration)

class Playlist:
    def __init__(self, title, songs):
        self._title = title
        self._songs = songs
        self.current_song = 0
        self.played = set()

    def get_title(self):
        return self._title

    def get_song_titles(self):
        list_of_songs=[]
        for s in self._songs:
            list_of_songs.append(s)
            return list_of_songs

    def load_song_by_title(self,title):
        for s in self._songs:
            if s == title:
                return title
            else:
                return None

    def load_next_song(self):
        if Settings.shuffle == True:
            random_song = random.choice(self._songs)
            while random_song in self.played:
                random_song = random.choice(self._songs)
            self.played.add(radnom_song)
            if len(self._songs) == len(self.played):
                self.played = set()
            return random_song
        elif not self.current_song < len(self._songs) and Settings.repeat == True: #
            Spotify._current_song = 0
            song = self.songs[Spotify._current_song]
            Spotify._current_song += 1
            return song
        else:
            if Spotify._current_song < len(self.songs) and Settings.repeat == False:
                song = self.songs[self.current_song]
                self.current_song += 1
                return song
            else:
                print("You reached the end of the playlist.")


class Spotify:
    def __init__(self, playlist, settings):
        self._playlist = Playlist
        self._settings = Settings
        self._current_song = None
        self._is_playing = False

    def get_current_song(self):
        return self._current_song

    def is_playing(self):
        return self._is_playing

    def get_playlist_title():
        return Playlist.get_title()

    def play(self, title=None):
        if not self._is_playing:
            self._current_song = Playlist.load_next_song(Settings.shuffle, Settings.repeat)
            self._is_playing = True
        elif self._current_song != None and self._is_playing == True:
            self._is_playing = True
        else:
            pass

    def pause(self):
        self._is_playing = False

    def next(self):
        self._current_song = Playlist.load_next_song(Settings.shuffle, Settings.repeat)


# =================================

if __name__ == '__main__':
    no_repeat_no_shuffle = Settings(False, False)

    songs = [Song("Hotel California", "Eagles", 390),
             Song("Harder Better Faster Stronger", "Daft Punk", 224),
             Song("2112", "Rush", 1233)]
    playlist = Playlist("MyPlaylist", songs)

    player = Spotify(playlist, no_repeat_no_shuffle)

    assert player.get_playlist_title() == "MyPlaylist"

    assert playlist.get_song_titles() == ["Hotel California", "Harder Better Faster Stronger", "2112"]

    assert playlist.load_next_song(False, False) == Song("Hotel California", "Eagles", 390)
    assert playlist.load_next_song(False, False) == Song("Harder Better Faster Stronger", "Daft Punk", 224)
    assert playlist.load_next_song(False, False) == Song("2112", "Rush", 1233)
    assert not playlist.load_next_song(False, False)

    assert playlist.load_song_by_title("2112") == Song("2112", "Rush", 1233)

    # Reset playlist
    playlist = Playlist("MyPlaylist", songs)

    player = Spotify(playlist, no_repeat_no_shuffle)

    # Should be first song, playing
    player.play()
    assert player.get_current_song() == songs[0]
    assert player.is_playing()

    # Should not change song or playing
    player.play()
    assert player.get_current_song() == songs[0]
    assert player.is_playing()

    # Should not change song, playing is False
    player.pause()
    assert player.get_current_song() == songs[0]
    assert not player.is_playing()

    # Should not change song, playing back to True
    player.play()
    assert player.get_current_song() == songs[0]
    assert player.is_playing()

    # Should change song, playing True
    player.next()
    assert player.get_current_song() == songs[1]
    assert player.is_playing()

    # Should change song, playing True
    player.next()
    assert player.get_current_song() == songs[2]
    assert player.is_playing()

    # No songs left, song == None and playing False
    player.next()
    assert not player.get_current_song()
    assert not player.is_playing()

    # Load song by title
    player.play("2112")
    assert player.get_current_song() == songs[2]
    assert player.is_playing()

    # Previous song was last in playlist, next should return None, playing False
    player.next()
    assert not player.get_current_song()
    assert not player.is_playing()

    # Start playlist
    player.play()
    assert player.get_current_song() == songs[0]
    assert player.is_playing()

    player.next()
    player.next()
    player.next()
    assert not player.get_current_song()
    assert not player.is_playing()

    # When playlist is finished, calling next starts playlist again.
    player.next()
    assert player.get_current_song() == songs[0]
    assert player.is_playing()
