# SUBTITLES

## What is subtitles for? ##

Just automates the subtitles renaming job.
**subtitles** will try to rename your subtitles matching video files names.

## Requisites ##
* [python](https://www.python.org/downloads/) >= 3.5

## Use ##
Download/clone the project, move inside:
 ```sh
 cd /subtitles
```
and execute:
```sh
python fix_subtitles.py -s -p /path/to/my/series/dir
```
**subtitles** will recursively search all the video and subtitles files under 
the provided path, then it will try to rename the subtitle as the video files 
if the season/episode matches.
 
## Execution options ##
**subtitles** execution options:
* **-p --path** Path to the series/movies
* **-s --series** Fix series subtitles, matching seasons/episodes
* **-m --movies** Fix movies subtitles

## Examples ##
Fixing series subtitles:
```sh
python fix_subtitles.py -s -p /path/to/my/series
```

Fixing a movie subtitle:
```sh
python fix_subtitles.py -m -p /path/to/my/movie
```

## Extras ##
In order avoid the terminal and ease the usage of **subtitles** in Ubuntu's 
Nautilus file manager, a Makefile is provided. When executed, you will be able
to use **subtitles** right-clicking on any file, being inside the series/movie directory
you want to fix. Tested in Ubuntu 18.04.

### Installation ###
In the project root execute: 
```sh
make
```
If the execution was successful, you can got to the series dir you need to fix and
right-click on any file and two new options will be displayed inside the "Scripts" 
option: "fixseries" and "fixmovies".

![alt text](https://github.com/moonrollersoft/subtitles/blob/master/extras/images/fix_example_1.png "Fix example 1")

![alt text](https://github.com/moonrollersoft/subtitles/blob/master/extras/images/fix_example_2.png "Fix example 2")

### Uninstall ###
In the project root execute: 
```sh
make uninstall
```


## Disclaimer ##
All the original subtitles are stored inside a new "original_subs" directory, so do not worry 
if something goes wrong or you click on "fixmovies" and you meant "fixseries", you can recover 
the original ones.

## Test ##
Execute:
```sh
pip install -r src/test/requirements-test.txt
pytest src/test/
```


## License
[MIT](LICENSE.txt)


## Contact ##
[moonrollersoft@gmail.com](mailto:moonrollersoft@gmail.com)
