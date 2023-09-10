sleep 1
echo "xvfb retroarch"
sleep 1
sudo modprobe uinput
sleep 2
sudo python3 app.py & sudo python3 gamepad.py & sudo Xvfb :99 -screen 0 1024x768x16 & sudo retroarch