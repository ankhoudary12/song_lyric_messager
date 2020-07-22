from py_imessage import imessage
from time import sleep

phone_num = ''

def get_lyrics(txt_file):

    with open(txt_file) as file:
        lyrics = [line.strip() for line in file]

    return lyrics


def send_messages(lyrics, phone_num):

    for lyric in lyrics:
        imessage.send(phone_num, lyric)
        sleep(0.5)

def main():

    lyrics = get_lyrics('lyrics.txt')

    send_messages(lyrics, phone_num)

if __name__ == '__main__':

    main()
