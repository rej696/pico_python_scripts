# MicroPython
## connect to repl
sudo minicom -o -D /dev/ttyACM0

## connect to rshell
sudo rshell --buffer-size=512 -p /dev/ttyACM0

## copy main.py (or other function) to board
cp <main.py> /pyboard/main.py

## exit minicom
<C-A> x
