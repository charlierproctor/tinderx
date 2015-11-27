# CPSC 458 Final Project

I propose to write a program that will automatically swipe left or right on Tinder, based on a combination of certain rules and prior swipes.

## Tinder

*In case you aren't familiar with the details of Tinder, in this section I'll walk through a quick description.*

Tinder is location-based dating app, where mutually interested users are connected in a chatroom. 

- If you both "like" each other, you'll be matched. Otherwise, nothing happens.
	- All swipes are anonymous, so your identity won't be revealed unless the candidate likes you back.
- When you are matched with a user, you'll be connected in a chatroom.

![](https://upload.wikimedia.org/wikipedia/en/3/3a/Tinder_screenshot.png)

- two key terms:
	- swipe left: this "likes" a candidate.
	- swipe right: this sends the "not interested" response.

Each user profile contains the following:

- first name, age, gender
- anywhere between 0-6 photos
- a 500 character description
- current work, school

## Algorithm

### Parameters

- age, gender
- current work, school
- the 500 character description
- primary profile picture (the first photo)

### Case-Based Reasoning: Seed data

I would require the user to swipe (under observation) a certain number of times before the program engages. This creates the seed data, which all future swipes will be based on.

Before any swiping occurs, the seed data must be processed, so that decisions can be made quickly and intelligently moving forward. 

Here's what will need to happen at this point:

- The faces will be normalized into two *average* faces. One for the likes, another for the dislikes. Moving forward, whichever average face the candidate is closer to will determine the bias.
- Key features from the liked / not-liked description will be selected.

For this portion of the app, I plan to make use of Python's [NLTK library](http://www.nltk.org/) to facilitate easier processing of the descriptions. I may also use an image processing library to facilitate the creation of an "average" face or maybe to help "vectorize" each image.

### Rule-Based Reasoning: User defines certain limits

There will also be a rule-based portion of the algorithm. 

- the user can define **age** and **gender** limits
- the user can define **school** and **work** limits

If any of the limits are **not** met, future candidates will be discarded.

Note that the seed data is irrelevant in determining these limits. The program will prompt the user.

### Process new candidates

Once the seed data has been obtained and the rules established, my program will start to automatically swipe left / right on new candidates. During this process, no learning occurs.

## Technology

- I plan to write the algorithm in Python. The algorithm takes the seed data and the rules as input and returns LIKE / NOT INTERESTED for each candidate.
- I will build a web interface for controlling the app. The interface will allow you to perform the seed swipes under observation. It will report the results of the automatic swipes.
- I'll store the data in some form of NoSQL database (maybe MongoDB or Firebase).
- I'll also create a "sandbox" environment with dummy data, so those not interested in signing up for Tinder can still play with the algorithm.
