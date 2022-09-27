from tkinter import *
import tkinter.font as font
import math

#  ---------------------------------------------------------------------------

window = Tk()
window.configure(bg='#000033')


secondary_number = ""
final_number = ""
enter_string = StringVar()
opperator_holder = ""
sum = 0
previous_sum = 0
background_color = "#b3b3ff"
button_color = "#8080ff"
history_background_color = "#000033"
count = 0
history_array = []


def colors_button():
    global count
    global square_root_button
    global background_color
    global button_color
    global history_background_color
    # Change to Purple
    if count == 0:
        background_color = "#d699ff"
        button_color = "#c266ff"
        history_background_color = "#1f0033"
        zero_button.config(bg=button_color)
        one_button.config(bg=button_color)
        two_button.config(bg=button_color)
        three_button.config(bg=button_color)
        four_button.config(bg=button_color)
        five_button.config(bg=button_color)
        six_button.config(bg=button_color)
        seven_button.config(bg=button_color)
        eight_button.config(bg=button_color)
        nine_button.config(bg=button_color)
        decimal_button.config(bg=button_color)
        equal_button.config(bg=button_color)
        add_button.config(bg=button_color)
        sub_button.config(bg=button_color)
        mult_button.config(bg=button_color)
        div_button.config(bg=button_color)
        del_button.config(bg=button_color)
        negative_button.config(bg=button_color)
        squared_button.config(bg=button_color)
        square_root_button.config(bg=button_color)
        color_button.config(bg=button_color)
        basic_clear_button.config(bg=button_color)
        full_clear_button.config(bg=button_color)
        previous_input.config(bg=background_color)
        current_input.config(bg=background_color)
        history.config(bg=history_background_color)
        history_label.config(bg=history_background_color)
        count += 1

    #  Change To pink
    elif count == 1:
        background_color = "#ecb3ff"
        button_color = "#ffccff"
        history_background_color ="#330022"
        zero_button.config(bg=button_color)
        one_button.config(bg=button_color)
        two_button.config(bg=button_color)
        three_button.config(bg=button_color)
        four_button.config(bg=button_color)
        five_button.config(bg=button_color)
        six_button.config(bg=button_color)
        seven_button.config(bg=button_color)
        eight_button.config(bg=button_color)
        nine_button.config(bg=button_color)
        decimal_button.config(bg=button_color)
        equal_button.config(bg=button_color)
        add_button.config(bg=button_color)
        sub_button.config(bg=button_color)
        mult_button.config(bg=button_color)
        div_button.config(bg=button_color)
        del_button.config(bg=button_color)
        negative_button.config(bg=button_color)
        squared_button.config(bg=button_color)
        square_root_button.config(bg=button_color)
        color_button.config(bg=button_color)
        basic_clear_button.config(bg=button_color)
        full_clear_button.config(bg=button_color)
        previous_input.config(bg=background_color)
        current_input.config(bg=background_color)
        history.config(bg=history_background_color)
        history_label.config(bg=history_background_color)
        count += 1

    #  Change to red
    elif count == 2:
        background_color = "#ffcccc"
        button_color = "#c91d1d"
        history_background_color="#330000"
        zero_button.config(bg=button_color)
        one_button.config(bg=button_color)
        two_button.config(bg=button_color)
        three_button.config(bg=button_color)
        four_button.config(bg=button_color)
        five_button.config(bg=button_color)
        six_button.config(bg=button_color)
        seven_button.config(bg=button_color)
        eight_button.config(bg=button_color)
        nine_button.config(bg=button_color)
        decimal_button.config(bg=button_color)
        equal_button.config(bg=button_color)
        add_button.config(bg=button_color)
        sub_button.config(bg=button_color)
        mult_button.config(bg=button_color)
        div_button.config(bg=button_color)
        del_button.config(bg=button_color)
        negative_button.config(bg=button_color)
        squared_button.config(bg=button_color)
        square_root_button.config(bg=button_color)
        color_button.config(bg=button_color)
        basic_clear_button.config(bg=button_color)
        full_clear_button.config(bg=button_color)
        previous_input.config(bg=background_color)
        current_input.config(bg=background_color)
        history.config(bg=history_background_color)
        history_label.config(bg=history_background_color)
        count += 1

    #  change to orange
    elif count == 3:
        background_color = "#ffcc99"
        button_color = "#ff9933"
        history_background_color="#331a00"
        zero_button.config(bg=button_color)
        one_button.config(bg=button_color)
        two_button.config(bg=button_color)
        three_button.config(bg=button_color)
        four_button.config(bg=button_color)
        five_button.config(bg=button_color)
        six_button.config(bg=button_color)
        seven_button.config(bg=button_color)
        eight_button.config(bg=button_color)
        nine_button.config(bg=button_color)
        decimal_button.config(bg=button_color)
        equal_button.config(bg=button_color)
        add_button.config(bg=button_color)
        sub_button.config(bg=button_color)
        mult_button.config(bg=button_color)
        div_button.config(bg=button_color)
        del_button.config(bg=button_color)
        negative_button.config(bg=button_color)
        squared_button.config(bg=button_color)
        square_root_button.config(bg=button_color)
        color_button.config(bg=button_color)
        basic_clear_button.config(bg=button_color)
        full_clear_button.config(bg=button_color)
        previous_input.config(bg=background_color)
        current_input.config(bg=background_color)
        history.config(bg=history_background_color)
        history_label.config(bg=history_background_color)
        count += 1

    elif count == 4:
        background_color = "#ffff99"
        button_color = "#ffff66"
        history_background_color="#333300"
        zero_button.config(bg=button_color)
        one_button.config(bg=button_color)
        two_button.config(bg=button_color)
        three_button.config(bg=button_color)
        four_button.config(bg=button_color)
        five_button.config(bg=button_color)
        six_button.config(bg=button_color)
        seven_button.config(bg=button_color)
        eight_button.config(bg=button_color)
        nine_button.config(bg=button_color)
        decimal_button.config(bg=button_color)
        equal_button.config(bg=button_color)
        add_button.config(bg=button_color)
        sub_button.config(bg=button_color)
        mult_button.config(bg=button_color)
        div_button.config(bg=button_color)
        del_button.config(bg=button_color)
        negative_button.config(bg=button_color)
        squared_button.config(bg=button_color)
        square_root_button.config(bg=button_color)
        color_button.config(bg=button_color)
        basic_clear_button.config(bg=button_color)
        full_clear_button.config(bg=button_color)
        previous_input.config(bg=background_color)
        current_input.config(bg=background_color)
        history.config(bg=history_background_color)
        history_label.config(bg=history_background_color)
        count += 1

    elif count == 5:
        background_color = "#c6ffb3"
        button_color = "#8cff66"
        history_background_color="#0d3300"
        zero_button.config(bg=button_color)
        one_button.config(bg=button_color)
        two_button.config(bg=button_color)
        three_button.config(bg=button_color)
        four_button.config(bg=button_color)
        five_button.config(bg=button_color)
        six_button.config(bg=button_color)
        seven_button.config(bg=button_color)
        eight_button.config(bg=button_color)
        nine_button.config(bg=button_color)
        decimal_button.config(bg=button_color)
        equal_button.config(bg=button_color)
        add_button.config(bg=button_color)
        sub_button.config(bg=button_color)
        mult_button.config(bg=button_color)
        div_button.config(bg=button_color)
        del_button.config(bg=button_color)
        negative_button.config(bg=button_color)
        squared_button.config(bg=button_color)
        square_root_button.config(bg=button_color)
        color_button.config(bg=button_color)
        basic_clear_button.config(bg=button_color)
        full_clear_button.config(bg=button_color)
        previous_input.config(bg=background_color)
        current_input.config(bg=background_color)
        history.config(bg=history_background_color)
        history_label.config(bg=history_background_color)
        count += 1

    elif count == 6:
        background_color = "#ccfff2"
        button_color = "#66ffd9"
        history_background_color="#003326"
        zero_button.config(bg=button_color)
        one_button.config(bg=button_color)
        two_button.config(bg=button_color)
        three_button.config(bg=button_color)
        four_button.config(bg=button_color)
        five_button.config(bg=button_color)
        six_button.config(bg=button_color)
        seven_button.config(bg=button_color)
        eight_button.config(bg=button_color)
        nine_button.config(bg=button_color)
        decimal_button.config(bg=button_color)
        equal_button.config(bg=button_color)
        add_button.config(bg=button_color)
        sub_button.config(bg=button_color)
        mult_button.config(bg=button_color)
        div_button.config(bg=button_color)
        del_button.config(bg=button_color)
        negative_button.config(bg=button_color)
        squared_button.config(bg=button_color)
        square_root_button.config(bg=button_color)
        color_button.config(bg=button_color)
        basic_clear_button.config(bg=button_color)
        full_clear_button.config(bg=button_color)
        previous_input.config(bg=background_color)
        current_input.config(bg=background_color)
        history.config(bg=history_background_color)
        history_label.config(bg=history_background_color)
        count += 1

    elif count == 7:
        background_color = "#b3b3ff"
        button_color = "#8080ff"
        history_background_color = "#000033"
        zero_button.config(bg=button_color)
        one_button.config(bg=button_color)
        two_button.config(bg=button_color)
        three_button.config(bg=button_color)
        four_button.config(bg=button_color)
        five_button.config(bg=button_color)
        six_button.config(bg=button_color)
        seven_button.config(bg=button_color)
        eight_button.config(bg=button_color)
        nine_button.config(bg=button_color)
        decimal_button.config(bg=button_color)
        equal_button.config(bg=button_color)
        add_button.config(bg=button_color)
        sub_button.config(bg=button_color)
        mult_button.config(bg=button_color)
        div_button.config(bg=button_color)
        del_button.config(bg=button_color)
        negative_button.config(bg=button_color)
        squared_button.config(bg=button_color)
        square_root_button.config(bg=button_color)
        color_button.config(bg=button_color)
        basic_clear_button.config(bg=button_color)
        full_clear_button.config(bg=button_color)
        previous_input.config(bg=background_color)
        current_input.config(bg=background_color)
        history.config(bg=history_background_color)
        history_label.config(bg=history_background_color)
        count = 0


