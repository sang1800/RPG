#! python3
import sys
import os
import random
import time

def Fab():
    append = ("""
    Minotaur
    I'm fabulous

     .      .
     |\____/|
    (\|----|/)
     \ 0  0 /
      |    |
   ___/\../\____
  /     --       \\
 /  \         /   \\
|    \___/___/(   |
\   /|  }{   | \  )
 \  ||__}{__|  |  |
  \  |;;;;;;;\  \ / 
   \ /;;;;;;;;| [,,
     |;;;;;;/ |   
     ||;;|\   |
     ||;;/|   /
     \_|:||__|
      \ ;||  /
      |= || =|
      |= /\ =|
      /_/  \_\
""")
    global append
    show()

def Mac():
    append = ("""
    Snapple computer
    You wanna play games on me?
    screw you
                  ____________________________
                 !\_________________________/!\\
                 !!                         !! \\
                 !!                         !!  \\
                 !!                         !!  !
                 !!      Snapple            !!  !
                 !!                         !!  !
                 !!                         !!  !
                 !!                         !!  !
                 !!                         !!  /
                 !!_________________________!! /
                 !/_________________________\!/
                   __\_________________/__/!_
                 /oooo  oooo  oooo  oooo /!
                /ooooooooooooooooooooooo/ /
               /ooooooooooooooooooooooo/ /
              /C=_____________________/_/
""")
    global append
    show()

def preacher():
    append = ("""
     Jehovah's witness
     would you like to talk about our lord and savior?
                     ___
                    /___\\
                    |. .|
                   (   > )
                    \ < /
                     )_(
                   .;_u_;.
                  /       \\
                 ; | _|_ | ;
                 | |  |  | |
                 | \  '  / |
                 | /\   /\ |
                 |/\/   \/\|
                 `|       |`
                  |       |
                  `;-----;`
                   |     |
                   |_____|
                    / | \\
                   (_/ \_)

""")
    global append
    show()
    
def Germany():
    append = ("""
     Germany
     Germany has attacked!
     again......
 +------------------+
 |       ___        |
 |   _  (,~ |   _   |
 |  (____/  |____)  |
 |  |||||    |||||  |
 |  |||||    |||||  |
 |  |||||\  /|||||  |
 |  |||'//\/\\`|||  |
 |  |' m' /\ `m `|  |
 |       /||\       |
  \_              _/
    `------------'
    """)
    global append
    show()

def Castle():
    append = ("""               
          The kingdom of SJW 
          you made one joke about the gays 
          and offended a whole nation            
                       
                                                    !_
                                                    |*~=-.,
                                                    |_,-'`
                                                    |
                                                    |
                                                   /^\\
                     !_                           /   \\
                     |*`~-.,                     /,    \\
                     |.-~^`                     /#"     \\
                     |                        _/##_   _  \_
                _   _|  _   _   _            [ ]_[ ]_[ ]_[ ]
               [ ]_[ ]_[ ]_[ ]_[ ]            |_=_-=_ - =_|
             !_ |_=_ =-_-_  = =_|           !_ |=_= -    |
             |*`--,_- _        |            |*`~-.,= []  |
             |.-'|=     []     |   !_       |_.-"`_-     |
             |   |_=- -        |   |*`~-.,  |  |=_-      |
            /^\  |=_= -        |   |_,-~`  /^\ |_ - =[]  |
        _  /   \_|_=- _   _   _|  _|  _   /   \|=_-      |
       [ ]/,    \[ ]_[ ]_[ ]_[ ]_[ ]_[ ]_/,    \[ ]=-    |
        |/#"     \_=-___=__=__- =-_ -=_ /#"     \| _ []  |
       _/##_   _  \_-_ =  _____       _/##_   _  \_ -    |\\
      [ ]_[ ]_[ ]_[ ]=_0~{_ _ _}~0   [ ]_[ ]_[ ]_[ ]=-   | \\
      |_=__-_=-_  =_|-=_ |  ,  |     |_=-___-_ =-__|_    |  \\
       | _- =-     |-_   | ((* |      |= _=       | -    |___\\
       |= -_=      |=  _ |  `  |      |_-=_       |=_    |/+\|
       | =_  -     |_ = _ `-.-`       | =_ = =    |=_-   ||+||
       |-_=- _     |=_   =            |=_= -_     |  =   ||+||
       |=_- /+\    | -=               |_=- /+\    |=_    |^^^|
       |=_ |+|+|   |= -  -_,--,_      |_= |+|+|   |  -_  |=  |
       |  -|+|+|   |-_=  / |  | \     |=_ |+|+|   |-=_   |_-/
       |=_=|+|+|   | =_= | |  | |     |_- |+|+|   |_ =   |=/
       | _ ^^^^^   |= -  | |  <&>     |=_=^^^^^   |_=-   |/
       |=_ =       | =_-_| |  | |     |   =_      | -_   |
       |_=-_       |=_=  | |  | |     |=_=        |=-    |
 `^^^^^^^^^^`^`^^`^`^`^^^""""""""^`^^``^^`^^`^^`^`^``^`^``^``^^""")
    global append
    show()

