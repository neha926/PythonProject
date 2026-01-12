import random
subjects=[
    "Mr. PM Modi",
    "Virat Kohli",
    "A Crocodile",
    "A Dinasours",
    "The Baffalo",
    "An Elephant",
    "The Girl",
    "The Boy"
]

actions=[
    "drinking",
    "falling in",
    "washing",
    "slaps",
    "eats",
    "fights",
    "showing",
    "dancing"
]


places=[
    "in Water",
    "on the Floor",
    "in plate",
    "in the Washroom",
    "on the Dining table",
    "in River",
    "in the Forest",
    "car",
    "Outside of the House"
]

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place=random.choice(places)


    headline=f"Breaking News: {subject} {action} {place}"
    print("\n"+ headline)

    u_input=input("Do you want to New Fake Generator :").strip().lower()
    if u_input=="no":
        break

print("\nThanks For Your Using Fake News Headline Generator📰. Have a fun Day🎉")