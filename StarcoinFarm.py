import datetime
import random
import time
from msp import invoke_method, get_session_id, ticket_header
logo ="""
  ____  _                      _         _____                    
 / ___|| |_ __ _ _ __ ___ ___ (_)_ __   |  ___|_ _ _ __ _ __ ___  
 \___ \| __/ _` | '__/ __/ _ \| | '_ \  | |_ / _` | '__| '_ ` _ \ 
  ___) | || (_| | | | (_| (_) | | | | | |  _| (_| | |  | | | | | |
 |____/ \__\__,_|_|  \___\___/|_|_| |_| |_|  \__,_|_|  |_| |_| |_|
 """
autor = """
discord.gg/TXXvjvbVQd
by p0nz1_
"""
print(logo,autor)
time.sleep(1)
USERNAME = input("USERNAME: ")
PASSWORD = input("PASSWORD: ")
SERVER = "fr"
code, resp = invoke_method(
    SERVER,
    "MovieStarPlanet.WebService.User.AMFUserServiceWeb.Login", 
    [
        USERNAME,
        PASSWORD,
        [],
        None,
        None,
        "MSP1-Standalone:XXXXXX"
    ],
    get_session_id()
)
status = resp.get('loginStatus', {}).get('status')
if status != "Success":
    print(f"Login failed, status: {status}")
    input(autor)
    quit()
