import random


wild_magic_dict = {
    1 : "Roll on this table at the start of each of your turns for the next minute, ignoring this result on subsequent rolls.",
    2 : "For the next minute, you can see any invisible creature if you have line of sight to it.",
    3 : "A modron chosen and controlled by the DM appears in an unoccupied space within 5 feet of you, then disappears I minute later.",
    4 : "You cast Fireball as a 3rd-level spell centered on yourself.",
    5 : "You cast Magic Missile as a 5th-level spell.",
    6 : "Roll a d10. Your height changes by a number of inches equal to the roll. If the roll is odd, you shrink. If the roll is even, you grow.",
    7 : "You cast Confusion centered on yourself.",
    8 : "For the next minute, you regain 5 hit points at the start of each of your turns.",
    9 : "You grow a long beard made of feathers that remains until you sneeze, at which point the feathers explode out from your face. ",
    10 : "You cast Grease centered on yourself",
    11 : "Creatures have disadvantage on saving throws against the next spell you cast in the next minute that involves a saving throw.",
    12 : "Your skin turns a vibrant shade of blue. A Remove Curse spell can end this effect.",
    13 : "An eye appears on your forehead for the next minute. During that time, you have advantage on Wisdom (Perception) checks that rely on sight.",
    14 : "For the next minute, all your spells with a casting time of 1 action have a casting time of 1 bonus action.",
    15 : "You teleport up to 60 feet to an unoccupied space of your choice that you can see.",
    16 : "You are transported to the Astral Plane until the end of your next turn, after which time you return to the space you previously occupied or the nearest unoccupied space if that space is occupied.",
    17 : "Maximize the damage of the next damaging spell you cast within the next minute.",
    18 : "Roll a d10. Your age changes by a number of years equal to the roll. If the roll is odd, you get younger (minimum 1 year old). If the roll is even, you get older.",
    19 : "1d6 flumphs controlled by the DM appear in unoccupied spaces within 60 feet of you and are frightened of you. They vanish after 1 minute.",
    20 : "You regain 2d10 hit points.",
    21 : "You turn into a potted plant until the start of your next turn. While a plant, you are incapacitated and have vulnerability to all damage. If you drop to 0 hit points, your pot breaks, and your form reverts.",
    22 : "For the next minute, you can teleport up to 20 feet as a bonus action on each of your turns.",
    23 : "You cast Levitate on yourself.",
    24 : "A unicorn controlled by the DM appears in a space within 5 feet of you, then disappears 1 minute later.",
    25 : "You can't speak for the next minute. Whenever you try, pink bubbles float out of your mouth.",
    26 : "A spectral shield hovers near you for the next minute, granting you a +2 bonus to AC and immunity to Magic Missile.",
    27 : "You are immune to being intoxicated by alcohol for the next 5d6 days.",
    28 : "Your hair falls out but grows back within 24 hours",
    29 : "For the next minute, any flammable object you touch that isn't being worn or carried by another creature bursts into flame.",
    30 : "You regain your lowest-level expended spell slot.",
    31 : "For the next minute, you must shout when you speak.",
    32 : "You cast Fog Cloud centered on yourself.",
    33 : "Up to three creatures you choose within 30 feet of you take 4d10 lightning damage.",
    34 : "You are frightened by the nearest creature until the end of your next turn.",
    35 : "Each creature within 30 feet of you becomes invisible for the next minute. The invisibility ends on a creature when it attacks or casts a spell.",
    36 : "You gain resistance to all damage for the next minute.",
    37 : "A random creature within 60 feet of you becomes poisoned for 1d4 hours.",
    38 : "You glow with bright light in a 30-foot radius for the next minute. Any creature that ends its turn within 5 feet of you is blinded until the end of its next turn.",
    39 : "You cast Polymorph on yourself. If you fail the saving throw, you turn into a sheep for the spell's duration.",
    40 : "Illusory butterflies and flower petals flutter in the air within 10 feet of you for the next minute.",
    41 : "You can take one additional action immediately.",
    42 : "Each creature within 30 feet of you takes 1d10 necrotic damage. You regain hit points equal to the sum of the necrotic damage dealt.",
    43 : "You cast Mirror Image.",
    44 : "You cast Fly on a random creature within 60 feet of you.",
    45 : "You become invisible for the next minute. During that time, other creatures can't hear you. The invisibility ends if you attack or cast a spell.",
    46 : "If you die within the next minute, you immediately come back to life as if by the Reincarnate spell.",
    47 : "Your size increases by one size category for the next minute.",
    48 : "You and all creatures within 30 feet of you gain vulnerability to piercing damage for the next minute.",
    49 : "You are surrounded by faint, ethereal music for the next minute.",
    50 : "You regain all expended sorcery points.",
     }

