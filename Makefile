current_dir = $(shell pwd)

all:
	cp -rf ../subtitles ~/
	> ~/.local/share/nautilus/scripts/fix_series_subtitles.sh
	chmod +x ~/.local/share/nautilus/scripts/fix_series_subtitles.sh
	echo python3 ~/subtitles/fix_subtitles.py -s -p "\$$(pwd)" >> ~/.local/share/nautilus/scripts/fix_series_subtitles.sh
	> ~/.local/share/nautilus/scripts/fix_movies_subtitles.sh
	chmod +x ~/.local/share/nautilus/scripts/fix_movies_subtitles.sh
	echo python3 ~/subtitles/fix_subtitles.py -m -p "\$$(pwd)" >> ~/.local/share/nautilus/scripts/fix_movies_subtitles.sh

# GNOME log errors: journalctl -xe
