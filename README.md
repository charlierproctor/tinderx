# tinderX

## Overview

tinderX is built with a Flask backend, which principally lives in `tinderx.py`.

## Dependencies

Unfortunately as tinderX involves multiple languages and a variety of technologies, there are a number of complicated dependencies. That being said, I'll outline the highlights here. Obviously, the details are system-dependent.

First and foremost, you must have some form of **Python 2.7**.

### mongodb 

I use MongoDB to store information on the users and the profiles. Installation instructions can be found here:

[https://docs.mongodb.org/v3.0/installation/](https://docs.mongodb.org/v3.0/installation/)

### opencv3

To process the images (detect faces, crop, resize, etc.), I use **OpenCV 3**. This is a nightmare to install... if you're on a Mac, [brew](http://brew.sh/) works. Otherwise, here are instructions for linux installation from source:

[http://docs.opencv.org/3.0-beta/doc/tutorials/introduction/linux_install/linux_install.html](http://docs.opencv.org/3.0-beta/doc/tutorials/introduction/linux_install/linux_install.html)

### pip

There are a series of pip packages, as listed in `requirements.txt`, that must be installed:

```
pip install -r requirements.txt
```

### gulp

I use `gulp` to manage the build process of the angular frontend. 

, so it's best to install the node modules:

```
npm install
```

To rebuild the angular frontend after any changes, just run the `gulp` command


### apache

mod_wsgi
apt-get install libapache2-mod-wsgi

## Structure

### Top-Level

| Directory / File | Contents |
|-----------|----------|
| `app/` | contains the angular application | 
| `bower.json` | frontend dependencies, managed by `bower`. |
| `config/` | app constants, sample config files for mongo, apache |
| `core/` | contains the core of the Python application: maintain a user's account, fetch / swipe on profiles, interact with database, etc. |
| `lib/opencv3/haarcascades/` | the cascaade classifiers used for face / eye detection |
| `package.json` | node dependencies (mainly just `gulp`) |
| `requirements.txt` | backend (Python / Flask) dependencies |
| `tinderx.py` | the Flask interface (defines the server) |
| `tinderx.wsgi` | WSGI file for deploying application using Apache |
| `utils/` | contains utilities for scraping usernames and showing images |

### Core Package

| Directory / File | Contents |
|-----------|----------|
| `core/errors` | defines a series of app-wide errors |
| `core/db/` | a package of database functions |
| `core/db/profiles.py` | functions to interact with the `tinder_profiles` document in MongoDB |
| `core/db/users.py` | functions to interact with the `users` document in MongoDB |
| `core/user/` | defines the `User` class. authorize a user, fetch a profile, swipe on a profile. |
| `core/user/auth.py` | authorize a user (verify their facebook tokens) |
| `core/user/fetch.py` | fetch the next profile, predict whether the user will like it |
| `core/user/swipe.py` | swipe on a profile, updating the liked or disliked average image |
| `core/profile/` | defines the `Profile` class. detect faces, normalize images. |
| `core/profile/detect.py` | detect faces / eyes. choose which face we should use. |
| `core/profile/img.py` | download images, normalize them: crop, resize, etc. |
| `core/profile/run.py` | run face detection locally, displaying the results in a pop-up window. |