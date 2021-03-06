def print_logo():
    """
    Prints a logo of M3RG.

    """
    print( '\033[1m'+'\033[95m'+
          '*---------------------------------------------------------------*\n'+
'\t'+     '    .--------.        '+'\033[91m'  +' __    __ '+  '\033[92m'  +' ______ '+    '\033[94m'   +' _____  '+    '\033[95m'  +' ______  \n'+
'\t'+     '    |\       |\       '+'\033[91m'  +'|  \  /  |'+  '\033[92m'  +'|____  |'+    '\033[94m'   +'|  _  | '+    '\033[95m'  +'|  ____| \n'+
'\t'+     '    | \______|_\      '+'\033[91m'  +'|   \/   |'+  '\033[92m'  +'   __| |'+    '\033[94m'   +'| |_| | '+    '\033[95m'  +'| |  __  \n'+
'\t'+     '--->|  |     |  |<--- '+'\033[91m'  +'| |\  /| |'+  '\033[92m'  +'  |__  |'+    '\033[94m'   +'|    /  '+    '\033[95m'  +'| | |. | \n'+
'\t'+     '    |__|_____|  |     '+'\033[91m'  +'| | \/ | |'+  '\033[92m'  +' ____| |'+    '\033[94m'   +'| |\ \  '+    '\033[95m'  +'| |__| | \n'+
'\t'+     '     \ |      \ |     '+'\033[91m'  +'|_|    |_|'+  '\033[92m'  +'|______|'+    '\033[94m'   +'|_| \_\ '+    '\033[95m'  +'|______| \n'+
'\t'+     '      \|_______\|     '+'\033[0m'   +'Credits: Ravinder Bhattoo\n'+'\033[95m'+
          '*---------------------------------------------------------------*'+
           '\033[0m'
        )

if __name__ == "__main__":
    print_logo()
