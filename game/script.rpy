# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
  def eyewarp(x):
    return x**1.33
  eye_open = ImageDissolve("eye.png", 2.5, ramplen=128, reverse=False, time_warp=eyewarp)
  eye_shut = ImageDissolve("eye.png", 2.5, ramplen=128, reverse=True, time_warp=eyewarp)
  
define y = Character("You")
define EM = Character("Elderly man")
define S= Character("Man in suit" , color="#0000ff")
define G= Character("Spectacle Man", color="#00ff00")
define W = Character("Women", color="#ff0000")
define C = Character("Colt", color="#0000ff")
define A = Character("Artemis", color="#ff0000")
define Fred = Character("Fred", color="#00ff00")
define SM = Character("Young Man", color="#ff0000")
define SV= Character("Sylvoski",color="#ff0000")
define pov = Character("[povname]")

image yi1 = "OBrien1.png"
image yi2 = "OBrien2.png"
image yi3 = "OBrien3.png"
image yi4 = "OBrien4.png"
image art1 = "jobiho.png"
image art2 = "jobiho2.png"
image art3 = "jobiho3.png"
image gla1 = "moorcam.png"
image gla2 = "moorcam1.png"
image gla3 = "moorcam2.png"
image gla4 = "moorcam3.png"
image s1 = "isacnetaro.png"
image s2 = "isacnetaro1.png"
image s3 = "isacnetaro2.png"
image om1 = "shahsaleem.png"
image om2 = "shahsaleem1.png"
image om3 = "shahsaleem2.png"
image om4 = "shahsaleem3.png"
image om5 = "shahsaleem4.png"
image om6 = "shahsaleem5.png"
image om7 = "shahsaleem6.png"
image om8 = "shahsaleem7.png"
image om9 = "shahsaleem8.png"
image om10 = "shahsaleem9.png"
image so1 = "solvoski1.png"
image so2 = "solvoski2.png"
image sn3 = "solvoski3.png"
image so3 = "solvoski.png"
image sn1 = "solvoski4.png"
image sn2 = "solvoski5.png"

image painting = "painting.jpg"
image painting2 = "painting2.png"
image bg1 = "bg4.png"
image persona = Movie(play="Persona_5_mp4.ogv", size=(1280,1400),pos=(0,-350),anchor=(0,0))
image street = Movie(play="street video.ogv", size=(1280,720) , pos=(0,0), anchor=(0,0))
image tvlounge = "tvlounge.png"
image warehouseout = "warehouse outside.png"
image warehousein = "warehouse.png"
image sewer = "sewer.png"
image sewer1 = "sewer1.png"
image manhole = "manhole cover.png"
image canvas = "canvas.jpg"
image book = "book.png"
image prison = "prison.png"

image site = "constructionsite.png"
image sitestairs= "sitestairs.png"
image site2 = "site2.png"
image sitedark = "site dark.jpg"
image siteout= "siteout.png"

image rotmanifest= "rotmanifest.jpg"
image rotfar="rotfar.jpg"
image rotpose= "rotpose.png"
image rotweird = "rotweird.jpg"

image schair="s_chair.jpg"
image sfallen="s_fallen.jpg"
image sfear = "s_fear.jpg"
image spower="s_power.png"
image sreveal="s_reveal.jpg"
image sstare="s_stare.jpg"
image ssword="s_sword.jpg"

image renclash="renclash.jpg"
image rencrystal1 ="rencrystal1.png"
image rencrystal2 ="rencrystal2.jpg"
image reneyeoff = "reneyeoff.jpg"
image reneyeon = "reneyeon.jpg"
image rengun = "rengun.jpg"
image renready= "renready.jpg"
image renslash="renslash.jpg"
image renweapon="renweapon.png"
image renactivate = Movie(play="renactivate.ogv", size=(1280,720) , pos=(0,0), anchor=(0,0))
image convergebirds = "convergebirds.jpg"
image lotbirds = "lotbirds.jpg"
image monster1 = "monster1.jpg"
image monster2 = "monster2.jpeg"

image crystal = "crystal.png"

# The game starts here.

label start:
    scene black
    play music "music1.mp3"
    
    label name:
    python:
        povname= renpy.input("Enter a name for your character")
        povname=povname.strip()
        
        if not povname:
            povname= "Ren"
    
if povname=="Ren":
    menu:
        "Is Ren ok as the character name ?"
        "Yes":
            jump start2
        "No":
            jump name
