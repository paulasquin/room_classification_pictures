import subprocess
import urllib.request
import socket
import os


def get_topics():
    p = subprocess.Popen(["ls"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p2 = subprocess.Popen(['grep', '.txt'], stdin=p.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    p.stdout.close()  # Allow proc1 to receive a SIGPIPE if proc2 exits.
    out, err = p2.communicate()
    names = out.decode('utf-8')
    names = names.split('\n')
    names.pop()  # We delete last, empty, element
    return names


def download_images(filename):
    jpgPath = "../JPG"

    if not os.path.isdir(jpgPath):
        os.mkdir(jpgPath)

    f = open(filename, 'r')
    #Extracting room type
    room_name = filename.split("_")[0]
    print(room_name)
    #Creation directory for pictures
    try:
        os.mkdir(jpgPath + "/" + str(room_name))
    except:
        print("folder " + str(room_name) + " already exist")

    #At maximum, we will wait for 3 seconds for the image reception
    socket.setdefaulttimeout(3)

    i = 0
    for ligne in f:
        ligne = ligne.replace("\n", "")
        filepath = jpgPath + "/" + str(room_name) + "/" + str(room_name) + "_" + str(i) + ".jpg"
        try:
            urllib.request.urlretrieve(ligne, filepath)
            try:
                img = open(filepath, 'rb')
                imgdata = img.read()
                if imgdata.startswith(b'\xff\xd8'):
                    img.close()
                    print(str(i) + " : OK")
                    i += 1
                else:
                    img.close()
                    os.remove(filepath)
            except:
                os.remove(filepath)
        except:
            print(str(i) + " : ko")

    f.close()

def main():
    for topic in get_topics():
        download_images(topic)

if __name__ == '__main__':
    main()