#  Trying to create grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)
window.columnconfigure(5, weight=1)
window.columnconfigure(6, weight=1)



window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=1)
window.rowconfigure(7, weight=1)


entry = Entry(window)
entry.grid(row=0, columnspan=4, sticky=W+E)

#  Create Font
history_font = font.Font(family="Elephant", weight="bold", size=20)
buttonFont = font.Font(family="Elephant", weight="bold")
firstlabelFont = font.Font(family="Elephant", weight="bold", size=30)
secondLabelFont = font.Font(family="Elephant", weight="bold", size=20)

#  Set name of window
window.title("Michael's Calculator")

#  Set size of the window
window.geometry("750x700+10+20")
width = window.winfo_reqwidth()

history_label = Label(window, text="History", fg="white", bg=history_background_color, font=firstlabelFont, relief="groove", anchor="center", width= 12)
history_label.grid(row= 0, column=4, columnspan= 7, sticky="news")

history = Label(window, text="", fg="white", bg=history_background_color, font=history_font, relief="groove", anchor="ne", width= 12)
history.grid(row= 1, rowspan= 8, column=4, columnspan= 7, sticky="news")



#  Creating label that will display input and output
placeHolder = StringVar(window, value=final_number)
global current_input




current_input = Entry(window, fg="black", textvariable = enter_string, bg=background_color, font=firstlabelFont, relief="groove", justify="right", width=22)
current_input.grid(row=1, column=0, columnspan=4, sticky="nsew")
entry_var = enter_string.get()
enter_string.set("")
print(entry_var)