else:
    jump start2
                
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    label start2:
        
    show bg1 at center:
        zoom 0.6
    with Dissolve(1)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    "At an art exhibit, you stare at the painting before you and silently admire your own brilliance."

    "{i}My brilliance truly knows no bounds. I do feel bad for all the other plebeians here though, As soon as they decided to submit their work in this exhibit they were destined to be over-looked, forgotten, used as mere background decoration to accentuate my artistic genius.{/i}"
    
    "{i}...{/i}"
    
    "{i}However, something doesn’t add up…{/i}"
    
    "You take a look around and notice the unmistakable lack of attention your painting is getting. It’s as if a force field had been erected around it, preventing people from coming near."

    "{i}Could it be?...{/i}"
    
    "{i}Did my peerless artistic talents prove to be too much for these philistines’ unrefined eyes?{/i}"
    show s1:
     size(330,550)
     pos(200,100)
     anchor(0,0)
    "An elderly man wearing an expensive looking suit approaches your painting."
    
    "{i}Ah, a man of culture!{/i}"
    
    y "Excuse me sir, May ask your opinion of this painting?"
    
    "The man looks at you with an inscrutable gaze and waits some time before responding"
    
    EM "I think the technique and composition are both splendid, And the painting itself is visually one of the most impressive pieces in the entire exhibit. On the whole though, I think it’s mediocre at best"
    hide s1
    show s2:
     size(330,550)
     anchor(0,0)
     pos(200,100)
    y "What? How dare you! May I ask why you would think to label my art mediocre?!"
    
    EM "Ah so you are the young man who made this. I apologize for offending you but you asked for my opinion and I gave it. As for why I would think this way, It is because I don’t believe your painting qualifies as true art"
    
    y "What? Why? How is it not art?!"
    hide s2
    show s1:
     size(330,550)
     anchor(0,0)
     pos(200,100)
    "The Elderly man’s inscrutable gaze returns. He turns back to the painting. " 
    
    EM "This is an abstract painting that depicts a multitude of swirling lines converging upon a single point"
    
    "The old man pauses"
    
    EM "So why would you name it “The heart”"
    
    menu:
        y "That’s because…"
        
        "I thought It would sound cool.":
            jump choice_1_1
        "I don’t know…":
            jump choice_1_2
        
    label choice_1_1:
        hide s1
        show s3:
         size(330,550)
         pos(200,100)
         anchor(0,0)
        EM "And therein lies the problem. Instead of having a concrete Idea or even an emotion it wants to convey, this painting is merely an aesthetically pleasing display, it doesn’t have an ounce of soul behind it. Therefore it is not “art” but a mere decorative piece. "
        jump Choice1_done
    label choice_1_2:
        hide s1
        show s3:
         size(330,550)
         pos(200,100)
         anchor(0,0)
        EM "Hmm, I see, in that case perhaps you need to think about what you want to convey through your art before you decide on naming it. In any case, if even the painter himself cares so little to adequately name the piece why would anyone else even spare the time to look at it?"
        jump Choice1_done
        
    label Choice1_done:    
    "You want to object to the elderly mans words but… "
    
    "{i}He’s right{/i}"
    
    "The man seems to read your mind"
    hide s3
    show s1:
     size(330,550)
     pos(200,100)
     anchor(0,0)
    EM "Looking at this painting, I can tell that you have talent, and you may even become a great artist someday. But for now I suggest you work on figuring out what exactly it is you want your art to say to those who view it."
    
    y "How?"
    
    EM "Well, first of all, perhaps you can start by trying to emulate the work of those that inspire you. Think about the works of art that drew you to art in the first place and then try asking yourself why you like them so much. Once you’ve figured that out, you’ll have taken a step toward becoming a true artist."
    hide s1
    with Dissolve(2)
    "And with that the elderly man turned around and walked away into the crowd, likely headed toward another exhibit."
    
    show painting
    with Dissolve(1.0)
    stop music fadeout 2
    "You force yourself to stare at your painting."

    
    "You mutter to yourself"
    
    y "“Emulate the work of those that inspire you”…"
    
    "{i}Do I even have someone I was inspired by? Why did I pursue art in the first place? Was it because I wanted to make beautiful paintings?{/i}"
    
    "You look at your painting one more time"
    
    y "How could I have fooled myself into thinking"
    extend " {i}this{/i}"
    extend " would be enough to get me recognized as an artist."
    
    "The more you stare at your painting the less appealing it becomes."
    
    "The elderly mans words echo in your head"
    
    "{i}“It’s mediocre at best”{/i}"
    
    y "How could I have been so disrespectful as to allow such mediocre  trash to sully these walls."
    
    "The urge to destroy the painting wells up inside you."
    
    "The more you stare at it the more you dislike it"
    
    "You clench your fists."
    
    menu:
        "Destroy the painting":
            jump Destroy
        "Don’t destroy it":
            jump Dont_destroy
            
    label Destroy:
        "You raise your right hand toward the painting and imagine it being torn apart. You imagine the fibers of the paper being pulled by an imaginary force"
        scene painting
        with vpunch
    
        "The painting begins to shake violently"
        "You imagine the painting erupting into a million peaces"
        play sound "Paper.mp3"
        pause 0.8
        scene black
        show painting2:
            size(1280,720)
        with vpunch
        with hpunch
        with vpunch
        with hpunch
        "The painting explodes without leaving a single trace of its existance. Only the frame holding it remains"
        
        scene bg1 at center:
            zoom 0.6

        "The entire exhibition goes silent"
        
        "you turn around and face the people that surround you"
        
        "Everyone in the art exhibit stares at you, their expressions ranging from fear to awe"
        
        y "I apologize for the interruption. The painting I made was not up to par so I removed it. Please enjoy the rest of your evening"
        
        "The silence continues as you make your way for the exit and go home"
        

        jump Choice_2_Done
            
    label Dont_destroy:
        scene bg1 at center:
            zoom 0.6
        "You turn around"
        
        "You make your way for the exit and go home"
        
        jump Choice_2_Done
    
    label Choice_2_Done:
    scene canvas:
        size(1280,720)
    with Dissolve(1.5)
    play music "music1.mp3" fadein 2
    "You spend the next few days painting and thinking about what happened at the art exhibit."

    "No matter how hard you try, none of the paintings you make seem to satisfy you. Eventually you run out of paint and decide to watch some TV to pass the time"
    scene tvlounge:
        size(1280,720)
    with Dissolve(1.5)
    "News Anchor" "… These allegations will likely spell the end of Kevin Spacey’s Career. In other news…"

    "{i}Who the hell is Kevin Spacey?{/i}"

    "News Anchor" "The Number of people who have inexplicably fallen into a coma has increased to 37 as another person, 21 year old Waqar Nadeem was found unconscious outside a diner"

    "News Anchor" "Like all the previous cases, the mans body was found completely unharmed and there seem to be no signs of any sort of struggle. Furthermore no witness were present when the man collapsed."

    "News Anchor" "The authorities are still unsure if these cases are the result of deliberate actions taken against the victims"

    "You turn off the TV" 

    extend "{i}    That reminds me. I haven’t had breakfast yet.{/i}"
    stop music fadeout 2
    
    label bar:
        scene black
        with Dissolve(2)
        show persona

    "Out of Curiosity, You decide to visit the same diner mentioned in the News Broadcast"

    "You arrive at the Diner and have breakfast."

    show om1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)
        
    "A man in a black suit takes a seat at your table"

    hide om1
    "You decide to ignore him."
    show art1:
        size(250,450)
        pos(0,150)
        anchor(0,0)
    show gla1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)

    "A thin man wearing glasses takes a seat beside him, followed by a woman in a black jacket."
    hide art1
    hide gla1
    "{i}Should I leave?{/i}"

    menu :
       "Leave":
           "You decide to leave and get murdered on your way home"
           menu:
             "Try Again ?":
               jump bar
       "Stay":
           "You decide to stay"
           jump bypass

label bypass:    
    show om1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)
    
    S "I didn’t expect this many people to show up."

    show art1:
        size(250,450)
        pos(0,150)
        anchor(0,0)
    
    W "Yeah, I think 4 people is a little too much for this case"
    hide art1
    
    y "I think you may have mistaken me for someone else"
    hide gla1
    show om1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)

    S "What? You’re a Creator are you not?"
    
    y "What? how do you know that?"

    "The three of them exchange quick glances"
    hide om1
    show gla1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)
        
    G "The Association sent out a request to all nearby Creators to investigate these recent incidents of people falling into comas. Isn’t that why you’re here? To investigate?"
