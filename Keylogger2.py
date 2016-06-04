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
print("test")
#import keycode
print("test2")
import string
import sys
import time

class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, aNotification): # When the application launches
        # Set up the different masks to search for
        keyMask = NSKeyDownMask

        mouseMask = (NSLeftMouseDownMask
                | NSOtherMouseDown
                | NSRightMouseDownMask)

        mouseMovedMask = (NSMouseMovedMask 
                        | NSScrollWheelMask)
        
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(keyMask, handler)
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mouseMask, mouseHandler)
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mouseMovedMask, mouseMoveHandler)

    def applicationWillResignActive(self, notification):
        self.applicationWillTerminate_(notification)

    def applicationShouldTerminate_(self, notification):
        self.applicationWillTerminate_(notification)

    def applicationWillTerminate_(self, notification):
        pass
        #print("Exiting")

'''
Write data to text files along with the time information
'''
def writeToLogs(log, text):
    log.write(text)
    log.write(' PTO ')
    log.write(time.strftime("%Y %m %d %H %M %S"))
    log.write('\n')

'''
Moving the mouse action
'''
def mouseMoveHandler(event):
    # Open the files and put it into a text format
    readLog = open("/Users/aturley/Desktop/mouseStats.txt", 'r').read()
    readLog = readLog.split('\n')

    try:
        loc = NSEvent.mouseLocation() # Get location of mouse
        if event.type() == NSMouseMoved: # If the mouse moved
            # Setup all of the variables in the log file
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
            mousePrevX = readLog[10] # Previous mouse location X
            mousePrevY = readLog[11] # Previous mouse location Y

            # Change in mouse location for x and y
            changedX = loc.x - float(mousePrevX)
            changedY = loc.y - float(mousePrevX)
            
            disMoved = float(disMoved) + abs(changedX) + abs(changedY)
            disMovedX = float(disMovedX) + abs(changedX)
            disMovedY = float(disMovedY) + abs(changedY)
            
            if changedX > 0: # If there was a positive change for X
                disMovedPosX = float(disMovedPosX) + changedX
            else:
                disMovedNegX = float(disMovedNegX) + changedX
                
            if changedY > 0: # If there was a positive change for Y
                disMovedPosY = float(disMovedPosY) + changedY
            else:
                disMovedNegY = float(disMovedNegY) + changedY

            disMovedAveX = (float(disMovedPosX) + float(disMovedNegX)) / 2
            disMovedAveY = (float(disMovedPosY) + float(disMovedNegY)) / 2
            disMovedAve = (disMovedAveX + disMovedAveY) / 2

            mousePrevX = float(loc.x)
            mousePrevY = float(loc.y)

            # Write the changes in mouse location to the file
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
            
        elif event.type() == NSScrollWheel: # If the scrollwheel moved instead
            # Read log information
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

            # Get change in scroll location for x and y
            deltaY = event.deviceDeltaY()
            deltaX = event.deviceDeltaX()
            
            disScrolledX = float(disScrolledX) + deltaX
            disScrolledY = float(disScrolledY) + deltaY
            disScrolled = float(disScrolled) + abs(deltaY) + abs(deltaX)

            if deltaX > 0: # If scrolled in a positive X direction
                disScrolledPosX = float(disScrolledPosX) + deltaX
            else:
                disScrolledNegX = float(disScrolledNegX) + deltaX

            if deltaY > 0: # If scrolled in a positive Y direction
                disScrolledPosY = float(disScrolledPosY) + deltaY
            else:
                disScrolledNegY = float(disScrolledNegY) + deltaY

            disScrolledAveX = (float(disScrolledPosX) + float(disScrolledNegX)) / 2
            disScrolledAveY = (float(disScrolledPosY) + float(disScrolledNegY)) / 2
            disScrolledAve = (disScrolledAveX + disScrolledAveY) / 2

            # Write scrollwheel changes
            mouseLog = open("/Users/aturley/Desktop/mouseStats.txt", 'w')
            readLog[12] = str(disScrolled)
            readLog[13] = str(disScrolledX)
            readLog[14] = str(disScrolledY)
            readLog[15] = str(disScrolledPosX)
            readLog[16] = str(disScrolledNegX)
            readLog[17] = str(disScrolledPosY)
            readLog[18] = str(disScrolledNegY)
            readLog[19] = str(disScrolledAve)
            readLog[20] = str(disScrolledAveX)
            readLog[21] = str(disScrolledAveY)
            toWrite = "\n".join(readLog)
            
            mouseLog.write(toWrite)
            mouseLog.close()
    except:
        pass

'''
Mouse buttons handler
'''
def mouseHandler(event):
    mouse = open("/Users/aturley/Desktop/mouseLogs.txt", 'a')
    log = open("/Users/aturley/Desktop/fullLogs.txt", 'a')
    
    if event.type() == NSLeftMouseDown: # If the left button was pressed
        writeToLogs(log, "</LEFTMOUSE>")
        writeToLogs(mouse, "</LEFTMOUSE>")
        #print("LEFTMOUSE")
    elif event.type() == NSRightMouseDown: # If the right button was pressed
        writeToLogs(log, "</RIGHTMOUSE>")
        writeToLogs(mouse, "</RIGHTMOUSE>")
        #print("RIGHTMOUSE")
    elif event.type() == NSOtherMouseDown: # ???????
        writeToLogs(log, "</OTHERMOUSE>")
        writeToLogs(mouse, "</OTHERMOUSE>")
        #print("OTHERMOUSE")
        
    log.close()
    mouse.close()


'''
Keyboard buttons handler
'''
def handler(event):
    flags = event.modifierFlags() # All of the modifiers that were pressed
    modifiers = []
    arrows = []

    try:
        s = event.charactersIgnoringModifiers() # Get misc. keys
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
        if flags & NSFunctionKeyMask and not arrowPressed: # ?????
            modifiers.append("</FUNCTION>")
        if flags & NSAlphaShiftKeyMask:
            modifiers.append("</ALPHASHIFT>")
    except:
        pass

    log = open("/Users/aturley/Desktop/fullLogs.txt", 'a')
    keyboard = open("/Users/aturley/Desktop/keyLogs.txt", 'a')
    
    for key in arrows: # Write arrow keys to log
        writeToLogs(log, key)
        writeToLogs(keyboard, key)

    for key in modifiers: # Write modifier keys to log
        writeToLogs(log, key)
        writeToLogs(keyboard, key)
        
    if event.type() == NSKeyDown: # Write normal ASCII keys to log
        #print(event.charactersIgnoringModifiers())
        writeToLogs(log, event.charactersIgnoringModifiers())
        writeToLogs(keyboard, event.charactersIgnoringModifiers())

    log.close()
    keyboard.close()
    
def main():
    print("TEST2")
    app = NSApplication.sharedApplication() # Set up application stuff
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()

main()
