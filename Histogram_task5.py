import time

def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)
        time.sleep(1)

histogram([2, 3, 6, 5, 15, 29, 11, 2, 1, 7])