y "Oh I wasn’t aware of that. And I have no intention of taking part in this “operation”"
G "Well, It seems like we have enough people here already, And we can’t force you into helping us anyway so I guess it’s fine."
y "Good, just… One more thing, how did you know I was a Creator?"
hide gla1
show om1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)
S "I noticed you’re license poking out of your shirts breastpocket"

    
"You look down at your shirt to notice that your license was indeed poking out of your pocket."
"{i}How did he notice such a small detail?{/i}"
"The license served as proof that you were a registered Creator and were qualified to take part in certain operations requested by the creators association."

"After saying your goodbyes you get up to leave but stop yourself. A thought crosses your mind"
y "You say you’re going to investigate this incident, does that mean you have an idea of what exactly is going on?"

"All three of them go quiet"
S "No"
hide om1
show gla1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)
G "nope"
show art1:
        size(250,450)
        pos(0,150)
        anchor(0,0)
W "..I think I may have a clue"
W "This case is really similar to one that happened around 10 years ago in this very city. People were being found collapsed and in a vegetative state, in the end, it was discovered that these weren’t the same people but copies made by a Creator."
"You, the man in the suit and the spectacled man all hold your breath"
W "That creators name was Sylvoski and he was a serial killer who murdered people and then used his powers to create an exact living copy of his victims. Because of this, no one investigated these incidents as murders."
hide gla1
show om1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)

S "An exact, living, copy of a person… Is that even possible?"
W "It’s not that different from Creators who create living creatures like animals."
hide om1
show gla1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)

G "...Still.. those aren’t people you know?"
hide art1

y "So you think Sylvoski’s come back?"
hide gla1
show art1:
        size(250,450)
        pos(1000,150)
        anchor(0,0)

W "That’s the weird thing, Sylvoski’s still serving his sentence, I checked and he’s still in prison, what’s more, his mental state has deteriorated considerably over the years. He can barely even speak now"
hide art1
show om1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)

S "Serves him right"

y "A creator with the ability to create exact replicas of people... What kind of person was he?"
show art1:
        size(250,450)
        pos(0,150)
        anchor(0,0)

W "He was a strange one. He was originally an artist who specialized in creating photo-realistic paintings of people, When he was captured, he said he grew tired of painting portraits and instead wanted to recreate his subjects entirely, using the world as his canvas"
"{i}An artist?{/i}"
hide om1
show gla1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)

G "In any case, we should begin looking into this quickly. We won’t gain anything just standing around"
W "I agree"
hide gla1
show om1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)

S "Same"
hide om1
show gla1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)

G "What about you? You said you had no interest in taking part but you’re still here. Have you decided to change your mind?"
hide art1

y "This Sylvoski… He has committed many atrocities, all in the name of art. As an artist myself, if Sylvoski really is involved in this, I cannot allow him to carry on. I shall join you"
hide gla1
show om1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)

S "Great. Welcome aboard. I suppose we should all introduce ourselves. My name is Colt Samuel"
hide om1
show gla1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)

G "Fred Wohler"
show art1:
        size(250,450)
        pos(0,150)
        anchor(0,0)

W "Artemis Leto"
hide gla1
show om1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)

C "We should begin our investigation tomorrow. It’s still raining outside so why don’t we all get to know each other a little better while we wait for the weather to die down a little."
hide om1
show gla1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)

Fred "I haven’t even had breakfast yet… I want something filling and healthy"
hide gla1
show om1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)

C "Just get the bacon and eggs"
A "I’m a vegetarian; I hope they have something I can eat.."
C "What about you? You already ate right? Why not go for another round?"
menu:
   "Bacon and Eggs!":
      C "Awesome! Hey waiter! four orders of bacon and eggs please!"
   "I’m not hungry.":
      C "C’mon you’re paper thin! You need nourishment"
      C "Hey waiter! four orders of bacon and eggs please!"

A "I told you I’m a vegetarian!"
C "Three of those plates are for me"
hide om1
show gla1:
        size(280,550)
        pos(1000,100)
        anchor(0,0)

Fred "The eggs will have twenty five percent of my daily protein requirement.. but the pancakes are full of carbs that will make me feel full and provide a long lasting source of energy.."
hide gla1
hide art1
"You Spend the next few hours at the diner with your new friends"

"Eventually, the rain lets up and you head home"
scene black
with Dissolve(1.2)
"You decide to spend the rest of the night reading a book"

label reset:
$ fredb=True
$ coltb=True
$ artb=True
$ fredp=False
$ coltp=False
$ artp=False
$ count=0
$ biochemb=False
$ dramab=False
$ adventureb=False

label anchor:
stop music fadeout 3
queue music "music1.mp3"
scene book:
    size(1280,720)
with Dissolve(1.2)

if count==3:
 jump Sylvoskibattle

if fredb and coltb and artb:
  menu:
    "Read a biochemistry book (May make you smarter)":
        jump readbiochem
    "Read an adventure book (May make you braver)":
        jump readadventure
    "Read a drama book (May make you kinder)":
        jump readdrama
    "Spend the day lazying around":
        jump lazyaround

if fredb and coltb:
  menu:
    "Read a biochemistry book (May make you smarter)":
        jump readbiochem
    "Read an adventure book (May make you braver)":
        jump readadventure
    "Spend the day lazying around":
        jump lazyaround



if coltb and artb:
  menu:
    "Read an adventure book (May make you braver)":
        jump readadventure
    "Read a drama book (May make you kinder)":
        jump readdrama
    "Spend the day lazying around":
        jump lazyaround


if fredb and artb:
  menu:
    "Read a biochemistry book (May make you smarter)":
        jump readbiochem
    "Read a drama book (May make you kinder)":
        jump readdrama
    "Spend the day lazying around":
        jump lazyaround


if coltb:
  menu:
    "Read an adventure book (May make you braver)":
        jump readadventure
    "Spend the day lazying around":
        jump lazyaround


if fredb:
  menu:
    "Read a biochemistry book (May make you smarter)":
        jump readbiochem
    "Spend the day lazying around":
        jump lazyaround


if artb:
  menu:
    "Read a drama book (May make you kinder)":
        jump readdrama
    "Spend the day lazying around":
        jump lazyaround

jump Sylvoskibattle

label lazyaround:
        $ count= count+1
        "You spend the day lazying around, try to watch a few shows but can’t concentrate."
        extend "You feel something big is happening with one of your new friends, right under your nose."
        "Perhaps you should’ve read that book,"
        extend "maybe tomorrow"
        "You go to sleep"
        scene black
        with Dissolve(0.8)
        "You wake up the next day, still tired"
        jump anchor

