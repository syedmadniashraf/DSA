cnt = 0
def func():
    global cnt
    if(cnt == 3):
        return
    else:
        print(cnt)
        cnt = cnt + 1
        func()

func()