previous_input = Label(window, text="", fg="black", bg=background_color, font=secondLabelFont, relief="groove", anchor="e")
previous_input.grid(row=0, column=0, columnspan=4, sticky="nsew")



#  ---------------------------------------------------------------------------


def equal_button():
    global history_array
    global secondary_number
    global final_number
    global previous_sum
    global sum

    print("The width of Tkinter window:", window.winfo_width())

    if secondary_number != "":
        try:
            final_number = enter_string.get()
            float(final_number)
            float(secondary_number)
        except ValueError:
            final_number = ""
            enter_string.set("")

        if opperator_holder == "+":
            sum = float(secondary_number) + float(final_number)
            previous_input.config(text="{0:,.2f}".format(float(secondary_number)) + " + " + "{0:,.2f}".format(float(final_number)) + " = " + "{:,}".format(sum))

            history_array.append("{0:,.2f}".format(float(secondary_number)) + " + " + "{0:,.2f}".format(float(final_number)) + " = " + "{:,}".format(sum))
            history_string = ""
            history_length = len(history_array)
            for x in range(history_length):
                history_value = history_array[x]
                history_string = str(history_string) + "\n" + str(history_value.strip("[]"))
            history.config(text= history_string)


            enter_string.set("")
            previous_sum=sum

        elif opperator_holder == "-":
            sum = float(secondary_number) - float(final_number)
            previous_input.config(text="{0:,.2f}".format(float(secondary_number)) + " + " + "{0:,.2f}".format(float(final_number)) + " = " + "{:,}".format(sum))
            enter_string.set("")
            previous_sum=sum

            history_array.append("{0:,.2f}".format(float(secondary_number)) + " + " + "{0:,.2f}".format(
                float(final_number)) + " = " + "{0:,.2f}".format(sum))
            history_string = ""
            history_length = len(history_array)
            for x in range(history_length):
                history_value = history_array[x]
                history_string = str(history_string) + "\n" + str(history_value.strip("[]"))
            history.config(text=history_string)

        elif opperator_holder == "/":
            sum = float(secondary_number) / float(final_number)
            previous_input.config(text="{0:,.2f}".format(float(secondary_number)) + " + " + "{0:,.2f}".format(float(final_number)) + " = " + "{:,}".format(sum))
            enter_string.set("")
            previous_sum=sum

            history_array.append("{0:,.2f}".format(float(secondary_number)) + " + " + "{0:,.2f}".format(
                float(final_number)) + " = " + "{0:,.2f}".format(sum))
            history_string = ""
            history_length = len(history_array)
            for x in range(history_length):
                history_value = history_array[x]
                history_string = str(history_string) + "\n" + str(history_value.strip("[]"))
            history.config(text=history_string)

        elif opperator_holder == "x":
            sum = float(secondary_number) * float(final_number)
            previous_input.config(text="{0:,.2f}".format(float(secondary_number)) + " + " + "{0:,.2f}".format(float(final_number)) + " = " + "{:,}".format(sum))
            enter_string.set("")
            previous_sum=sum

            history_array.append("{0:,.2f}".format(float(secondary_number)) + " + " + "{0:,.2f}".format(
                float(final_number)) + " = " + "{0:,.2f}".format(sum))
            history_string = ""
            history_length = len(history_array)
            for x in range(history_length):
                history_value = history_array[x]
                history_string = str(history_string) + "\n" + str(history_value.strip("[]"))
            history.config(text=history_string)