trinket_dict_1 = {

1 : "A miniature, tame mimic.",
2 : "A carved marble elephant.",
3 : "A small round cactus with two eyes.",
4 : "A pocket book of dwarven poetry.",
5 : "A bronze box containing a tiny wooden owl.",
6 : "A solid blue metal sphere, one inch in diameter, with three parallel grooves around the circumference.",
7 : 'A pouch containing ten dried peas.',
8 : "A ceramic puzzle cube, with each face divided into four independently rotating squares enameled with astronomical signs.",
9 : "A square of bear-beetle leather, a creature unique to the misty woods of Cix.",
10 : "A sheet of vellum on which is crudely painted a herbal plant that you have yet to identify.",
11 : "A petrified frog.",
12 : "A twenty-sided die.",
13 : "A cut yellow chrysanthemum that never dies.",
14 : "A palm-sized iron cage: the door doesn't shut properly, as the tiny lock was broken from the inside.",
15 : "A blob of grey goo, slippy but safe to touch, kept in a ceramic pot.",
16 : "A dried sky lily, from the tip of the Godshead, an impossibly high mountain.",
17 : "A glowing blue-green line, six inches long, but with no discernible radius.",
18 : "A pretty conch shell.",
19 : "A scrap of paper on which is written, in Goblin, 'My dearest Bess,'.",
20 : "A keychain holding the head of a broken key.",
21 : "An echo pearl from the depths of the Vibration Lake.",
22 : "A toy crossbow.",
23 : "Lip balm",
24 : "A fossil of an extinct many-limbed critter.",
25 : "A brass prosthetic nose.",
26 : "A corkscrew.",
27 : "A dried poison gland of a jagged fish.",
28 : """A bronze gear on which is etched the word "Moon".""",
29 : "A map of a labyrinth, on which is penciled a line that starts at the centre but fails to connect to the entrance.",
30 : "A cube of ice that never melts",
31 : "A square of ironsilk sewn by the geargrubs of ancient Siclari.",
32 : "An ivory knitting needle.",
33 : "A peacock feather.",
34 : "A travel set of paints: someone has used up all the black.",
35 : "A wig of short platinum-blonde hair.",
36 : "A child's charm bracelet.",
37 : "A small bar of orichalcum, a metal only mentioned in ancient literature.",
38 : "A deed to a ruined tower.",
39 : "An invitation to a formal ball to be held in two years time.",
40 : "A smoking pipe carved from granite.",
41 : "A vial of scented oil.",
42 : "A preserved basilisk eye.",
43 : """A torn page on which is written "Death! / Plop. / The barges down in the river flop. / Flop, plop. / Above, beneath".""",
44 : "An intricate knot that nobody seems to know how to tie or untie – sailors believe it to be bad luck.",
45 : "Pages ripped out of an accounting journal of a local merchant.",
46 : "A ring with a poison reservoir for slipping into drinks and a tiny razor edge for cutting purse-strings.",
47 : "A glass globe of swirling green goop, no openings.",
48 : """"A bundle of ragged "treasure maps" drawn by inventive local children.""",
49 :" A sliver from a spear said to have pierced the armpit of a saint.",
50 : "A portfolio of pressed flowers.",
51 : "A small handbook of foreign coins, for travelers to identify denominations.",
52 : "A slightly out of date guidebook to foreign inns, taverns, and transportation.",
53 : "Six useless wooden tokens previously issued by a traitor-prince as currency.",
54 : "Two false fingernails painted with mysterious symbols.",
55 : "A set of cosmetic tools for cleaning the ears.",
56 : "A harmless stage dagger with retracting blade and blood-compartment.",
57 : "A floating glass orb that follows you around and makes whirring sounds.",
58 : "A goblin-made key that can lock any door, but unlock none.",
59 : "A translucent coin, minted in an unknown land.",
60 : "A bronze ring engraved with dark symbols that was supposedly buried with a legendary necromancer long ago.",
61 : "A ring carved with the unfinished insignia to a defunct secret organization.",
62 : "A thimble on which is an enamel painting of a turtle.",
63 : "A puzzle box holding 10 fingernail clippings.",
64 : "A pair of badly worn hairdressing scissors.",
65 : "A wax hand shaped to hold a large cup.",
66 : "A measuring tape, marked in ink at 23 inches.",
67 : "A seashell that is silent when held up to your ear.",
68 : "A coprolite.",
69 : "One piece of unknown paper currency with no obvious denomination.",
70 : "A bootlace entwined with gold thread.",
71 : "A dented sheriff's badge.",
72 : "A tiny bubble level that is calibrated incorrectly.",
73 : "A belt buckle.",
74 : "A letter of complaint to a toy shop owner.",
75 : "A decorative leather stud.",
76 : "A penny whistle that plays the same note no matter which holes are covered.",
77 : """A ticket admitting an adult and child onto a thing called a "semiotic tram".""",
78 : "A small glass vial holding three eyelashes.",
79 : "A tub of putty.",
80 : "A leather shoe made for a dog.",
81 : "A doll head with no hair and poorly applied makeup.",
82 : "A pewter fork.",
83 : "Illustrated instructions on how to make a paper hat.",
84 : "A clear glass dish with four round notches around the outside edge.",
85 : "A wire circlet that bestows upon its wearer perfect posture.",
86 : "A small hand-sized box covered with numbered buttons.",
87 : "An empty whiskey tumbler that causes any liquid poured into it to become bourbon.",
88 : "A book of flumph grammar.",
89 : "A hunk of metal which appears to be several gears jammed together at unnatural and impossible angles: attempting to turn it causes it to emit a horrible shrieking sound.",
90 : "A crystal prism that refracts shadow instead of light.",
91 : "A smokeless and odorless candle.",
92 : "A flat disc of layered metal and prismatic glass with a hole in the centre.",
93 : "An ornate pewter tankard made without a bottom.",
94 : "A wooden device designed to be gripped in two hands; two levers protrude from the top, and two triggers from the underside.",
95 : "Two perfectly identical pine cones.",
96 : "A sponge that can absorb 60 gallons of ale (and only ale).",
97 : "A pepper grinder containing an unlimited supply of pepper unless opened, at which point it becomes half empty.",
98 : "A poorly cultivated bonsai juniper in a glazed ceramic pot.",
99 : "An oval-shaped soapstone tablet inscribed with a short list of religious prohibitions.",
100 :"A wooden doll with a door that opens to reveal a slightly smaller, identical, doll; this one is empty, perhaps there are still smaller dolls that are missing?"
    
}

