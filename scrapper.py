from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ScrapeData:
    songs = []

    def __init__(self, url) -> None:
        """
        pass your playlist url here only initializes the browser
        """
        assert "https://www.youtube.com/watch?v=" in url, "only youtube url"
        self.url = url
        self.browser = webdriver.Firefox()

    def get_songs_title(self):
        """
        get songs title from here this is only limted to 28 songs idk why
        """
        self.browser.get(self.url)
        titles = self.browser.find_elements_by_id("video-title")
        self.songs = [i.get_attribute("innerText") for i in titles]

    def dump_songs(self):
        """'
        dump your songs title in songs.txt file
        """
        with open("songs.txt", "w") as file:
            for song_title in self.songs:
                file.write(song_title + "\n")


if __name__ == "__main__":
    scraper = ScrapeData(
        "https://www.youtube.com/watch?v=ky0N23MKs_k&list=RDky0N23MKs_k&start_radio=1"
    )
    scraper.get_songs_title()
    scraper.dump_songs()
