import threading

loc_obj = threading.RLock()
print('Acquire 1st time')
loc_obj.acquire()
print('Acquire 2nd time')
loc_obj.acquire()

print('Realising')
loc_obj.release()

# def reentrance():
#     print('Start')
#     loc_obj.acquire()
#     print('Acquire')
#     reentrance()
#
# reentrance()
