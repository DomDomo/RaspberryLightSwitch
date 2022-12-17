# RaspberryLightSwitch
This repository contains the code for my remote light switch app. The app allows you to turn a light on and off remotely using a Raspberry Pi hosting a web server that is connected to a relay.

## Steps

1) Install python 3. Follow [this tutorial](https://projects.raspberrypi.org/en/projects/python-web-server-with-flask)
2) Install pip3. Hope this works: `sudo apt-get install python3-pip`
3) Install flask. Follow the previous site's steps. With sudo, though!!!!
4) Install this project and run it in the background. `sudo python3 app.py &`
5) Follow [this tutorial](https://www.youtube.com/watch?v=zRXauWUumSI) to do it on startup.


### Things of note to me and other readers

1) The template HTML and CSS seems counter-intuitive. That's because I rewired the relay so it's set to always on.
2) The tutorials aren't perfect and you'll need to do some thinking to make them work. Usually, just add sudo to commands.
3) The final app is not perfect but works as intented.
