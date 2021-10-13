from gtts import gTTS
import speech_recognition as sr
import playsound
import random
import time


def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        our_speech = r.recognize_google(audio, language="ru")
        print('Вы: ' + our_speech)
        return our_speech
    except sr.UnknownValueError:
        return 'Ошибка'
    except sr.RequestError as e:
        return 'Ошибка'


def parsing_command(command):
    command = command.lower()
    if 'привет' in command:
        say_message('Привет, друг!', 'hifriend.mp3')
    elif 'пока' in command:
        say_message('До встречи.', 'goodbye.mp3')
        exit()
    elif 'ошибка' in command:
        pass
    else:
        say_message('Скажи что-то другое', "zaebalo.mp3")
        # zaebalo - необходимое название. С названием файла idont, idontunderstand и так далее вывдавало ошибку


def say_message(message, file_voice_name):
    playsound.playsound(file_voice_name)
    print("Голосовой ассистент: " + message)


def main():
    while True:
        command = listen_command()
        parsing_command(command)


if __name__ == '__main__':
    main()
