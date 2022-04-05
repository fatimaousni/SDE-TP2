#Exo1
noms = "Fatima Ousni"
basic.show_string(nom)

def on_forever():
    pass
basic.forever(on_forever)


#Exo2
def on_forever():
    led.plot(3, 2)
    basic.pause(200)
    led.unplot(3, 2)
basic.forever(on_forever)


#Exo3
def on_button_pressed_a():
    images.icon_image(IconNames.HAPPY).show_image(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    images.icon_image(IconNames.SAD).show_image(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

#Exo4
var3 = 0

def on_forever():
    global var3
    for var2 in range(10):
        var3 = var2 % 2
        if var3 == 0:
            basic.show_number(var2)
basic.forever(on_forever)

#Exo5

var3 = 0

def on_forever():
    global var3
    for var2 in range(10):
        var3 = var2 % 2
        if var3 != 0:
            basic.show_number(var2)
basic.forever(on_forever)

#Exo6

def on_forever():
    basic.show_leds("""
        # # # # #
                . # # # #
                . . # # #
                . . . # #
                . . . . #
    """)
    basic.clear_screen()
    basic.pause(500)
basic.forever(on_forever)

#Exo7
def on_forever():
    for colonne in range(5):
        for ligne in range(5):
            led.plot(colonne, ligne)
            basic.pause(500)
            led.unplot(colonne, ligne)
basic.forever(on_forever)

#Exo8
index = 0
liste = [images.create_image("""
        . . . . .
            . . # . .
            . . . . .
            . . . . .
            . . . . .
    """),
    images.create_image("""
        . . . . .
            . . . # .
            . . . . .
            . # . . .
            . . . . .
    """),
    images.create_image("""
        . . # . .
            . . . . .
            # . . . #
            . . . . .
            . . . . .
    """),
    images.create_image("""
        # . . . #
            . . . . .
            . . . . .
            . . . . .
            # . . . #
    """)]
liste[index].show_image(0)
while index < len(liste):
    if input.button_is_pressed(Button.B):
        index += 1
        basic.clear_screen()
        basic.pause(100)
        liste[index].show_image(0)
    elif input.button_is_pressed(Button.A):
        index = index - 1
        basic.clear_screen()
        basic.pause(100)
        liste[index].show_image(0)