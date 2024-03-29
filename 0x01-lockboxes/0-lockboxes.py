#!/usr/bin/python3
"""
Lockboxes:
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """Check if all boxes can be unlocked"""
    if not isinstance(boxes, list) or boxes is None:
        return False

    total_boxes = len(boxes)
    keys = set([0])
    entered = {}

    if total_boxes > 1:
        for idx, box in enumerate(boxes):
            if idx in keys:
                keys.update({x for x in box if x < total_boxes})
                entered[idx] = True
            else:
                entered[idx] = False
        for idx, val in entered.items():
            if val is False and idx in keys:
                keys.update({x for x in boxes[idx] if x < total_boxes})

    if total_boxes == len(keys) or total_boxes == 0:
        return True
    return False
