
[sound,fs]=audioread('speech_TRAIN_1/TIMIT_TRAIN_1/DR1/FDAW0/SA1.wav');

N=512; %fenêtre de durée 32 ms (localement stationnaire)
H=N/2; %H est choisi tel que N/H est une puissance de 2
w=hamming(N);
L=fix(length(sound)/H);
short_sound=sound(1:(L*H));

STFT = stft_LG(short_sound,w,N,H);

figure,
im = imagesc(log(abs(STFT).^2))

% imwrite(log(abs(STFT).^2),'saved_image.png')