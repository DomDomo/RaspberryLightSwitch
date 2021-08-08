# RaspberryLightSwitch
This is the code to run my webserver for my website activated light

## Steps

1) Install python 3. Follow [this tutorial](https://projects.raspberrypi.org/en/projects/python-web-server-with-flask)
2) Install pip3. Hope this works: `sudo apt-get install python3-pip`
3) Install flask. Follow the previous site's steps. With sudo, though!!!!
4) Install this project and run it in the background. `sudo python3 app.py &`
5) Follow [this tutorial](https://www.youtube.com/watch?v=zRXauWUumSI) to do it on startup.


### Things of note to me and other readers

1) The template HTML and CSS seems counter-intuitive. That's because I rewired the relay so it's set to always on.
2) The tutorials aren't perfect and you'll need to do some thinking to make them work. Usually, just add sudo to commands.
3) I am a dumbass.
