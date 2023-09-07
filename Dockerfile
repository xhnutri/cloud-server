FROM ubuntu:20.04

WORKDIR /usr/src/app

# Install dependencies
RUN apt-get update
RUN apt-get -y install sudo
RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER docker
# Install dependencies
RUN sudo apt-get update
# RUN apt install dbus-x11
RUN sudo apt-get install -y python3.6 python3-distutils python3-pip python3-apt
# RUN sudo apt-get install kmod
COPY requirementsGamepad.txt ./
RUN pip3 install --no-cache-dir -r requirementsGamepad.txt
RUN sudo apt-get -y install python3-uinput
RUN sudo apt-get install -y linux-modules-5.15.0-1039-gcp
RUN sudo apt-get install -y libevdev-dev
RUN sudo groupadd uinput
RUN sudo usermod -a -G uinput docker
COPY 40-uinput.rules ./
RUN sudo tee -a 40-uinput.rules > /dev/uinput
COPY . .
# Start server on port 3000∂
EXPOSE 8080:8080
# ENV PORT=8000
# Creating Display
ENV DISPLAY :1

# Start script on Xvfb
CMD python3 gamepad.py 