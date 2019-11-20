function X = stft_LG(x,w,N,H)

% STFT of monochannel signal
%
% X = stft_LG(x,w,N)
%
% Inputs:
% x: monochannel input signal
% w: N-point analysis window
% N: size of analysis window
% H: hop size
%
% Output:
% X: N x M matrix containing the STFT coefficients with N frequency bins
% and M time frames
%
% Note: this code and corresponding istft_LG.m work well if:
%   - the size of x is a multiple of H.
%   - N/H is a power of 2.
%   It may work for other conditions, but this is not guaranteed.
%   The important point is that it works for 50%-overlap and for
%   75%-overlap... (but not for 25%-overlap :-(
%   Also, if you want perfect reconstruction analysis-synthesis, choose
%   carefully the analysis and synthesis window. It is OK for sinus window.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Laurent Girin - GIPSA-lab - 2017
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

L = length(x);
x = x(:)'; w = w(:)';
x =[zeros(1,N-H) x zeros(1,N-H)];  % zero-padding
M = L/H + N/H - 1;      % number of TF frames
X = zeros(N,M);

for m = 1 : M
    frame = x(1 + (m-1)*H: N + (m-1)*H).*w; % framing
    X(:,m) = fft(frame);
end

return;