README
    Project Name: QCard

Overview
Flask build for qcard website

Setup and Run

(This steps are done for linux, for Windows/Mac follow the same steps with its Windows alternative)

    cmd: pip install flask OR pip install -r requirements.txt
    cmd: export FLASK_ENV=development
    cmd: export FLASK_APP=main.py 
    cmd: export FLASK_DEBUG=1 
    cmd: flask run
    Program should run inside localhost:5000
    Access any of the pages currently available (check test cases section)
Database and Server
    Server is currently located at root, digitalocean website
    To access the VM, ssh login root@164.90.140.135 (requires public.key to be passed to administrator)

Resources to be installed
    Python 3.x (preferably 3.9)
    Required python packages under requirements.txt

Organizational Structure
    main.py : project general build
    requirements.txt : python libraries
    templates/ : html pages
    static/ : style packages, script packages, images not tied to the database
    util/ : database functions, other utility functions
    errors/ : error catching content
    legacy/ : test code, unused content still useful for reference
    modals/ : html modals

Contact Information:
    If there are any concerns regarding the program, please contact:
    Julian Bottero (jbo231@uky.edu) front end
    Kevin Ramirez (krja239@uky.edu) back end
    Anthony Lopez (aclo242@uky.edu) graphic design
    Cooper Jordana (cdjo249@uky.edu) back end

    Both Julian Bottero and Anthony Lopez will be active and part of the future team this summer.

Supplement Content:
    This folder includes content such as diagram for the back end, logo, notes, demo mockups, and sample data
    Check this folder to understand the timeline of the project, how parts of it work, and ideas on how to move forward

Test Cases:
    The pages currently accessible are:
    http://127.0.0.1:5000/home
    http://127.0.0.1:5000/login
    http://127.0.0.1:5000/sign
    http://127.0.0.1:5000/assignment_one
    
    To access them, run the project and enter these websites


