import wave
from math import sqrt
import numpy as np

def rms(arr, window_size):
    ans = []
    n = len(arr)
    if (window_size > n):
        return ans
    
    def compute_rms(x):
        return sqrt(x) / window_size
    
    cur = 0

    for i in range(window_size):
        cur += arr[i] * arr[i]
    ans.append(compute_rms(cur))
    for i in range(1, n - window_size + 1):
        cur -= arr[i - 1] * arr[i - 1]
        cur += arr[i + window_size - 1] * arr[i + window_size - 1]
        ans.append(compute_rms(cur))
    
    return ans

def PSD(arr, window_size_fft, window_size_psd):
    ffts = []
    n = len(arr)
    
    for i in range(0, n - window_size_fft + 1):
        ffts.append(np.fft.fft(arr[i:i+window_size_fft]))
    
    psds = []

    n_fft = len(ffts)
    for i in range(0, n_fft - window_size_psd + 1):
        cur = ffts[i]
        for fft in range(i + 1, i + window_size_psd):
            for x in range(len(fft)):
                cur[x] += fft[x]

def main():
    file = wave.open('01.wav', 'rb')
    n = file.getnframes()
    arr = list(file.readframes(n))



main()
