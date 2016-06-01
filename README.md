# OSX-Keylogger

### Features

* Records the keys you pressed in a log file along with the time
* Records mouse clicks (both left and right)
* Records mouse stats
  * Mouse movements
     * Total distance
     * Distance x and y
     * Average x and y
     * Positive and negative x and y
  * Scroll wheel movements
     * Total distance
     * Distance x and y
     * Average x and y
     * Positive and negative x and y
* Constantly saves the file to ensure no lost data
* Saves file in an easy format for reading into other applications
* Saves files for keyboard buttons, mouse buttons, and both in three seperate log files

##### Features to be added

* For some reason it only saves the a-z, 0-9 keys, punctuation, and whitespace keys. I am working on getting it to save the modifier keys as well as backspace and function keys.
* Getting rid of that stupid System Preferences bug (see below)
* Expanding to add the user options such as more control over:
  * which keys are recorded
  * format of saved file
  * format of saved time
  * Schedule of when to save keys
  * Easy button to start or stop keylogging

### Installation

**Requires Python 2.7**

This keylogger requires some dependencies from other sources.

Install [PyObjC](http://pythonhosted.org/pyobjc/install.html) from this website in order for the app to work. I had to perform a manual installation, which is featured lower down on the website.

If you are using IDLE, follow these instructions. I am unaware of the requirements for other Python IDEs.

Since System Preferences is stupid, you must add IDLE to the Accessibility pane in the Security page.

Go to System Preferences, Security & Privacy, Privacy, Accessibility, then add basically all of the apps in your Python folder. I added IDLE, Python Launcher, and Build Applet. I'm not sure which are required since I am lazy, just do it. Also everytime you run it, IDLE will get unchecked from the pane so you will have to check it again. Although it might just be me. Who knows.

### Usage

In the actual python file, replace the given path with where you want the log file to be saved.

Remember to add IDLE to the security pane in System Preferences each time. My apologies, I am working on a fix for that. However, the script should keep running if you close your laptop, so this should not happen often.
