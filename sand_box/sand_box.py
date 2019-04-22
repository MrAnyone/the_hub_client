# from threading import Thread
#
#
# class Test(Thread):
#
#     def __init__(self,):
#         Thread.__init__(self)
#         self.ready = True
#
#     def run(self):
#         while self.ready:
#             pass
#
#     def kill(self):
#         self.ready = False
#
#
# my_test = Test()
#

counter = 0


def count():
    global counter
    counter = counter + 1


key = None
count()
print(counter)
# while key != 'q':
#     key = input('press a key:')
#     if (key == '+'):
#         count()



