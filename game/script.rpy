# Under the Sakura - Expanded VN MVP

define t = Character("T", color="#b7ffcf")
define m = Character("Mika", color="#ffd3ea")
define r = Character("Ren", color="#c8d8ff")
define n = Character(None)

default trust_mika = 0
default focus_score = 0
default chapter_done = 0

image bg street_night = "images/bg/street_night.png"
image bg sakura_path = "images/bg/sakura_path.png"
image bg cafe_evening = "images/bg/cafe_evening.png"

image cg first_meet = "images/cg/cg_first_meet.png"
image cg choice_split = "images/cg/cg_choice_split.png"
image cg dawn_promise = "images/cg/cg_dawn_promise.png"

label start:
    scene bg street_night
    with fade

    n "Bangkok at dusk. Neon hum, bike engines, and unread messages."
    t "Another day gone."

    scene bg sakura_path
    with dissolve
    show cg first_meet
    with dissolve

    m "You're late."
    t "Mika...?"

    m "I waited anyway."

    menu:
        "How do you answer?"

        "Sit under the sakura and talk":
            $ trust_mika += 1
            $ focus_score += 1
            t "Then... let's not waste the night."
            m "Good answer."

        "Keep walking, pretend you're busy":
            $ trust_mika -= 1
            $ focus_score -= 1
            t "I can't stop. Deadlines."
            m "You always say that."

    show cg choice_split
    with dissolve

    jump chapter_1

label chapter_1:
    scene bg cafe_evening
    with dissolve

    r "You two look like unfinished code."
    t "Helpful."

    n "Ren slides a notebook across the table: 'Life System v0.1'."

    menu:
        "Pick your strategy for tomorrow"

        "Deep work blocks + agent planning":
            $ focus_score += 2
            t "I'll let agents handle planning, I'll do execution."

        "Just wing it and hope":
            $ focus_score -= 1
            t "I'll improvise. Maybe."

    $ chapter_done = 1
    jump ending_router

label ending_router:
    if trust_mika >= 1 and focus_score >= 2:
        jump ending_true
    elif trust_mika >= 0:
        jump ending_neutral
    else:
        jump ending_distant

label ending_true:
    scene bg sakura_path
    with fade
    show cg dawn_promise
    with dissolve

    m "Morning's close. Still here?"
    t "Yeah. This time, I stay."
    n "TRUE END (Prologue): Under the Sakura"
    return

label ending_neutral:
    scene bg street_night
    with fade
    n "You made progress, but not peace."
    n "NEUTRAL END (Prologue): Keep Walking"
    return

label ending_distant:
    scene bg street_night
    with fade
    n "Some roads are chosen by silence."
    n "DISTANT END (Prologue): Echoes"
    return