def main():
    decision_tree()


def wild_magic_roll():
    wild_keys = list(wild_magic_dict.keys())
    wild_values = list(wild_magic_dict.values())
    roll = random.randint(1, 100)
    print(f"You rolled a {roll}! ")
    if roll %2 == 0:
        half_roll = roll /2
    else:
        half_roll = round((roll /2) + 0.5)

    print(wild_values[wild_keys.index(half_roll)])
    print()
    main()

def trinket_roll():
    trinket_keys = list(trinket_dict_1.keys())
    trinket_values = list(trinket_dict_1.values())
    roll = random.randint(1, 100)
    print(f"You rolled {roll}!\n")
    print(trinket_values[trinket_keys.index(roll)])
    print()
    main()

def loot_roll():
    pass

def decision_tree():
    roll_options = ["Wild Magic", "Trinkets", "Loot"]
    print(f"Enter a number for the option you'd like to roll on.")

    for index, r in enumerate(roll_options, start=1):
        print(f"{index}: {r}")
    decision = input("Enter number here: ")
    print()
    int_decision = int(decision) - 1

    if int_decision < 0 or int_decision >= len(roll_options):
        print(f"I'm sorry, {int_decision + 1} is not a valid option.")
        return None
    if int_decision == 0:
        wild_magic_roll()
    elif int_decision == 1:
        trinket_roll()
    elif int_decision == 2:
        print(f"This feature is not available yet\n")
        main()
    else:
        pass



if __name__ == '__main__':
    main()

