## Aircraft finder (via API from aviapages.com)

# ABOUT
> This web application allows you to find aircrafts by their SERIAL or TAIL number.
  Simply, just type at least 2 characters and press find button.
  After this, you can press on the row to get more info about aircraft.

# REQUIREMENTS (python packages)
* Django>=4.0.1
* django-tables2>=2.4.1
* django-debug-toolbar>=3.2.4
* django-bootstrap4>=21.2
* requests>=2.27.1

# HOW TO INSTALL
1. First of all, you need to install Docker and Docker-compose to deploy application.
2. Set up SECRET_KEY and AVIAPAGES_TOKEN in the core/env.dev file.
> ! IMPORTANT ! Current api key have been banned.
3. Run commands in terminal/cmd from the core DIR of the project.

 <code>docker-compose build</code>
 
 <code>docker-compose up</code>

> ! IMPORTANT ! Port 8000 should be open and accessible.
4. Go to localhost:8000 or 127.0.0.1:8000 or 0.0.0.0:8000
