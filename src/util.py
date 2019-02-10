# encoding=utf8
import subprocess
# Set of colors in order to check status in the terminal
reset = '\x1b[0m'    # reset all colors to white on black
bold = '\x1b[1m'     # enable bold text
uline = '\x1b[4m'    # enable underlined text
nobold = '\x1b[22m'  # disable bold text
nouline = '\x1b[24m'  # disable underlined text
red = '\x1b[31m'     # red text
green = '\x1b[32m'   # green text
blue = '\x1b[34m'    # blue text
cyan = '\x1b[36m'    # cyan text
white = '\x1b[37m'   # white text (use reset unless it's only temporary)
yellow = '\x1b[33m'
# Nomenclaturas :
# err : Mensaje que genera algun tipo de error
# ok : Mensaje que genera una operacion correcta
# warning : Mensaje que genera una operacion de atencion
# info : Mensaje que presenta una operacion de informacion
# atn : Mensaje puesto para establecer ingreso e datos
err = '{}{}[✘✘✘]{} '.format(bold, red, reset)
ok = '{}{}[✓]{} '.format(bold, green, reset)
warning = '{}{}[~]{} '.format(bold, yellow, reset)
info = '{}{}[+]{} '.format(bold, cyan, reset)
atn = '{}{}[>>]{} '.format(bold, yellow, reset)


version__ = '{}0.1v{}'.format(cyan, reset)
authors = '{}Coded by Héctor F. Jimenez S,Catalina Castro, Juan Jose Jimenez{}'\
            .format(red, reset)
emails = '{}hfjimenez@utp.edu.co{}'.format(white, reset)
topic = '{}{}\n\tDistributed Systems 2018-2{}'.format(
    uline, white, reset)

def cleanscreen():
    subprocess.call(['clear'], shell=False)


def banners():
    print("""
        {}        
             _________                                
            /   _____/ ______________  __ ___________ 
            \_____  \_/ __ \_  __ \  \/ // __ \_  __ \\
            /        \  ___/|  | \/\   /\  ___/|  | \/
            /_______  /\___  >__|    \_/  \___  >__|   
                    \/     \/                 \/       
            {}{}Final Project Distributed Systems
            UTP-2018-2, 2019{}                            
            """.format(cyan, white, bold, reset))


def bannerc():
    print("""{}        
              _____ _ _            _   
             / ____| (_)          | |  
            | |    | |_  ___ _ __ | |_ 
            | |    | | |/ _ \ '_ \| __|
            | |____| | |  __/ | | | |_ 
             \_____|_|_|\___|_| |_|\__|
            {}{}Final Project Distributed Systems
            UTP-2018-2, 2019 {}                            
        """.format(cyan, white, bold, reset))