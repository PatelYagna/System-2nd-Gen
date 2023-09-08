#All Imports
from tkinter import *
import os
import random 
from statistics import variance as v, mean as m, median as med, median_high as med_h, median_low as med_l, mode as mo, harmonic_mean as hm

#Function starts off the whole Program. It lets one select to whether Login or Sign Up.
def main_screen():
    global screen
    screen = Tk()
    screen.geometry('300x300')
    screen.title('Operating')
    #Label(text = 'Fire', bg = 'grey', width = '300', height = '2', font = ('Calibri', 13)).pack()
    Label(text = '').pack()
    Button(text = 'Login', height = '2', width = '30', command = login).pack()
    Label(text = '').pack()
    Button(text = 'Sign up', height = '2', width = '30', command = sign_up).pack() 
    screen.mainloop()

#Function is executed when one clicks Login. It asks one for Username and Password
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title('Login')
    screen2.geometry('300x350')

    Label(screen2, text = 'Enter details below').pack()
    Label(screen2, text = '').pack()

    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1
    Label(screen2, text = 'Username * ').pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = '').pack()
    Label(screen2, text = 'Password * ').pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label (screen2, text = '').pack()
    Button(screen2, text = 'Login', width = 10, height = 1, command = login_verify).pack()

#Function is executed when one has entered Username and Password. It opens the file to check If one's Username and Password are authorized.
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open (username1, 'r')
        verify = file1.read().splitlines()
        if password1 in verify:
            session()
            destory_login()
        else:
            incorrect_password()
    else:
        user_not_found()

#Function is executed when one has logged in successfully.
def session():
    global screen8
    screen8 = Toplevel(screen)
    screen8.title('Dashboard')
    screen8.geometry('400x400')

    Label (screen8, text = 'Welcome to the Dashboard').pack()
    Button(screen8, text = 'Create a Note', command = create_note).pack()
    Button(screen8, text = 'View Notes', command = view_notes).pack()
    Button(screen8, text = 'Delete Notes', command = delete_note).pack()
    Button(screen8, text = 'Random', command = randomizer).pack()
    Button(screen8, text = 'Guessing Game', command = guessrange).pack()
    Button(screen8, text = 'Flip a Coin', command = flip).pack()
    Button(screen8, text = 'Calculator', command = calculator).pack()
    Button(screen8, text = 'Statistics', command = statistics).pack()

#Function is executed when one creates a file.
def create_note():
    global raw_filename
    raw_filename = StringVar()
    global raw_notes
    raw_notes = StringVar()
    global screen9
    screen9 = Toplevel(screen)
    screen9.title('Information')
    screen9.geometry('300x250')
    Label(screen9, text = 'Please enter a file name Below: ').pack()
    Entry(screen9, textvariable = raw_filename).pack()
    Label(screen9, text = 'Please enter the notes for the file: ').pack()
    Entry(screen9, textvariable = raw_notes).pack()
    Button(screen9, text = 'Save', command  = save).pack()

#Function is executed when one saves a the file tht was created.
def save():
    file_name = raw_filename.get()
    notes = raw_notes.get()

    data = open(file_name, 'w')
    data.write(notes)
    data.close()
    saved()

#Function is executed when one's file is saved successfully.
def saved():
    Label(screen9, text = 'Saved!').pack()

#Function is executed when one enters the file name to view the file.
def view_notes():
    screen11 = Toplevel(screen)
    screen11.title("Information")
    screen11.geometry('250x250')
    all_files = os.listdir()

    Label(screen11, text = 'Please use one of the file names below').pack
    Label(screen11, text = 'all_files').pack
    global raw_filename1
    raw_filename1 = StringVar()
    Entry(screen11, textvariable = raw_filename1).pack()
    Button(screen11, command = view_notes1, text = 'Veiw').pack()

#Function is executed when one's file is being views.
def view_notes1():
    filename1 = raw_filename1.get()
    data = open(filename1, 'r')
    data1 = data.read()
    data.close

    screen12 = Toplevel(screen)
    screen12.title('Notes')
    screen12.geometry('400x400')
    Label(screen12, text = data1).pack()

#Function is executed when one click to delete a file.
def delete_note():
    screen13 = Toplevel(screen)
    screen13.title("Information")
    screen13.geometry('250x250')
    all_files = os.listdir()

    Label(screen13, text = 'Please use one of the file names below').pack
    Label(screen13, text = 'all_files').pack
    global raw_filename2
    raw_filename2 = StringVar()
    Entry(screen13, textvariable = raw_filename2).pack()
    Button(screen13, command = delete_note1, text = 'Delete').pack()