#  --------------------------------------------------------------------------------------------------------

def addition_button():
    global opperator_holder
    global final_number
    global secondary_number
    global previous_sum

    if previous_sum != 0:
        secondary_number = previous_sum
        previous_input.config(text="{0:,.2f}".format(previous_sum) + " +")
        opperator_holder = "+"
    else:
        try:
            final_number = enter_string.get()
            float(final_number)
            previous_input.config(text="{0:,.2f}".format(float(final_number)) + " +")
            secondary_number = final_number
            enter_string.set("")
            opperator_holder = "+"

        except ValueError:
            final_number = ""
            enter_string.set("")


def subtraction_button():
    global opperator_holder
    global final_number
    global secondary_number
    global previous_sum


    if previous_sum != 0:
        secondary_number = previous_sum
        previous_input.config(text="{0:,.2f}".format(previous_sum) + " -")
        opperator_holder = "-"
    else:
        try:
            final_number = enter_string.get()
            float(final_number)
            previous_input.config(text="{0:,.2f}".format(float(final_number)) + " -")
            secondary_number = final_number
            enter_string.set("")
            opperator_holder = "-"

        except ValueError:
            final_number = ""
            enter_string.set("")


def division_button():
    global opperator_holder
    global final_number
    global secondary_number
    global previous_sum

    if previous_sum != 0:
        secondary_number = previous_sum
        previous_input.config(text="{0:,.2f}".format(previous_sum) + " /")
        opperator_holder = "/"
    else:
        try:
            final_number = enter_string.get()
            float(final_number)
            previous_input.config(text="{0:,.2f}".format(float(final_number)) + " /")
            secondary_number = final_number
            enter_string.set("")
            opperator_holder = "/"

        except ValueError:
            final_number = ""
            enter_string.set("")


