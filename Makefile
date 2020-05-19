from-binary:
	sudo dpkg -i extras/filemanager-actions/filemanager-actions_3.4-3_amd64.deb
	$(MAKE) installed

download:
	sudo add-apt-repository -y ppa:daniel-marynicz/filemanager-actions
	sudo apt update -y
	sudo apt install -y filemanager-actions-nautilus-extension
	$(MAKE) installed

installed:
	sudo cp fix_subtitles.py /usr/bin/
	sudo mkdir -p ~/.local/share/file-manager/actions/
	sudo cp extras/filemanager-actions/movies_entry.desktop ~/.local/share/file-manager/actions/
	sudo cp extras/filemanager-actions/series_entry.desktop ~/.local/share/file-manager/actions/