#Function is executed when one's file has been deleted successfully
def delete_note1():
    filename3 = raw_filename2.get()
    os.remove(filename3)

    screen14 = Toplevel(screen)
    screen14.title('Notes')
    screen14.geometry('400x400')
    Label(screen14, text = filename3 + ' has been deleted').pack()

#Function is executed when one clicks to get a random number out of 1 to 100
def randomizer():
    global screen16
    screen16 = Toplevel(screen)
    screen16.title('Random Number')
    screen16.geometry('200x200')
    
    Label(screen16, text = "Random Number").pack()
    randomnum = random.randint(1, 100)
    Label(screen16, text = randomnum, fg = '#0ca4eb', font = ('calibri', 15)).pack()

#Function is executed when clicks Guessing Game
def guessrange():
    global screen17
    screen17 = Toplevel(screen)
    screen17.title('Range of Guesses')
    screen17.geometry('200x250')
    Label(screen17, text = 'First number in range').pack()
    global num1
    num1 = Entry(screen17)
    num1.pack()
    Label(screen17, text = 'Second number in range').pack()
    global num2
    num2 = Entry(screen17)
    num2.pack()
    Button(screen17, text = 'Go', command = guessinggame).pack()

#Function is executed when click Go
def guessinggame():
    global screen18
    screen18 = Toplevel(screen)
    screen18.title('Guessing Game')
    screen18.geometry('300x250')
    global num
    num = int(num1.get())
    global nume
    nume = int(num2.get())
    global secret
    secret = random.randint(num, nume)
    global guess1
    guess1 = Entry(screen18)
    guess1.pack()
    Button(screen18, text = 'Reset', command = reset).pack()
    Button(screen18, text = 'Guess', command = guesscheck).pack()

#Function is executed when one clicks Guess
def guesscheck():
    guess = int(guess1.get())
    guess1.delete(0, END)
    if guess == secret:
        Label(screen18, text = 'You Win!', fg = '#1fdb80', font = ('calibri', 15)).pack()
    elif guess < secret:
        Label(screen18, text = 'Your guess is too low', fg = 'red', font = ('calibri', 15)).pack()
    elif guess > secret:
        Label(screen18, text = 'Your guess is too high', fg = 'red', font = ('calibri', 15)).pack()
    else:
        Label(screen18, text = 'Invalid', fg = 'red', font = ('calibri', 15)).pack()

#Function is executed when one clicks Reset
def reset():
    global secret
    secret = random.randint(num, nume)

#Function is executed when one clicks to Flip a Coin
def flip():
    global screen19
    screen19 = Toplevel(screen)
    screen19.title("Flip a Coin")
    screen19.geometry('300x300')
    Button(screen19, text = 'Flip', command = coin).pack()

#Function is executed when one clicks Flip
def coin():
    global coinside
    sides = ['Heads', 'Tales']
    coinside = random.choice(sides)
    if coinside == 'Heads':
        Label(screen19, text = 'Heads').pack()
    else:
        Label(screen19, text = 'Tales').pack()

#Function is executed when one clicks Calculator
def calculator():
    global screen20
    screen20 = Toplevel(screen)
    screen.title("Calculator")
    screen.geometry('330x370')

    Label(screen20, text = 'Enter 1st number').pack()
    global firstnum
    firstnum = Entry(screen20)
    firstnum.pack()
    Label(screen20, text = 'Enter second number').pack()
    global secondnum
    secondnum = Entry(screen20)
    secondnum.pack()
    Button(screen20, text = 'Addition', command = addition).pack()
    Button(screen20, text = 'Subtraction', command = substraction).pack()
    Button(screen20, text = 'Multiplication', command = multiplication).pack()
    Button(screen20, text = 'Division', command = divison).pack()
    Button(screen20, text = 'Power', command = powering).pack()

#Function is executed when one clicks Addition.
def addition():
    fn = int(firstnum.get())
    sn = int(secondnum.get())
    firstnum.delete(0, END)
    secondnum.delete(0, END)
    added = fn + sn
    Label(screen20, text = added, fg = 'red', font = ('calibri', 15)).pack()

#Function is executed when one clicks Substraction.
def substraction():
    fn = int(firstnum.get())
    sn = int(secondnum.get())
    firstnum.delete(0, END)
    secondnum.delete(0, END)
    subtracted = fn - sn
    Label(screen20, text = subtracted, fg = 'red', font = ('calibri', 15)).pack()

#Function is executed when one clicks Mltiplication.
def multiplication():
    fn = int(firstnum.get())
    sn = int(secondnum.get())
    firstnum.delete(0, END)
    secondnum.delete(0, END)
    multiplied = fn * sn
    Label(screen20, text = multiplied, fg = 'red', font = ('calibri', 15)).pack()

