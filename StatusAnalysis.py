import os
from multiprocessing import Pool
from threading import Timer


check=0


def instant():
    if (check == 1):
        print("CHANGE OF STATE ... SUCCESSFULL")

    else:
        if (check == 0):
            print("RESTART DETECTION MODULE")
            os.system('python StatusAnalysis.py')


processes = ('MovementAnalysis.py', 'EmotionAnalysis.py')


def run_process(process):
    os.system('python {}'.format(process))

t = Timer(40.0, instant)
t.start()  # after 20 seconds, "hello, world" will be printed

pool = Pool(processes=10)
pool.map(run_process, processes)


check = 1

instant()




