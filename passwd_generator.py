import tkinter as tk
from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk, Image

def clean_exit():
    base.destroy()
  
#Changement de fenêtre avec le boutton
def alternate_window(is_in_base, is_in_window, window):
    def alternate_processing():
        if is_in_base and not is_in_window:
            base.withdraw()
            window.withdraw()
            window.deiconify()
        else:
            window.withdraw()
            base.deiconify()
    return alternate_processing

#Créer les 2 fenêtres :
def create_window(window, text_label):
    label = tk.Label(window, text=text_label)
    button = tk.Button(window, text="Revenir à l'accueil", command=alternate_window(False, True, window))
    window.protocol("WM_DELETE_WINDOW", clean_exit)


#Page d'accueil : 
base = tk.Tk()
generator = tk.Toplevel(base)
img = ImageTk.PhotoImage(Image.open("psswd.png"))
background_image = ImageTk.PhotoImage(Image.open("ZTMCORP.png"))
background_label = Label(base, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
base.geometry("1920x1080")
base.title('Password Manager x Generator')  
base['bg'] = '#245690'
boutton1 = tk.Button(base, image=img,command=alternate_window(True, False, generator), text="affiche le generator").pack(pady = 300)



#Script Generateur Password : 
from colorama import Fore, Back, Style
from random import shuffle 

#Liste de Caractères : 
global caractere_a, caracter_A, caractere_1, speciaux, choix
caractere_a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
caractere_A = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
caractere_1 = [0,1,2,3,4,5,6,7,8,9]
speciaux = ['@','%','&','#','+','-','_','*','/','$','¤','£','µ','§','|','!','.','?',',']



  
 
#Page generateur : 
create_window(generator, "Password Generator")
generator.geometry("1920x1080")
generator['bg'] = 'black'
#Boutton Password : 
shuffle(caractere_1)
shuffle(caractere_a)
shuffle(caractere_A)
shuffle(speciaux)
def psswd_1() :
    password = "{}{}{}{}{}{}{}{}".format(caractere_1[0],caractere_1[1],caractere_1[2],caractere_1[3],caractere_1[4],caractere_1[5],caractere_1[6],caractere_1[7],caractere_1[8])
    tk.messagebox.showinfo("ZTM Corp", "Password numérique copié") 
    generator.clipboard_clear()
    generator.clipboard_append(password)
    print(password)
def psswd_2() :
    password = "{}{}{}{}{}{}{}{}".format(caractere_a[0],caractere_A[1],caractere_1[2],caractere_a[3],caractere_A[4],caractere_a[5],caractere_1[6],caractere_1[7],caractere_1[8])
    tk.messagebox.showinfo("ZTM Corp", "Password alphanumérique copié") 
    generator.clipboard_clear()
    generator.clipboard_append(password)  
def psswd_3() : 
    password = "{}{}{}{}{}{}{}{}".format(speciaux[0],caractere_1[1],speciaux[2],caractere_A[3],caractere_a[4],caractere_1[5],speciaux[6],caractere_A[7],caractere_a[8])
    tk.messagebox.showinfo("ZTM Corp", "Password complexe copié") 
    generator.clipboard_clear()
    generator.clipboard_append(password)
password1img = ImageTk.PhotoImage(Image.open("numeric.png"))
password2img = ImageTk.PhotoImage(Image.open("alphanumeric.png"))
password3img = ImageTk.PhotoImage(Image.open("strong.png"))
presentation = ImageTk.PhotoImage(Image.open("rules.png"))
label = tk.Label(generator, image=presentation).pack(pady = 10)
Boutton1 = tk.Button(generator, image = password1img,command = psswd_1).place(x = 50, y = 500)
Boutton2 = tk.Button(generator, image = password2img, command = psswd_2).place(x = 750, y = 500)
Boutton3 = tk.Button(generator, image = password3img, command= psswd_3).place(x = 1400, y = 500)
generator.withdraw()


base.mainloop()









