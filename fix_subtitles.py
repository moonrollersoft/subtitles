#!/usr/bin/python3
import argparse

from src.subtitles_fixer import SubtitlesFixer


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fix subtitles.')
    parser.add_argument('-p', '--path', dest='path', type=str, help='Path to fix subtitles', required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-s', '--series', dest='series', help='Fix series subtitles', action='store_true')
    group.add_argument('-m', '--movies', dest='movie', help='Fix movies subtitles', action='store_true')

    args = parser.parse_args()
    current_path = args.path

    sub_fixer = SubtitlesFixer(current_path)
    if args.series:
        sub_fixer.fix_series()
    else:
        sub_fixer.fix_movies()
