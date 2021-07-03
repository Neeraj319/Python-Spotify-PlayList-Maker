import spotipy

scope = "playlist-modify-public"
username = "your username"
token = spotipy.util.prompt_for_user_token(
    scope=scope,
    username=username,
    client_id="your client id",
    client_secret="your client secret",
    redirect_uri="http://127.0.0.1:8000/",
)
spotifyObject = spotipy.Spotify(auth=token)
playListName = input("enter playList name:")
play_list = spotifyObject.user_playlist_create(user=username, name=playListName)


songs = list()
with open("songs.txt", "r") as file:
    # i have created a file named something where all my songs are
    for song in file.readlines():
        result = spotifyObject.search(song)
        try:
            songs.append(result["tracks"]["items"][0]["uri"])
        except:
            pass
spotifyObject.user_playlist_add_tracks(
    user=username, playlist_id=play_list["id"], tracks=songs
)
# note you can only add 100 tracks at once if you want to add more i will edit the code later
