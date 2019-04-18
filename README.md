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
[format]
bitrate=320
codec="mp3"

[meta]
title="test"
artist="test"
year=2019
copyright="2019 test"
```

## License

This project is licensed under the [MIT license](/LICENSE).