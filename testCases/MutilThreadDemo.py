#coding=utf-8
import  time
from multiprocessing import Pool


def run(fn):
    time.sleep(1)
    print(fn)
    return fn* fn


if __name__ == '__main__':
    testFl =[1,2,3,4,5,6]
    for fn in testFl:
        run(fn)
        pass

    print("multi processing")

    pool = Pool(5)

    rl = pool.map(run,testFl)
    pool.close() #
    pool.join()

    print("end ..")