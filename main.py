# 4007 0000 0000 0027

import requests as req
import threading
from faker import Faker

myFacory = Faker()


url = ""

post_data = {
    "name": myFacory.name(),
    "em": myFacory.name(),
    "ey": myFacory.name(),
    "c": myFacory.name()
}





def main():
    def do_req():
        for i in range(5_000_000):
            res = req.post(url, data=post_data).text
            print(res)


    threads = []

    for j in range(50):
        t = threading.Thread(target=do_req)
        t.daemon = True
        threads.append(t)

    for k in range(50):
        threads[k].start()

    for l in range(50):
        threads[l].join()

    return 0




if __name__ == "__main__":
    exit_res = main()
    if exit_res == 0:
        print("SUCCESSFULLY EXECUTED")
    else:
        print(f"ERROR: {exit_res}")