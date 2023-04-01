clear
termux-vibrate -d 100
echo -e "\033[1;32m Abrindo o Caixa de Economias GUI\033[m"
termux-open-url http://127.0.0.1:5000; python /data/data/com.termux/files/usr/share/cde/App.py