#Function is executed when one clicks Divison.
def divison():
    fn = int(firstnum.get())
    sn = int(secondnum.get())
    firstnum.delete(0, END)
    secondnum.delete(0, END)
    divided = fn / sn
    Label(screen20, text = divided, fg = 'red', font = ('calibri', 15)).pack()

#Function is executed when one clicks Power.
def powering():
    fn = int(firstnum.get())
    sn = int(secondnum.get())
    firstnum.delete(0, END)
    secondnum.delete(0, END)
    powered = fn ** sn
    Label(screen20, text = powered, fg = 'red', font = ('calibri', 15)).pack()

#Function is executed when one clicks Statistics.
def statistics():
    global screen21
    screen21 = Toplevel(screen)
    screen21.title('Statistics Calculator')
    screen21.geometry('320x400')
    global statlist
    statlist = []
    global rnumber_entry
    rnumber_entry = Entry(screen21)
    rnumber_entry.pack()
    Button(screen21, text = 'OK', command = listing).pack()
    Button(screen21, text = 'Clear', command = clear).pack()
    Button(screen21, text = 'Variance', command = variance).pack()
    Button(screen21, text = 'Mean', command = mean).pack()
    Button(screen21, text = 'Median', command = median).pack()
    Button(screen21, text = 'Meadian High', command = median_high).pack()
    Button(screen21, text = 'Meadian Low', command = median_low).pack()
    Button(screen21, text = 'Mode', command = mode).pack()
    Button(screen21, text = 'Harmonic Mean', command = harmonic_mean).pack()

#Function is executed when one clicks OK.
def listing():
    sn = int(rnumber_entry.get())
    statlist.append(sn)
    rnumber_entry.delete(0, END)

#Function is executed when one clicks Clear.
def clear():
    del statlist [:]

#Function is executed when one clicks Variance.
def variance():
    sa = v(statlist)
    Label(screen21, text = sa).pack()

#Function is executed when one clicks Mean.
def mean():
    sa = m(statlist)
    Label(screen21, text = sa).pack()

#Function is executed when one clicks Median.
def median():
    sa = med(statlist)
    Label(screen21, text = sa).pack()

#Function is executed when one clicks Median High.
def median_high():
    sa = med_h(statlist)
    Label(screen21, text = sa).pack()

#Function is executed when one clicks Median Low.
def median_low():
    sa = med_l(statlist)
    Label(screen21, text = sa).pack()

#Function is executed when one clicks Mode.
def mode():
    sa = mo(statlist)
    Label(screen21, text = sa).pack()

#Function is executed when one clicks Harmonic Mean.
def harmonic_mean():
    sa = hm(statlist)
    Label(screen21, text = sa).pack()


#Function is executed when one's Username is not authorized.
def user_not_found():
    Label(screen2, text = 'User not recognized', fg = 'red', font = ('calibri', 13)).pack()

#Function is executed when one's Password is incorrect.
def incorrect_password():
    Label(screen2, text = 'Incorrect Password', fg = 'red', font = ('calibri', 13)).pack()

#Function is executed when one clicks Sign Up. It asks one for Username and Password.
def sign_up():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title('Sign Up')
    screen1.geometry('350x450')

    global username
    global password
    global agee
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = 'Enter details below').pack()
    Label(screen1, text = '').pack()
    Label(screen1, text = 'Age * ').pack()
    agee = Entry(screen1)
    agee.pack()
    Button(screen1, text = 'Ok', command = age_verification).pack()
    Label(screen1, text = '').pack()
    Label(screen1, text = 'Username * ').pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = 'Password * ').pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = '').pack()
    Button(screen1, text = 'Sign up', width = 10, height = 1, command = sign_up_user).pack()

#Function is executed when one enters Username and Password in Sign Up. This function stores Username and Password in a file.
def sign_up_user():
    username_info = username.get()
    password_info = password.get()

    fileq = open(username_info, 'w')
    fileq.write('' + username_info + '\n')
    fileq.write('' + password_info)
    fileq.close

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label (screen1, text = 'Sign up successful', fg = 'green', font = ('calibri', 11)).pack()

#Function is executed when age is entered.
def age_verification():
    global age
    age = int(agee.get())
    agee.delete(0, END)
    if age < 15:
        destroy_sign_up()
    else:
        Label(screen1, text = 'Eligible', fg = 'green').pack()

#Function is executed when age is not Eligible.
def destroy_sign_up():
    screen1.destroy()

#Function is executed when one is logged in.
def destory_login():
    screen2.destroy()

#Begins the programs
main_screen()
