gfskDemod = comm.CPMDemodulator( ...
    'ModulationOrder',2, ...
    'FrequencyPulse','Gaussian', ...
    'BandwidthTimeProduct',0.5, ...
    'ModulationIndex',1, ...
    'BitOutput',true); %Crea el demodulador

filetext=fileread('modulado_hamming7.txt'); %Lee el archivo con ruido y modulacion GFSK
filetext = strrep(filetext, '(', ''); % Elimina el paréntesis  izquierdo
filetext = strrep(filetext, ')', ''); % Elimina el paréntesis derecho
filetext=str2num(filetext)
size(filetext);
tic();% Tiempo que dura demodulando
y = gfskDemod(filetext)


%Demodula el archivo con ruido
tiempo=toc()
plot(real(y))
csvwrite('demodulado7.txt',real(y))