current_dir_name=$${PWD\#\#*/}

all:
	cp -rf "../$(current_dir_name)" ~/
	> ~/.local/share/nautilus/scripts/fix_series_subtitles.sh
	chmod +x ~/.local/share/nautilus/scripts/fix_series_subtitles.sh
	echo python3 ~/\"$(current_dir_name)\"/fix_subtitles.py -s -p '"$$(pwd)"' >> ~/.local/share/nautilus/scripts/fix_series_subtitles.sh
	> ~/.local/share/nautilus/scripts/fix_movies_subtitles.sh
	chmod +x ~/.local/share/nautilus/scripts/fix_movies_subtitles.sh
	echo python3 ~/\"$(current_dir_name)\"/fix_subtitles.py -m -p '"$$(pwd)"' >> ~/.local/share/nautilus/scripts/fix_movies_subtitles.sh

uninstall:
	rm -rf ~/"$(current_dir_name)"
	rm -f ~/.local/share/nautilus/scripts/fix_series_subtitles.sh
	rm -f ~/.local/share/nautilus/scripts/fix_movies_subtitles.sh

# GNOME log errors: journalctl -xe
