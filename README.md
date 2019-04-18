# Music Transcoder

A ffmpeg wrapper that takes an input file, config file and outputs a file with the format and metadata defined in the config.

## CLI

```
usage: transcode.py [-h] -c CONFIG -f FILE

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG  Config file to use
  -f FILE, --file FILE  A list of files to apply the config to
```

## Config file

```toml
# both bitrate and codec tags are required
[format]
bitrate=320
codec="mp3"

# Only the title meta tag is required
[meta]
title="test"
artist="test"
year=2019
copyright="2019 test" # automatically adds the © symbol
art="test.png" # must be a path to a file!
album_artist="test"
genre="test"
publisher="testing co."
language="eng"
```

## License

This project is licensed under the [MIT license](/LICENSE).