label readbiochem:
    $ biochemb=True
    $ count=count+1
    $ fredb=False
    "You spend the rest of the night learning about biochemistry before going to bed"
    "The next day you get a message from Fred asking if you would like to accompany him on his investigation"
    menu:
       "Go with him":
           "You go to meet Fred at a specified address"
           jump Fredstory
       "Don’t go with him":
           "You decide to decline freds invitation"
           "You decide to read another book"
           scene black
           with Dissolve(1)
           jump anchor

label readadventure:
    $ adventureb=True
    $ count=count+1
    $ coltb=False
    "You decide to spend the rest of the day reading about a hobbit going to destroy a ring"
    "The next day Colt calls you asking if you would like to help him with his investigation"
    menu:
        "Go with him":
            "You Go to meet Colt at a specified address"
            jump ColtsStory
        'Don’t go with him':
            'You decide to decline Colt’s invitation'
            scene black
            with Dissolve(1)
            jump anchor

label readdrama:
$ dramab=True
$ count=count+1
$ artb=False
'You decide to spend the rest of the day reading a book about a lawyer fighting for the rights of an innocent man falsely accused of a crime by a racist society'
'The next day you receive message from Artemis asking if you’d like to help her investigate'
menu:
    'Go with her':
        'You decide to go meet her at a specified address'
        jump Artemisstory
    'Don’t go':
        "You decide to decline Artemis's invitation"
        scene black
        with Dissolve(1)
        jump anchor

label Fredstory:
scene black
with Dissolve(1.5)
"The address Fred Sent you leads you to a run-down looking ware-house"
scene warehouseout:
    size(1280,720)
with Dissolve(1.2)
stop music fadeout 2
queue music "warehouse.mp3"
"Fred walks up to you"
show gla1:
  size(280,500)
  pos(200,100)
  anchor(0,0)
with Dissolve(1.5)
Fred "I suppose you’re wondering why we’re here… "
y "Yes I am"
Fred "This warehouse was owned by Sylvoski. I think these two cases aren’t unconnected, so I thought maybe we could find some clues if we came here."
y "But wouldn’t the police have cleaned the place out once he was caught"
Fred "Sylvoski’s case was handled by the creators association, so this information is only available to us. And I checked the records and found that this warehouse was never given a thorough search because he never mentioned it in any interrogations or testimonies."
y "Ok then, lead the way"
"You head inside"

scene warehouse:
    size(1280,720)
with Dissolve(1.2)

show gla3:
  size(280,500)
  pos(200,100)
  anchor(0,0)
Fred "Look for anything that looks out of place, anything that seems like it doesn’t serve any purpose"
"Nothing really stands out to you. "
extend "Fred looks at you in disappointment."
extend " Fred looks around"
Fred "This room is smaller than it should be…"
"He walks up to a wall and looks at it intently. "
"An enormous crystal materialises over his head and smashes through the wall, revealing a staircase that leads underground"
hide gla3
with Dissolve(0.5)
"Fred calmly walks in"
show gla1:
  size(280,500)
  pos(200,100)
  anchor(0,0)

Fred "My affinity is the element Carbon by the way"
y "…I see… I can make paper…"

Fred "That sounds useful"
"You follow him down"
"At the bottom of the staircase you find a Steel door with A lock on it."
"Fred Materialises another large crystal and destroys the door with ease"
"He walks inside."
"You find yourself in a room with multiple passage ways "
y "So where do we go?"
Fred "We don’t need to. Somethings coming, from all of them."
hide gla1
show gla3:
  size(280,500)
  pos(200,100)
  anchor(0,0)

"You see something moving around in the shadows of the passageways"
"A crystal tears through the creature and you hear screams coming from the passage ways"
"You immediately cover the passages with walls of paper"
"You feel something tearing at the paper walls and start repairing it"
Fred "How long can you hold that?"
y "fifteen minutes. tops"
Fred "It’ll have to do"
hide gla3
show gla4:
  size(280,500)
  pos(200,100)
  anchor(0,0)

"Fred walks up to a paper wall"
Fred "How thick is this?"
y "…3  meters…"
"The tears keep coming. You keep repairing them but find it hard to concentrate"
"He touches the wall with his right hand holds the same position for 2 minutes. You feel the damage on that wall lessen and you no longer need to repair it"
"He does the same to all the others"
"By the time he’s finished with the last wall he looks exhausted"
"He rubs his forehead and tells you to stop"
"You disintegrate the walls"
"Fred turns on the flashlight on his phone and illuminates the passages "
"Inside you find several dozen small humanoid looking beings lying dead"
y "What did you do"
Fred "I turned the air inside these passageways into carbon monoxide."
y "You poisoned them"
hide gla4
show gla1:
  size(280,500)
  pos(200,100)
  anchor(0,0)

Fred "They all died rather quickly. I had to convert the air back to oxygen and eliminate the residual carbon and that’s why it took so much time"
"You check each passageway and find that they all contained signs of being used quite recently"
Fred "Someone besides those things has been living here"
y "What were those things?"
Fred "I think those were creations. I think this place was used as a space to practice creating self sustaining, biological creations. Those were just defects"
y "You think it was Sylvoski who made them? "
Fred "He’s still in jail. This has to be the work of someone who wants to do the same thing he did"
Fred "I’ll contact the others and tell them about what we found"
y "You look exhausted, you should head home and rest"
"Fred sighs, he looks like he just ran a marathon"
Fred "We’re both exhausted. We should head home for today."
"You decide to catch your breath outside the warehouse"

scene warehouseout:
    size(1280,720)
with Dissolve(1)
stop music fadeout 2
queue music "music1.mp3"
y "never knew you could use Carbon like that"
show gla1:
  size(280,500)
  pos(200,100)
  anchor(0,0)

Fred "Oh that was nothing. Theres a lot more you can do with Carbon, The entire field of Organic chemistry is based on the fact that Carbon reacts in so many different ways"
y "Is that why you chose it as your affinity?"
Fred "Kind of.. I’m a PhD student trying to get my doctorate in organic chemistry. I guess I’ve always been interested in it"
y "Wow, So you’re saying you could do more than that"
hide gla1
show gla2:
  size(280,500)
  pos(200,100)
  anchor(0,0)

"Fred smiles"
Fred "Oh yes"
scene black
with Dissolve(0.8)
"Back home. You can’t help but think about the way Fred used his powers."
scene canvas:
    size(1280,720)
