# Under the Sakura - Narrative Build v0.4 (Act 2 expansion)

define t = Character("T", color="#b7ffcf")
define m = Character("Mika", color="#ffd3ea")
define r = Character("Ren", color="#c8d8ff")
define a = Character("Aoi", color="#ffe8b7")
define p = Character("Ploy", color="#ffd9b3")
define n = Character(None)

default trust_mika = 0
default discipline = 0
default clarity = 0
default chapter = 0

default journal = []
default side_aoi_seen = False
default side_rooftop_seen = False

default festival_fight = False

default route_focus = "none"

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
            $ route_focus = "balanced"
            t "Structure first, then I actually show up."
            call add_journal("Plan: focus blocks + one honest conversation.")

        "Raw grind, no social detours":
            $ discipline += 2
            $ trust_mika -= 1
            $ route_focus = "grind"
            t "No distractions. Just execution."
            call add_journal("Plan: pure grind, zero emotional overhead.")

        "Go with vibes and react live":
            $ clarity -= 1
            $ route_focus = "drift"
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

    # Stat-gated side scene 1
    if clarity >= 2:
        jump side_scene_aoi
    else:
        jump chapter_3

label side_scene_aoi:
    $ side_aoi_seen = True
    scene bg cafe_evening
    with dissolve

    a "People think burnout sounds loud. It doesn't."
    a "It sounds like 'I'm fine' sent at 2:47 AM."
    t "...you read people too well."
    a "No. I just listen when they joke."

    $ clarity += 1
    call add_journal("Aoi called out my fake 'I'm fine'.")

    jump chapter_3

label chapter_3:
    $ chapter = 3
    scene bg cafe_evening
    with dissolve

    p "Project demo moved up. Forty-eight hours."
    t "Of course it did."

    if discipline >= 3:
        n "Your checklist is clean. Your sleep schedule is not."
    else:
        n "Tabs multiply. So do excuses."

    menu:
        "Team-pressure response"
        "Delegate and stabilize the sprint":
            $ discipline += 1
            $ clarity += 1
            t "I'll split tasks and protect the core."
            call add_journal("I switched from panic to structure.")

        "Solo carry everything":
            $ discipline += 1
            $ trust_mika -= 1
            t "I can brute-force this."
            call add_journal("I chose hero mode over collaboration.")

        "Ask Mika for help":
            $ trust_mika += 1
            $ clarity += 1
            t "Can you review UX flow tonight?"
            m "If you actually listen, yes."
            call add_journal("I invited Mika into my work, not just my stress.")

    jump chapter_4

# --- ACT 2 START ---
label chapter_4:
    $ chapter = 4
    scene bg street_night
    with dissolve

    n "The city gets louder as your world gets narrower."
    n "Ren sends a voice note: 'Systems aren't cages. They're promises.'"

    menu:
        "Night routine choice"
        "Shut down at midnight and reset":
            $ discipline += 1
            $ clarity += 1
            call add_journal("I respected limits and slept.")

        "Push until sunrise":
            $ discipline += 1
            $ clarity -= 1
            call add_journal("I traded tomorrow's mind for tonight's output.")

        "Walk to sakura path first":
            $ trust_mika += 1
            $ clarity += 1
            call add_journal("I chose reflection before execution.")

    # Stat-gated side scene 2
    if trust_mika >= 2:
        jump side_scene_rooftop
    else:
        jump chapter_5

label side_scene_rooftop:
    $ side_rooftop_seen = True
    scene bg sakura_path
    with dissolve

    m "Do you know what hurts?"
    m "Not your schedule. Not your work."
    m "Being treated like a postponed tab."
    t "...I hear you."

    if clarity >= 2:
        t "And I'm done hiding behind productivity."
        $ trust_mika += 1
        $ clarity += 1
    else:
        t "I'm trying, but I don't know how yet."
        $ clarity += 1

    call add_journal("Rooftop talk: named the emotional debt.")
    jump chapter_5

