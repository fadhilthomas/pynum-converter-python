disp(char({' _   _                  _____                          _            ' ...
'| \ | |                / ____|                        | |           ' ...
'|  \| |_   _ _ __ ___ | |     ___  _ ____   _____ _ __| |_ ___ _ __ ' ...
'| . ` | | | | `_ ` _ \| |    / _ \| `_ \ \ / / _ \ `__| __/ _ \ `__|' ...
'| |\  | |_| | | | | | | |___| (_) | | | \ V /  __/ |  | ||  __/ |   ' ...
'|_| \_|\__,_|_| |_| |_|\_____\___/|_| |_|\_/ \___|_|   \__\___|_|   ' ...
'' ...
'Oleh: Muhammad Thomas Fadhila Yahya' ...
'::::::::::::::::::::::::Input::::::::::::::::::::::::::' ...
'' ...
'1. Bilangan Biner (Contoh: 1100100)' ...
'2. Bilangan Hexadesimal (Contoh: 3e8)' ...
'3. Bilangan Desimal (Contoh: 10000)'}));

pilihan_input = input('Masukkan pilihan input: ');

bilangan_input = input('Masukkan bilangan input: ','s');

disp(char({'1. Bilangan Biner' ...
'2. Bilangan Hexadesimal' ...
'3. Bilangan Desimal'}));

pilihan_konversi = input('Masukkan pilihan konversi: ');

disp(char({'' ...
'::::::::::::::::::::::::Result::::::::::::::::::::::::::' ...
'' ...
[banner(pilihan_input), ' => ' , banner(pilihan_konversi)]}));

hasil = strcat(bilangan_input , ' (' , banner(pilihan_input), ') => ');

if pilihan_input == pilihan_konversi
    hasil_tmp = [hasil, bilangan_input];
else
    hasil_tmp = [hasil, convert(bilangan_input, pilihan_input, pilihan_konversi)];
end

output = strcat(hasil_tmp, ' (' , banner(pilihan_konversi) , ')');

disp(output);

function a = banner(i)
    if i == 1
        a = 'Biner';
    elseif i == 2
        a = 'Hexadesimal';
    elseif i == 3
        a = 'Desimal';	
    end
end

function a = convert(input, iin, out)
    if iin ~= 3
        if iin == 1
            temp = bin2dec(input);
        elseif iin == 2
            temp = hex2dec(input);
        end
    else
        temp = str2double(input);
    end
	
    if out == 1
        a = dec2bin(temp);
    elseif out == 2
        a = dec2hex(temp);
    else
        a = int2str(temp);
    end
end