with Dissolve(0.8)
"You decide to try Painting a hyper realistic diamond based on the one you saw today"
"You remember the way Fred talked about his Carbon powers with so much enthusiasm and it motivates you to try painting as well as you can"
"You imagine the diamond as vividly as possible"
"You imagine it’s shape, The way the light would reflect off of its surface"
"You even try to imagine the Carbon atoms held together through their covalent bonds."
"You paint until you can paint no more and are finally satisfied"
"You decide to go to sleep"
scene black
with Dissolve(0.8)
$ fredp= True
jump anchor

label ColtsStory:
scene black:
with Dissolve(1)
"You arrive at the place Colt mentioned and wait for him to arrive"
scene manhole:
    size(1280,720)
with Dissolve(1)

"You look around to see that the only thing significant here is a manhole cover"
"{i}Don’t tell me{/i}"
show om1:
 size(280,500)
 pos(250,100)
 anchor(0,0)
with Dissolve(1.5)

"The manhole cover  lifts open and Colt’s head pops out. He’s still wearing the same suit"
C "Come on, get in!"
"Without hesitation, you climb down the manhole"
scene sewer:
    size(1280,720)
with Dissolve(1)
stop music fadeout 2
queue music "Sewer.mp3"
"Inside the sewers Colt hands you a torch and a gas mask"
y "Why are we here?"
show om1:
 size(280,500)
 pos(250,100)
 anchor(0,0)
C "Out of the 37 victims so far, 6 of them have been sewage maintenance workers"
y "what?"
C "The police think it’s because they were exposed to toxic gases"
y "And what if that actually turns out to be the case"
hide om1
show om8:
 size(280,500)
 pos(250,100)
 anchor(0,0)

C "Here’s the thing, Years ago, that Sylvoski guy used these same sewers to get from one part of the city to the other without being seen"
y "And?"
C "And the same thing happened then too, an odd percent of the victims were sewage maintenance workers"
y "So you think He’s behind this too?"
hide om8
show om2:
 size(280,500)
 pos(250,100)
 anchor(0,0)

C "No he’s still in prison. It has to be someone with the same M.O"
"You decide to Concede and continue with Colt’s plan"
y "Fine, but why did we have to use THIS manhole"
hide om2
show om1:
 size(280,500)
 pos(250,100)
 anchor(0,0)
C "It’s close to my house"
"You and Colt start making you’re way through an entire route Colt planned out. "
hide om1
with Dissolve(1)
"It marked all the places the victims were found"
"You find nothing of value"
"You decide to head to a location Sylvoski apparently used to use as a safespot."
"You arrive Find a wooden door imbedded in the wall"
"Colt kicks down the door but finds that it was nothing more than a broom closet"
show om9:
 size(280,500)
 pos(250,100)
 anchor(0,0)
C "Damnit!"
C "I guess this was a waste of time after all, I’m sorry for-"
"The Ground Shakes as if an earthquake had occurred"
with hpunch
"You look behind to see a massive, hulking monster barreling towards you"
"Colt Pulls out a fire arm and quickly shoots the creature several times in it’s knees"
with vpunch
with hpunch
with vpunch
"The creature tumbles to the ground "
"He walks up to it and shoots the creature in the head, killing it"
with hpunch
C "Well I guess this wasn’t a waste of time after all"
y "Where’d you get that gun?"
C "I made it, my affinity is guns. Didn’t I tell you?"
y "No, you most certainly didn’t… mine’s paper by the way"
C "That sounds pretty usele-"
with hpunch
"Another Earthquake shakes the ground, This time even more intense than the one before"
"You look around to see two monsters, even bigger than the previous one moving towards you"
"Colt shoots the Creatures but the bullets seem to have little effect"
"You quickly manifest some paper and cover the creatures eyes with it"
"You both run"
hide om9
"You turn a corner and find that there is no exit"
"Colt uses a larger, one handed automatic rifle to shoot at the creatures but the bullets have little effect"
"An idea occurs to you"
y "Can you make an explosive weapon?"
C "Yes, but in close quarters like this the explosion would kill us both"
y "Do it"
"Colt hesitates for a second but then manifests an enormous, intricate looking rocket launcher"
C "Now what "
y "Fire the rocket at them on three"
y "1…"
y "2 …"
y "3!"
"Colt fires and as soon as it’s far enough away, you create a paper barrier, several meters thick between yourselves and the rocket"
play sound "launcher.mp3"
pause 5.5
play sound "rooffall.mp3"
with vpunch
with hpunch
scene white:
with Dissolve(1)
scene sewer1:
 size(1280,720)
with Dissolve(6)
"The entire tunnel shakes and the paper barrier you created is torn to shreds, the shock wave sends you flying back several meters"
"Colt helps you up"
y "Are they dead?"
C "See for yourself"
"You look around to see light pouring down the from above . The explosion seemed to have blown a hole straight through the top of the roof"
y "Why do you have the ability to make so many guns?"
show om1:
 anchor(0,0)
 pos(200,100)
 size(280,500)
C "I like guns. Do I need any other reason?"
"You raise you’re voice to argue but end up laughing instead"
C "What’s so funny? "
y "Nothing, it’s just. You remind me of someone"
C "Who?"
y "Myself"
hide om1
show om10:
 anchor(0,0)
 pos(200,100)
 size(280,500)
"Colt smiles"
"You and Colt go decide to head home for the day"
scene black:
with Dissolve(1)
C "I’ll contact the association and tell them about what happened. We may be asked to pay for the damages though… I hope you have a few million to spare"
scene canvas:
    size(1280,720)
with Dissolve(1.2)
stop music fadeout 2
queue music "music1.mp3"
"Back home, You think about todays events and decide to paint something"
"You decide to paint the rocket launcher Colt created"
"You Imagine the launcher as vividly as possible, "
"You imagine it’s shape in exact detail"
"You imagine the Intricate carvings etched into it"
"You even imagine the Way all of its components fit together to make it work"
"You paint until you can paint no more and are finally satisfied"
"You decide to go to sleep"
scene black:
with Dissolve(2.5)
$ coltp= True
jump anchor

label Artemisstory:
scene black
with Dissolve(1.5)
"You arrive at the location specified by Artemis and find yourself standing outside of a federal prison"
scene prison:
 size(1280,720)
with Dissolve(1)
stop music fadeout 2
queue music "warehouse.mp3"
"{i}This must be where they’re keeping Sylvoski{/i}"
"The Guard checks your creators license and allows you to go in"
"You find Artemis already waiting for you"
show art1:
 size(250,450)
 pos(200,150)
 anchor(0,0)