def Alien():
    append = ("""       
       Ay Lmao
       please stop making that joke, it's very old
                _____
             ,-"     "-.
            / o       o \\
           /   \     /   \\
          /     )-"-(     \\
         /     ( 6 6 )     \\
        /       \ " /       \\
       /         )=(         \\
      /   o   .--"-"--.   o   \\
     /    I  /  -   -  \  I    \\
 .--(    (_}y/\       /\y{_)    )--.
(    ".___l\/__\_____/__\/l___,"    )
 \                                 /
  "-._      o O o O o O o      _,-"
      `--Y--.___________.--Y--'
         |==.___________.==| 
         `==.___________.=='
""" )
    global append
    show()

def Imp():
    append = ("""
    IMP
    I'm magical, be scared,
    boooooooooooooooo
       *                       *
        *                 *
       )       (\___/)     (
    * /(       \ (. .)     )\ *
      # )      c\   >'    ( #
       '         )-_/      '
     \\|,    ____| |__    ,|//
       \ )  (  `  ~   )  ( /
        #\ / /| . ' .) \ /#
        | \ / )   , / \ / |
         \,/ ;;,,;,;   \,/
          _,#;,;;,;,
         /,i;;;,,;#,;
        //  %;;,;,;;,;
       ((    ;#;,;%;;,,
      _//     ;,;; ,#;,
     /_)      #,;    ))
             //      \|_
             \|_      |#\\
              |#\      -  """)
    global append
    show()

def Troll():
    append = ("""
        Troll
        I'm not the troll on the internet!
                                              ,--,  ,.-.
                ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\         }  )/  / `-,',
               [ '          |\  /|   | |        /  \|  |/`  ,`
               | |       ,.`  `,` `, | |  _,...(   (      _',
               \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\\
                \  \_\,``,   ` , ,  /  |         )         _,/
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `\\
                -,-..\  _  \  `  /  ,  / `._) _,-\`       \\
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                ,` )  | \_\       '-`  |  `(               \\
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \\ V   V, /`     /
    ,--\(        ,     <_/`\\     ||      /
   (   ,``-     \/|         \-A.A-`|     /
  ,>,_ )_,..(    )\          -,,_-`  _--`
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`
   `                      ```""")
    global append
    show()

def Spider():
    append = (""" 
        Spider
        touch me, I dare you            
           /      \\
        \  \  ,,  /  /
         '-.`\  /`.-'
        .--_'    '_--.
       / /` /`  `\ `\ \\
        |  |      |  |
        \  \      /  /
            '.__.        """)
    show()

def Reaper():
    append = ("""
        Reaper
        i just wanna hang out with people, why is it so hard?
                                           .""--..__
                     _                     []       ``-.._
                  .'` `'.                  ||__           `-._
                 /    ,-.\                 ||_ ```---..__     `-.
                /    /:::\\               /|//}          ``--._  `.
                |    |:::||              |////}                `-. \\
                |    |:::||             //'///                    `.\\
                |    |:::||            //  ||'                      `|
                /    |:::|/        _,-//\  ||
               /`    |:::|`-,__,-'`  |/  \ ||
             /`  |   |'' ||           \   |||
           /`    \   |   ||            |  /||
         |`       |  |   |)            \ | ||
        |          \ |   /      ,.__    \| ||
        /           `         /`    `\   | ||
       |                     /        \  / ||
       |                     |        | /  ||
       /         /           |        `(   ||
      /          .           /          )  ||
     |            \          |     ________||
    /             |          /     `-------.|
   |\            /          |              ||
   \\/`-._      |           /              ||
    //   `.    /`           |              ||
   //`.    `. |             \              ||
  ///\ `-._  )/             |              ||
 //// )   .(/               |              ||
 ||||   ,'` )               /              //
 ||||  /                    /             || 
 `\\` //`                    |             // 
     |`                     \            ||  
    /                        |           //  
  /`                          \         //   
/`                            |        ||    
`-.___,-.      .-.        ___,'        (/    
         `---'`   `'----'`""")
    global append
    show()

