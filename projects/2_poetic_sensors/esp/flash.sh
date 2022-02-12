# python3 -m pip install esptool --user

if [[ $# -eq 0 ]]
  then
    echo "[PORT] (check ls /dev/tty.*)"
    exit 1
fi
PORT=$1
echo $PORT
read -p "Erase $PORT [y/N]? " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo
    echo "Flashing..."
    python3 -m esptool --chip esp32 --port $PORT erase_flash
    python3 -m esptool --chip esp32 --port $PORT --baud 460800 write_flash -z 0x1000 esp32-20220117-v1.18.bin
    echo "--> done"
else
    echo "Exiting..."
fi
