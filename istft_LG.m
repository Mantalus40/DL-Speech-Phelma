function x = istft_LG(X,wa,ws,N,H)

% ISTFT of monochannel signal
%
% x = istft_LG(X,wa,ws,N,H)
%
% Inputs:
% X: N x M matrix containing the STFT coefficients with N frequency bins
% and M time frames
% wa: N-point analysis window (as used in stft_LG)
% ws: N-point synthesis window
% N: size of analysis window
% H: hop size
%
% Output:
% x: monochannel output signal
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Laurent Girin - GIPSA-lab - 2018
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

M = size(X,2);       % number of TF frames
L = M*H + N - H;     % size of signal
x = zeros(1,L);
wa = wa(:)';
ws = ws(:)';

% calculating the 'normalization window'
P = N/H;
w = zeros(1,H);
for p = 1:P
    w = w + wa(1+(p-1)*H:p*H).*ws(1+(p-1)*H:p*H);
end;

for m = 1 : M
    frame = real(ifft(X(:,m),N)); frame = frame(:)';  % ifft of frame m
    ind = 1 + (m-1)*H: N + (m-1)*H;
    x(ind) = x(ind) + frame.*ws;                % OLA
    ind = 1 + (m-1)*H: H + (m-1)*H;
    x(ind) = x(ind)./w;                         % window effect normalization
end

x = x(1 + N - H : end - N + H);           % back to original signal size

return;