#!/usr/bin/python3
import argparse
import copy
import os
import re
from pathlib import Path
from shutil import copyfile, move

VIDEO_FORMATS = [".mp4", ".mkv", ".avi", ".mov", ".wmv"]
SUBTITLE_FORMATS = [".srt", ".sub"]
SERIES_REGEX = r'[sS][0-9][0-9][eE][0-9][0-9]|[0-9][0-9][xX][0-9][0-9]'


def fix_subtitles(path, options):
    video_files = get_files_recursively(path, VIDEO_FORMATS)
    sub_files = get_files_recursively(path, SUBTITLE_FORMATS)
    if 'm' in options:
        fixed_subs = fix_movies_subs(video_files, sub_files)
    else:
        fixed_subs = fix_series_subs(video_files, sub_files)

    move_subs_to_fixed_dir(path, fixed_subs)


def get_files_recursively(path, formats):
    path_files = []
    for file_format in formats:
        path_files.extend(Path(path).rglob("*{}".format(file_format)))

    files = {str(s): s for s in path_files}

    return files


def fix_movies_subs(video_files, sub_files):
    fixed_subs = {}
    for video in video_files:
        for subtitle in sub_files:
            new_sub = str(video_files[video].with_suffix('')) + sub_files[subtitle].suffix
            if not os.path.exists(new_sub):
                copyfile(subtitle, new_sub)
            fixed_subs[subtitle] = sub_files[subtitle]
            break

    return fixed_subs


def fix_series_subs(video_files, sub_files):
    fixed_subs = {}
    for video in video_files:
        pattern = re.compile(SERIES_REGEX)
        v_matched_pattern = pattern.search(video)
        if v_matched_pattern:
            v_season_episode = v_matched_pattern.group().lower()
            for subtitle in copy.deepcopy(sub_files):
                s_matched_pattern = pattern.search(subtitle)
                if s_matched_pattern:
                    s_season_episode = s_matched_pattern.group().lower()
                    if v_season_episode == s_season_episode:
                        new_sub = str(video_files[video].with_suffix('')) + sub_files[subtitle].suffix
                        if not os.path.exists(new_sub):
                            copyfile(subtitle, new_sub)
                            fixed_subs[subtitle] = sub_files[subtitle]
                        del sub_files[subtitle]
                        break

    return fixed_subs


def move_subs_to_fixed_dir(path, subs):
    if subs:
        fixed_subs_path = os.path.join(path, 'fixed_subs')
        Path(fixed_subs_path).mkdir(exist_ok=True)
        for subtitle in subs:
            move(subtitle, os.path.join(fixed_subs_path, subs[subtitle].name))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fix subtitles.')
    parser.add_argument('-p', '--path', dest='path', type=str, help='Path to fix subtitles', required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-s', '--series', dest='series', help='Fix series subtitles', action='store_true')
    group.add_argument('-m', '--movies', dest='movie', help='Fix movies subtitles', action='store_true')

    args = parser.parse_args()
    current_path = args.path
    format_options = ''
    format_options += 's' if args.series else ''
    format_options += 'm' if args.movie else ''

    fix_subtitles(current_path, format_options)