ticket = resp['loginStatus']['ticket']
actor_id = resp['loginStatus']['actor']['ActorId']
pets =[
        3510330,3547505,2320229,1750253,1999077,4196487,2347541,3790632,2017916,2407715,        #Chambre de POUPINIE
        1769661,915279,1023555,786708,64079,64783,1952118,64125,64095,1209017,                  #Chambre de #LUSSY
        790398,1820536,2502648,869701,778860,1539150,2568090,695932,565245,1754529,             #Chambre de iavanka3009
        516,518,2513954,2352112,2400927,527,3138476,1616145,523,2351800,                        #Chambre de guilty974
        1057757,1391821,1106627,717291,961830,1015618,741586,847670,1305688,891933,             #Chambre de célyne
        520629,551142,50662,2665041,50659,50658,50664,50661,50663,508893,                       #Chambre de #Tom
        3356880,2762385,3849801,4304152,2531222,2822335,4211873,4146831,3928359,3007823,        #Chambre de thelm@
        553299,524737,248985,2867816,3079936,787293,248999,2665050,2116204,5150972,             #Chambre de prescillah
        1275198,282458,282460,1396939,1041779,855399,58642,4304620,529309,471529,               #Chambre de chana21
        1497946,1235839,2438028,2672534,2651360,2584436,1791602,1647763,1469531,2627822,        #Chambre de Lucianna 2521
        157939,849057,230744,670459,22696,431274,1065920,754196,1009485,529059,                 #Chambre de vita 83
        4323103,4323128,4287463,4287468,4318077,4304178,4287462,1410205,926994,4287465,         #Chambre de Circus
        4284744,4284738,4284740,4284742,4284741,4284749,4284745,4284736,4284747,4284743,        #Chambre de moon77
        3533260,3533262,3034883,3461297,3449536,3141569,2323357,3140281,3185384,3128019,        #Chambre de /Rebecca
        1735216,416550,2431318,2557560,494477,769306,1765322,547022,812740,520393,              #Chambre de larry0410
        5289049,5286713,5308980,5289040,5318626,5286715,5286708,5286712,5309184,5286711,        #Chambre de Boh
        2587516,2688917,3162357,2702529,4922416,2587507,2587515,4916828,2587523,2587529,        #Chambre de Bloodblazy
        2720206,2720190,2720204,3678108,2720193,2720192,2824809,2720211,3678114,3546251,        #Chambre de big boss du 25
        232696,1839,784716,232693,784715,232695,785466,784714,784712,1500581,                   #Chambre de FashonGirlish
        1690603,1551096,1234133,556246,1832691,2654734,816411,1977238,2172724,2455527,          #Chambre de Chelinca
        2528277,1958053,1318890,2528278,1751870,1115718,2528280,1819862,2221716,1243631,        #Chambre de #BIANKA
        5332878,5332882,5332885,5332884,5332879,5332981,5332982,5332980,5332979,5332883,        #Chambre de Matis
        1389,499914,574380,2305487,1381163,1687,1938381,1383,574362,1766069,                    #Chambre de Wallis la guerrière
        45826,4744151,1227354,4273677,5050546,2789507,2789505,4493716,2789503,4336270,          #Chambre de lazagne95
        2387600,2387592,2387589,2387605,2387607,2387608,2387603,2387615,2387606,2387616,        #Chambre de Cute-Angel
        4774096,4771950,4771957,4771964,4771953,4938047,4773215,4771960,4938046,4771958,        #Chambre de Framboise
        4735173,4735055,4735177,4735174,4735172,4735168,4735171,4735175,4735169,4735176,        #Chambre de sailor moon
        1945889,5235622,1330544,1607505,1218412,5065291,4480005,4628840,4182466,5043550,        #Chambre de claudine princesse
        5140866,5141216,5131341,5135461,4901630,5140692,5131359,5131361,4882578,5135464,        #Chambre de -modèle
        1143122,1143125,1574561,1143128,4929113,1143132,1143131,2537543,2537528,4639905,        #Chambre de houhoudake 79
        1449547,1378018,1631578,2704281,4848257,1572652,1572653,5300740,2813267,8175,           #Chambre de gygynana
        5222608,5218054,5215498,5174115,5245953,5196242,5231254,5144971,5156083,5228624,        #Chambre de XxXThunderXxX
        2073,1491693,1594088,130629,2379188,2320201,857638,130630,857187,130628,                #Chambre de Dcshoes 64
        2200670,2207206,2211542,2233853,5145593,2551529,2766949,2551533,2722720,2551532,        #Chambre de mathias89402
        1572629,1320719,4789076,4905917,2067992,5237009,5300743,4848719,1630824,1756392,        #Chambre de dany sam
        2412861,794358,811471,728564,1079912,839794,1035731,1211037,1210996,969952,             #Chambre de Nicotoy974
        3866191,4092813,5395883,6328557,6328549,6328559,6328551,6327805,3900226,3921986,        #Chambre de -Summer'
        995946,2154623,2871738,2481090,2871739,2627307,5323059,2251014,1964007,2871737,         #Chambre de estellebg21  
        2586399,2392096,2236681,2100698,2586396,2095047,2586380,2580694,2318941,2318943,        #Chambre de Spaghetti777
        2239963,2773363,1977353,2149571,2219305,2526035,2150354,2189578,3035440,3041948,        #Chambre de kazzandra
        4417339,4417338,4417337,4417334,4417336,4417335,4417333,4416516,4416495,4418026,        #Chambre de G0lden!
        2132718,3395373,1877498,1091566,1092579,1230893,1877499,1406611,2050483,1618111,        #Chambre de pépita !!!
        2992557,2992560,2992562,2992563,2992558,2992559,2992561,2981329,2982228,2981369,        #Chambre de Snow Gold
        3038232,3038276,3038283,3038282,3038281,3038280,3038277,3038279,3038284,3038229,        #Chambre de Sawaney
        1640572,1046693,656804,304778,501204,2061102,301095,1219091,289193,6555,                #Chambre de mis beaute3456
        4979548,4530144,2347752,4364134,4198214,4156626,4615605,4811799,5178110,4474175,        #Chambre de lili evangeline
        1499244,1438004,1660945,1106317,4919154,1365621,1660946,1660943,882461,1060808,         #Chambre de coeurdeperle
        3080731,1470721,1485261,2387560,1462202,5319108,1560876,1641112,1354328,1505800,        #Chambre de MAMINOU67
        3833233,4948918,4948846,4948825,3833237,4948824,3833235,3833244,4019130,3833236,        #Chambre de -Gücci
        521150,382662,547318,639967,4975652,4249839,3640564,473707,506932,4937816,              #Chambre de pinklove49 
      ]
Sc_count = 0
pets_count = 0
pets_pets = 0
for pet_id in pets:
    code, resp = invoke_method(
        SERVER,
        "MovieStarPlanet.WebService.Bonster.AMFBonsterService.PetFriendBonster", 
        [
            ticket_header(ticket),
            actor_id,
            pet_id
        ],
        get_session_id()
    )
    if code != 200:
        print(f"Error: HTTP Status Code {code}")
        continue
    pets_pets +=1
    if resp == 5:
        print(f'{pets_pets}/500  Starcoin: +5')
        Sc_count+=5
    elif resp == 0:
        print(f'{pets_pets}/500  Starcoin: +0')
    else:
        print(f'{pets_pets}/500  Error:  {resp}')    
    time.sleep(random.randint(1, 3))
    pets_count += 1
    if pets_count >= 10:
        time.sleep(random.randint(2, 6))
        pets_count = 0
print(f"Total + {Sc_count} Starcoin")  
input(autor)
input("Appuyez sur Entrée pour quitter...")