def RandEnemy():
    y = random.randint(1,10)
    if y == 1:
        Troll()
    elif y == 2:
        Spider()
    elif y == 3:
        Reaper()
    elif y == 4:
        Imp()
    elif y == 5:
        Alien()
    elif y == 6:
        Castle()
    elif y == 7:
        preacher()
    elif y == 8:
        Mac()
    elif y == 9:
        Fab()
    else:
        Germany()



def show():
    print (append)

class WeirdEnemy:
    def __intit__(self):
        self.Maxhp = 50
        self.hp = 50
        self.attack = 10
EnemyIG = WeirdEnemy()


class MonkeyBoy:
    def __init__(self):
        self.name = "Monkey Boy"
        self.Maxhp = 100
        self.Hp= self.Maxhp
        self.attack = 10
        self.defense = 10
MonkeyBoyIG = MonkeyBoy()

#start game
def main():
    os.system('cls')
    print ("""
   _.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._._.-._.-._.-._.-._.-._.-._.-._
 ,'_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._._.-._.-._.-._.-._.-._.-._.-. `.
 ( (                                                                                     ) )
 ) )                                                                                    ( (
( (                         ____     _____                                               ) )
 ) )                        / __ \   / ____|                                             ( (
( (                        | |  | | | |     _ __ _____      __                            ) )
 ) )                       | |  | | | |    | '__/ _ \ \ /\ / /                           ( (
( (                        | |__| | | |____| | |  __/\ V  V /                             ) )
 ) )                        \___\_\  \_____|_|  \___| \_/\_/                             ( (
( (                                                                                       ) )
 ) )                                                                                     ( (
( (                                                                                      ) )
 ) )           -----------------------::/+++++//:--------------------------             ( (
( (            --------------------/oyyhhhhhhhhhhys+/----------------------              ) )
 ) )           -----://////:----:oyhhhhhhhhhhhdhdhhhhy+----://++++/:-------             ( (
( (            --:+syhyyyyyyyo/+hhhhhhhhhhhhhhhhdhhhdhhs:/syhhhhdddhs:----:              ) )
 ) )           -+yyyhyhhhhhhhhhhhhhhhhddhhdhddddmdddddddhdhhhddmmmdddh/--:-             ( (
( (            +hyyhhddddddddhhhhhhhdhddmddddmmmmmmmmddddddmmmmmNNNmhdh::::              ) )
 ) )           yyyyhdmmmmmmmmhhhhhhdddmmmmmmdmmmmmmmmmddddmmNNmNNNNNddds:-:             ( (
( (            hhhydmmmmmmmmdhhhhhhddmmmmmmmmmmmmmmmmdddddmNNNNNNNNNmddm:::              ) )
 ) )           yhhhdmmmmmmmmdhhhhhhdmmmmmmmmmmmmmmmmddddddmNNNNNNNNNmddm:::             ( (
( (            ohhhhdmmmmmmmmhhhhhhhdddmmmmmmmmmmmmmdddddddmNNNNNNNNdddy:-:              ) )
 ) )           :yhhhhddmmmdddhddhhhhhdddmmmmmmmmmmmmmmddddmmmmmNNmmdddd::-:             ( (
( (            -:yhhhyhhhhhhhhhhhhdhhddmmmmmmmmmmmmmmmddddddhhdddhhddd+-:::              ) )
 ) )           ---+yyhhhhhyso/+hhhddhddmmmmmmmmmmmmmmmddho+oyhhhhhhhy/---::             ( (
( (            -----/+oo+/:----:oyhhhddmmmmmmmmmmmmmmdyo:----:++++/:------:              ) )
 ) )           -------------------:/+oymmmmmmmmmmmmms:---------------------             ( (
( (            --------------------------QCrewTM---------------------------              ) )
 ) )                                                                                    ( (
( (                                                                                      ) )
 ) )                                                                                    ( (
( (_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.) )
 `._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.,'
          """)
    print("welcome to the game\n")
    print("1) start")
    print("2) load")
    print("3) exit")
    option = input("--> ")
    if option == "1":
        selection()
    elif option == "2":
        main()
    elif option == "3":
        print("leaving already?")
        time.sleep(3)
        sys.exit()

    else:
        main()

