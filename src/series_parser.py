import re

SERIES_SEPARATOR_GROUP_REGEX = '([eE]|[xX])'
SERIES_GROUPS_REGEX = r'([0-9]+){}([0-9]+)'.format(SERIES_SEPARATOR_GROUP_REGEX)


class SeriesFilenameParser:

    def __init__(self, filename):
        pattern = re.compile(SERIES_GROUPS_REGEX)
        matched_pattern = pattern.search(filename)
        self._season = matched_pattern.group(1)
        self._episode = matched_pattern.group(3)

    @property
    def season(self):
        return int(self._season)

    @property
    def episode(self):
        return int(self._episode)
