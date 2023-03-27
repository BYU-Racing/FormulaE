from enum import Enum


# convert each sensor to a number
class Sensor(Enum):
    ACC1 = 0
    ACC2 = 1
    BRAKE = 2
    SWITCH = 3
    ANGLE = 4
    TIRE1 = 5
    TIRE2 = 6
    TIRE3 = 7
    TIRE4 = 8
    DAMP1 = 9
    DAMP2 = 10
    DAMP3 = 11
    DAMP4 = 12
    TEMP = 13
    LIGHT = 14


# convert an index to a sensor display name
sensors = {0: 'Accelerator 1',
           1: 'Accelerator 2',
           2: 'Brake Pressure',
           3: 'Power Switch',
           4: 'Steering Wheel Angle',
           5: 'Front Left Tire',
           6: 'Front Right Tire',
           7: 'Back Left Tire',
           8: 'Back Right Tire',
           9: 'Front Left Damper',
           10: 'Front Right Damper',
           11: 'Back Left Damper',
           12: 'Back Right Damper',
           13: 'Battery Temperature',
           14: 'Rain Light'}

# theme customization
themes = {"Arduino": {  # theme name
    "color": {  # color palette for graphs and backgrounds
        0: ["gray", "rgba(60,60,60,1)", "#3C3C3C"],  # assigned to overall background
        1: ["dark-gray", "rgba(40,40,40,1)", "#222222"],  # subplot background to differentiate from background
        2: ["green", "rgba(0,154,0,1)", "#009900"],  # Text color
        3: ["white", "rgba(255,2555,255,1)", "#FFFFFF"],  # Alternate text color, also just white
        4: ["black", "rgba(0,0,0,1)", "#000000"],  # Steering wheel color, also just black
    },
    "trace": {
        0: ["green", "rgba(0,154,0,1)", "#009900"],  # color for traces and bar charts
        1: ["red", "rgba(154,0,0,1)", "#990000"],
        2: ["green", "rgba(0,154,0,1)", "#009900"],  # color for traces and bar charts
        3: ["green", "rgba(0,154,0,1)", "#009900"],
        4: ["green", "rgba(0,154,0,1)", "#009900"],  # color for traces and bar charts
        5: ["green", "rgba(0,154,0,1)", "#009900"],
        6: ["green", "rgba(0,154,0,1)", "#009900"],  # color for traces and bar charts
    },
    "size": {
        "large": "22",  # large text like graph titles
        "medium": "16",  # medium text like like legends
        "small": "14",  # small text like graph ticks
    },
    "font": {
        "title": "Courier New",  # dashboard title
        "p": "Courier New",  # most text
        "graph": "Courier New",  # alt text font for some graphs
    }
},
    "Jarvis": {
        "color": {
            0: ["black", "rgba(0,0,0,1)", "#000000"],  # assigned to overall background
            1: ["dark-blue", "rgba(1, 2, 44,1)", "#01022C"],  # subplot background to differentiate from background
            2: ["neon_blue", "rgba(2, 255, 252, 1)", "#02fffc"],  # Text color
            3: ["white", "rgba(255,2555,255,1)", "#FFFFFF"],  # Alternate text color, also just white
            4: ["dark-gray", "rgba(216, 216, 216,1)", "#888888"],  # Steering wheel color, also just black
        },
        "trace": {
            0: ["neon_blue", "rgba(2, 255, 252, 1)", "#02fffc"],
            1: ["neon_yellow", "rgba(248, 255, 51, 1)", "#f8ff33"],
            2: ["neon_blue", "rgba(2, 255, 252, 1)", "#02fffc"],
            3: ["neon_blue", "rgba(2, 255, 252, 1)", "#02fffc"],
            4: ["neon_blue", "rgba(2, 255, 252, 1)", "#02fffc"],
            5: ["neon_blue", "rgba(2, 255, 252, 1)", "#02fffc"],
            6: ["white", "rgba(255,2555,255,1)", "#FFFFFF"],  # Alternate text color, also just white
        },
        "size": {
            "large": "24",
            "medium": "18",
            "small": "15",
        },
        "font": {
            "title": "Arial, sans-serif",
            "p": "Arial, sans-serif",
            "graph": "Arial, sans-serif",
        }
    },
    "Daylight": {
        "color": {
            0: ["white", "rgba(255,255,255,1)", "#FFFFFF"],  # assigned to overall background
            1: ["light-gray", "rgba(239, 239, 239,1)", "#EEEEEE"],
            # subplot background to differentiate from background
            2: ["black", "rgba(0,0,0,1)", "#000000"],  # Text color
            3: ["black", "rgba(0,0,0,1)", "#000000"],  # Alternate text color, also just white
            4: ["black", "rgba(0,0,0,1)", "#000000"],  # Steering wheel color, also just black
        },
        "trace": {
            0: ["black", "rgba(0,0,0,1)", "#000000"],
            1: ["black", "rgba(0,0,0,1)", "#000000"],
            2: ["black", "rgba(0,0,0,1)", "#000000"],
            3: ["black", "rgba(0,0,0,1)", "#000000"],
            4: ["black", "rgba(0,0,0,1)", "#000000"],
            5: ["black", "rgba(0,0,0,1)", "#000000"],
            6: ["black", "rgba(0,0,0,1)", "#000000"],  # Alternate text color, also just white
        },
        "size": {
            "large": "28",
            "medium": "22",
            "small": "18",
        },
        "font": {
            "title": "Arial, sans-serif",
            "p": "Arial, sans-serif",
            "graph": "Arial, sans-serif",
        }
    }
}

