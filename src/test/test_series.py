import os
import pytest
import random
import shutil
from pathlib import Path

from fix_subtitles import SubtitlesFixer, OLD_SUBS_DIR

# Videos and subs match 1x1 at least with season and episode number
VIDEOS = [
    "{}s01e01{}.mp4",
    "{}s01E02{}.mkv",
    "{}S02e03{}.avi",
    "{}S02E04{}.mov",
    "{}03e11{}.wmv",
    "{}s03E20{}.mkv",
    "{}04x354{}.mp4",
    "{}342504X88{}.mkv",
    "{}05x00{}.avi",
    "{}3x3{}.mov",
    "{}4x04{}.wmv",
    "{}12x1{}.mp4",
    "{}e13x15{}.mkv"
]

SUBS = [
    "{}s13e15{}.srt",
    "{}s12E01{}.sub",
    "{}S04e04{}.srt",
    "{}S03E03{}.sub",
    "{}05e00{}.srt",
    "{}s342504E88{}.sub",
    "{}4x354{}.srt",
    "{}03X20{}.sub",
    "{}03x11{}.srt",
    "{}2x4{}.sub",
    "{}2x03{}.srt",
    "{}01x1{}.sub",
    "{}1x02{}.srt"
]


@pytest.fixture(scope="module")
def series_fixture():
    test_dir = './test_subs'
    subs_dir = 'subs'
    print('Setup, creating dir: "{}" with video and subtitle files'.format(test_dir))
    test_subs_dir = os.path.join(test_dir, subs_dir)
    Path(test_dir).mkdir(exist_ok=True)
    Path(test_subs_dir).mkdir(exist_ok=True)

    formatted_videos = []
    for v in VIDEOS:
        video = v.format(generate_random_str(), generate_random_str())
        formatted_videos.append(video)
        video_file = os.path.join(test_dir, video)
        Path(video_file).touch()

    for s in SUBS:
        sub = s.format(generate_random_str(), generate_random_str())
        sub_file = os.path.join(test_subs_dir, sub)
        Path(sub_file).touch()

    yield test_dir, subs_dir, formatted_videos

    print('Teardown, removing dir: "{}" dir'.format(test_dir))
    shutil.rmtree(test_dir, ignore_errors=True)


def generate_random_str():
    non_numeric_ascii_range = (58, 200)
    return "".join([chr(n) for n in random.sample(range(*non_numeric_ascii_range), random.randint(0, 30))])


def test_series(series_fixture):
    test_path, subs_dir, formatted_videos = series_fixture
    sub_fixer = SubtitlesFixer(test_path)
    sub_fixer.fix('s')
    assert len(list(Path(os.path.join(test_path, subs_dir)).rglob('*'))) == 0
    assert len(list(Path(os.path.join(test_path, OLD_SUBS_DIR)).rglob('*'))) == len(SUBS)
    for video in formatted_videos:
        video_path = Path(os.path.join(test_path, video))
        assert os.path.exists(video_path.with_suffix(".srt")) or os.path.exists(video_path.with_suffix(".sub"))
