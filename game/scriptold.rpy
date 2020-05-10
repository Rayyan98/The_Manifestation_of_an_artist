# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")
define M = Character("Elderly man")
define S= Character("Man in suit" , color="#0000ff")
define G= Character("Spectacle Man", color="#00ff00")
define W = Character("Women", color="#ff0000")

image yi1 = "OBrien1.png"
image yi2 = "OBrien2.png"
image yi3 = "OBrien3.png"
image yi4 = "OBrien4.png"
image bg1 = "OBrien1.png"
image painting = "painting.jpg"
image painting2 = "painting2.png"
image bg1 = "bg4.png"
image yi animated:
    "yi1"
    pause 5
    "yi2"
    pause 5
    repeat 
image persona = Movie(play="Persona_5_mp4.ogv", size=(1280,1400),pos=(0,-350),anchor=(0,0))

# The game starts here.

label start1:
 
    play music "music1.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show bg1 at center:
        zoom 0.6
    with Dissolve(1)
    show yi1:
        zoom 0.5
    with Dissolve(2)
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    "At an art exhibit, you stare at the painting before you and silently admire your own brilliance."

    "{i}My brilliance truly knows no bounds. I do feel bad for all the other plebeians here though, As soon as they decided to submit their work in this exhibit they were destined to be over-looked, forgotten, used as mere background decoration to accentuate my artistic genius.{/i}"
    
    "{i}...{/i}"
    
    "{i}However, something doesn’t add up…{/i}"
    
    "You take a look around and notice the unmistakable lack of attention your painting is getting. It’s as if a force field had been erected around it, preventing people from coming near."
    
    hide yi1
    show yi2:
        zoom 0.5

    "{i}Could it be?...{/i}"
    

return
