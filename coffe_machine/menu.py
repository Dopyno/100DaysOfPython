MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 150,
    },
    "double": {
        "ingredients": {"water": 100, "coffee": 36},
        "cost": 300,
    },
    "chocolate": {
        "ingredients": {"water": 100, "milk": 100, "coffee": 15},
        "cost": 350,
    },
    "latte": {
        "ingredients": {"water": 50, "milk": 150, "coffee": 18},
        "cost": 400,
    },
}

extra_steps = {
    "double": ["Adding extra flavour!☕️"],
    "chocolate": [
        "Adding milk...🥛",
        "Adding marshmallows...",
        "Adding crushed chocolate...🍫",
    ],
    "latte": [
        "Adding steamed milk...🥛",
        "Adding cream..🥤",
    ],
}

actions = [
    "espresso",
    "double",
    "chocolate",
    "latte",
    "receipt",
    "exit",
    "report",
    "refill",
    "cash",
]

resources = {"water": 650, "milk": 500, "coffee": 200}
