"""
离线语音引擎
pyttsx3 是一个跨平台的文本转语音（TTS）工具，支持 Windows、MacOS 和 Linux 系统，能够实现离线语音合成并调整语速、音量和音色。
    1.运行前需要安装第三方库 pyttsx3，可使用以下命令进行安装：
        pip install pyttsx3
    2.若安装过程中出现超时问题，可使用国内镜像源进行安装，命令如下：
        pip install -i https://mirrors.aliyun.com/pypi/simple/ pyttsx3
    Linux Ubuntu 系统安装 espeak-ng 库
        sudo apt update && sudo apt install espeak-ng libespeak1
    MacOS 系统安装 espeak-ng 库
        brew install espeak-ng

"""

import os
import pyttsx3


def speak_text(text = "学习Python, 热爱Python"):
    """
    该函数用于使用 pyttsx3 库将传入的文本转换为语音并播放。
        1.参数:
            text (str): 要转换为语音的文本内容。
    """
    # 初始化语音引擎
    engine = pyttsx3.init()

    # 可以通过 engine.setProperty('rate', new_rate) 方法来调整语音的语速。
    # new_rate 是一个整数，表示每分钟的单词数。
    # 例如，默认语速可能是 150，若想加快语速，可以将其设置为 200。
    engine.setProperty('rate', 150)

    # engine.setProperty('volume', new_volume) 来设置音量。
    # new_volume 是一个介于 0.0（静音）和 1.0（最大音量）之间的浮点数。
    # 比如，engine.setProperty('volume', 0.8) 会将音量设置为最大音量的 80%。
    engine.setProperty('volume', 0.8)

    # 获取可用的语音列表
    voices = engine.getProperty('voices')
    for index, voice in enumerate(voices):
        print(index, voice.id, voice.name)

    # 设置需要朗读的文本。
    # text = "Hello, this is a simple text-to-speech example."
    # 指定要转换为语音的文本内容。
    engine.say(text)
    # 执行语音播放任务。
    engine.runAndWait()

    engine.stop()


def changing_voice_rate_volume():
    """
    Changing Voice , Rate and Volume:
    """
    engine = pyttsx3.init() # object creation

    # RATE
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    print (rate)                        # printing current voice rate
    engine.setProperty('rate', 125)     # setting up new voice rate

    # VOLUME
    volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
    print (volume)                          # printing current volume level
    engine.setProperty('volume',1.0)        # setting up volume level  between 0 and 1

    # VOICE
    voices = engine.getProperty('voices')       # getting details of current voice
    #engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
    #engine.setProperty('voice', voices[5].id)  # changing index, changes voices. o for male
    # engine.setProperty('voice', voices[180].id)   # changing index, changes voices. 1 for female
    engine.setProperty('voice', 'com.apple.voice.compact.zh-CN.Tingting')   # changing index, changes voices. 1 for female
    # for index, voice in enumerate(voices):
    #     if "zh-CN" not in voice.id:
    #         continue
    #     engine.setProperty('voice', voice.id)
    #     print(index, voice.id, voice.name)
    #     engine.say("学习Python, 热爱Python")

    engine.say("Hello World!")
    engine.say('My current speaking rate is ' + str(rate))
    engine.say("学习Python, 热爱Python")
    engine.say("It's a beautiful day.")
    engine.runAndWait()
    engine.stop()


def text_to_mp3():
    """
    文本转换为语音
    """
    engine = pyttsx3.init("espeak") # object creation
    engine.setProperty('voice', 'english+f3')  # 根据需要调整语音和方言设置

    # RATE
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    print (rate)                        # printing current voice rate
    engine.setProperty('rate', 125)     # setting up new voice rate

    # VOLUME
    volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
    print (volume)                          # printing current volume level
    engine.setProperty('volume',1.0)        # setting up volume level  between 0 and 1

    # VOICE
    voices = engine.getProperty('voices')       # getting details of current voice
    #engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
    engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female

    # Saving Voice to a file
    # On Linux, make sure that 'espeak-ng' is installed
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(current_dir, "text_audio.mp3")
    text = "Hello, World!"
    engine.save_to_file(text, filename)
    engine.runAndWait()


def main():
    print('python ttsx3 study...')

    # 离线语音引擎
    speak_text()
    changing_voice_rate_volume()
    text_to_mp3()


if __name__ == '__main__':
    main()