#character selection
def selection():
    os.system('cls')
    print ("""
*/***/***/*/*/*******////*//////*/*/////,*,**/((((((((/*****/*//**************************,********
/***/*////////*****/*/////*/*//*//////**(((****/*********((((/****/**/*///**/********************,*
//////*////////****//*//*//***/*****((*****///*/*******/*/****/#(/////////**/*/***/****************
///////////////****///*////*/*,**((**********/*/**********/*******((/**///////***/**/**//**********
//////////////////**/****/***/((/************/***/************//*/**/(/*////**/***/**/*//**********
//////////(//////**/**,*****((/*****,******//*/*************//*////****#(*///*******/**///*//******
////////////////////***/**/#****************/**/*****,******///////******#//*//**//*///////********
/////////////////////****/(*****,**********///*/*/*******/***/////****//**/#*//****//////////*****/
//////////(//////////***/(****************/**/*/////***//***/*////////*/*/**#/******/((/****///****
*/////////##(***//##/***/#***************/*///////**//*//////*/***////**/****(//(#/**//*/*/#(//////
////////#(****//*////(#//(**************//////////////*//***////**/(((#(*///**#/********///*/(*////
///////(/**//*/////////###/********(((((((((((###(//**//******(###((((((((#(*/((*/((////**////#////
////(/#/////*///////*////#//**/**#((((#(((((((((#####//***/##(((((#(((((((((#*(%#(((((##(//*///#///
/////((/*/*///########(//#(/*//*(((((((#((##(#(#(((#(##(#(((((#((#(#((#(((#((#(#(((#(((((##////((//
///*(#/****###(#(####(##/((/*///#((/(/(((##((#####(###(((((((((((/,   /#((#(((%(#(((((#((((#////#//
////#/*/**##(((###(#####(/////*/#(/#.     *((##((#####((((((((      .((#(#(#(###(((((((###(##////(/
//*((////###(((((#####(##///////#((/((        *###(##(#(((((((*   *(((((((#(##(#((((((((###(#////#*
//(#(////######(((((##((##////*//#((((((#(((((##((((#####(#(#(#((#(##(##(####//#(#((((((##((#(//*(*
(//#/////###(##(((((###((##//**//*(#((((((((((((((##(####(#####((##((#####(*///#(((((((((##(##///(/
///(#////##(##((#((#((##((##/***/////(########(##(#(#(###(((##(#######(////////#((((((((((((#(*/*/(
////#////(#(#(((((((((((##(##//////********(#(((((((((((#(#(#(#(#(((((##//****/##(((((((((((#(*/*/(
//(/(#////####((((((((#(###((#//*/********/#(((((((((((((((((((((((##((##/***/######((((((((#///*((
/(//*#(////#########(###(###(///#/*/******#((#((((((((((((((((((((((((((#/***#/#####((((#((#/////#(
//(///##////(##############/*///#********(#((#((((((((((((((((((((((((((##**/(*//##########//**/#//
/(/////(#//////#########(////*((#//******#(((((((((/((((((((((((((((((((##//#////////////////**#///
///////((#(////*///////*//**/#/#/#/******#((((((((((((/(((/((((((((((((((#*#//#////////////**/#////
///////((/(##////*//*///***(#**#//(#****/#((((((((((/(((((((((((((((((#((%#(****#(/////*/**/#(***/*
//(//////////##(**//*,*/###/*/*/#////#(**##(((((((((/((((((((((((((((((((#(******/(###(///#(***//**
////////(/////(/((####(////*////#///*//##(#((((((((((((((((((((((((((((((#********////////////////*
/////////////((((((((///////////#(//////*/##(((((((((((((((((((((((((((##*/*********///*////*/**//*
//((((/(//(//(((((/(((//////////(#*///**/*/*/###((((((#(#((###((((((((##//**********/**///*////////
///////(///(((((//(/((//////////*#*//*/*//***/*/##(((####(#((##(((((##/*///****,,***/*//***////////
/////(//((//(((//(/(/(//////(###%#//*//*/******///*#####(######(#((#/*///*/*************/////////*/
////////////(((((((((////(###((((#/**/***//**/***/*/***/*/(////######////////**/*,***//**//////////
/////*/*////((/((((///###((#((((/#/**/****#/***************#***(#((#####(*/////*****///////////////
********/////////(#####(##(#((((/#/*//*****#/************(#***//#(####(#(###/*//*///////////(/////*
********///////(#########((((((/(((///******#*******,***/#/*****#(((#(####((##(////////////////////
    """)
    print ("""
                                         __                 __               
                  ____ ___  ____  ____  / /_____  __  __   / /_  ____  __  __
                 / __ `__ \/ __ \/ __ \/ //_/ _ \/ / / /  / __ \/ __ \/ / / /
                / / / / / / /_/ / / / / ,< /  __/ /_/ /  / /_/ / /_/ / /_/ / 
               /_/ /_/ /_/\____/_/ /_/_/|_|\___/\__, /  /_.___/\____/\__, /  
                                               /____/               /____/  
    """)
    choose2 = input("-->")
    load()

