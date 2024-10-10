#!/usr/bin/python3
"""
   You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
     # locked_rooms = rooms[1::]
        for room_key, room in enumerate(boxes[1:], start=1):
            key_available = False #we yet to found the key

            for prev_room in boxes[:room_key]:
                if room_key in prev_room:
                     key_available = True #we found a key in previous rooms
                     break      
            if key_available is False:
                return False
            
        return True
