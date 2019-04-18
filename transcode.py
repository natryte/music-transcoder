import argparse
import toml
import subprocess

def meta_to_command(file, conf):
	if "art" in conf["meta"].keys():
		command = ["ffmpeg", "-i", file, "-i", conf["meta"]["art"], "-map", "0:0", "-map", "1:0", "-c:a", conf["format"]["codec"], "-b:a", str(conf["format"]["bitrate"])+"k", "-id3v2_version", "3", "-metadata:s:v", "title='Album cover'", "-metadata:s:v", "comment='Cover (front)'"]
	else:
		command = ["ffmpeg", "-i", file, "-c:a", conf["format"]["codec"], "-b:a", str(conf["format"]["bitrate"])+"k"]
	
	for data, value in conf["meta"].items():
		if data == "title":
			command.extend(["-metadata", "title="+value])
		elif data == "artist":
			command.extend(["-metadata", "artist="+value])
		elif data == "year":
			command.extend(["-metadata", "year="+str(value)])
		elif data == "copyright":
			command.extend(["-metadata", "copyright="+value])
		elif data == "album":
			command.extend(["-metadata", "album="+value])
		elif data == "album_artist":
			command.extend(["-metadata", "album_artist="+value])
		elif data == "genre":
			command.extend(["-metadata", "genre="+value])
		elif data == "publisher":
			command.extend(["-metadata", "publisher="+value])
		elif data == "language":
			command.extend(["-metadata", "language="+value])

	if conf["format"]["codec"] == "mp3":
		command.append(conf["meta"]["title"]+".mp3")
	elif conf["format"]["codec"] == "aac":
		command.append(conf["meta"]["title"]+".aac")
	elif conf["format"]["codec"] == "ogg":
		command.append(conf["meta"]["title"]+".ogg")

	return command

def transcode(file, format, conf):
	"This takes a file, and transcodes it into the specified format using ffmpeg"
	com = meta_to_command(file, conf)
	print(com)
	subprocess.run(com)

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--config", required=True, help="Config file to use")
ap.add_argument("-f", "--file", required=True, help="A list of files to apply the config to")
args = vars(ap.parse_args())

config=toml.load(args["config"])

transcode(args["file"], config["format"], config)