def load():
    for x in range (0, 4):
        os.system('cls')
        print ("""  


   
loading...
 

        *  *              *  *
     *        *        *        *
    *          *      *          *
    *          *      *          *
     *        *        *        *
        *  *              *  *   
            """)
        time.sleep(.1)
        os.system('cls')
        print ("""      


   
loading...


        *                    *
     *        *        *        *
    *          *      *          *
    *          *      *          *
     *        *        *        *
        *  *              *  * 
           """)
        time.sleep(.1)
        os.system('cls')
        print ("""



loading...


        *  *              *   *     
     *                           * 
    *          *      *           *  
    *          *      *           *  
     *        *        *         *  
        *  *              *   *             
           """)
        time.sleep(.1)
        os.system('cls')
        print ("""



loading...


        *  *              *  *
     *        *        *        *
    *                            *
    *          *      *          *
     *        *        *        *
        *  *              *  *

           """)
        time.sleep(.1)
        os.system('cls')
        print ("""



loading...


        *  *              *  *
     *        *        *        *
    *          *      *          *
    *                            *
     *        *        *        *
        *  *              *  *

           """)
        time.sleep(.1)
        os.system('cls')
        print ("""



loading...


        *  *              *  *
     *        *        *        *
    *          *      *          *
    *          *      *          *
     *                          *
        *  *              *  *

           """)
        time.sleep(.1)
        os.system('cls')
        print ("""



loading...


        *  *              *  *
     *        *        *        *
    *          *      *          *
    *          *      *          *
     *        *        *        *
        *                    *

           """)
        time.sleep(.1)
        os.system('cls')
        print ("""



loading...


        *  *              *  *
     *        *        *        *
    *          *      *          *
    *          *      *          *
     *        *        *        *
           *              *    

           """)
        time.sleep(.1)
        os.system('cls')
        print ("""



loading...


        *  *              *  *
     *        *        *        *
    *          *      *          *
    *          *      *          *
              *        *        
        *  *              *  *

           """)
        time.sleep(.1)
        os.system('cls')
        print ("""



loading...


        *  *              *  *
     *        *        *        *
    *          *      *          *
               *      *          
     *        *        *        *
        *  *              *  *

           """)
        time.sleep(.1)
        os.system('cls')
        print ("""



loading...


        *  *              *  *
     *        *        *        *
               *      *          
    *          *      *          *
     *        *        *        *
        *  *              *  *
           """)
        time.sleep(.1)
    start()

#begin game
def start():
    os.system('cls')
    print("                                                                    ..;===+.")
    print("                                                                .:=iiiiii=+=")
    print("                                                              .=i))=;::+)i=+,")
    print("                                                           ,=i);)I)))I):=i=;")
    print("                                                        .=i==))))ii)))I:i++")
    print("                                                      +)+))iiiiiiii))I=i+:'")
    print("                                 .,:;;++++++;:,.       )iii+:::;iii))+i='")
    print("                              .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'")
    print("                            ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:")
    print("                         ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+")
    print("                         ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,")
    print("                       ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+")
    print("                      ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='")
    print("                     ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`")
    print("                    =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'")
    print("                    +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,")
    print("                    =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;")
    print("                   .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;")
    print("                   :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:")
    print("                   :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=")
    print("                   .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+")
    print("                   =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'")
    print("                 +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;")
    print("               +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;")
    print("              =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;")
    print("            +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,")
    print("         :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+'")
    print("        .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+")
    print("       ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'")
    print("      +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'")
    print("    .+=:))iiiiiiii)))+ii;")
    print("   .+=;))iiiiii)));ii+")
    print("  .+=i:)))))))=+ii+")
    print(" .;==i+::::=)i=;")
    print(" ,+==iiiiii+,")
    print(" `+=+++;`")
    print("your ship arrived at and unknown planet\n")
    time.sleep(1)
    print("1) land\n2) no\n")
    choose3 = input("Mother Board: would you like to land? ")
    if choose3 == "1":
        begin()
    elif choose3 == "2":
        print("I guess we're not having an adventure today")
        time.sleep(3)
        sys.exit()
    else:
        print("Mother Board: I did not get that\n")
        start()

