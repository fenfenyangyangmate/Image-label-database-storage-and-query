import os
import tkinter
from tkinter import messagebox

# reload(sys)
# sys.setdefaultencoding('utf-8')
import pymysql
from deepdanbooru import commands
from math import floor, ceil


def AppropriateFraction(down, up, left, right):
    answer = []
    for k in range(left, right + 1):
        if ceil(k * down) <= floor(k * up):
            for l in range(ceil(k * down), floor(k * up) + 1):
                answer.append((l, k))
    return answer


def Phigros(score):
    low = (score - 0.5) * 0.0002
    high = (score + 0.5) * 0.0002
    # ver 2.1.4
    noteNumber = [("Introduction EZ", 180), ("dB doll EZ", 60), ("dB doll HD", 124), ("dB doll IN", 237),
                  ("dB doll AT", 377), ("もぺもぺ EZ", 125), ("もぺもぺ HD", 289), ("もぺもぺ IN", 412), ("もぺもぺ AT", 720),
                  ("Eradication Catastrophe EZ", 111), ("Eradication Catastrophe HD", 319),
                  ("Eradication Catastrophe IN", 463), ("Initialize EZ", 117), ("Initialize HD", 354),
                  ("Initialize IN", 581), ("Dash EZ", 114), ("Dash HD", 210), ("Dash IN", 346),
                  ("Dash Legacy", 296), ("Demiurge EZ", 100), ("Demiurge HD", 445), ("Demiurge IN", 520),
                  ("-Arkhei- EZ", 462), ("-Arkhei- HD", 454), ("-Arkhei- IN", 644), ("Sparkle New Life EZ", 305),
                  ("Sparkle New Life HD", 497), ("Sparkle New Life IN", 684), ("Glaciaxion EZ", 66),
                  ("Glaciaxion HD", 418), ("Glaciaxion IN", 729), ("Glaciaxion Legacy", 611),
                  ("Sultan Rage EZ", 159), ("Sultan Rage HD", 334), ("Sultan Rage IN", 485),
                  ("Clock Paradox EZ", 188), ("Clock Paradox HD", 312), ("Clock Paradox IN", 520),
                  ("HumaN EZ", 182), ("HumaN HD", 382), ("HumaN IN", 554), ("HumaN Legacy", 651),
                  ("Next Time EZ", 240), ("Next Time HD", 303), ("Next Time IN", 387), ("云女孩 EZ", 220),
                  ("云女孩 HD", 538), ("云女孩 IN", 669), ("云女孩 Legacy", 740), ("桜樹街道 EZ", 292), ("桜樹街道 HD", 421),
                  ("桜樹街道 IN", 459), ("Colorful Days♪ EZ", 156), ("Colorful Days♪ HD", 186),
                  ("Colorful Days♪ IN", 407), ("Leave All Behind EZ", 210), ("Leave All Behind HD", 394),
                  ("Leave All Behind IN", 523), ("Rubbish Sorting EZ", 229), ("Rubbish Sorting HD", 475),
                  ("Rubbish Sorting IN", 613), ("Ποσειδών EZ", 533), ("Ποσειδών HD", 397), ("Ποσειδών IN", 450),
                  ("光 EZ", 249), ("光 HD", 453), ("光 IN", 517), ("光 Legacy", 532), ("NYA!!! EZ", 122),
                  ("NYA!!! HD", 428), ("NYA!!! IN", 666), ("Aphasia EZ", 283), ("Aphasia HD", 362),
                  ("Aphasia IN", 553), ("萤火虫の怨 EZ", 245), ("萤火虫の怨 HD", 746), ("萤火虫の怨 IN", 885),
                  ("萤火虫の怨 Legacy", 875), ("Dreamland EZ", 338), ("Dreamland HD", 476), ("Dreamland IN", 627),
                  ("Electron EZ", 219), ("Electron HD", 423), ("Electron IN", 576), ("游园地 EZ", 220),
                  ("游园地 HD", 444), ("游园地 IN", 481), ("Another Round EZ", 136), ("Another Round HD", 353),
                  ("Another Round IN", 505), ("JunXion Between Life And Death(VIP Mix) EZ", 262),
                  ("JunXion Between Life And Death(VIP Mix) HD", 593),
                  ("JunXion Between Life And Death(VIP Mix) IN", 722), ("万吨匿名信 EZ", 307), ("万吨匿名信 HD", 648),
                  ("万吨匿名信 IN", 781), ("万吨匿名信 Legacy", 857), ("-SURREALISM- EZ", 302), ("-SURREALISM- HD", 532),
                  ("-SURREALISM- IN", 914), ("Apocalyptic EZ", 282), ("Apocalyptic HD", 329),
                  ("Apocalyptic IN", 676), ("Engine x Start!! (melody mix) EZ", 126),
                  ("Engine x Start!! (melody mix) HD", 262), ("Engine x Start!! (melody mix) IN", 433),
                  ("Engine x Start!! (melody mix) Legacy", 564), ("Winter↑cube↓ EZ", 401), ("Winter↑cube↓ HD", 696),
                  ("Winter↑cube↓ IN", 733), ("Winter↑cube↓ Legacy", 909), ("With You EZ", 226),
                  ("With You HD", 654), ("With You IN", 774), ("Class Memories EZ", 612),
                  ("Class Memories HD", 801), ("Class Memories IN", 1194), ("Get Ready!! EZ", 363),
                  ("Get Ready!! HD", 584), ("Get Ready!! IN", 819), ("Another Me EZ 1.7", 111),
                  ("Another Me HD 5.6", 259), ("Another Me IN 13.6", 564), ("Another Me Legacy 13.2", 549),
                  ("Infinity Heaven EZ", 164), ("Infinity Heaven HD", 422), ("Infinity Heaven IN", 1029),
                  ("Snow Desert EZ", 236), ("Snow Desert HD", 534), ("Snow Desert IN", 552),
                  ("Time to Night Sky (feat. Lee Yu Jin) EZ", 165),
                  ("Time to Night Sky (feat. Lee Yu Jin) HD", 559),
                  ("Time to Night Sky (feat. Lee Yu Jin) IN", 540), ("WATER EZ", 338), ("WATER HD", 703),
                  ("WATER IN", 643), ("Credits EZ", 188), ("Credits HD", 355), ("Credits IN", 535),
                  ("cryout EZ", 221), ("cryout HD", 529), ("cryout IN", 733), ("Demonkin EZ", 426),
                  ("Demonkin HD", 513), ("Demonkin IN", 829), ("Miracle Forest (VIP Mix) EZ", 323),
                  ("Miracle Forest (VIP Mix) HD", 586), ("Miracle Forest (VIP Mix) IN", 839),
                  ("Miracle Forest (VIP Mix) Legacy", 917), ("Äventyr EZ", 345), ("Äventyr HD", 626),
                  ("Äventyr IN", 954), ("风屿 EZ", 368), ("风屿 HD", 802), ("风屿 IN", 1155), ("Get Back EZ", 321),
                  ("Get Back HD", 550), ("Get Back IN", 708), ("Wavetapper EZ", 470), ("Wavetapper HD", 507),
                  ("Wavetapper IN", 866), ("XING EZ", 310), ("XING HD", 587), ("XING IN", 711),
                  ("Chronologika EZ", 271), ("Chronologika HD", 456), ("Chronologika IN", 776), ("Drop It EZ", 505),
                  ("Drop It HD", 602), ("Drop It IN", 1031), ("Drop It Legacy", 912), ("華灯爱 EZ", 318),
                  ("華灯爱 HD", 394), ("華灯爱 IN", 520), ("華灯爱 Legacy", 493), ("Bonus Time EZ", 190),
                  ("Bonus Time HD", 319), ("Bonus Time IN", 689), ("Bonus Time Legacy", 762), ("GOODTEK EZ", 295),
                  ("GOODTEK HD", 609), ("GOODTEK IN", 873), ("Khronostasis Katharsis EZ", 394),
                  ("Khronostasis Katharsis HD", 747), ("Khronostasis Katharsis IN", 861),
                  ("Khronostasis Katharsis Legacy", 883), ("MARENOL EZ", 95), ("MARENOL HD", 467),
                  ("MARENOL IN", 689), ("MARENOL Legacy", 1368), ("Orthodox EZ", 304), ("Orthodox HD", 627),
                  ("Orthodox IN", 962), ("End Me EZ", 217), ("End Me HD", 320), ("End Me IN", 724),
                  ("Final Step! EZ", 355), ("Final Step! HD", 604), ("Final Step! IN", 931), ("Speed Up! EZ", 262),
                  ("Speed Up! HD", 463), ("Speed Up! IN", 711), ("Dead Soul EZ", 273), ("Dead Soul HD", 613),
                  ("Dead Soul IN", 787), ("Eltaw EZ", 391), ("Eltaw HD", 608), ("Eltaw IN", 855),
                  ("Find_Me EZ", 465), ("Find_Me HD", 657), ("Find_Me IN", 836), ("GOODBOUNCE EZ", 588),
                  ("GOODBOUNCE HD", 797), ("GOODBOUNCE IN", 898), ("Luminescent EZ", 330), ("Luminescent HD", 608),
                  ("Luminescent IN", 650), ("MOBILYS EZ", 311), ("MOBILYS HD", 530), ("MOBILYS IN", 938),
                  ("Nick of Time EZ", 328), ("Nick of Time HD", 429), ("Nick of Time IN", 745),
                  ("Parallel Retrogression(Game Ver.) EZ", 507), ("Parallel Retrogression(Game Ver.) HD", 697),
                  ("Parallel Retrogression(Game Ver.) IN", 851), ("The Mountain Eater EZ", 210),
                  ("The Mountain Eater HD", 386), ("The Mountain Eater IN", 697), ("Unorthodox Thoughts EZ", 512),
                  ("Unorthodox Thoughts HD", 644), ("Unorthodox Thoughts IN", 729), ("开心病 EZ", 158),
                  ("开心病 HD", 442), ("开心病 IN", 840), ("开心病 Legacy", 815), ("狂喜蘭舞 EZ", 472), ("狂喜蘭舞 HD", 651),
                  ("狂喜蘭舞 IN", 968), ("狂喜蘭舞 AT", 1325), ("狂喜蘭舞 Legacy", 954), ("996 EZ", 392), ("996 HD", 453),
                  ("996 IN", 996), ("Cervelle Connexion EZ", 301), ("Cervelle Connexion HD", 569),
                  ("Cervelle Connexion IN", 563), ("GOODWORLD EZ", 215), ("GOODWORLD HD", 805),
                  ("GOODWORLD IN", 960), ("Magenta Potion EZ", 334), ("Magenta Potion HD", 631),
                  ("Magenta Potion IN", 791), ("micro.wav EZ", 196), ("micro.wav HD", 459), ("micro.wav IN", 649),
                  ("Shadow EZ", 393), ("Shadow HD", 549), ("Shadow IN", 840), ("Träne EZ", 148), ("Träne HD", 420),
                  ("Träne IN", 661), ("ジングルベル(Jingle Bell) EZ", 639), ("ジングルベル(Jingle Bell) HD", 492),
                  ("ジングルベル(Jingle Bell) IN", 1239), ("Dlyrotz EZ", 279), ("Dlyrotz HD", 382), ("Dlyrotz IN", 764),
                  ("Future Mind EZ", 365), ("Future Mind HD", 570), ("Future Mind IN", 866),
                  ("Hardcore Kwaya EZ", 340), ("Hardcore Kwaya HD", 611), ("Hardcore Kwaya IN", 852),
                  ("INFiNiTE ENERZY -Overdoze- EZ", 333), ("INFiNiTE ENERZY -Overdoze- HD", 666),
                  ("INFiNiTE ENERZY -Overdoze- IN", 888), ("INFiNiTE ENERZY -Overdoze- AT", 888),
                  ("Re_Nascence (Psystyle Ver.) EZ", 378), ("Re_Nascence (Psystyle Ver.) HD", 806),
                  ("Re_Nascence (Psystyle Ver.) IN", 827), ("重生 EZ", 354), ("重生 HD", 650), ("重生 IN", 900),
                  ("Cipher : /2&//<|0 EZ", 380), ("Cipher : /2&//<|0 HD", 526), ("Cipher : /2&//<|0 IN", 969),
                  ("Disorder EZ", 444), ("Disorder HD", 629), ("Disorder IN", 918), ("FULi AUTO BUSTER EZ", 285),
                  ("FULi AUTO BUSTER HD", 596), ("FULi AUTO BUSTER IN", 755), ("HAZARD EZ", 283),
                  ("HAZARD HD", 507), ("HAZARD IN", 588), ("mechanted EZ", 184), ("mechanted HD", 500),
                  ("mechanted IN", 662), ("modulus EZ", 258), ("modulus HD", 482), ("modulus IN", 774),
                  ("ρars/ey EZ", 181), ("ρars/ey HD", 449), ("ρars/ey IN", 777), ("Burn EZ", 278), ("Burn HD", 497),
                  ("Burn IN", 707), ("Cereris EZ", 470), ("Cereris HD", 703), ("Cereris IN", 898),
                  ("Doppelganger EZ", 257), ("Doppelganger HD", 437), ("Doppelganger IN", 921),
                  ("Doppelganger Legacy", 746), ("ENERGY SYNERGY MATRIX EZ", 190),
                  ("ENERGY SYNERGY MATRIX HD", 468), ("ENERGY SYNERGY MATRIX IN", 750),
                  ("ENERGY SYNERGY MATRIX Legacy", 615), ("FULi AUTO SHOOTER EZ", 165),
                  ("FULi AUTO SHOOTER HD", 537), ("FULi AUTO SHOOTER IN", 843),
                  ("life flashes before weeb eyes EZ", 567), ("life flashes before weeb eyes HD", 960),
                  ("life flashes before weeb eyes IN", 1065), ("volcanic EZ", 1052), ("volcanic HD", 985),
                  ("volcanic IN", 1178), ("volcanic AT", 1650), ("大和撫子 -Wild Dances- EZ", 274),
                  ("大和撫子 -Wild Dances- HD", 549), ("大和撫子 -Wild Dances- IN", 1002), ("混乱-Confusion EZ", 290),
                  ("混乱-Confusion HD", 602), ("混乱-Confusion IN", 978), ("混乱-Confusion Legacy", 753), ("Ark EZ", 290),
                  ("Ark HD", 523), ("Ark IN", 726), ("Break Through The Barrier EZ", 384),
                  ("Break Through The Barrier HD", 623), ("Break Through The Barrier IN", 1090),
                  ("Break Through The Barrier Legacy", 1293), ("Sein EZ", 203), ("Sein HD", 473), ("Sein IN", 721),
                  ("[PRAW] EZ", 419), ("[PRAW] HD", 692), ("[PRAW] IN", 1171), ("[PRAW] Legacy", 817),
                  ("Reimei EZ", 325), ("Reimei HD", 644), ("Reimei IN", 983), ("Starduster EZ", 280),
                  ("Starduster HD", 578), ("Starduster IN", 874), ("energy trixxx EZ", 252),
                  ("energy trixxx HD", 477), ("energy trixxx IN", 930), ("Pixel Rebelz EZ", 250),
                  ("Pixel Rebelz HD", 698), ("Pixel Rebelz IN", 941), ("Pixel Rebelz Legacy", 961),
                  ("RIPPER EZ", 520), ("RIPPER HD", 704), ("RIPPER IN", 1186), ("RIPPER Legacy", 1093),
                  ("Spasmodic EZ", 637), ("Spasmodic HD", 904), ("Spasmodic IN", 1389), ("Spasmodic AT", 1671),
                  ("尊師 ～The Guru～ EZ", 180), ("尊師 ～The Guru～ HD", 346), ("尊師 ～The Guru～ IN", 738),
                  ("After Dawn EZ", 194), ("After Dawn HD", 478), ("After Dawn IN", 975),
                  ("Better Graphic Animation EZ", 178), ("Better Graphic Animation HD", 469),
                  ("Better Graphic Animation IN", 616), ("Chronomia EZ", 338), ("Chronomia HD", 663),
                  ("Chronomia IN", 992), ("雪降り、メリクリ EZ", 316), ("雪降り、メリクリ HD", 559), ("雪降り、メリクリ IN", 939),
                  ("GOODFORTUNE EZ", 455), ("GOODFORTUNE HD", 733), ("GOODFORTUNE IN", 1011), ("Kerberos EZ", 262),
                  ("Kerberos HD", 683), ("Kerberos IN", 978), ("Nhelv EZ", 196), ("Nhelv HD", 571),
                  ("Nhelv IN", 833), ("NO ONE YES MAN EZ", 394), ("NO ONE YES MAN HD", 612),
                  ("NO ONE YES MAN IN", 844), ("Another Me EZ 4.8", 455), ("Another Me HD 9.2", 715),
                  ("Another Me IN 15.5", 1449), ("Concvssion EZ", 450), ("Concvssion HD", 700),
                  ("Concvssion IN", 1000), ("Aleph-0 EZ", 124), ("Aleph-0 HD", 438), ("Aleph-0 IN", 684),
                  ("Don't Never Around EZ", 308), ("Don't Never Around HD", 639), ("Don't Never Around IN", 1028),
                  ("Igallta EZ", 414), ("Igallta HD", 601), ("Igallta IN", 1018), ("Igallta AT", 1114),
                  ("SIGMA EZ", 352), ("SIGMA HD", 516), ("SIGMA IN", 785), ("Cthugha EZ", 378), ("Cthugha HD", 697),
                  ("Cthugha IN", 1333), ("Cthugha AT", 1444), ("Palescreen EZ", 224), ("Palescreen HD", 772),
                  ("Palescreen IN", 1059), ("Rrhar'il EZ", 446), ("Rrhar'il HD", 700), ("Rrhar'il IN", 1300),
                  ("Rrhar'il AT", 1300), ("望影の方舟Six EZ", 276), ("望影の方舟Six HD", 526), ("望影の方舟Six IN", 1066),
                  ("GOODRAGE EZ", 308), ("GOODRAGE HD", 628), ("GOODRAGE IN", 1034),
                  ("Non-Melodic Ragez (MUG Edit) EZ", 221), ("Non-Melodic Ragez (MUG Edit) HD", 604),
                  ("Non-Melodic Ragez (MUG Edit) IN", 1235), ("Non-Melodic Ragez (MUG Edit) Legacy", 1028),
                  ("RESSiSTANCE EZ", 499), ("RESSiSTANCE HD", 744), ("RESSiSTANCE IN", 1026),
                  ("Chronos Collapse - La Campanella EZ", 350), ("Chronos Collapse - La Campanella HD", 773),
                  ("Chronos Collapse - La Campanella IN", 1500), ("Chronostasis EZ", 596), ("Chronostasis HD", 665),
                  ("Chronostasis IN", 1156), ("CROSS†SOUL EZ", 517), ("CROSS†SOUL HD", 892),
                  ("CROSS†SOUL IN", 1305), ("Lyrith -迷宮リリス- EZ", 248), ("Lyrith -迷宮リリス- HD", 700),
                  ("Lyrith -迷宮リリス- IN", 1122), ("Lyrith -迷宮リリス- AT", 1236)]
    noteMin = 60
    noteMax = 1671
    scoreAnswer = AppropriateFraction(low, high, noteMin, noteMax)
    scoreList = []
    for i in scoreAnswer:
        for j in noteNumber:
            if j[1] == i[1]:
                scoreList.append([j[0], i[1], i[0]])
    for i in scoreList:
        m = i[2]
        good = (13 * m) % 20
        perfect = ceil((m - 137 * good) / 200)
        miss = i[1] - perfect - good
        combo = (m - 180 * perfect - 117 * good) // 20
        i[2] = (perfect, good, miss, combo)
    t = 0
    while t < len(scoreList):
        if scoreList[t][2][0] < 0 or scoreList[t][2][2] < 0 or scoreList[t][2][3] < 1 or (
                scoreList[t][2][0] + scoreList[t][2][1] == scoreList[t][1] and scoreList[t][2] != scoreList[t][1]):
            del scoreList[t]
        else:
            t = t + 1
    scoreListed = []
    for good in range(0, 20):
        for i in scoreList:
            if i[2][1] == good:
                scoreListed.append(i)
    if len(scoreListed) == 0:
        return "No Reasonable Output for Score=%d\n\n" % (score)
    else:
        answerList = ""
        i = 0
        while i < len(scoreListed):
            No = "%d" % (i + 1)
            answerList = answerList + No.zfill(len(str(
                len(scoreListed)))) + ". Score:%d Perfect:%d Good:%d Miss:%d Max Combo:%d in %s (note:%d)\n" % (
                         score, scoreListed[i][2][0], scoreListed[i][2][1], scoreListed[i][2][2],
                         scoreListed[i][2][3], scoreListed[i][0], scoreListed[i][1])
            i = i + 1
        print(answerList[:-1])
