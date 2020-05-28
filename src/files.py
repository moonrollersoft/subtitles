from pathlib import Path

from src.series_parser import SeriesFilenameParser

VIDEO_FORMATS = [".mp4", ".mkv", ".avi", ".mov", ".wmv"]
SUBTITLE_FORMATS = [".srt", ".sub"]


class FilmFile:

    def __init__(self, filename):
        self._path = Path(filename)
        self.type = self._path.suffix.lower()

    @property
    def path(self):
        return self._path

    def __str__(self):
        return str(self._path)


class MovieFile(FilmFile):
    pass


class SeriesFile(FilmFile):

    def __init__(self, filename):
        super().__init__(filename)
        self._parser = SeriesFilenameParser(filename)
        self._season = self._parser.season
        self._episode = self._parser.episode

    @property
    def season(self):
        return self._season

    @property
    def episode(self):
        return self._episode

    def __eq__(self, other):
        if type(other) != SeriesFile:
            return False

        return self.season == other.season and self.episode == other.episode

    def __hash__(self):
        return hash((str(self.season), self.episode))