#on the planet
def begin():
    os.system('cls')
    print("           ccee88oo                  ccee88oo")
    print("        C8O8O8Q8PoOb o8oo          C8O8O8Q8PoOb o8oo")
    print("      dOB69QO8PdUOpugoO9bD       dOB69QO8PdUOpugoO9bD")
    print("     CgggbU8OU qOp qOdoUOdcb    CgggbU8OU qOp qOdoUOdcb")
    print("        6OuU  /p u gcoUodpP     CgggbU8OU qOp qOdoUOdcb")
    print("           \\\//  /douUP           6OuU  /p u gcoUodpP")
    print("            \\\////                 \\\//  /douUP")
    print("             |||||                   \\\////")
    print("             |||||                    |||||")
    print("             |||||                    |||||" )
    print("       .....//||||\....               |||||"  )                                                                                                                                                
    print("you landed")
    time.sleep(3)
    option()

#player's choice 
def option():
    os.system('cls')
    print ("""
                          ___\____
                       0)__/... \_
                      00)__)  .___)
     ___              _0__)\_/ OOO/`':.
    0)_^'-._    __..-'`:  \ | / ::  \ o`:
    0)_\ \~_..-': \ \   :  \|/   ::  |   \\
        \ /      : | |  :    :  ::  /  _./>-
         (__ ))): /_/____.))_____//.-'`
    """)
    print("1) explore\n2) stand around\n3) sleep\n")
    choice = input("What you you like to do? ")
    if choice == "1":
        explore()
    elif choice == "2":
        print("you stood around")
        time.sleep(3)
        print("doing nothing\n")
        time.sleep(1)
        option()
    elif choice == "3":
        print("you went to sleep\n")
        time.sleep(1)
        option()
    else:
        option()
 

#explore
def explore():
    os.system('cls')
    time.sleep(1)
    global chance
    chance = random.randint(0,19)
    if chance == 1:
        print("you walked deeper into the dark wood")
        time.sleep(1)
        option()
    elif chance == 2:
        print("you encountered an enemy!")
        time.sleep(1)
        RandEnemy()
        fight()
    elif chance == 3:
        print("you've been ambushed!")
        time.sleep(1)
        RandEnemy()
        fight()
    elif chance == 4:
        print("you hear rustling behind you")
        time.sleep(1)
        RandEnemy()
        fight()
    elif chance == 5:
        print("you stubbed your toe on a rock")
        time.sleep(1)
        option()
    elif chance == 6:
        print("""     
you see a pyramid and thought to yourself:
do I really want to die today?
you say no          
               '
              /=\\
             /===\ \\
            /=====\' \\
           /=======\'' \\
          /=========\ ' '\\
         /===========\''   \\
        /=============\ ' '  \\
       /===============\   ''  \\
      /=================\' ' ' ' \\
     /===================\' ' '  ' \\
    /=====================\' '   ' ' \\
   /=======================\  '   ' /
  /=========================\   ' /
 /===========================\'  /
/=============================\/""")
        time.sleep(3)
        option()
    elif chance == 7:
        print("you got bored of walking")
        time.sleep(1)
        option()
    elif chance == 8:
        print("you think about life as you walk")
        time.sleep(1)
        option()
    elif chance == 9:
        print("You start humming your favorite song")
        time.sleep(1)
        option()
    elif chance == 10:
        print("a branch smacked you across the face")
        time.sleep(1)
        option()
    elif chance == 11:
        print("you looked up in the sky and regret this decision")
        time.sleep(2)
        option()
    elif chance == 12:
        print("What was that?!")
        time.sleep(1)
        RandEnemy()
        fight()
    elif chance == 13:
        print("uh oh")
        time.sleep(1)
        RandEnemy()
        fight()
    elif chance == 14:
        print("Aw hell naw")
        time.sleep(1)
        RandEnemy()
        fight()
    elif chance == 15:
        print("who the hell?")
        time.sleep(1)
        RandEnemy()
        fight()
    elif chance == 16:
        print("every single time!!")
        time.sleep(2)
        RandEnemy()
        fight()
    elif chance == 17:
        print(" fly me to the moon, and let me play among the stars ")
        time.sleep(1)
        option()    
    elif chance == 18:
        print("""" Start spreadin' the news, I'm leavin' today
            I want to be a part of it, New York, New York """)
        time.sleep(2)
        option()   
    elif chance == 19:
        print(""" 
                 And now, the end is near
                 And so I face the final curtain
                 My friend, I'll say it clear
                 I'll state my case, of which I'm certain """)
        time.sleep(3)
        option()   
    else:
        print ("you stepped into the wrong territory")
        time.sleep(2)
        bossfight()


