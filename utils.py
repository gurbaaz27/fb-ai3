import pyaudio
import wave
from wit import Wit


class Speech2Intent:

    def __init__(self, access_token):

        self.client = Wit(access_token)
        self.headers = {'authorization': 'Bearer '+ access_token, 'Content-Type': 'audio/wav'} 


    def recognize_speech(self, AUDIO_FILENAME, num_seconds = 4):
    
        self.record_audio(num_seconds, AUDIO_FILENAME) # record audio of specified length in specified audio file
        audio = self.read_audio(AUDIO_FILENAME) # reading audio
        text = self.client.speech(audio, self.headers)['text']

        return self.client.message(text)['intents'][0]['name']


    def record_audio(self,RECORD_SECONDS, WAVE_OUTPUT_FILENAME):

        #--------- SETTING PARAMS FOR OUR AUDIO FILE ------------#
        FORMAT = pyaudio.paInt16    # format of wave
        CHANNELS = 2                # no. of audio channels
        RATE = 44100                # frame rate
        CHUNK = 1024                # frames per audio sample
        #--------------------------------------------------------#
        
        # creating PyAudio object
        audio = pyaudio.PyAudio()
        
        # open a new stream for microphone
        # It creates a PortAudio Stream Wrapper class object
        stream = audio.open(format=FORMAT,channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)


        #----------------- start of recording -------------------#
        print("Listening...")

        # list to save all audio frames
        frames = []

        for i in range(int(RATE / CHUNK * RECORD_SECONDS)):
            # read audio stream from microphone
            data = stream.read(CHUNK)
            # append audio data to frames list
            frames.append(data)

        #------------------ end of recording --------------------#   
        print("Finished listening.")
        
        stream.stop_stream()    # stop the stream object
        stream.close()          # close the stream object
        audio.terminate()       # terminate PortAudio

        #------------------ saving audio ------------------------#

        # create wave file object
        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')

        # settings for wave file object
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))

        # closing the wave file object
        waveFile.close()


    def read_audio(self, WAVE_FILENAME):

        with open(WAVE_FILENAME, 'rb') as f:
            audio = f.read()
        
        return audio

    