def multiplication_button():
    global opperator_holder
    global final_number
    global secondary_number
    global previous_sum

    if previous_sum != 0:
        secondary_number = previous_sum
        previous_input.config(text="{0:,.2f}".format(previous_sum) + " x")
        opperator_holder = "x"
    else:
        try:
            final_number = enter_string.get()
            float(final_number)
            previous_input.config(text="{0:,.2f}".format(float(final_number)) + " x")
            secondary_number = final_number
            enter_string.set("")
            opperator_holder = "x"

        except ValueError:
            final_number = ""
            enter_string.set("")


#  ------------------------------------------------------------------

def full_clear_button():
    enter_string.set("")
    global final_number
    global opperator_holder
    global sum
    global previous_sum
    global history_array
    final_number = ""
    global secondary_number
    secondary_number = ""
    previous_input.config(text=" ")
    previous_sum = 0
    sum = 0
    opperator_holder = ""
    history_array.clear()
    history.config(text="")


def light_clear_button():
    global final_number
    final_number = ""
    enter_string.set("")


def negative_positive_button():
    global final_number
    final_number = enter_string.get()

    if float(final_number) > 0.0:
        current_input.insert(0, "-")
        final_number = enter_string.get()
    else:
        current_input.delete(first="0", last="1")
        final_number = enter_string.get()


def delete_button_function():
    global final_number
    if len(final_number) >= 0:
        current_input.delete(first=len(final_number)-1, last=len(final_number))
        final_number = enter_string.get()

def squared_button_function():
    global final_number
    global secondary_number
    global previous_sum


    if previous_sum != 0:
        sum = previous_sum * previous_sum
        previous_input.config(text="{0:,.2f}".format(previous_sum) + "² = " + "{0:,.2f}".format(sum))
        previous_sum = sum

        history_array.append("{0:,.2f}".format(previous_sum) + "² = " + "{0:,.2f}".format(sum))
        history_string = ""
        history_length = len(history_array)
        for x in range(history_length):
            history_value = history_array[x]
            history_string = str(history_string) + "\n" + str(history_value.strip("[]"))
        history.config(text=history_string)
    else:
        try:
            final_number = enter_string.get()
            float(final_number)
            sum = float(final_number) * float(final_number)
            previous_input.config(text="{0:,.2f}".format(float(final_number)) + "² = " + "{0:,.2f}".format(sum))
            enter_string.set("")
            previous_sum = sum

            history_array.append("{0:,.2f}".format(previous_sum) + "² = " + "{0:,.2f}".format(sum))
            history_string = ""
            history_length = len(history_array)
            for x in range(history_length):
                history_value = history_array[x]
                history_string = str(history_string) + "\n" + str(history_value.strip("[]"))
            history.config(text=history_string)
        except ValueError:
            final_number = ""
            enter_string.set("")

