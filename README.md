# INFO490-Pi-Nametag
This repo contains the code for my Pi Zero W + LED Nametag.  The Pi will run a webserver that other people can access to activate LEDs on the nametag

Note that since this repo uses Conda for virtual environments and package management and to run on a Pi Zero W, you'll have to
   use a different method to install Conda onto the Pi.  Berryconda contains builds for Pi Zero W that you can use
   ==> https://github.com/jjhelmus/berryconda

After you've installed Conda, import the pi-nametag environment from environment.yml.  Then activate that environment and run
	pip install -r requirements.txt
to install the other dependencies


# Running The Server

Activate the pi-nametag conda environment, then navigate to the server/ directory.  Then run 
	python app.py
to start the webserver
