import queue
Myqueue = queue.Queue(3)
print(Myqueue.empty())
input("Please enter any key when ready: ")
Myqueue.put(1)
Myqueue.put(2)
print(Myqueue.full())
Myqueue.put(3)
print(Myqueue.full())
input("Press any key when ready...")
print(Myqueue.get())
print(Myqueue.empty())
print(Myqueue.full())
input("Press any key when ready...")
print(Myqueue.get())
print(Myqueue.get())

# deque is a que that items can be added or removed from both end
import collections
MyDeque = collections.deque("abcdef", 10)

print("Starting state:")
for Item in MyDeque:
    print(Item, end=" ")

print("\r\n\r\nAppending and extending right")
MyDeque.append("h")
MyDeque.extend("ij")
for Item in MyDeque:
    print(Item, end=" ")

print("\r\nMyDeque contains {0} items."
      .format(len(MyDeque)))

print("\r\nPopping right")
print("Popping {0}".format(MyDeque.pop()))
for Item in MyDeque:
    print(Item, end=" ")

print("\r\n\r\nAppending and extending left")
MyDeque.appendleft("a")
MyDeque.extendleft("bc")
for Item in MyDeque:
    print(Item, end=" ")

print("\r\nMyDeque contains {0} items."
      .format(len(MyDeque)))
