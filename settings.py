import os

# The prefix that will be used to parse commands.
# It doesn't have to be a single character!
COMMAND_PREFIX = "v!"

# The bot token. Keep this secret!
BOT_TOKEN = "ODU3NTAxOTMwMjAzNjQzOTY0.YNQg5w.-s31HLSFQmt9btdV_al53NxpZ_Y"

# The now playing game. Set this to anything false-y ("", None) to disable it
NOW_PLAYING = COMMAND_PREFIX + "help"

# Base directory. Feel free to use it if you want.
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

DEV = False

ranks = {
    "Unrated": 0,
    "Iron 1": 50,
    "Iron 2": 150,
    "Iron 3": 250,
    "Bronze 1": 350,
    "Bronze 2": 450,
    "Bronze 3": 550,
    "Silver 1": 650,
    "Silver 2": 750,
    "Silver 3": 850,
    "Gold 1": 950,
    "Gold 2": 1050,
    "Gold 3": 1150,
    "Plat 1": 1250,
    "Plat 2": 1350,
    "Plat 3": 1450,
    "Diamond 1": 1550,
    "Diamond 2": 1650,
    "Diamond 3": 1750,
    "Immortal": 1850,
    "Radiant": 1950,
}

lobby = 865842885558403072
attacking = 865842949706481664
defending = 865842968803278868

agents = [
    "Astra",
    "Breach",
    "Brimstone",
    "Cypher",
    "Jett",
    "Kayo",
    "Killjoy",
    "Omen",
    "Phoenix",
    "Raze",
    "Reyna",
    "Sage",
    "Skye",
    "Sova",
    "Viper",
    "Yoru",
]

maps = ["Ascent‎", "Bind", "Haven", "Split", "Icebox", "Breeze"]

tourney_msg = 857871348906065920
giveaway_msg = 865841306952925184

starts_a = [
    [
        "Is this CS:GO???",
        "No one on your team is allowed to use any abilities for this round. You might as well just be playing CS:GO.",
    ],
    [
        "Shoutcasters",
        "Every player that is alive must narrate every action that they make. Do this as a shoutcaster would while spectating a professional match. Everyone that is alive must participate but stop if they die.",
    ],
    [
        "Gunswap",
        "Everytime you kill an enemy, you must pick up their gun and use it for your next kill. It doesn't matter what gun they had or how hard it will be to pick up, you cannot get a kill with the exact same gun more than once.",
    ],
    [
        "Trickshot",
        "Everytime you encounter an enemy, you must 360 before you are allowed to shoot them.",
    ],
    [
        "Is that a tornado?",
        "Everytime a teammate dies, they must constantly blow into their mic simulating a wind sound. They cannot stop until the round is over.",
    ],
    [
        "Wild west",
        "Your whole team must buy only Sheriffs. Armor is allowed, but no other guns. Extra points if you can use a western accent while making callouts",
    ],
    [
        "How do I stand up?",
        "Everyone on your team must play the entire round crouched, you can not standup at any time for any reason.",
    ],
    [
        "I think my W key is stuck",
        "you must hold the W key for the entire round and you are not allowed to walk",
    ],
    ["Evasive maneuvers", "You must jump every time you turn or peak a corner."],
    [
        "One mic",
        "Whoever is at the bottom of the scoreboard for your team is the only person allowed to use their mic this round. They must attempt to make callouts for all of their teammates. They clearly aren't getting kills anyway, so don't worry if this hinders their playing.",
    ],
    [
        "Glass cannon",
        "Each teammate must buy the most expensive weapon they can afford, but they are not allowed to have any armor.",
    ],
    [
        "Confusing callouts",
        "Play the round normally, however, you cannot use any normal callouts. Preferably use callouts that don't exist on this map, callouts from other games/maps, or just very broadly describe what you are trying to callout. Sounding confident is key for this strat.",
    ],
    [
        "Knives out",
        "You are only allowed to move if you are currently holding your knife. If you would like to shoot, you must stand stationary and cannot make any movement until you pull your knife back out.",
    ],
    [
        "Silent but deadly",
        "Everyone on your team must set their game's master volume to 0.",
    ],
    [
        "Protect the president",
        "Elect one teammate to be the 'President' and this player must carry the spike. The President is not allowed to have any guns or abilities, just armor. Your team must surround the president and protect him/her for the entire round.",
    ],
    [
        "Follow the leader",
        "Elect a teammate to be the leader, your whole team must move in a line everywhere that they travel following the leader. No one can stray away from the line.",
    ],
    [
        "Odin rush",
        "If your team has the funds to support this, every player must buy an Odin and rush the enemy team as a group, doesn't matter if you are attacking or defending. Buy an Ares if you can't afford an Odin.",
    ],
    [
        "Motivational speech",
        "Elect one player on your team to give a motivational speech at the start of the round. No one is allowed to leave spawn until the speech is finished. Once the speech is over, your whole team must rush one of the sites.",
    ],
    [
        "Sneaky-Beaky like",
        "Your team can only buy suppressed weapons and no one on the team is allowed to speak for the entire round.",
    ],
    [
        "The fakeout",
        "Each teammate must buy every ability that they possibly can. Rush towards one of the sites, and use all of your abilities as fast as you can on the site. Then quickly retreat and plant the spike at a different site.",
    ],
    [
        "Intimidation",
        "Each teammate must buy every ability that they possibly can. Rush mid and use every single ability before eventually taking B site.",
    ],
    [
        "Tourists",
        "Every teammate must visit each spikesite at least once before you are allowed to plant. Try to not kill the entire enemy team before planting.",
    ],
    [
        "Fnatic on Inferno",
        "Each teammate can only have a Classic and armor. They must crouch walk the entire way to A site going long. You may play normally if you get the bomb planted.",
    ],
    [
        "Doppelgänger",
        "If there is an enemy on the other team with the same agent as you, you must ignore all other enemies until you have killed your doppelgänger. If you don't have a doppelgänger, try to let your teammates kill theirs before killing anyone. (credit: rdee3)",
    ],
    [
        "X-ray vision",
        "You are only allowed to kill enemies through walls. You may peak them to see where they are, but to kill them, it must be through a wall. (credit: dehenergy)",
    ],
]

