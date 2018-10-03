# Panzerspiel
A small tank game where you can customize your own tank.

# Idea
The basic idea of this game was to make a customizable tank game.
Therefor you have 100 credits to spend on different attributes of
you tank are:

1. Speed
2. Acceleration
3. Health
4. DPS (damage per shot)
5. Fire Rate

You will notice, that the acceleration is also used to calculate the angular
velocity of your tank.

# Goal
"Of course I know the rules. Simple. You hit him, don't let him hit you." -- Mr. Han

# Movement
The red tank is controlled by the keys w, a, s, d and alt (left).

The blue tank is controlled by the keys i, j, k, l and space.

# Arena
The consists of two different types of obstacles.

1. Wood Boxes (500 life points)
2. Stone Boxes (indestructible)

The position and number of stone and wood boxes as well as the start positions
of the tanks are generated randomly.
You may encounter to stuck within a box.
Hopefully your enemy is a honourable gentleman and will restart the match.

# Surge Factor
The surge factor specifies how many credit points do you need to set an attribute
to its max. A surge factor of 0.9, the default value, means that you need 90 of 100
credit points to set you health to the max of 5000.
You can change the surge factor in the options menu.
