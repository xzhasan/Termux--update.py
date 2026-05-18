import os

banner1 = '''
-- ╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗
-- ╠╬╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╬╣
-- ╠╣M""MMMM""M             M""MMMMM""MM MMP"""""""MM MP""""""`MM MMP"""""""MM M"""""""`YM╠╣
-- ╠╣M  `MM'  M             M  MMMMM  MM M' .mmmm  MM M  mmmmm..M M' .mmmm  MM M  mmmm.  M╠╣
-- ╠╣MM.    .MM d888888b    M         `M M         `M M.      `YM M         `M M  MMMMM  M╠╣
-- ╠╣M  .mm.  M    .d8P'    M  MMMMM  MM M  MMMMM  MM MMMMMMM.  M M  MMMMM  MM M  MMMMM  M╠╣
-- ╠╣M  MMMM  M  .Y8P       M  MMMMM  MM M  MMMMM  MM M. .MMM'  M M  MMMMM  MM M  MMMMM  M╠╣
-- ╠╣M  MMMM  M d888888P    M  MMMMM  MM M  MMMMM  MM Mb.     .dM M  MMMMM  MM M  MMMMM  M╠╣
-- ╠╣MMMMMMMMMM             MMMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMM╠╣
-- ╠╬╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╬╣
-- ╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝
                                                                                                                                                                                                                                                                                        '''
banner2='''                                                                                                  
<!-- ██████████████████████████████████████████████████████████████████ -->
<!-- █▌db    db d88888D      db   db  .d8b.  .d8888.  .d8b.  d8b   db▐█ -->
<!-- █▌`8b  d8' YP  d8'      88   88 d8' `8b 88'  YP d8' `8b 888o  88▐█ -->
<!-- █▌ `8bd8'     d8'       88ooo88 88ooo88 `8bo.   88ooo88 88V8o 88▐█ -->
<!-- █▌ .dPYb.    d8'        88~~~88 88~~~88   `Y8b. 88~~~88 88 V8o88▐█ -->
<!-- █▌.8P  Y8.  d8' db      88   88 88   88 db   8D 88   88 88  V888▐█ -->
<!-- █▌YP    YP d88888P      YP   YP YP   YP `8888Y' YP   YP VP   V8P▐█ -->
<!-- ██████████████████████████████████████████████████████████████████ -->                            '''

os.system('clear')
print(banner1)
#start program
print("1)update termux")
print("2)exit")
user = int(input("==>"))
if user == 1:
    print(banner2)
    os.system('pkg update -y')
    os.system('pkg upgrade -y')
    os.system('pkg install python -y')
    os.system('pkg install python-pip -y')
    os.system('pkg install wget -y')
    os.system('pkg install fish -y')
    os.system('pkg install git -y')
    os.system('pkg install nmap -y')
    os.system('pkg install bash -y')
    os.system('pkg install nano -y')
    os.system('pkg install figlet -y')
    os.system('pkg install tor -y')
    os.system('pkg install openssl -y')
    os.system('pkg install openssl-tool -y')
    os.system('pkg install toilet -y')
    os.system('pkg install net-tools -y')
    os.system('pkg install goaccess -y')
    os.system('pkg install golang -y')
    os.system('pkg install tar -y')
    os.system('pip install requests ')
    os.system('pip install termcolor')
elif user==2:
    os.system('exit')
    print('exit the program.........')
print("Thanks for using thi's tools")
  
