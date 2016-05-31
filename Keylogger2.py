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

        mouseMovedMask = (NSMouseMovedMask 
                        | NSScrollWheelMask)
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask, handler)
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mouseMovedMask, mouseHandler)

    def applicationWillResignActive(self, notification):
        self.applicationWillTerminate_(notification)

    def applicationShouldTerminate_(self, notification):
        self.applicationWillTerminate_(notification)

    def applicationWillTerminate_(self, notification):
        print("Exiting")
        
def writeToLogs(log, text):
    log.write(text)
    log.write(' PTO ')
    log.write(time.strftime("%Y %m %d %H %M %S"))
    log.write('\n')

def mouseHandler(event):
    readLog = open("/Users/aturley/Desktop/mouseStats.txt", 'r').read()
    readLog = readLog.split('\n')

    try:
        loc = NSEvent.mouseLocation()
        if event.type() == NSMouseMoved:
            disMoved = readLog[0]
            disMovedX = readLog[1]
            disMovedY = readLog[2]
            disMovedPosX = readLog[3]
            disMovedNegX = readLog[4]
            disMovedPosY = readLog[5]
            disMovedNegY = readLog[6]
            disMovedAve = readLog[7]
            disMovedAveX = readLog[8]
            disMovedAveY = readLog[9]
            mousePrevX = readLog[10]
            mousePrevY = readLog[11]

            changedX = loc.x - float(mousePrevX)
            changedY = loc.y - float(mousePrevX)
            
            disMoved = float(disMoved) + abs(changedX) + abs(changedY)
            disMovedX = float(disMovedX) + abs(changedX)
            disMovedY = float(disMovedY) + abs(changedY)
            
            if changedX > 0:
                disMovedPosX = float(disMovedPosX) + changedX
            else:
                disMovedNegX = float(disMovedNegX) + changedX
                
            if changedY > 0:
                disMovedPosY = float(disMovedPosY) + changedY
            else:
                disMovedNegY = float(disMovedNegY) + changedY

            disMovedAveX = (float(disMovedPosX) + float(disMovedNegX)) / 2
            disMovedAveY = (float(disMovedPosY) + float(disMovedNegY)) / 2
            disMovedAve = (disMovedAveX + disMovedAveY) / 2

            mousePrevX = float(loc.x)
            mousePrevY = float(loc.y)

            mouseLog = open("/Users/aturley/Desktop/mouseStats.txt", 'w')
            readLog[0] = str(disMoved)
            readLog[1] = str(disMovedX)
            readLog[2] = str(disMovedY)
            readLog[3] = str(disMovedPosX)
            readLog[4] = str(disMovedNegX)
            readLog[5] = str(disMovedPosY)
            readLog[6] = str(disMovedNegY)
            readLog[7] = str(disMovedAve)
            readLog[8] = str(disMovedAveX)
            readLog[9] = str(disMovedAveY)
            readLog[10] = str(mousePrevX)
            readLog[11] = str(mousePrevY)
            toWrite = "\n".join(readLog)
            
            mouseLog.write(toWrite)
            mouseLog.close()
            
        elif event.type() == NSScrollWheelMask:
            disScrolled = readLog[12]
            disScrolledX = readLog[13]
            disScrolledY = readLog[14]
            disScrolledPosX = readLog[15]
            disScrolledNegX = readLog[16]
            disScrolledPosY = readLog[17]
            disScrolledNegY = readLog[18]
            disScrolledAve = readLog[19]
            disScrolledAveX = readLog[20]
            disScrolledAveY = readLog[21]

    except:
        pass

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