label chapter_5:
    $ chapter = 5
    scene bg sakura_path
    with dissolve

    n "Sakura festival night. Lanterns, noise, and unresolved things."
    n "Mika finds you near the food stalls."

    menu:
        "Festival confrontation"
        "Be fully honest":
            $ trust_mika += 2
            $ clarity += 2
            $ festival_fight = False
            t "I keep choosing efficiency when I'm scared. I'm sorry."
            m "That's the first honest sentence all week."
            call add_journal("At the festival, I chose honesty over defense.")

        "Deflect with jokes":
            $ trust_mika -= 1
            $ clarity -= 1
            $ festival_fight = True
            t "Hey, at least the project isn't on fire."
            m "You do this every time."
            call add_journal("At the festival, I dodged the real conversation.")

        "Turn it into a logic debate":
            $ discipline += 1
            $ trust_mika -= 2
            $ festival_fight = True
            t "I'm optimizing for long-term stability."
            m "I'm not a KPI."
            call add_journal("At the festival, I reduced feelings to framework.")

    jump chapter_6

label chapter_6:
    $ chapter = 6
    scene bg cafe_evening
    with dissolve

    r "So. What's your system now?"

    if festival_fight:
        n "Your silence answers first."
    else:
        n "For once, your answer isn't a shortcut."

    menu:
        "Final alignment choice"
        "Rewrite my system around values":
            $ clarity += 2
            $ discipline += 1
            t "Output serves life. Not the other way around."
            call add_journal("I redesigned my system around values.")

        "Double down on performance":
            $ discipline += 2
            $ trust_mika -= 1
            t "Feelings can wait until after finals."
            call add_journal("I chose performance as my shield.")

        "Pause and choose presence":
            $ trust_mika += 1
            $ clarity += 1
            t "I need to stop treating people like future tasks."
            call add_journal("I chose presence over momentum.")

    jump ending_router

label ending_router:
    if trust_mika >= 4 and discipline >= 3 and clarity >= 4:
        jump ending_true_plus
    elif trust_mika >= 3 and discipline >= 2 and clarity >= 2:
        jump ending_true
    elif discipline >= 4 and trust_mika >= 0:
        jump ending_functional
    else:
        jump ending_distant

label ending_true_plus:
    scene bg sakura_path
    with fade
    show cg dawn_promise
    with dissolve

    n "Dawn. The city softens."
    m "You changed your workflow."
    t "No. I changed my priorities."
    m "...good. Then let's build something that includes us both."

    n "TRUE+ END: Bloom Protocol"
    jump epilogue_week_later

label ending_true:
    scene bg sakura_path
    with fade
    show cg dawn_promise
    with dissolve

    m "Morning already."
    t "Yeah. But for once, I'm not late to my own life."
    n "TRUE END: Under the Sakura"
    jump epilogue_week_later

label ending_functional:
    scene bg cafe_evening
    with fade
    n "You built a stable system. The heart is still buffering."
    n "FUNCTIONAL END: Clean Workflow, Messy Feelings"
    jump epilogue_week_later

label ending_distant:
    scene bg street_night
    with fade
    n "Deadlines met. Distance preserved."
    n "DISTANT END: Echoes on Asphalt"
    jump epilogue_week_later

label epilogue_week_later:
    scene bg street_night
    with dissolve
    n "One week later."

    if trust_mika >= 3:
        n "A message from Mika arrives: 'same bench tonight?'"
        t "I smile before I type."
    elif discipline >= 4:
        n "Your planner is immaculate. Your chest is quieter, not lighter."
    else:
        n "You keep walking the old route, hoping it feels different."

    if side_aoi_seen:
        n "Aoi leaves a sticky note on your cup: 'still listening.'"
    if side_rooftop_seen:
        n "You still remember the rooftop sentence: 'not a postponed tab.'"

    jump credits_stub

label credits_stub:
    n "Thanks for playing this build."
    n "Journal recap:"
    python:
        for i, entry in enumerate(journal, 1):
            renpy.say(n, f"{i}. {entry}")
    return
