import time
import sys
from multiprocessing import Pool


def func(n):
    a = [[50 for j in range(n)] for i in range(n)]
    b = [[50 for j in range(n)] for i in range(n)]
    c = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k]*b[k][j]
    return c

stratTime = time.time
argv = int(sys.argv[1])
if __name__ == "__main__":
    p = Pool(2)
    p.map(func, range(argv))
print(func(argv))
endTime = time.time() #プログラムの終了時刻
runTime = endTime - stratTime #処理時間
print('time = {0}sec'.format(runTime)) #処理時間を表示

