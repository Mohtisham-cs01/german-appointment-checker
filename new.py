import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from pydub import AudioSegment
from pydub.playback import play
import os
 
# URL to be requested
URL = 'https://service2.diplo.de/rktermin/extern/choose_categoryList.do?locationCode=isla&realmId=108&request_locale=en'



def play_sound(filename):
    # Get the path to the sound file
    sound_file_path = os.path.join(os.path.dirname(__file__), filename)

    # Load the audio file
    sound = AudioSegment.from_mp3(sound_file_path)

    # Play the audio file
    play(sound)

# Function to check the page and print HTML content
def print_page_html(): 
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    wrapper = soup.find(class_='wrapper')
    # print(wrapper)
    if wrapper:
        divs = [child for child in wrapper.find_all('div') if 'study'.lower() in child.get_text().strip().lower()]
        print(divs)
        if len(divs) >= 1:
            print("Alert: Divs with 'study' found")
            while True:
                play_sound("success.wav")
                time.sleep(0.5)
                print("🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩🥶🥶🤩🤩")
                print("_____________________Got Response_____________________" , datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        else:
            print("😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇___No Response___😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇😇" , datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # print(wrapper)


# Call the function to print HTML content
while True:
    try:
        print_page_html()
    except:
        play_sound("err.wav")  
        play_sound("err.wav") 
        time.sleep(2)
        continue          
    # print_page_html()
    time.sleep(25)