with Dissolve(1)
"She looks distressed"
y "What happened? "
A "I’m sorry, I thought we could talk to Sylvoski, see if he could lead us to a clue but…"
A "He’s really lost his mind, He couldn’t even talk or eat… He’s just sad to look at"
y "It’s okay"
A "Hey are you free? There’s something I need to talk to you about…"
scene street
with Dissolve(2)
stop music fadeout 1
queue music "westwrold.mp3"
"You and artemis decide to go for a walk"
show art1:
 size(250,450)
 pos(200,150)
 anchor(0,0)
A "My creation affinity is to Create living organic creatures… "
A "Sylvoski has similar powers," 
hide art1
show art3:
 size(290,450)
 pos(200,150)
 anchor(0,0)

extend " but he’s nothing like me…"
hide art3
show art1:
 size(250,450)
 pos(200,150)
 anchor(0,0)
A "He doesn’t care about his creations at all…"
A "Hey have what do you think about the way he worked?"
y "He killed people. of course I abhore him"
A "Yes.. But have you ever though about the creations he left behind?"
A "They’re all living creatures. They’re brain damaged and have never been conscious in their entire lives, But they’re still alive! Don’t you feel bad for them?"
"Artemis’ concern for these creatures startles you. Before this, you had never even given them much thought"
y "You’re right. It is sad"
A "Right?"
hide art1
show art3:
 size(290,450)
 pos(200,150)
 anchor(0,0)
A "Let me show you some thing"
"Artemis raises her hand and a small creature begins to manifest in the palm of her hand"
"The The creature completely manifests and you see that it is a small blue bird, A blu jay to be exact"
"The bird begins to move, leaps up into the air, and flyes off"
A "Making self sustaining creatures is difficult, making creatures that can actually survive in this world is even more difficult."
hide art3
show art2:
 size(290,450)
 pos(200,150)
 anchor(0,0)
A "I only make creatures that I know will survive,  As their creator, I owe them that much."
"You and Artemis decide to head home"
scene black
with Dissolve(1)
"Back home, you keep thinking thinking about the way the bird manifested in Artemis’ hand, How it flew off so majestically"
scene canvas:
    size(1280,720)
with Dissolve(1.2)
stop music fadeout 2
queue music "music1.mp3"
"You decide to paint the bird the moment it flew off"
"You Imagine the bird as vividly as possible, "
"You imagine it’s form"
"You imagine the Intricate carvings etched into it"
"You even imagine the Way all of its components fit together to make it work"
"You paint until you can paint no more and are finally satisfied"
"You decide to go to sleep"
scene black
with Dissolve(1)
$ artp=True
jump anchor

label Sylvoskibattle:
"The next day you decide to stay home and do some painting"
"Soon you receive several messages from the others requesting your urgent help."
"You decide to go meet them at a specified address"
stop music fadeout 2
scene black
with Dissolve(1.5)

"You go to the location the others told you about and find yourself at a deserted construction site"
queue music "warehouse.mp3"

scene site:
    size(1280,720)
with Dissolve(1)
"{i} Where are they? {/i}"
"Why hello there, darling"
show so1:
    size(400,625)
    pos(0.5,0.75)
    anchor(0.5,0.75)
"You turn around to see an effeminate looking man"
y "I’m sorry, do I know you?"
SM "No… But I know you mmmmmmmm"
y "Umm okay?"
SM "Jokes aside, I’m here to help you, Mr. [povname]"
SM "You seem to be investigating a rather peculiar case and I think my expertise will be useful to you."
y "How do you know I’m investigating this case?"
hide so1
show so2:
    size(400,625)
    pos(0.5,0.75)
    anchor(0.5,0.75)
SM "I happen to be a Creator myself, In the past, I worked for the Government and was a member of the human recreation project. I also have a personal interest in this case"

if biochemb==False:
    y "“the human recreation project” ? I’m sorry but I have no idea what that is."
    SM "It was a research project funded by the Government. Unique Creators from all over the country were country were gathered up"
    SM "they wanted to find a way to create vital human organs for medical purposes"
    SM "I was one of the Creators the government contacted"
    "{i} That sounds similar to Sylvoski’s powers… Could he be connected to this guy?{/i} "
if biochemb==True:
    "{i} I read about that, I don’t remember someone like this being mentioned in the list of founders though…{/i}"

y "I see. Well, we already have 4 creators on our team. And I don’t think we really need one more. Any information you may have would be greatly appreciated though"
"The man goes silent"
SM "This case……it means a lot to me. You see, my brother was one of the people who “died” at the hands of this… this monster…"
SM "My brother was the only family I had left, He was all I had… and he took him from me"
SM "Afterwords, I was unable to concentrate on my work and ended up losing my job."
SM "My family, my lively hood, my entire life was taken away from me."
SM "I ask you again."
SM "Please, let me join you"

if dramab==True:
    "listening to the mans story fills you with a desire to help him"
    y "I’m sorry, I had no idea…"
    y "I apologise for rudely denying you’re kindness earlier"
    y "Please, lend us your aid"
if not dramab:
    y "I’m sorry, but I don’t think we really need this many people working on this case."
    y "but if you want to help, we won’t deny you"

hide so2
show so1:
    size(400,625)
    pos(0.5,0.75)
    anchor(0.5,0.75)

"The mans mood lightens up"
SM "thank you"
"He walks toward you and shakes your hand"
y "The other people I’m working with will be here shortly, They all called me here so they must have found an important clue. It’ll be a good opportunity to introduce you to them Mr…"
stop music fadeout 2
y "I’m sorry, what was your name again?"
"The man grins"
play music "rock.mp3"
hide so1
show so3:
    size(400,625)
    pos(0.5,0.75)
    anchor(0.5,0.75)
SM "Sylvoski"
"Before You even have time to react, someone comes from behind and grabs your arms"
"You try to break free but find yourself unable to do anything"
"Sylvoski laughs maniacally as he walks toward you with a knife "
"You Manifest a ball of paper and jam it into his throat"
"You make the ball bigger and also cover his eyes and mouth"
"Sylvoski drops the knife and tries to pull the paper out of his mouth using his hands"
"You use a sheet of paper to pull the knife towards your hand"
"You grab the knife jam it into the skull of the creature holding you. It lets go of you and collapses to the ground. Dead"
"You walk towards Sylvoski, who is still struggling to remove the paper from his mouth. You keep recreating the paper as soon as he destroys it."
"You feel a powerful blow at the back of your head and begin to lose consciousness."
"The blow makes it impossible to focus on recreating the paper on sylvoski’s head"
stop music fadeout 2.5
scene black
with eye_shut
"As you’re consciousness slowly fades, You manage to get a glimpse of the creature that knocked you down. It looks almost human."
scene rotmanifest:
    size(1280,720)