def square_root_button_function():
    global final_number
    global secondary_number
    global previous_sum

    if previous_sum != 0:
        sum = math.sqrt(previous_sum)

        previous_input.config(text="√" + "{0:,.2f}".format(previous_sum) + " = " + "{0:,.2f}".format(sum))

        history_array.append("√" + "{0:,.2f}".format(float(previous_sum)) + " = " + "{0:,.2f}".format(sum))
        previous_sum = sum
        history_string = ""
        history_length = len(history_array)
        for x in range(history_length):
            history_value = history_array[x]
            history_string = str(history_string) + "\n" + str(history_value.strip("[]"))
        history.config(text=history_string)
    else:
        try:
            final_number = enter_string.get()
            float(final_number)
            sum = math.sqrt(float(final_number))
            previous_input.config(text="√" + "{0:,.2f}".format(float(final_number)) + " = " + "{0:,.2f}".format(sum))
            enter_string.set("")
            previous_sum = sum

            history_array.append("√" + "{0:,.2f}".format(float(final_number)) + " = " + "{0:,.2f}".format(sum))
            history_string = ""
            history_length = len(history_array)
            for x in range(history_length):
                history_value = history_array[x]
                history_string = str(history_string) + "\n" + str(history_value.strip("[]"))
            history.config(text=history_string)

        except ValueError:
            final_number = ""
            enter_string.set("")


#  -----------------------------------------------------------------


def number_zero():
    global final_number
    current_input.insert(len(final_number), "0")
    final_number=enter_string.get()


def number_one():
    global final_number
    current_input.insert(len(final_number), "1")
    final_number=enter_string.get()


def number_two():
    global final_number
    current_input.insert(len(final_number), "2")
    final_number=enter_string.get()


def number_three():
    global final_number
    current_input.insert(len(final_number), "3")
    final_number=enter_string.get()


def number_four():
    global final_number
    current_input.insert(len(final_number), "4")
    final_number=enter_string.get()


def number_five():
    global final_number
    current_input.insert(len(final_number), "5")
    final_number=enter_string.get()


def number_six():
    global final_number
    current_input.insert(len(final_number), "6")
    final_number=enter_string.get()


def number_seven():
    global final_number
    current_input.insert(len(final_number), "7")
    final_number=enter_string.get()


def number_eight():
    global final_number
    current_input.insert(len(final_number), "8")
    final_number=enter_string.get()


def number_nine():
    global final_number
    current_input.insert(len(final_number), "9")
    final_number=enter_string.get()


def decimal_button():
    global final_number
    current_input.insert(len(final_number), ".")
    final_number = enter_string.get()

#  ---------------------------------------------------------------------------------
#  Normal Operation Buttons

#  Create equals button
equal_button = Button(window, text="=", bg=button_color,  fg="black", font=buttonFont, command=equal_button)
equal_button.grid(row=7, column=3, sticky="nsew")

#  Creates Addition Button
add_button = Button(window, text="+", bg=button_color, fg="black", font=buttonFont, command=addition_button)
add_button.grid(row=6, column=3, sticky="nsew")

#  Creates Subtraction Button
sub_button = Button(window, text="_", bg=button_color, fg="black", font=buttonFont, command=subtraction_button)
sub_button.grid(row=5, column=3, sticky="nsew")

#  Creates Multiplication Button
mult_button = Button(window, text="X", bg=button_color, fg="black", font=buttonFont, command=multiplication_button)
mult_button.grid(row=4, column=3, sticky="nsew")

