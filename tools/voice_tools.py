#!/usr/bin/env python3
# encoding: utf-8
"""
声音的本质是震动，震动的本质是位移关于时间的函数，波形文件(.wav)中记录了不同采样时刻的位移。
通过傅里叶变换，可以将时间域的声音函数分解为一系列不同频率的正弦函数的叠加，通过频率谱线的特殊分布，建立音频内容和文本的对应关系，
以此作为模型训练的基础。
语音格式： wmv, wma
@summary:
 打印语音通道信息
@since: 2020-5-31
@author: Keefe Wu
@requires: speechrecognition numpy scipy matplotlib
"""

__author__ = 'Keefe Wu'

# -*- encoding:utf-8 -*-
import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf
import matplotlib.pyplot as plt
import speech_recognition as sr


def show_image(src_voicce_path='../data/voice/1.wma'):
    """

    :param src_voicce_path:
    :return:
    """
    sample_rate, sigs = wf.read(src_voicce_path)
    print(sample_rate)  # 8000采样率
    print(sigs.shape)  # (3251,)
    sigs = sigs / (2 ** 15)  # 归一化
    times = np.arange(len(sigs)) / sample_rate
    freqs = nf.fftfreq(sigs.size, 1 / sample_rate)
    ffts = nf.fft(sigs)
    pows = np.abs(ffts)
    plt.figure('Audio')
    plt.subplot(121)
    plt.title('Time Domain')
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Signal', fontsize=12)
    plt.tick_params(labelsize=10)
    plt.grid(linestyle=':')
    plt.plot(times, sigs, c='dodgerblue', label='Signal')
    plt.legend()
    plt.subplot(122)
    plt.title('Frequency Domain')
    plt.xlabel('Frequency', fontsize=12)
    plt.ylabel('Power', fontsize=12)
    plt.tick_params(labelsize=10)
    plt.grid(linestyle=':')
    plt.plot(freqs[freqs >= 0], pows[freqs >= 0], c='orangered', label='Power')
    plt.legend()
    plt.tight_layout()
    plt.show()


def speech_to_text(path_file):
    """
    语音转文本
    :param path_file:
    :return:
    """
    song = AudioSegment.from_mp3(path_file)
    song.export("audio.wav", format="wav")  # 默认是本地路径

    with sr.AudioFile('audio.wav') as source:  # AudioFile 类可以通过音频文件的路径进行初始化，并提供用于读取和处理文件内容的上下文管理器界面。

        audio = r.record(source)  # 从音频文件中获取数据
        print(audio)
        print("Submitting To Speech to Text:")
        determined = sphinx(audio)  # Instead of google, you can use ibm or bing here
        print(determined)
    return determined


if __name__ == '__main__':
    show_image()
