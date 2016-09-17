
# Bookmarks backend

This is the backend for a centralized storage of bookmarks on various devices, I'm using the simplenote api to store to bookmarks in a single note.

On the device part (mainly in Android) I'm using Tasker and AutoShare to intercept share intent from the apps and send a post to this code and store the bookmark in simplenote.

This same code could be use to store the data on any storage service, but I really love the simplenote app on mac, is really light so for me was the best choise.

# Bookmarks recorder (android)

For sending the links that I want to read later on Android, I use the AutoShare and tasker apps.

With the AutoShare When I press on share on any application, you can share with the AutoShare and configure Tasker, to create a post request with the link and title.

# Configuration

You have to add your credentials from simplenote in the config.json (just copy the template and change your credentials)

Also on the simplenote, you must create a empty note with the tag bookmarks

To install do a:
```
pip install -r requirements.txt
python index.py
```

This is the curl command I use to test the code
```
curl -H "Content-Type: text/plain" -X POST -d 'For example たとえば - The Japanese Page' http://localhost:5000/
```

# Building the container

First be sure to create and fill the config.json file with the credentials, then:

```
docker build --rm -t bookmarks:latest .
```

To start the container simply:

```
docker run -d -p 80:80 bookmarks:latest
```

If you are using the jwilder/nginx-proxy to various containers on diferents subdomains you can use this:

```
docker run -d -e VIRTUAL_HOST="bookmarks.domain.net" -e VIRTUAL_PORT=80 bookmarks:latest
```