with eye_open
scene black 
with eye_shut
pause 2
scene site2:
    size(1280,720)
with eye_open
play music "warehouse.mp3"
"Slowly, you begin to regain consciousness."
"You find one of your arms chained to an enormous steel pillar"
" {i} How long has it been? Am I still at the same place {/i}"
"A quick glance of the environment confirms that you are indeed still at the same construction site"
"{i} where are the others? Did he kill them? {/i}"
show so3:
    size(400,625)
    pos(0.5,0.75)
    anchor(0.5,0.75)
stop music fadeout 0.4
queue music "strongbattle.mp3"

"Sylvoski comes out from behind a pillar and slowly walks towards you."
scene rotmanifest:
    size(1280,720)
with Dissolve(0.7)
"Behind him, you see the same humanoid being that knocked you out, along with some other, similar looking creatures."

if fredp == True:
    "{i} These are the same things that attacked us! {/i}"
if fredp == False:
    "{i} What the hell are these things{/i}"

SV "I’m sorry, we didn’t have the time to take you somewhere more comfortable, We had to make due with chaining you up"
"You try to choke him using paper but one of the creatures immediately grabs you by the throat and pins you against the still pillar"
SV "You understand don’t you? Even if you did manage to kill me, my puppets would tear you apart"
y "What did you do to the others?"
SV "Don’t worry, I haven’t killed them yet. It would be too suspicious if all the people working on this investigation were to just up an die you know?"
scene site2:
    size(1280,720)
with Dissolve(0.6)    
show so1:
    size(400,625)
    pos(0.5,0.75)
    anchor(0.5,0.75)
SV "That’s why I’m going to make you kill them"
y "I would never do that"
y "You won’t need to actually kill {i}them{/i}. These will do just fine"
show gla1:
  size(280,500)
  pos(0,100)
  anchor(0,0)
show om1:
 size(280,500)
 pos(250,100)
 anchor(0,0)
show art1:
 size(250,450)
 pos(800,150)
 anchor(0,0)
"three more creatures emerge. Only these look exactly like Fred, Colt and Artemis"
"Your knees lose all strength. You would fall to the ground if the creature wasn’t holding you up"
y "….No"
SV "I could make a copy of you and make it kill them you know? I’m only doing this to make it more interesting"
y "Then do it. You’re going to kill me anyway right?"
y "I won’t give you the satisfaction of doing as you tell me to"
"Sylvoski sighs"
hide so1
show so2:
    size(400,700)
    pos(0.5,0.8)
    anchor(0.5,0.75)
SV "fine"
hide gla1
hide om1
hide art1
show om9:
 size(280,500)
 pos(250,100)
 anchor(0,0)
 linear 1.0 zoom 1.4
"One of the creatures walks towards you with the same knife as earlier"
"It holds the knife in front of your face for a moment before lifting up your shirt and placing the blade on your abdomen"

if fredp == False:
    "The creature plunges the blade into your stomach. "
    "You die"
    "Maybe you could have survived if you had gained some knowledge by meeting Fred after reading the biochemistry book"
    menu:
        "Go back to book readings":
            jump reset
        "Accept your fate":
            jump endcredits

label fredtrue:
"Seeing the creatures from up close reminds you of Fred"
"It reminds you of the painting you made the day you hung out with him"
"{i} That diamond he made was so beautiful {/i}"
"The creature plunges the blade into your stomach but stops"
"Something hard stops the blade from penetrating your skin"
"The creature raises the blade towards your head"
scene black
with Dissolve(0.7)
"You close your eyes and let out a scream"
stop music fadeout 2
y "NO!"
"the creature holding you lets go of its grip"
scene site2:
    size(1280,720)
show so2:
    size(400,700)
    pos(0.5,0.75)
    anchor(0.5,0.75)
    zoom 0.6
with eye_open

"You open your eyes to see both creatures impaled on gigantic crystals"
play music "musicg1.mp3"
"{i} Did I do this? {i}"
"You look at the chain on your hand and imagine a crystal cutting through it"
"A small crystal manifests and destroys the chain"
show so3:
    size(400,625)
    pos(0.5,0.75)
    anchor(0.5,0.75)
"Sylvoski and the other creatures seem too shocked to do anything"
"You Manifest more diamonds and launch them at the creatures surrounding you"
scene sitestairs:
    size(1280,720)
"Sylvoski dodges the crystals and runs towards a stairwell that leads up the second floor of the building being constructed"
"You run after him"
y "Hey, How did you escape from prison?"
scene black
with Dissolve(0.2)
"You manage to get to the same floor as sylvoski and find yourself unable to see anything"
SV "I didn’t need to."

if artp == False:
    "{i} What does that mean?{/i}"
    "Something cuts your arm and you try to grab it but fail"
    "Something crashes"
    "You feel it claw into your eyes and you fall on your back as it begins to eat away at your face"
    "You die an agonizing death"
    "Maybe you could have survived if you had gained some knowledge by meeting Artemis after reading the drama book"
    menu:
        "Go back to book readings":
            jump reset
        "Accept your fate":
            jump endcredits
        
"{i} Does that mean he was never caught?{/i}"
"{i} The thing Artemis saw must have been a fake{/i}"
"You remember what Artemis said. Creating self sustaining creations is extremely difficult."
"The fact that he has been creating so many of them all day must mean that he’s currently low on stamina"
"{i} Then this must be a trap. He lured me in here because he’s currently low on energy and can’t fight back directly{/i} "
"You retreat from the dark floor"
scene sitedark:
    size(1280,720)
with Dissolve(0.2)
"You are Back outside"
"{i} That floor doesn’t have any other exit, the only other way he’s getting out is by jumping 20 feet down{/i}"
"{i} I have to find a way to flush him out{/i}"
"You look around and notice a blow torch lying near by"
"You materialize several large sheets of paper on the floor surrounding building"
stop music fadeout 3
queue music "afetr.mp3"

menu: 
    "Use the blow torch and paper to smoke him out":
        scene siteout:
            size(1280,720)
        with Dissolve(0.2)
        play sound "firestart.mp3"
        "You use the blow torch to ignite the paper and the fire spreads quickly, almost the entire construction area is illuminated"
        "From within the fire you hear several deafening screams"
        "{i} I’m sorry Artemis, I had no choice{/i}"
        scene rotpose:
            size(1280,720)
        "Something jumps off the second floor of the building and falls flat on the round"
        "You approach it with caution"
        scene reneyeoff:
            size(1280,720)
        "The smoke from the fire makes it hard for you to breath and you use your scarf to avoid inhaling it"
        scene reneyeon:
            size(1280,720)
        "From the corner of your eye you notice a large winged creature gliding towards you"
        scene black
        show renactivate
        pause 4.9
        hide renactiavte
        scene renweapon:
            size(1280,720)
        "You quickly manifest a crystal and impale the creature before it even gets to you"
        "Upon closer inspection you notice that it is an owl"
        "You continue walking toward the fallen body."
        "Sylvoski’s eyes open and he tries to crawl away from you "

