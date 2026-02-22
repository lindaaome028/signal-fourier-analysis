% analisis_completo_matlab.m
% MATLAB Code for Fourier Signal Analysis

% Define the signal parameters
Fs = 1000;            % Sampling frequency
T = 1/Fs;             % Sampling period
L = 1000;             % Length of signal

% Create a time vector
t = (0:L-1)*T;        % Time vector

% Generate a sample signal (sine wave)
f = 50;               % Frequency of the sine wave
x = 0.7*sin(2*pi*f*t);  % Signal

% Compute the Fourier Transform
Y = fft(x);

% Compute the two-sided spectrum P2
P2 = abs(Y/L);

% Compute the single-sided spectrum P1
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);

% Define the frequency domain f
f = Fs*(0:(L/2))/L;

% Plot the results
figure;
plot(f,P1);

title('Single-Sided Amplitude Spectrum of x(t)');
xlabel('Frequency (f) [Hz]');
ylabel('|P1(f)|');

% Save the figure
saveas(gcf, 'spectrum.png');

