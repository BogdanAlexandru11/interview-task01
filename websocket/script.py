import websockets
import os
from collections import deque
import time
import asyncio
import datetime
import random

filename = "myfile.txt"

# get the last element in the file
def getlastelem(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        last_read_position = lines[-1]
        return last_read_position

# get the number of lines in the file
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# function that sends the data using a websocket
async def time(websocket, path):
    # last time the file was modified
    last_modified = format(os.stat(filename).st_mtime)
    # last line in the file
    last_read_position = getlastelem(filename)
    # index used to get hte last 10 lines in the file
    lastindex=0
    f = open(filename, "r")
    for i in f:
        lastindex+=1
        myvar = i.strip()
        # if the lastindex is greater or equal than the total length - 10 -> send the data
        # it represents the last 10 lines in the file
        if lastindex >= (int(file_len(filename)-10)):
            await websocket.send(i)
    # while loop that runs forever 
    while True:
        # boolean used to find all the elements from the last_read_position until the last line of the file
        mybool=False
        # checks whether the file was modified
        if last_modified != format(os.stat(filename).st_mtime):
            # update the file modified with the new time
            last_modified = format(os.stat(filename).st_mtime)  
            # open the file
            f = open(filename, "r")
            for i in f:
                # gets rid of the newlines at the end of the string
                myvar = i.strip()
                # if the myvar is equal to the last_read_position then set the boolean to true
                if myvar == last_read_position:
                    mybool=True
                # from now on i represent the new elements that were added
                # therefore they will be sent using a websocket
                if mybool == True:
                    if last_read_position != myvar:
                        await websocket.send(i)
                        # last_read_position is being updated to the last item in the file
                        last_read_position=i
        await asyncio.sleep(1)

# the websocket runs on the port 5678
start_server = websockets.serve(time, '127.0.0.1', 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()