import spotipy
from scrapper import ScrapeData


class SpotifyPlaylistMaker:
    def __init__(self, username, client_id, client_secret) -> None:
        """
        spotify username , app client_id , client_secret
        """
        self.scope = "playlist-modify-public"
        self.username = username
        self.token = spotipy.util.prompt_for_user_token(
            scope=self.scope,
            username=self.username,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri="http://127.0.0.1:8000/",
        )
        self.spotifyObject = spotipy.Spotify(auth=self.token)

    def create_playlist(self, name):
        """
        name = your play list name
        create your play list from here
        """
        self.play_list = self.spotifyObject.user_playlist_create(
            user=self.username, name=name
        )
        return self.play_list

    def scrape_data(self, url):
        """
        url = youtube play list url
        """
        scraper = ScrapeData(url)
        scraper.get_songs_title()
        scraper.dump_songs()

    def add_songs_to_playlist(self):
        self.songs = list()
        with open("songs.txt", "r") as file:
            for song in file.readlines():
                result = self.spotifyObject.search(song)
                try:
                    self.songs.append(result["tracks"]["items"][0]["uri"])
                except:
                    pass
        self.spotifyObject.user_playlist_add_tracks(
            user=self.username, playlist_id=self.play_list["id"], tracks=self.songs
        )