def fight():
    os.system('cls')
    show()
    print ("1.) Attack")
    print ("2.) Drink Q Juice")
    print ("3.) Run")
    option = input("--> ")
    if option == "1":
        attack()
    elif option == "2":
        print ("you drank some of those delicious goodness")
        time.sleep(1)
        print ("heyyyyy, that's pretty goooooood")
        time.sleep(1)
        os.system('cls')
        fight()
    elif option == "3":
        run()
    else:
        fight()

def attack():
    os.system('cls')
    Pattack = random.randint(0, 10)
    if Pattack < 4:
        os.system('cls')
        show()
        print ("you missed\n")
        time.sleep(1)
        enemyAttack()
        fight()
    elif Pattack > 4 < 6:
        os.system('cls')
        show()
        print ("you damaged the enemy!")
        time.sleep(1)
        enemyAttack()
        fight()
    elif Pattack == 6:
        os.system('cls')
        win()
    else:
        os.system('cls')
        global Pattack
        print ("you ended the enemy rightly")
        print ("""
           $$$$$$$$$$$$$$$$$$$$$$$$$
           $$$$$'`$$$$$$$$$$$$$'`$$$
           $$$$$$  $$$$$$$$$$$  $$$$
           $$$$$$$  '$/ `/ `$' .$$$$
           $$$$$$$$. i  i  /! .$$$$$
           $$$$$$$$$.--'--'   $$$$$$
           $$^^$$$$$'        J$$$$$$
           $$$   ~""   `.   .$$$$$$$
           $$$$$e,      ;  .$$$$$$$$
           $$$$$$$$$$$.'   $$$$$$$$$
           $$$$$$$$$$$$.    $$$$$$$$
           $$$$$$$$$$$$$     $$$$$$$
""")
        time.sleep(2)
        option()
        

def enemyAttack():
    os.system('cls')
    Eattack = random.randint(0, 20)
    if Eattack < 7:
        os.system('cls')
        show()
        print ("the enemy missed\n")
        time.sleep(1)
        fight()
    elif Eattack > 7 < 16:
        os.system('cls')
        show()
        print ("the enemy deals damage!\n")
        time.sleep(1)
        fight()
    if Eattack > 19:
        death = random.randint(1,5)
        if death == 1:
            print ("you lived a good life")
            time.sleep(2)
            die()
        elif death == 2:
            print ("woops")
            time.sleep(2)
            die()
        elif death == 3:
            print ("you died a hero...I think")
            time.sleep(2)  
            die()
        elif death == 4:
            print ("I'm so sorry Wilson!!!! oh, wrong reference?")
            time.sleep(2)
            die()
        else:
            print ("it's ok, tis' but a scratch wound")
            time.sleep(2)
            die()
    else: 
        fight()

def run():
    os.system('cls')
    runChance = random.randint(1,2)
    if runChance == 1:
        print ("you got the hell out of there")
        time.sleep(1)
        option()
    else:
        print ("fight! you lil chicken!")
        time.sleep(1)
        fight()

