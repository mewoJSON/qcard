
How to run the program

1. cmd: pip install flask

2.  cmd: export FLASK_ENV=development    
    cmd: export FLASK_APP=main.py        <--- this sets main as root
    cmd: export FLASK_DEBUG=1            <--- this lets you debug/print

3. go to utils/database.py, uncomment line 38, run database.py

4. delete line 38

5. cmd: flask run