menu:
    "Destroy his legs with diamond":
        "You materialize a large diamond crystal and hurl it at Sylvoskis legs"
        "It completely crushes both his legs and he lets out a blood curdling scream"
    "Bind him with paper":
        "You create several large sheets of paper and bind both of his legs and arms"
        show rotweird:
            pos(0.5,0.5)
            anchor(0.5,0.5)
            size(1280,1100)
        "Sylvoski continues to crawl away like a caterpillar"
        "Two small humanoid beings manifest in front of him and one tries to carry him away while the other attacks you"
        "You impale the attacking one using a crystal"
        "The other creature tries to run away but you impale it’s legs and it ends up throwing Syvloski in close to the fire"
        "The paper ignites and Sylvoski is burned alive"
        "You look on in horror as Sylvoski struggles to stand"

scene rotfar:
    size(1280,720)
"Several more creatures materialize"
"Instead of attacking you the creatures remain motionless and their bodies explode into a pile of blood and guts that completely coats sylvoski."
"The pile of flesh begins to move upon Syloski’s body and he stops screaming "
"You look on in horror as Sylvoski gets to his feet Covered in guts"
"He is barely recognizable as human"
scene spower:
    size(1280,720)
"The blood and guts begin to disintegrate to reveal that Sylvoski now looks completely different"
y "So That’s why the police never found you."
scene sreveal:
    size(1280,720)
y "You changed your face and made a copy of yourself to throw off the police"
"Two large behemoths manifest "
scene monster1:
    size(1280,720)
if coltp == False:
    "You attempt to hit the creatures with diamonds but they do nothing more than slow them down as the creatures trample over you and kill you"
    "You Die"
    "Maybe you could have survived if you had gained some knowledge by meeting Colt after reading the adventure book"
    menu:
        "Go back to book readings":
            jump reset
        "Accept your fate":
            jump endcredits

"The monsters stampede towards you"
"{i} The same things that attacked us in the sewers {/i}"
"You remember the creatures not being able to deal with being blinded"
menu:
    "Use paper to cover their eyes":
        "The paper blinds them and you run perpendicular to where the creatures were going."
        "The creatures miss you entirely."
        "{i} I wonder if this’ll work{/i}"

"You imagine the same rocket launcher Colt made"
"The creatures pull of the paper and begin moving towards you"
"You imagine manifesting it"
"A large weight begins to weigh on you as the Rocket launcher begins to materialize"
"The creatures get closer"
scene rengun:
    size(1280,720)
"The rocket launcher completely manifests and you pull down on the trigger"
"The recoil from the launch pushes you off your feet "
"The missile obliterates the creatures"
scene sfallen:
    size(1280,720)
"Sylvoski looks disgruntled"
SV "You are the most annoying person I’ve ever killed"
"Dozens of the smaller humanoid creatures materialize"
"Materializing so many creations in such a small amount of time has left you exhausted"
scene rencrystal1:
    size(1280,720)
"You manifest a Diamond sword"
scene rencrystal2:
    size(1280,720)
"You slay the creatures one by one"
scene renslash:
    size(1280,720)
    
"As the last of the creatures dies you look around to see that Sylvoski is nowhere to be found"
scene sfear:
    size(1280,720)
"As the last of the creatures dies Sylvoski Looks furious"
scene monster2:
    size(1280,720)
"He manifests another large behemoth"
scene rengun:
    size(1280,720)
"You manifest another rocket launcher and fire it at one of the steel pillars supporting the building under construction"
"The building collapses and crushes both sylvoski and the monster"
"As the dust settles, you see the silhouette of a man emerge from the rubble. Covered in blood and guts "
scene spower:
    size(1280,720)
y "You are the most annoying person I’ve ever killed"
scene lotbirds:
    size(1280,720)
"You manifest several hundred small blue birds"
scene convergebirds:
    size(1280,720)
"The birds tear Sylvoski to shreds, killing him."
"You wait"
extend "You wait"
"{i} Is he really dead? {/i}"
stop music fadeout 7
scene renready:
    size(1280,720)
"The birds you manifested all sit still"
"You worry they may attack you."
"{i} Blue jays are typically herbivores. These ones are starving. But even so, what the hell did I make?{/i}"
"The birds all fly away"
"{i} I didn’t de materialize them. I don’t know if that’s a good thing though{/i}"
scene black
with Dissolve(4)

label epilogue:
play music "music1.mp3"
"2 months later"
scene bg4:
    size(1280,720)
with Dissolve(2)
"At an art exhibit, You stand in front of three paintings. "
"You feel anxious as more and more people come to admire your paintings"
"A large crowd gathers and you find yourself being approached by many different people"
"From the corner of your eye. You see them arrive"
show gla1:
  pos(100,100)
  size(280,500)
  anchor(0,0)
show om1:
 pos(500,100)
 size(280,500)
 anchor(0,0)
show art3:
 pos(700,150)
 size(250,450)
 anchor(0,0)

C "There you are!"
Fred "Hello"
A "Hi!"
y "You made it. I was beginning to think you weren’t going to show up"
Fred "We would never dream of it"
C "looks at the painting of the missile launcher"
C "Wow, You even got the etchings right"
Fred "And the way the light refracts off of this diamond is perfectly true to real life"
A "The bird looks so beautiful"
y "… I… never thanked you for saving me"
"The three of them look confused"
y "I mean it. I don’t think I would have survived the encounter with Sylvoski had I not met you"
A "Maybe… but, I don’t think I would have survived in that dungeon if you hadn’t come and found us. So let’s just call it even"
C "He only found us because of MY map"
Fred "In any case these are all beautiful paintings. I’m sure they’ll each sell for quite a large"
y "Oh these come as a set"
C "What are their names?"
A "I want to know too"
Fred "As do I"
y "Like I said they all come as a set. Collectively, they’re called “Inspiration”"

scene black
with Dissolve(1)
label endcredits:
"Thank You for playing"
"Credits: Abdullah Iqbal, Ajlal, Rayyan, Rizwan and ofcourse the internet"
stop music fadeout 2
pause 2
# This ends the game.

return
