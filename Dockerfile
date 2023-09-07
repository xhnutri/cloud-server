FROM i386/ubuntu:bionic

WORKDIR /usr/src/app
# Install dependencies
RUN apt-get update
RUN apt install dbus-x11
RUN apt-get install -y python3.6 python3-distutils python3-pip python3-apt
RUN apt-get -y install python3-uinput
COPY requirementsGamepad.txt ./
RUN pip3 install --no-cache-dir -r requirementsGamepad.txt
RUN apt-get install -y libevdev-dev
COPY . .
# Start server on port 3000∂
EXPOSE 8080:8080
# ENV PORT=8000
# Creating Display
ENV DISPLAY :1

# Start script on Xvfb
CMD python3 gamepad.py 