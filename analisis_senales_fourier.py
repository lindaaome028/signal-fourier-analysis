import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
Fs = 1000  # Sampling frequency
T = 1/Fs   # Sampling period
L = 1000   # Length of signal

# Time vector
x = np.linspace(0, L*T, L, endpoint=False)

# Creating a signal
f1 = 50   # Frequency of the signal
f2 = 120  # Another frequency
A1 = 0.7  # Amplitude of the first signal
A2 = 1.0  # Amplitude of the second signal
signal = A1 * np.sin(2 * np.pi * f1 * x) + A2 * np.sin(2 * np.pi * f2 * x)

# Plotting the time domain signal
plt.figure(figsize=(10, 4))
plt.plot(x, signal)
plt.title('Signal in Time Domain')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Fourier Transform
Y = np.fft.fft(signal)
P2 = np.abs(Y/L)  # Two-sided spectrum
P1 = P2[:L//2+1]  # One-sided spectrum
P1[1:-1] = 2*P1[1:-1]

# Frequency domain
f = Fs * np.arange(0, (L/2)+1) / L

# Plotting the frequency domain representation
plt.figure(figsize=(10, 4))
plt.plot(f, P1)
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency (f) [Hz]')
plt.ylabel('|P1(f)|')
plt.grid()
plt.show()

# Phase spectrum
phase = np.angle(Y)

# Plotting the phase spectrum
plt.figure(figsize=(10, 4))
plt.plot(f, phase[:L//2+1])
plt.title('Phase Spectrum')
plt.xlabel('Frequency (f) [Hz]')
plt.ylabel('Phase (radians)')
plt.grid()
plt.show()

# Verifying Fourier Transform properties with a unit impulse
impulse = np.zeros(L)
impulse[0] = 1  # Create unit impulse
Y_impulse = np.fft.fft(impulse)

# Frequency domain representation of impulse
P_impulse = np.abs(Y_impulse/L)

# Plotting impulse spectrum
plt.figure(figsize=(10, 4))
plt.plot(f, P_impulse[:L//2+1])
plt.title('Magnitude Spectrum of Unit Impulse')
plt.xlabel('Frequency (f) [Hz]')
plt.ylabel('|P_impulse(f)|')
plt.grid()
plt.show()