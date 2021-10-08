from threading import Thread
import random
import time
import string

spisok = ''
kali = ''

# Рандомится 5 буквенный пароль, который нужно угадать
for i in range(5):
    kali = kali + string.ascii_lowercase[random.randint(0, len(string.ascii_lowercase) - 1)]

# Это брутфорс, он также рандомит парои, только по кругу пока не найдет нужный
def broot():
    array = ''
    for i in range(5):
        array = array + string.ascii_lowercase[random.randint(0, len(string.ascii_lowercase) - 1)]
    return array


while True:
    if broot == kali:
        print('Брутфорс закончен, загаданный пароль ----------', broot)
        break
    else:
        print(broot() + '-----------' + kali)


thread1 = Thread(target=broot)
thread2 = Thread(target=broot)
thread3 = Thread(target=broot)
thread4 = Thread(target=broot)
thread5 = Thread(target=broot)
thread6 = Thread(target=broot)
thread7 = Thread(target=broot)


if __name__ == "__main__":
    start = time.time()
    thread1.start()
    thread1.join()
    end = time.time()
    print("Общее время работы одного потока: ", end - start)
    #-----------------------------------------
    time.sleep(0.0)
    thread2.start()
    thread3.start()
    thread2.join()
    thread3.join()
    end1 = time.time()
    print("Общее время работы двух потоков: ", end1 - end)
    #-----------------------------------------
    time.sleep(0.0)
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    end2 = time.time()
    print("Общее время работы одного потока: ", end - start)
    print("Общее время работы двух потоков: ", end1 - end)
    print("Общее время работы четырех потоков: ", end2 - end1)