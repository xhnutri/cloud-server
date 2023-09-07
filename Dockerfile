FROM ubuntu:20.04

WORKDIR /usr/src/app

# Install dependencies
RUN apt-get update
# RUN apt install dbus-x11
RUN apt-get install -y python3.6 python3-distutils python3-pip python3-apt
# RUN apt-get install kmod
COPY requirementsGamepad.txt ./
RUN pip3 install --no-cache-dir -r requirementsGamepad.txt
RUN apt-get -y install python3-uinput
RUN apt-get install -y  linux-modules-extra-5.15.0-1021-gcp
COPY . .
# Start server on port 3000∂
EXPOSE 8080:8080
# ENV PORT=8000
# Creating Display
ENV DISPLAY :1

# Start script on Xvfb
CMD python3 gamepad.py 