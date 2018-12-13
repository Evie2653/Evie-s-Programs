import pyautogui as pg
import webbrowser as wb
import time as t

points = 0
show = pg.prompt("What is your favorite show? ")

if show == "The Office":
    wb.open ("https://www.youtube.com/watch?v=WaaANll8h18")
    pg.alert ("Best shows ever!!!")
    points += 8
elif show == "Friends":
    wb.open ("https://www.youtube.com/watch?v=4ltx3PBnWcI")
    pg.alert ("Joey is the best")
    points += 4
elif show == "Parks and Rec":
    wb.open ("https://www.youtube.com/watch?v=Y1hVFbdMP5Y")
    pg.alert ("Jerry always falls and spills:)")
elif show == "How I Met Your Mother":
    wb.open ("https://www.youtube.com/watch?v=q6PKnrfRADM")
    pg.alert ("Ted is actually really smart")
    points += 5
elif show == "30 Rock" :
    pg.alert ("It is kind of old")
elif show == "Gossip Girl" :
    pg.alert ("It's sooooooooooo good")
else:
    pg.alert ("Your favorite show is " + show)

t.sleep (5)
    
food = pg.prompt ("What is your favorite food? ")
if food == "Pizza":
    wb.open ("https://www.youtube.com/watch?v=HCAPjIVOdJw")
    pg.alert ("Cheese is the best!")
elif food == "Calzone":
    pg.alert ("EWwWWWWwwww those are the worst")
    points -= 3
elif food == "Pasta":
    wb.open ("https://www.youtube.com/watch?v=v41-SNTCCOw")
    pg.alert ("I like plain pasta the best")
    points += 9
elif food == "Tacos":
    wb.open ("https://www.youtube.com/watch?v=3NLDcPNJzzE")
    pg.alert ("Fish tacos are really good")
    points += 6
elif food == "Burgers":
    wb.open ("https://www.youtube.com/watch?v=3YkRVRGBfm")
    pg.alert ("That is so American")
elif food == "French Toast":
    pg.alert ("I don't like breakfast foods")
else:
    pg.alert ("Your favorite food is" + food)
t.sleep (4)
dog = pg.prompt ("What is your favorite type of dog?")
if dog == "Great Dane":
    wb.open ("https://www.youtube.com/watch?v=s9amcwt0h7M")
    pg.alert ("I love them too")
    points += 8
elif dog == "Chuwawa":
    wb.open ("https://www.youtube.com/watch?v=ohDSTMguO5A")
    pg.alert ("Small dogs can be very annoying, except for frenchies!")
    points -= 4
elif dog == "Lebrador":
    wb.open ("https://www.youtube.com/watch?v=nb8ky5RoHTQ")
    pg.alert ("They are such good family dogs.")
elif dog == "Cat":
    wb.open ("https://www.youtube.com/watch?v=1Wh8RzcQZr4")
    pg.alert ("I hate cats, and they are not even dogs")
    points -= 8
elif dog == "German Shepard":
    pg.alert ("They are so cute")
elif dog == "Labradoodle":
    pg.alert ("Awwwwwwwwww")
else:
    pg.alert ("Your favorite dogs is " + dog)
t.sleep (5)
sports = pg.prompt ("What is your favorite type of sports?")
if sports == "Dance":
    wb.open ("https://www.youtube.com/watch?v=Jt2dGIfE4Z0")
    pg.alert ("I love that too")
    points += 7
elif sports == "Soccer":
    wb.open ("https://www.youtube.com/watch?v=bKOTKHtbM54")
    pg.alert ("We all have different prefrences")
    points -= 4
elif sports == "Horseback Riding":
    wb.open ("https://www.youtube.com/watch?v=9vtCsiobXh4")
    pg.alert ("That is a sport")
    points += 6
elif sports == "Skiing":
    pg.alert ("I don't like skiing")
elif sports == "Hockey":
    wb.open ("https://www.youtube.com/watch?v=QdBD_870fyA")
    pg.alert ("I guess")
elif sports == "Feild Hockey":
    pg.alert ("ehh")
else:
    pg.alert ("Your favorite sports is " + sports)
t.sleep (6)
animal = pg.prompt ("What is your favorite type of animal?")
if animal == "Dogs":
    wb.open ("https://www.youtube.com/watch?v=e-OPyR_P7rU")
    pg.alert ("I love them too")
    points += 9
elif animal == "Elephants":
    wb.open ("https://www.youtube.com/watch?v=FkvGFEPzr1M")
    pg.alert ("I love them")
    points += 8
elif animal == "Horses":
    pg.alert ("It's like ahving a kid.")
elif animal == "Cats":
    pg.alert ("I hate cats")
    points -= 6
elif animal == "Cheetas":
    wb.open ("https://www.youtube.com/watch?v=zgQ0cyNJZV4")
    pg.alert ("They are so cute")
    points += 6
elif animal == "Dolphins":
    wb.open ("https://www.youtube.com/watch?v=FraLBRLqEhg")
    pg.alert ("Awwwwwwwwww")
else:
    pg.alert ("Your favorite animal is " + animal)

pg.alert("You scored this many points:" + str(points))