#  Creates Division Button
div_button = Button(window, text="/", bg=button_color,  fg="black", font=buttonFont, command=division_button)
div_button.grid(row=3, column=3, sticky="nsew")

#  Creates Delete Button
del_button = Button(window, text="DEL", bg=button_color, fg="black", font=buttonFont, command=delete_button_function)
del_button.grid(row=2, column=3, sticky="nsew")

#  ----------------------------------------------------------------------------------------
#  Numerical Buttons

#  Row one
#  Creates 0 button
zero_button = Button(window, text="0", bg=button_color, fg="black", font=buttonFont, command=number_zero)
zero_button.grid(row=7, column=0, columnspan= 2, sticky="nsew")

#  Creates Decimal button
decimal_button = Button(window, text=".", bg=button_color, fg="black", font=buttonFont, command=decimal_button)
decimal_button.grid(row=7, column=2, sticky="nsew")



#  Row two
#  Creates 1 button
one_button = Button(window, text="1", bg=button_color,  fg="black", font=buttonFont, command=number_one)
one_button.grid(row=6, column=0, sticky="nsew")

#  Creates 2 button
two_button = Button(window, text="2", bg=button_color, fg="black", font=buttonFont, command=number_two)
two_button.grid(row=6, column=1, sticky="nsew")

#  Creates 3 Button
three_button = Button(window, text="3", bg=button_color,  fg="black",font=buttonFont, command=number_three)
three_button.grid(row=6, column=2, sticky="nsew")


#  Row 3
#  Creates 4 button
four_button = Button(window, text="4", bg=button_color, fg="black",font=buttonFont, command=number_four)
four_button.grid(row=5, column=0, sticky="nsew")

#  Creates 5 button
five_button = Button(window, text="5", bg=button_color, fg="black",font=buttonFont, command=number_five)
five_button.grid(row=5, column=1, sticky="nsew")

#  Creates 6 Button
six_button = Button(window, text="6", bg=button_color, fg="black",font=buttonFont, command=number_six)
six_button.grid(row=5, column=2, sticky="nsew")



#  Row 3
#  Creates 7 button
seven_button = Button(window, text="7", bg=button_color,  fg="black",font=buttonFont, command=number_seven)
seven_button.grid(row=4, column=0, sticky="nsew")

#  Creates 8 button
eight_button = Button(window, text="8", bg=button_color,  fg="black",font=buttonFont, command=number_eight)
eight_button.grid(row=4, column=1, sticky="nsew")

#  Creates 9 Button
nine_button = Button(window, text="9", bg=button_color,  fg="black",font=buttonFont, command=number_nine)
nine_button.grid(row=4, column=2, sticky="nsew")


#  Misc Operation Buttons

#  Row 4
#  Creates +/- Button
negative_button = Button(window, text="+/-", bg=button_color,  fg="black", font=buttonFont, command=negative_positive_button)
negative_button.grid(row=3, column=2, sticky="nsew")

#  Creates squared button
squared_button = Button(window, text="x²", bg=button_color, fg="black", font=buttonFont, command=squared_button_function)
squared_button.grid(row=3, column=1, sticky="nsew")

#  Creates Square Root Button
square_root_button = Button(window, text="√x", bg=button_color, fg="black", font=buttonFont, command=square_root_button_function)
square_root_button.grid(row=3, column=0, sticky="nsew")


#  Row 5
#  Creates the basic Clear
basic_clear_button = Button(window, text="CE", bg=button_color, fg="black", font=buttonFont, command=light_clear_button)
basic_clear_button.grid(row=2, column=2, sticky="nsew")

#  Creates Full clear button
full_clear_button = Button(window, text="C", bg=button_color,  fg="black", font=buttonFont, command=full_clear_button)
full_clear_button.grid(row=2, column=1, sticky="nsew")

#  Creates swap color button
color_button = Button(window, text="Color", bg=button_color,  fg="black", font=buttonFont, command=colors_button)
color_button.grid(row=2, column=0, sticky="nsew")

window.mainloop()
