import subprocess
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-v", "--video", dest="video_name",
                  help="enter the name of the video or its path, for example [test.wmv]")
(options, args) = parser.parse_args()

video_name = options.video_name

def run(video_name):
    id_name = subprocess.getoutput('weebp\\wp id')
    subprocess.call(f'weebp\\wp run mpv\\mpv --wid={id_name} "{video_name}" --loop=inf --player-operation-mode=pseudo-gui --force-window=yes -no-audio', shell=True)

run(video_name)