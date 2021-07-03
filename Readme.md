# Python Spotify Playlist Maker

This is a scraper made with python that uses Selenium to scrape the data from youtube
and add makes that playlist in your spotify account

To use this you first need to create a spotify developer account after that

- create a app from spotify developer page
- you need to get the client id client secret of your app and your spotify username
- you need to edit the settings of your app and add there redirect URI to http://127.0.0.1:8000/
- this project depends upon the firefox browser so it won't work with others

---

Installation

```
you need python 3.6+ installed
pip install selenium
you also need gecko driver installed in your pc
```

---

Demo

```
spotify_instance = SpotifyPlaylistMaker(username, client_id, client_secret)
spotify_instance.create_playlist(playlist_name , public=True)
spotify_instance.add_songs_to_playlist()
```

- It's not my fault that if songs don't get added to your playlist . This is probably because of Spotify's search did not recognized your song title which lead to the song not getting added to the play list . This issue will happen in most cases since the song title in YouTube and spotify are miss matched or the song is not available on Spotify