starts_d = [
    [
        "Is this CS:GO???",
        "No one on your team is allowed to use any abilities for this round. You might as well just be playing CS:GO.",
    ],
    [
        "Shoutcasters",
        "Every player that is alive must narrate every action that they make. Do this as a shoutcaster would while spectating a professional match. Everyone that is alive must participate but stop if they die.",
    ],
    [
        "Gunswap",
        "Everytime you kill an enemy, you must pick up their gun and use it for your next kill. It doesn't matter what gun they had or how hard it will be to pick up, you cannot get a kill with the exact same gun more than once.",
    ],
    [
        "Trickshot",
        "Everytime you encounter an enemy, you must 360 before you are allowed to shoot them.",
    ],
    [
        "Is that a tornado?",
        "Everytime a teammate dies, they must constantly blow into their mic simulating a wind sound. They cannot stop until the round is over.",
    ],
    [
        "Wild west",
        "Your whole team must buy only Sheriffs. Armor is allowed, but no other guns. Extra points if you can use a western accent while making callouts",
    ],
    [
        "How do I stand up?",
        "Everyone on your team must play the entire round crouched, you can not standup at any time for any reason.",
    ],
    [
        "I think my W key is stuck",
        "you must hold the W key for the entire round and you are not allowed to walk",
    ],
    ["Evasive maneuvers", "You must jump every time you turn or peak a corner."],
    [
        "One mic",
        "Whoever is at the bottom of the scoreboard for your team is the only person allowed to use their mic this round. They must attempt to make callouts for all of their teammates. They clearly aren't getting kills anyway, so don't worry if this hinders their playing.",
    ],
    [
        "Glass cannon",
        "Each teammate must buy the most expensive weapon they can afford, but they are not allowed to have any armor.",
    ],
    [
        "Confusing callouts",
        "Play the round normally, however, you cannot use any normal callouts. Preferably use callouts that don't exist on this map, callouts from other games/maps, or just very broadly describe what you are trying to callout. Sounding confident is key for this strat.",
    ],
    [
        "Knives out",
        "You are only allowed to move if you are currently holding your knife. If you would like to shoot, you must stand stationary and cannot make any movement until you pull your knife back out.",
    ],
    [
        "Silent but deadly",
        "Everyone on your team must set their game's master volume to 0.",
    ],
    [
        "Where are they coming from?",
        "Everyone on your team must put their headset on backwards for the entire round.",
    ],
    [
        "One at a time",
        "Only one player can leave spawn at a time, the rest of the team must do their best to hide in spawn.",
    ],
    [
        "Up close and personal",
        "Each member of the team can only buy a Shorty or Bucky. Everyone must hide on the bombsites holding close range angles.",
    ],
    [
        "Retakes are fun",
        "Your whole team must hide in spawn until the spike has been planted. You are then allowed to leave spawn and play normally.",
    ],
    [
        "Gambling",
        "Your whole team must go to one spikesite to defend. You've got a 1/3 chance to choose the right one, goodluck.",
    ],
    [
        "Doppelgänger",
        "If there is an enemy on the other team with the same agent as you, you must ignore all other enemies until you have killed your doppelgänger. If you don't have a doppelgänger, try to let your teammates kill theirs before killing anyone. (credit: rdee3)",
    ],
    [
        "X-ray vision",
        "You are only allowed to kill enemies through walls. You may peak them to see where they are, but to kill them, it must be through a wall. (credit: dehenergy)",
    ],
]