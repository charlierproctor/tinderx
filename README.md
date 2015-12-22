# tinderX

## Overview

tinderX is built with a Flask backend, which principally lives in `tinderx.py`.

## Usage

To use tinderX, visit the following URL:

[http://tinderx.charlieproctor.com](http://tinderx.charlieproctor.com)

You are welcome to sign-in with your own Facebook account or one of the following test accounts:

| name | email | pwd |
|--------|--------|--------|
| Helen Alaakdeajacg Changsky | `muauibf_changsky_1450782672@tfbnw.net` | `tinderx` |
| Karen Alajijcjiaade Romanson | `yqnxffb_romanson_1450782670@tfbnw.net` | `tinderx` |
| John Alajhgbebdffb Yangescu | `zgxeqyy_yangescu_1450782668@tfbnw.net` | `tinderx` |
| Richard Alajhfaifehgh Zamoresky	 | `qhbgchf_zamoresky_1450782673@tfbnw.net` | `tinderx` |

Once you've signed in, you will be represented with a candidate on the left. First, the name, age, and an optional 'teaser'. Then a picture. And then three buttons: `Dislike`, `Like`, and `Pass`.

On the right, you'll see a table of your likes / dislikes and the number of correct predictions made so far. Since you have yet to swipe on any images, no prediction will be made. You should see something like the following:

![](docs/screenshots/initial.png)

Now let's suppose you want to 'like' this candidate. You can swipe right on the image itself, press the `Like` button, or press the right arrow key. Same for dislike.

After swiping, you should be presented with a new candidate. You statistics should update on the right. 

Now, keep doing this... after you have liked and disliked at least one candidate each, the algorithm will kick in and start to make predictions. The prediction appears on the left. Correctness statistics are updated as you progress. You'll also note that average liked / disliked faces are displayed: these are the images the normalized candidate is compared against. If the candidate lies closer to the liked-average, they will be liked; if they lie close to the disliked-average, they will be disliked.

Here's a screenshot of the righthand panel after a series of swipes:

![](docs/screenshots/prediction.png)

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

## Directory Structure

### Top-Level

| Directory / File | Contents |
|-----------|----------|
| `app/` | contains the angular application. see detail below. | 
| `bower.json` | frontend dependencies, managed by `bower`. |
| `config/` | app constants, sample config files for mongo, apache |
| `core/` | contains the core of the Python application: maintain a user's account, fetch / swipe on profiles, interact with database, etc. see detail below. |
| `docs/` | my original proposal |
| `lib/opencv3/haarcascades/` | the cascaade classifiers used for face / eye detection |
| `package.json` | node dependencies (mainly just `gulp`) |
| `requirements.txt` | backend (Python / Flask) dependencies |
| `tinderx.py` | the Flask interface (defines the server) |
| `tinderx.wsgi` | WSGI file for deploying application using Apache |
| `utils/` | contains utilities for scraping usernames and showing images |
| `utils/scrape.py` | scrape usernames off gotinder.com |
| `utils/show.py` | show the liked or disliked image locally (in a pop-up window) |

### Angular Application

| Directory / File | Contents |
|-----------|----------|
| `app/app.js` | defines the application |
| `app/bower_components/` | all the application dependencies |
| `app/controllers` | the controllers: `login.js`, `swipe.js` |
| `app/css` | the styling |
| `app/directives` | contains the `swipeable` directive (allows you to swipe on cards) |
| `app/index.html` | the base page |
| `app/partials` | the HTML views: `login.html`, `swipe.html` |

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

## Routes

All routes are defined in `tinderx.py`. Most API requests of interest are made in `app/controllers/swipe.js`.

- `GET /`: send down the angular application (`index.html`)
- `POST /login`: log a user into the app
- `GET /fetch`: fetch a single user profile
- `POST /swipe`: allow a user to swipe left / right on a candidate
- `GET /img/<name>`: download liked.jpg or disliked.jpg for this user