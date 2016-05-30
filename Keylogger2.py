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
        mask = (  NSKeyDownMask
                | NSLeftMouseDownMask
                | NSOtherMouseDown
                | NSRightMouseDownMask)
        
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask, handler)

def writeToLogs(log, text):
    log.write(text)
    log.write(' PTO ')
    log.write(time.strftime("%Y %m %d %H %M %S"))
    log.write('\n')


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
        pass

    log = open("/Users/aturley/Desktop/fullLogs.txt", 'a')
    mouse = open("/Users/aturley/Desktop/mouseLogs.txt", 'a')
    keyboard = open("/Users/aturley/Desktop/keyLogs.txt", 'a')
    
    for key in arrows:
        writeToLogs(log, key)
        writeToLogs(keyboard, key)

    for key in modifiers:
        writeToLogs(log, key)
        writeToLogs(keyboard, key)
        
    if event.type() == NSLeftMouseDown:
        writeToLogs(log, "</LEFTMOUSE>")
        writeToLogs(mouse, "</LEFTMOUSE>")
        print("LEFTMOUSE")
    elif event.type() == NSRightMouseDown:
        writeToLogs(log, "</RIGHTMOUSE>")
        writeToLogs(mouse, "</RIGHTMOUSE>")
        print("RIGHTMOUSE")
    elif event.type() == NSOtherMouseDown:
        writeToLogs(log, "</OTHERMOUSE>")
        writeToLogs(mouse, "</OTHERMOUSE>")
        print("OTHERMOUSE")
    elif event.type() == NSKeyDown:
        print(event.charactersIgnoringModifiers())
        writeToLogs(log, event.charactersIgnoringModifiers())
        writeToLogs(keyboard, event.charactersIgnoringModifiers())

    log.close()
    mouse.close()
    keyboard.close()
    
def main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()
    
main()