if __name__ == '__main__':

    # db = pymysql.connect(host='localhost',
    #                      user='root',
    #                      password='123456',
    #                      database='tag')  # 这里一定要改
    # i=r'c:/Users/46045/Desktop/deep'
    #
    # #('" + aaa + "')"
    # aaa='sadf'
    # cursor = db.cursor()
    # cursor.execute("insert into all_pic (FIRST_NAME) values ('"+ i + "')")
    # db.commit()

    # os.removedirs('asd')

    # def aaa():
    #     global ccc
    #     ccc={'dsfa':54,'g':54}
    #     return ccc
    # for c in aaa():
    #     print(c)
    # cursor.execute(sql)
    # cursor.fetchall()
    # print(table)
    # ass=['asdf','asd','sdfg','gsdghh']
    # aaa=input('dsa:')
    # for i in ass:
    #     if aaa in i:
    #         print(i)
    # os.startfile()
    # def hello():
    #     messagebox.showerror('hello')
    # b=tkinter.Button(text='点我',command=hello)
    # b.pack()
    # dict={}
    # def Merge(dict1, dict2):
    #     return (dict2.update(dict1))
    #
    #     # 两个字典
    # dict1 = {'a': 10, 'b': 8}
    # dict2 = {'d': 6, 'b': 4}
    #
    # # 返回  None
    # Merge(dict1, dict2)
    #
    # # dict2 合并了 dict1
    # dict1.update(dict2)
    # print(dict1)
    # for i in range(1,3):
    #     if i==1:
    #         dict=dict1
    #     else:
    #         dict=dict2
    #     print(dict.update(dict))




    Phigros(555555)