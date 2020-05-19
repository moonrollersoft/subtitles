# SUBTITLES

## What is subtitles for? ##

Just automates the subtitles renaming job.
**subtitles** will try to rename your subtitles matching video files names.

## Requisites ##
* [python](https://www.python.org/downloads/) >= 3.5

## Use ##
Download/clone the project, move inside and execute:
```sh
python fix_subtitles.py -s -p /path/to/my/serie
```
**subtitles** will recursively search all the video and subtitles files under the provided path, then it will rename 
the subtitles as the video files if the name matches (it excludes the format suffix).
 
## Execution options ##
**subtitles** execution options:
* **-p --path** Path to the series/movies
* **-s --series** Fix series subtitles, matching seasons/episodes
* **-m --movies** Fix movies subtitles

### Example ###
Fixing a movie subtitle:
```sh
python fix_subtitles.py -s -m /path/to/my/movie
```

### Extras ###
In order avoid the terminal and ease the usage of **subtitles** in Ubuntu's Nautilus, a Makefile is provided. When 
executed, it will try to install a preconfigured filemanager package, adding two actions to be launched through the 
file manager's context menu. Tested in Ubuntu 18.04.

In the project root execute: 
```sh
make
```

If the execution was successful, you can use the right click on Nautilus and two new options will be displayed: "Fix 
movies" and "Fix series". 


## License
[MIT](LICENSE.txt)


## Contact ##
[moonrollersoft@gmail.com](mailto:moonrollersoft@gmail.com)