def bossfight():
    append = ("""
        Knight on a dragon

                       //\\
                        ||
                        ||
                        ||
                        ||                                               ~-----~
                        ||                                            /===--  ---~~~
                        ||                   ;'                 /==~- --   -    ---~~~
                        ||                (/ ('              /=----         ~~_  --(  '
                        ||             ' / ;'             /=----               \__~
     '                ~==_=~          '('             ~-~~      ~~~~        ~~~--\~'
     \\                (c_\_        .i.             /~--    ~~~--   -~     (     '
      `\               (}| /       / : \           / ~~------~     ~~\   (
      \ '               ||/ \      |===|          /~/             ~~~ \ \(
      ``~\              ~~\  )~.~_ >._.< _~-~     |`_          ~~-~     )
       '-~                 {  /  ) \___/ (   \   |` ` _       ~~         '
       \ -~\                -<__/  -   -  L~ -;   \\    \ _ _/
       `` ~~=\                  {    :    }\ ,\    ||   _ :(
        \  ~~=\__                \ _/ \_ /  )  } _//   ( `|'
        ``    , ~\--~=\           \     /  / _/ / '    (   '
         \`    } ~ ~~ -~=\   _~_  / \ / \ )^ ( // :_  / '
         |    ,          _~-'   '~~__-_  / - |/     \ (
          \  ,_--_     _/              \_'---', -~ .   \\
           )/      /\ / /\   ,~,         \__ _}     \_  "~_
           ,      { ( _ )'} ~ - \_    ~\  (-:-)       "\   ~ 
                  /'' ''  )~ \~_ ~\   )->  \ :|    _,       " 
                 (\  _/)''} | \~_ ~  /~(   | :)   /          }
                <``  >;,,/  )= \~__ {{{ '  \ =(  ,   ,       ;
               {o_o }_/     |v  '~__  _    )-v|  "  :       ,"
               {/"\_)       {_/'  \~__ ~\_ \\_} '  {        /~
               ,/!          '_/    '~__ _-~ \_' :  '      ,"  ~ 
              (''`                  /,'~___~    | /     ,"  \ ~' 
             '/, )                 (-)  '~____~";     ,"     , }
           /,')                    / \         /  ,~-"       '~'
       (  ''/                     / ( '       /  /          '~'
    ~ ~  ,, /) ,                 (/( \)      ( -)          /~'
  (  ~~ )`  ~}                   '  \)'     _/ /           ~'
 { |) /`,--.(  }'                    '     (  /          /~'
(` ~ ( c|~~| `}   )                        '/:\         ,'
 ~ )/``) )) '|),                          (/ | \)                 
  (` (-~(( `~`'  )                        ' (/ '
   `~'    )'`')                              '
      """)
    global append
    os.system('cls')
    Eattack = random.randint(0, 20)
    if Eattack < 4:
        os.system('cls')
        show()
        print ("the enemy missed\n")
        time.sleep(2)
        fight()
    elif Eattack > 4 < 6:
        os.system('cls')
        show()
        print ("the enemy deals damage!\n")
        time.sleep(2)
        fight()
    elif Eattack > 6 < 13:
        death = random.randint(1,5)
        if death == 1:
            print ("you lived a good life")
            time.sleep(2)
            die()
        elif death == 2:
            print ("woops")
            time.sleep(2)
            die()
        elif death == 3:
            print ("you died a hero...I think")
            time.sleep(2)  
            die()
        elif death == 4:
            print ("I'm so sorry Wilson!!!! oh, wrong reference?")
            time.sleep(2)
            die()
        else:
            print ("it's ok, tis' but a scratch wound")
            time.sleep(2)
            die()
    else: 
        os.system('cls')
        show()
        print ("The knight channels his energy")
        time.sleep(2)
        energy = random.randint(1,5)
        if energy > 1 < 3:
            print ("woops")
            time.sleep(2)
            die()
        elif energy == 4:
            print ("you died a hero...I think")
            time.sleep(2)  
            die()
        else:
            print ("it's ok, tis' but a scratch wound")
            time.sleep(2)
            die()

def win():
    print ("""thank you for playing!
            please support QCrew comics and have a good day!""")
    time.sleep(4)
    main()


def die():
    print ("""      __.....__
            .'         ':,
           /  __  _  __  \\
           | |_)) || |_))||
           | | \\ || |   ||
           |             ||   _,
           |             ||.-(_{}
           |             |/    `
           |        ,_ (\;|/)
         \\|       {}_)-,||`
         \\;/,,;;;;;;;,\\|//,
        .;;;;;;;;;;;;;;;;,
       \,;;;;;;;;;;;;;;;;,//
      \\;;;;;;;;;;;;;;;;,//
     ,\';;;;;;;;;;;;;;;;'
       ;;;;;;;;;;;'''`
 """)
    main()


main()
