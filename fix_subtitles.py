#!/usr/bin/python3
import argparse
import os
from pathlib import Path
from shutil import move

from src.files import SeriesFile, MovieFile, VIDEO_FORMATS, SUBTITLE_FORMATS

OLD_SUBS_DIR = 'old_subs'


class SubtitlesFixer:

    def __init__(self, path):
        self._path = path
        self._video_files = self._get_files_recursively(VIDEO_FORMATS)
        self._sub_files = self._get_files_recursively(SUBTITLE_FORMATS)

    def fix(self, fix_options):
        self._move_subs_to_old_dir()
        if 'm' in fix_options:
            self._fix_movies_subs()
        else:
            self._fix_series_subs()

    def _move_subs_to_old_dir(self):
        moved_subtitles = []
        if self._sub_files:
            old_subs_path = os.path.join(self._path, OLD_SUBS_DIR)
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fix subtitles.')
    parser.add_argument('-p', '--path', dest='path', type=str, help='Path to fix subtitles', required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-s', '--series', dest='series', help='Fix series subtitles', action='store_true')
    group.add_argument('-m', '--movies', dest='movie', help='Fix movies subtitles', action='store_true')

    args = parser.parse_args()
    current_path = args.path
    f_options = ''
    f_options += 's' if args.series else ''
    f_options += 'm' if args.movie else ''

    sub_fixer = SubtitlesFixer(current_path)
    sub_fixer.fix(f_options)
