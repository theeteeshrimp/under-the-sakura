# Under the Sakura - starter script

define t = Character("T", color="#c8ffc8")
define m = Character("Mika", color="#ffd2e9")
define n = Character("Narrator", color="#cfd8ff")

default trust_mika = 0

label start:
    scene black
    with fade

    n "Bangkok evenings always hum the same—motorbikes, neon, and unfinished thoughts."
    n "But tonight, the wind smells like spring."

    scene bg street
    with dissolve

    t "I should go home..."
    t "...but the sakura path is faster."

    scene bg sakura_night
    with dissolve

    m "You’re late."
    t "Mika?"

    m "I was wondering if you’d still choose this road."

    menu:
        "How do you respond?"

        "Smile and sit with her":
            $ trust_mika += 1
            t "Couldn’t skip this place. Not tonight."
            m "Good. Then stay a little."

        "Keep your distance":
            $ trust_mika -= 1
            t "I’m just passing through."
            m "Mm. You always say that."

    if trust_mika > 0:
        n "Petals drift between you, and the silence feels warm."
        m "Then let me ask one thing... when morning comes, do we stay strangers?"
    else:
        n "The petals keep falling, but the air turns cold."
        m "If you keep running, one day even memory won’t catch you."

    n "To be continued in Chapter 1."

    return
