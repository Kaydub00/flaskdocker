This just a dockerized flask app. You can add dependencies to requirements.txt.

Needs a different deployment for production environments


## Build and deploy this

    docker build -t my-flask-app .
    docker run -p 5000:5000 --rm --name running-my-flask-app my-flask-app
    
