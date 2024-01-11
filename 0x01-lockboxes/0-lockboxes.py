#!/usr/bin/python3
"""
Lockboxes:
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """Check if all boxes can be unlocked"""
    total_boxes = len(boxes)
    keys = set([0])
    entered = {}
    for idx, box in enumerate(boxes):
        if idx in keys:
            keys.update(box)
            entered[idx] = True
        else:
            entered[idx] = False
    for idx, val in entered.items():
        if val == False and idx in keys:
            keys.update(boxes[idx])

    if total_boxes == len(keys):
        return True
    return False