FROM ubuntu:latest
# Libraries Linux
RUN apt-get update
RUN apt-get -y install sudo
# Libraries Python
RUN apt-get update && apt-get install -y python3-uinput
RUN apt-get install -y python3.6 python3-distutils python3-pip python3-apt
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
# Libraries Kernel Linux
RUN apt-get install -y kmod
# Libraries Display & App Retroarch
RUN apt-get install -y xvfb
RUN apt-get install -y imagemagick
RUN apt install -y retroarch 
# User sudo
RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER docker
# Permission Display
RUN sudo apt-get install -y dbus-x11
RUN sudo chmod +x /tmp
ENV DISPLAY :99
# Archives App
WORKDIR /usr/src/app
COPY . .
RUN sudo chmod +x init.sh
CMD /usr/src/app/init.sh 