import argparse
import toml
import subprocess

def meta_to_command(file, conf):
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
	# command.append(conf["meta"]["title"])
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