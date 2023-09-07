FROM ubuntu:22.04

WORKDIR /usr/src/app

# Install dependencies
RUN apt-get update
RUN apt-get install -y xvfb
# RUN apt-get install -y gconf-service
# RUN apt-get install -y libasound2
# RUN apt-get install -y libatk1.0-0
# RUN apt-get install -y libc6
# RUN apt-get install -y libcairo2
# RUN apt-get install -y libcups2
# RUN apt-get install -y libdbus-1-3 
# RUN apt-get install -y libexpat1
# RUN apt-get install -y libfontconfig1
# RUN apt-get install -y libgcc1
# RUN apt-get install -y libgconf-2-4
# RUN apt-get install -y libgdk-pixbuf2.0-0
# RUN apt-get install -y libglib2.0-0
# RUN apt-get install -y libgtk-3-0
# RUN apt-get install -y libnspr4 
# RUN apt-get install -y libpango-1.0-0
# RUN apt-get install -y libpangocairo-1.0-0
# RUN apt-get install -y libstdc++6
# RUN apt-get install -y libx11-6
# RUN apt-get install -y libx11-xcb1
# RUN apt-get install -y libxcb1
# RUN apt-get install -y libxcomposite1 
# RUN apt-get install -y libxcursor1
# RUN apt-get install -y libxdamage1
# RUN apt-get install -y libxext6
# RUN apt-get install -y libxfixes3
# RUN apt-get install -y libxi6
# RUN apt-get install -y libxrandr2
# RUN apt-get install -y libxrender1
# RUN apt-get install -y libxss1
# RUN apt-get install -y libxtst6 
# RUN apt-get install -y ca-certificates
# RUN apt-get install -y fonts-liberation
# RUN apt-get install -y libappindicator1
# RUN apt-get install -y libnss3
# RUN apt-get install -y lsb-release
# RUN apt-get install -y xdg-utils
# RUN apt-get install -y wget 
# RUN apt-get install -y xvfb
# RUN apt-get install -y x11vnc
# RUN apt-get install -y x11-xkb-utils
# RUN apt-get install -y xfonts-100dpi
# RUN apt-get install -y xfonts-75dpi
# RUN apt-get install -y xfonts-scalable
# RUN apt-get install -y x11-apps
RUN apt install retroarch -y
RUN apt install dbus-x11
RUN apt-get install -y imagemagick
RUN apt-get install -y python3.6 python3-distutils python3-pip python3-apt
RUN apt-get install kmod
# RUN apt-get -y install python3-uinput
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY requirementsGamepad.txt ./
RUN pip3 install --no-cache-dir -r requirementsGamepad.txt
RUN apt-get install linux-modules-extra-6.2.0-24-generic
RUN apt-get -y install sudo
RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER docker

RUN sudo apt-get update
RUN sudo apt-get -y install python3-uinput
# RUN sudo modprobe uinput
COPY . .
# RUN apt install modprobe
# CMD modprobe uinput
# Start server on port 3000∂
EXPOSE 8000:8000 8080:8080
# ENV PORT=8000
# Creating Display
ENV DISPLAY :1

# Start script on Xvfb
CMD /bin/bash & \
    python3 gamepad.py & \
    Xvfb :1 -screen 0 1024x768x16 \
    & \
    python3 app.py & \
    retroarch 
# retroarch & \

# CMD [ "uvicorn", "app:app", "--reload" ]