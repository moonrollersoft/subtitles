import os
from pathlib import Path
from shutil import move

from src.files import VIDEO_FORMATS, SUBTITLE_FORMATS, MovieFile, SeriesFile

ORIGINAL_SUBS_DIR = 'original_subs'


class SubtitlesFixer:

    def __init__(self, path):
        self._path = path
        self._video_files = self._get_files_recursively(VIDEO_FORMATS)
        self._sub_files = self._get_files_recursively(SUBTITLE_FORMATS)

    def fix_movies(self):
        self._move_subs_to_original_dir()
        self._fix_movies_subs()

    def fix_series(self):
        self._move_subs_to_original_dir()
        self._fix_series_subs()

    def _move_subs_to_original_dir(self):
        moved_subtitles = []
        if self._sub_files:
            old_subs_path = os.path.join(self._path, ORIGINAL_SUBS_DIR)
            Path(old_subs_path).mkdir(exist_ok=True)
            for subtitle in self._sub_files:
                new_sub = os.path.join(old_subs_path, subtitle.name)
                move(subtitle, new_sub)
                moved_subtitles.append(Path(new_sub))

        self._sub_files = moved_subtitles

    def _get_files_recursively(self, formats):
        path_files = []
        for file_format in formats:
            path_files.extend(Path(self._path).rglob("*{}".format(file_format)))

        return path_files

    def _fix_movies_subs(self):
        video_files = [MovieFile(s) for s in self._video_files]
        sub_files = [MovieFile(s) for s in self._sub_files]
        for video in video_files:
            for subtitle in sub_files[:1]:
                new_sub = video.path.with_suffix(subtitle.path.suffix)
                new_sub.touch()

    def _fix_series_subs(self):
        video_files = [SeriesFile(str(s)) for s in self._video_files]
        sub_files = {SeriesFile(str(s)): SeriesFile(str(s)) for s in self._sub_files}
        for video in video_files:
            try:
                subtitle = sub_files[video]
                new_sub = video.path.with_suffix(subtitle.path.suffix)
                new_sub.touch()
            except KeyError:
                pass
