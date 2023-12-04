# FIFO - First In First Out
# a queue removes the first item at the beginning (0 index which is the number 1 at the list located in line 5)
# remember that when you remove an item from the beginning of the list, all other items need to be shifted to the left
# imagine having a list of 1001 items. Removing one item will then need to shift 1000 items in memmory which is not efficient
# [1, 2, 3]

from collections import deque
queue = deque([])
