#!/data/data/com.termux/files/usr/bin/bash

echo -e '\n\n'
echo -e '\033[1;31mInstalando dependências...\033[m'
echo -e '\n'
apt update
apt install -y python figlet termux-api git

pip install requests lolcat

clear
termux-vibrate -d 100
figlet CDE | lolcat
echo -e '\n\n'
echo -e '\033[1;31mInstalando o CDE...\033[m'
echo -e '\n'

git clone https://github.com/Visto-Preto/CaixaDeEconomias-GUI.git $PREFIX/share/cde
ln -srf $PREFIX/share/cde/cde $PREFIX/bin/cde
termux-vibrate -d 100
echo -e '\n\n'
echo -e 'Para iniciar o cde entre com o comando: \033[1;32mcde\033[m'
echo -e '\n\n\n'