# Under the Sakura - Narrative Build v0.3

define t = Character("T", color="#b7ffcf")
define m = Character("Mika", color="#ffd3ea")
define r = Character("Ren", color="#c8d8ff")
define a = Character("Aoi", color="#ffe8b7")
define n = Character(None)

default trust_mika = 0
default discipline = 0
default clarity = 0
default chapter = 0

default journal = []

image bg street_night = "images/bg/street_night.png"
image bg sakura_path = "images/bg/sakura_path.png"
image bg cafe_evening = "images/bg/cafe_evening.png"

image cg first_meet = "images/cg/cg_first_meet.png"
image cg choice_split = "images/cg/cg_choice_split.png"
image cg dawn_promise = "images/cg/cg_dawn_promise.png"

label add_journal(entry):
    $ journal.append(entry)
    return

label start:
    $ chapter = 0
    scene bg street_night
    with fade

    n "Bangkok at dusk. Neon hum, bike engines, and unread messages."
    n "Your planner says you're on track. Your chest says otherwise."

    t "Just get through this week."

    scene bg sakura_path
    with dissolve
    show cg first_meet
    with dissolve

    m "You're late."
    t "Mika...?"
    m "I waited anyway."

    menu:
        "How do you answer?"
        "Sit with her under the trees":
            $ trust_mika += 1
            $ clarity += 1
            t "Then let me be on time now."
            m "...okay."
            call add_journal("I chose to stay instead of running.")

        "Keep moving, say you're busy":
            $ trust_mika -= 1
            $ discipline += 1
            t "I have to ship tomorrow."
            m "You always do."
            call add_journal("I prioritized output over conversation.")

    show cg choice_split
    with dissolve

    jump chapter_1

label chapter_1:
    $ chapter = 1
    scene bg cafe_evening
    with dissolve

    r "You two look like unresolved merge conflicts."
    t "Thanks, Ren. Very healing."

    r "Try this: three priorities, one non-negotiable human action. Daily."

    menu:
        "Pick your day strategy"

        "Deep work blocks + one honest conversation":
            $ discipline += 2
            $ clarity += 1
            t "Structure first, then I actually show up."
            call add_journal("Plan: focus blocks + one honest conversation.")

        "Raw grind, no social detours":
            $ discipline += 2
            $ trust_mika -= 1
            t "No distractions. Just execution."
            call add_journal("Plan: pure grind, zero emotional overhead.")

        "Go with vibes and react live":
            $ clarity -= 1
            t "I'll improvise."
            r "That is not a plan."
            call add_journal("Plan: improvisation (risky).")

    jump chapter_2

label chapter_2:
    $ chapter = 2
    scene bg street_night
    with dissolve

    n "A message from Mika sits unread for three hours."
    n "'Can we talk tonight?'"

    menu:
        "What do you do?"

        "Reply immediately and make time":
            $ trust_mika += 2
            $ clarity += 1
            t "Yes. Give me 20 minutes."
            call add_journal("I answered before it became avoidance.")

        "Send a short delay, but keep your promise":
            $ trust_mika += 1
            $ discipline += 1
            t "Finishing one task, then I'm all yours."
            call add_journal("I delayed honestly and followed through.")

        "Ignore for now":
            $ trust_mika -= 2
            $ clarity -= 1
            t "I'll deal with it later."
            call add_journal("I postponed something important again.")

    jump chapter_3

label chapter_3:
    $ chapter = 3
    scene bg cafe_evening
    with dissolve

    a "You can optimize a calendar. Not a silence."
    t "...that's annoyingly accurate."

    n "You review your week: output improved, but what about alignment?"

    menu:
        "Final pre-ending choice"

        "Own your pattern and apologize clearly":
            $ clarity += 2
            $ trust_mika += 1
            t "No excuses. I was avoidant. I want to do better."
            call add_journal("I named the pattern directly.")

        "Defend yourself with results":
            $ discipline += 1
            $ trust_mika -= 1
            t "I did all this for our future."
            call add_journal("I used results to dodge vulnerability.")

        "Stay quiet and hope time fixes it":
            $ trust_mika -= 2
            $ clarity -= 1
            call add_journal("I chose silence.")

    jump ending_router

label ending_router:
    if trust_mika >= 3 and discipline >= 2 and clarity >= 2:
        jump ending_true
    elif discipline >= 3 and trust_mika >= 0:
        jump ending_functional
    else:
        jump ending_distant

label ending_true:
    scene bg sakura_path
    with fade
    show cg dawn_promise
    with dissolve

    m "Morning already."
    t "Yeah. But for once, I'm not late to my own life."
    n "TRUE END: Under the Sakura"
    jump credits_stub

label ending_functional:
    scene bg cafe_evening
    with fade
    n "You built a stable system. The heart is still buffering."
    n "FUNCTIONAL END: Clean Workflow, Messy Feelings"
    jump credits_stub

label ending_distant:
    scene bg street_night
    with fade
    n "Deadlines met. Distance preserved."
    n "DISTANT END: Echoes on Asphalt"
    jump credits_stub

label credits_stub:
    n "Thanks for playing this build."
    n "Journal recap:"
    python:
        for i, entry in enumerate(journal, 1):
            renpy.say(n, f"{i}. {entry}")
    return
