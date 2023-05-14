from rich.console import Console
import hn_encryption as decenc
from pick import pick
import tkinter as tk
from tkinter import filedialog
import os
from time import sleep as wait
from random import randint

root = tk.Tk()
root.withdraw()
con = Console()


name = r"""
 ________  _______   ________ _________  ________  ________  ___       ________      
|\   ___ \|\  ___ \ |\   ____\\___   ___\\   __  \|\   __  \|\  \     |\   ____\     
\ \  \_|\ \ \   __/|\ \  \___\|___ \  \_\ \  \|\  \ \  \|\  \ \  \    \ \  \___|_    
 \ \  \ \\ \ \  \_|/_\ \  \       \ \  \ \ \  \\\  \ \  \\\  \ \  \    \ \_____  \   
  \ \  \_\\ \ \  \_|\ \ \  \____   \ \  \ \ \  \\\  \ \  \\\  \ \  \____\|____|\  \  
   \ \_______\ \_______\ \_______\  \ \__\ \ \_______\ \_______\ \_______\____\_\  \ 
    \|_______|\|_______|\|_______|   \|__|  \|_______|\|_______|\|_______|\_________\
                                      encrypting your files since XXXX!   \|_________|
                                                                          by some_one
                                                      decenc module by algmur (github)                     
                                                                                     
"""

print(name)
wait(2)
option,index = pick(['Encypher', "Decypher", "DECHead", "Decypher-BRUTE"], title="Welcome to DECTools! Choose an option.")
if option == "Encypher":
    con.print('Encypher Initialised', style="green")
    #     encfile = filedialog.askopenfilename()
    con.print('Asking user about encryption', style="white")
    option,index = pick(['File'], title="What exactly do you want to encrypt? (YOU GOT NO CHOICE HAHAHAHAHA)")
    if option == "File":
        con.print('Dropping out Open dialog...', style="green")
        encfile = filedialog.askopenfilename()
        print('Hamlet is a hamster...')
        wait(.1)
        print('Cutting onions...')
        wait(.1)
        print('Reading files...')
        FileAFile = os.path.join(encfile)
        target = open(FileAFile)
        dataToEnc = target.read()
        con.print('File has been read.')
        password = str(input('Enter password to encrypted file (leave it empty to make it without any password):'))
        comment = str(input('Enter comment to encrypted file header (leave it empty to make it without any comments):'))
        sign = str(input('Enter signature to encrypted file header (leave it empty to make it without any signatures):'))
        Encrupted = None
        cipher = decenc.encrypt_with_pass(comment, sign, dataToEnc,
                                      dataToEnc, password)
        outfile = f"{randint(133,999)}-{os.path.basename(target.name)}-ENC_OUT.dec"
        with open(outfile, 'a+') as f:
            f.write(cipher)
        print('ENTIRE ENCRYPTED MESSAGE IF FILE DECIDES TO BREAK')
        print('-------------------------------------------------')
        print(cipher)
        print('-------------------------------------------------')
        print('COMPLETE - SAVED OUT.dec')
        target.close()
        con.print(f'Successful Encryption complete. File saved as {outfile}. Shutting down in 15 seconds', style="green")
        wait(15)
        exit()
elif option == "Decypher":
    con.print('DECYPHER INITIALISED -- PLEASE CHOOSE FILE')
    con.print('Dropping out Open dialog...', style="green")
    decfile = filedialog.askopenfilename()
    FileAFile = os.path.join(decfile)
    target = None
    try:
        target = open(FileAFile)
    except FileNotFoundError:
        con.print('ERORR: FILE NOT FOUND', style='red')
        con.print('SHUTTING DOWN IMMEDIATELY')
        exit()
    dataToDec = target.read()
    con.print('File has been read. Starting decrypting...')
    password = str(input('Enter password to encrypted file (if there is any)>'))
    a, Decypher = decenc.decrypt_with_pass(dataToDec, password, nlayers=1, verbose=False)
    print('Encryption is successful. Dumping file...')
    outfile = f"{randint(133,999)}-{os.path.basename(target.name)}-ENC_OUT.txt"
    with open(outfile, 'a+') as f:
        f.write(Decypher)
    print(Decypher)
    con.print(f'Successful Decryption complete. Decrypted file dropped as {outfile}. Shutting down in 15 seconds', style="green")
    print('HEADERS')
    print('-------------------------------------------------')
    decenc.decrypt_header_only(dataToDec)
    print('-------------------------------------------------')
    wait(15)
    exit()
elif option == "DECHead":
    con.print('HEADERS_READ INITIALISED -- PLEASE CHOOSE FILE')
    con.print('Dropping out Open dialog...', style="green")
    decfile = filedialog.askopenfilename()
    FileAFile = os.path.join(decfile)
    target = None
    try:
        target = open(FileAFile)
    except FileNotFoundError:
        con.print('ERORR: FILE NOT FOUND', style='red')
        con.print('SHUTTING DOWN IMMEDIATELY')
        exit()
    ENCData = target.read()
    con.print('File has been read. Starting checking headers...')
    decenc.decrypt_header_only(ENCData)
    con.print('\n\nSuccessful Headers Check complete. Shutting down in 15 seconds', style="green")
    wait(15)
    exit()
elif option == "Decypher-BRUTE":
    con.print('SYSTEM INVADI G DET C E  -- DISAB 011 01 01')
    wait(0.5)
    con.print('[red]The DECTools Jailbreak[/red] - DECYPHER BRUTE')
    con.print('D 0110 p ing out O01101en di log...', style="green")
    decfile = filedialog.askopenfilename()
    FileAFile = os.path.join(decfile)
    target = None
    try:
        target = open(FileAFile)
    except FileNotFoundError:
        con.print('ERORR: FILE NOT FOUND', style='red')
        con.print('SHUTTING DOWN IMMEDIATELY')
        exit()
    ENCData = target.read()
    con.print('File has been read. Starting dec ph ring [red]BRUTEFORCING[/red]...')
    dec, plain = decenc.decrypt_brute(ENCData)
    outfile = f"{randint(133,999)}-{os.path.basename(target.name)}-ENC_OUT.txt"
    with open(outfile, 'a+') as f:
        f.write(plain)
    con.print('\n\nE R RO R ) # # (% #$ #$ $$ % % *@# # $*$', style="green")
    print('H A  RS')
    print('-------------------------------------------------')
    decenc.decrypt_header_only(ENCData)
    print('-------------------------------------------------')
    con.print(f'Emergency memory reset will now commence. Bruteforce complete. File saved in your DECTools folder as {outfile}. Jailbreak shutting down in 15 seconds with DECTools.', style="red")
    wait(15)
    exit()