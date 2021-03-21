const trinketArray = ["A picture you drew as a child of your imaginary friend", "A lock that opens when blood is dripped in its keyhole", "Clothes stolen from a scarecrow", "A spinning top carved with four faces: happy, sad, wrathful, and dead", "The necklace of a sibling who died on the day you were born", "A wig from someone executed by beheading", "The unopened letter to you from your dying father", "A pocket watch that runs backward for an hour every midnight", "A winter coat stolen from a dying soldier", "A bottle of invisible ink that can only be read at sunset", "A wineskin that refills when interred with a dead person for a night", "A set of silverware used by a king for his last meal", "A spyglass that always shows the world suffering a terrible storm", "A cameo with the profile’s face scratched away", "A lantern with a black candle that never runs out and that burns with green flame", "A teacup from a child’s tea set, stained with blood", "A little black book that records your dreams, and yours alone, when you sleep", "A necklace formed of the interlinked holy symbols of a dozen deities", "A hangman’s noose that feels heavier than it should", "A birdcage into which small birds fly but once inside never eat or leave", "A lepidopterist’s box filled dead moths with skull-like patterns on their wings", "A jar of pickled ghouls’ tongues", "The wooden hand of a notorious pirate", "An urn with the ashes of a dead relative", "A hand mirror backed with a bronze depiction of a medusa", "Pallid leather gloves crafted with ivory fingernails", "Dice made from the knuckles of a notorious charlatan", "A ring of keys for forgotten locks", "Nails from the coffin of a murderer", "A key to the family crypt", "A bouquet of funerary flowers that always looks and smells fresh", "A switch used to discipline you as a child", "A music box that plays by itself whenever someone holding it dances", "A walking cane with an iron ferrule that strikes sparks on stone", "A flag from a ship lost at sea", "Porcelain doll’s head that always seems to be looking at you", "A wolf’s head wrought in silver that is also a whistle", "A small mirror that shows a much older version of the viewer", "A small, worn book of children’s nursery rhymes", "A mummified raven claw", "A broken pendent of a silver dragon that’s always cold to the touch", "A small locked box that quietly hums a lovely melody at night but you always forget it in the morning", "An inkwell that makes one a little nauseous when staring at it", "An old little doll made from a dark, dense wood and missing a hand and a foot", "A black executioner’s hood", "A pouch made of flesh, with a sinew drawstring", "A tiny spool of black thread that never runs out", "A tiny clockwork figurine of a dancer that’s missing a gear and doesn’t work", "A black wooden pipe that creates puffs of smoke that look like skulls", "A vial of perfume, the scent of which only certain creatures can detect"]

window.addEventListener("DOMContentLoaded", domLoaded);

function domLoaded() {
    let distance = document.querySelector('#distance')
    let waitTime = document.querySelector('#waitTime')
    distance.addEventListener("input", () => waitTime.value = "")
    waitTime.addEventListener("input", () => distance.value = "")
}

const oldRoll = function(rangeArray = [1, 20]) {
    let min = rangeArray[0]
    let max = rangeArray[1]
    let range = max - min
    return Math.floor(math.random() * range) + min
}

const roll = function(diceString = '1d20') {
    let bonus = 0
    let numberOfDice
    let diceSize
    if (!(diceString.includes('d'))) {
        throw new TypeError("Dice string must include 'd'")
    }
    let splitDice = diceString.split('d')
    if (splitDice[1].includes('+')) {
        let secondSplit = splitDice[1].split('+')
        splitDice = [splitDice[0], ...secondSplit]
        numberOfDice = parseFloat(splitDice[0])
        diceSize = parseFloat(splitDice[1])
        bonus = parseFloat(splitDice[2])
    }
    else if (splitDice[1].includes('-')) {
        let secondSplit = splitDice[1].split('-')
        splitDice = [splitDice[0], ...secondSplit]
        numberOfDice = parseFloat(splitDice[0])
        diceSize = parseFloat(splitDice[1])
        bonus = parseFloat(splitDice[2]) * -1
    }
    else {
        numberOfDice = parseFloat(splitDice[0])
        diceSize = parseFloat(splitDice[1])
    }
    let sum = 0
    for (let i = 0;i < numberOfDice;i++) {
        sum = Math.floor(Math.random() * diceSize) + 1
    }
    return sum + bonus
}

const advantage = function(mod = 0) {
    let formString = '1d20'
    if (mod >= 0) {
        formString += '+' + mod
    }
    else {
        formString += mod
    }
    firstRoll = roll(formString)
    secondRoll = roll(formString)
    return Math.max(firstRoll, secondRoll)
}

const defaultRules = {
    paceRules:{
        fast: {
            milesPerHour: 4,
            milesPerDay: 30,
            bonus: "-5 to Perception and Survival checks"
        },
        normal: {
            milesPerHour: 3,
            milesPerDay: 24,
            bonus: "-"
        },
        slow: {
            milesPerHour: 2,
            milesPerDay: 18,
            bonus: "Can use stealth"
        }
    },
    guideRules: {
        noGuideRange: '1d20',
        guideRange: '1d12'
    },
    encounterChances: {
        roadChance: 18,
        wildChance: 15
    },
    maxEncounters: 2,
}

const repeatEncounters = {
    bloodPine: {
        name: "Blood Pine",
        travelOnly: true,
        perception: 13,
        description: "One of the nearby pine trees shudders suddenly. You notice dark red sap dripping from its bark and needles, and a root covered in spikes slithers through the brush towards you.",
        rules: "",
        get init() {
            this.snippet = `a ${this.name}`
        }
    },
    huntingTrap: {
        name: "Hunting Trap",
        travelOnly: true,
        perception: 15,
        description: "You spot a wolf trap, its steel jaws caked with rust. Someone has carefully hidden the trap under a thin layer of pine needles and detritus.",
        get init() {
            this.rules = `Barovian hunters and trappers set these traps hoping to thin out the wolf population, but Strahd’s wolves are too clever to be caught in them. If none of the characters spot the hidden trap, one random party member steps on it.<br><strong>Wolf Trap:</strong> A creature that steps on the plate must make a DC 13 Dexterity saving throw or take ${roll('1d4')} (1d4) piercing damage and stop moving. Until the creature breaks free of the trap, its movement is limited by the 3 foot length of chain. A creature can use its action to make a DC 13 Strength check, freeing itself or another creature within its reach on a success. Each failed check deals 1 piercing damage to the trapped creature.`
            this.snippet = `a ${this.name}`
        }
    },
    grave: {
        name: "Grave",
        travelOnly: true,
        get init() {
            if (Math.random() >= .25) {
                let graveAppearance
                if (Math.random() > .5) {
                    graveAppearance = "an elongated earthen mound"
                }
                else {
                    graveAppearance = "a rocky cairn"
                }
                this.description = `You stumble upon an old grave. It appears intact, ${graveAppearance}.`
                this.rules = "Characters who dig up the grave find the skeletal remains of a human clad in rusted chain mail (a soldier). Among the bones lie corroded weapons."
            }
            else {
                this.description = "You stumble upon an old grave. It's clearly been violated. All that's left is a shallow, mud-filled hole with dirt and rocks strewn around it and a few scattered bones within."
                this.rules = ""
            }
            this.snippet = `a ${this.name}`
        }
    },
    trinket: {
        name: "Trinket",
        description: "You find something on the ground.",
        travelOnly: true,
        get init() {
            let trinket = trinketArray[Math.floor(Math.random() * trinketArray.length)]
            this.rules = `A random character finds a lost trinket: ${trinket}`
            this.snippet = `${this.name}: ${trinket}`
        }
    },
    hiddenBundle: {
        name: "Hidden Bundle",
        travelOnly: true,
        perception: 12,
        get init() {
            let location
            switch(roll('1d3')) {
                case 1:
                    location = "hidden in the underbrush"
                    break
                case 2:
                    location = "stuffed inside a hollow log"
                    break
                case 3:
                    location = "nestled in the boughs of a tree"
            }
            this.description = `You find a leather-wrapped bundle ${location}. The bundle contains one set of common clothes sized for a human adult.`
            let owner
            if (Math.random < .5) {
                owner = "werewolf"
            }
            else {
                owner = "wereraven"
            }
            this.rules = `The clothes have a drab Barovian style to them. They belong to a ${owner} in the area.`
            this.snippet = `a ${this.name}`
        }
    },
    corpse: {
        name: "Corpse",
        description: "You find a corpse.",
        travelOnly: true,
        get init() {
            switch(roll('1d6')) {
                case 1:
                case 2:
                    this.rules = "The corpse belongs to a wolf killed by spears and crossbow bolts."
                    break
                case 3:
                case 4:
                case 5:
                    switch(roll('1d4')) {
                        case 1:
                            person = "man"
                            break
                        case 2:
                            person = "woman"
                            break
                        case 3:
                            person = "boy"
                            break
                        case 4:
                            person = "girl"
                            break
                    }
                    this.rules = `The corpse belongs to a Barovian ${person} who was clearly torn to pieces by dire wolves. If the party is accompanied by Barovian scouts, the scouts recognize the corpse as the person they were searching for.`
                    break
                case 6:
                    this.rules = "The corpse looks like one of the characters (determined randomly) but has been stripped of armor, weapons, and valuables. If moved, its flesh melts away until only the skeleton remains."
                    break
            }
            this.snippet = `a ${this.name}`
        }
    },
    skeletalRider: {
        name: "Skeletal Rider",
        description: "Through the mist comes a skeletal warhorse and rider, both clad in ruined chainmail. The skeletal rider holds up a rusted lantern that sheds no light.",
        rules: "The human skeleton and warhorse skeleton are all that remain of a rider and mount, both of whom perished trying to escape through the fog that surrounds Barovia. They are doomed to ride through the valley in search of another way out, without hope of salvation. The skeletons ignore the characters unless attacked.<br>If both the rider and its mount are destroyed, this encounter can’t occur again. The destruction of one skeleton doesn’t prevent future encounters with the other.",
        get init() {
            this.snippet = `the ${this.name}`
        }
    },
    direWolves: {
        name: "Dire Wolves",
        range: '1d6',
        description: "A snarling wolf the size of a grizzly bear steps out of the fog.",
        rules: "The area is lightly obscured by fog. If more than one dire wolf is present, the others aren’t far behind and can be seen as dark shadows in the fog. The dire wolves of Barovia are cruel, overgrown wolves and Strahd’s loyal servants. They can’t be charmed or frightened.",
        get init() {
            this.number = roll(this.range)
            this.snippet = `${this.name} ${this.name}`
        }
    },
    wolves: {
        name: "Wolves",
        range: '3d6',
        description: "This land is home to many wolves, their howls at the moment too close for comfort.",
        get init() {
            this.rules = `Characters have a few minutes to steel themselves before these wolves attack. They heed the will of Strahd and can’t be charmed or frightened. If the characters prepare accordingly, they may be able to hide from the wolves. (DC ${advantage(3)})`
            this.number = roll(this.range)
            this.snippet = `${this.number} ${this.name}`
        }
    },
    berserkers: {
        name: "Berserkers",
        range: '1d4',
        description: "You startle a wild-looking figure caked in gray mud and clutching a crude stone axe. Whether it’s a man or a woman, you can’t tell.",
        rules: "These wild mountain folk are covered head to toe in thick gray mud, which makes them hard to see in the fog and well hidden in the mountains they call home. While so camouflaged, they have advantage on Dexterity (Stealth) checks made to hide.<br>The berserkers shun civilized folk. They try to remain hidden and withdraw if they are spotted, attacking only if trapped or threatened.",
        get init() {
            let stealthBonus = 1
            this.perception = advantage(stealthBonus)
            this.number = roll(this.range)
            this.snippet = `${this.number} ${this.name}`
        }
    },
    twigBlights: {
        name: "Twig Blights",
        range: '2d6',
        description: "A gaunt figure with wild hair and bare feet bounds toward you on all fours, wearing a tattered gown of stitched animal skins. You can’t tell whether it’s a man or a woman. It stops, sniffs the air, and laughs like a lunatic. The ground nearby is crawling with tiny twig monsters.",
        rules: "The Barovian wilderness is home to druids who worship Strahd because of his ability to control the weather and the beasts of Barovia. The druids are savage and violent, and each controls a host of twig blights, which fights until destroyed. If all the twig blights are destroyed or the druid loses more than half of its hit points, the druid flees, heading toward Yester Hill.",
        get init() {
            this.number = roll(this.range)
            this.snippet = `Druid + ${this.number} ${this.name}`
        }
    },
    needleBlights: {
        name: "Needle Blights",
        range: '2d4',
        description: "Hunched figures lurch through the mist, their gaunt bodies covered in needles.",
        get init() {
            this.perception = roll('1d20+1')
            let enemyPercep = -1
            this.number = roll(this.range)
            this.rules = `The woods crawl with needle blights that serve the evil druids of Barovia. If the characters are moving quietly and not carrying light sources, they can try to hide from these blights. (DC ${roll('1d20' + -enemyPercep)})`
            this.snippet = `${this.number} ${this.name}`
        }
    },
    scarecrows: {
        name: "Scarecrows",
        range: '1d6',
        description: "A scarecrow lurches into view. Its sackcloth eyes and rictus are ripe with malevolence, and its gut is stuffed with dead ravens. It has long, rusted knives for claws.",
        rules: "If more than one scarecrow is present, the others are close by. If none of the characters perceived them, the scarecrows catch the party by surprise.<br>Baba Lysaga crafted these scarecrows to hunt down and kill ravens and were­ravens. The scarecrows are imbued with evil spirits and delight in murdering anyone they encounter.",
        get init() {
            this.number = roll(this.range)
            this.perception = roll('1d20+1')
            this.snippet = `${this.number} ${this.name}`
        }
    },
    revenant: {
        name: "Revenant",
        description: "A figure walks alone with the stride and bearing of one who knows no fear. Clad in rusty armor, it clutches a gleaming longsword in its pale hand and looks ready for a fight.",
        rules: "From a distance, the revenant looks like a zombie and might be mistaken for such. A character within 30 feet of the revenant who succeeds on a DC 10 Wisdom (Insight) check can see the intelligence and hate in its sunken eyes. The revenant is clad in tattered chain mail that affords the same protection as leather armor.<br>The revenant was a knight of the Order of the Silver Dragon, which was annihilated defending the valley against Strahd’s armies more than four centuries ago. The revenant no longer remembers its name and wanders the land in search of Strahd’s wolves and other minions, slaying them on sight. If the characters attack it, the revenant assumes they are in league with Strahd and fights them until destroyed.<br>If the characters present themselves as enemies of Strahd, the revenant urges them to travel to Argynvostholt and convince Vladimir Horngaard, the leader of the Order of the Silver Dragon, to help them. The revenant would like nothing more than to kill Strahd, but it will not venture to Castle Ravenloft unless it receives orders to do so from Vladimir. If the characters ask the revenant to lead them to Horngaard in Argynvostholt, it does so while avoiding contact with Barovian settlements.",
        get init() {
            this.snippet = `a ${this.name}`
        }
    }
}

const dayEncounters = {
    1: repeatEncounters.bloodPine,
    2: {
        name: "Barovian Commoners",
        range: '3d6',
        description: "The sound of snapping twigs draws your attention to several dark shapes in the fog. They carry torches and pitchforks.",
        rules: "If the characters are moving quietly and not carrying light sources, they can try to hide from these Barovians, who carry pitchforks (+2 to hit) instead of clubs, dealing 3 (1d6) piercing damage on a hit.<br>Barovian commoners rarely leave their settlements. This group might be a family looking for a safer place to live, or an angry mob searching for the characters or heading toward Castle Ravenloft to confront Strahd.",
        get init() {
            this.number = roll(this.range)
            this.snippet = `${this.number} ${this.name}`
        }
    },
    3: {
        name: "Barovian Scouts",
        range: '1d6',
        description: "You see a dark figure crouched low and perfectly still, aiming a crossbow in your direction.",
        rules: "If more than one scout is present, the others are spread out over a 100-foot-square area.<br>These scouts are Barovian hunters or trappers searching for a missing villager or townsperson. Once they realize the characters aren’t out to kill them, they lower their weapons and request help in finding their missing person. If the characters decline, the scouts point them in the direction of the nearest settlement and depart without so much as a farewell. They wield light crossbows (+4 to hit, range 80/320 ft.) instead of longbows, dealing 6 (1d8 + 2) piercing damage on a hit.",
        get init() {
            let stealthBonus = 6
            this.perception = roll(`1d20+` + stealthBonus)
            this.number = roll(this.range)
            this.snippet = `${this.number} ${this.name}`
        }
    },
    4: repeatEncounters.huntingTrap,
    5: repeatEncounters.grave,
    6: {
        name: "False Trail",
        description: "You discover a foot trail that cuts through the wilderness.",
        travelOnly: true,
        perception: 13,
        get init() {
            this.rules = `Evil druids left this trail. Following it in either direction leads to a spiked pit. A thin tarp made of twigs and pine needles conceals the pit, the bottom of which is lined with sharpened wooden stakes.<br><strong>Spiked Pit:</strong> This hidden pit trap is 3 ft across and 10 ft deep, and it has sharpened wooden spikes at the bottom. A creature falling into the pit takes ${roll('2d10')} (2d10) piercing damage from the spikes, ${roll('3d8')} (3d8) poison damage from the venom on the spikes, and ${roll('1d6')} (1d6) bludgeoning damage from the fall.`
            this.snippet = `a ${this.name}`
        }
    },
    7: {
        name: "Vistani Bandits",
        range: '1d4+1',
        description: "You catch a whiff of pipe smoke in the cold air and hear laughter through the fog.",
        get init() {
            this.number = roll(this.range)
            this.rules = `These Vistani servants of Strahd march through the Barovian wilderness, laughing and telling ghost stories. They are searching for graves to plunder or hunting small game. For a price of 100 gp, they offer to serve as guides. As long as these Vistani are with the party, roll a d12 instead of a d12 + d8 when determining random encounters in the wilderness. In addition, wolves and dire wolves don’t threaten the characters as long as the Vistani are traveling with them and aren’t their prisoners.<br><strong>Treasure:</strong> One Vistani bandit carries a pouch that holds ${roll('2d4')} small gemstones (worth 50 gp each).`
            this.snippet = `${this.number} ${this.name}`
        }
    },
    8: repeatEncounters.skeletalRider,
    9: repeatEncounters.trinket,
    10: repeatEncounters.hiddenBundle,
    11: {
        name: "Ravens",
        range: '1d4',
        get init() {
            if (Math.random() < .5) {
                this.description = "Your presence in this dreary land has not gone unnoticed. A raven follows you for several minutes while keeping a respectful distance."
                this.rules = "The raven doesn’t caw or try to communicate with the characters. If they leave it alone, read:<aside class=readAloud>More ravens begin to take an interest in you. Before long, their numbers swell, and soon hundreds of them are watching you.</aside>The ravens fly away if attacked. If they are left alone, they watch over the party, remaining with the characters until they reach Castle Ravenloft or a settlement. If the characters have a random encounter with hostile creatures, the raven swarms aid the characters by attacking and distracting their enemies."
                this.number = roll(this.range)
                this.snippet = `${this.number} Swarms of Ravens`
            }
            else {
                let stealthBonus = 2
                this.perception = roll("1d20+" + stealthBonus)
                this.description = "Through the mist, you see a black bird circling overhead. When it feels your eyes upon it, the raven flies away, but it’s back before long, keeping its distance."
                this.rules = `This wereraven in raven form watches the characters from a distance.<br>The wereraven belongs to a secret order called the Keepers of the Feather. If the characters don’t spot it, the wereraven shadows them for ${roll('1d4')} hours. At the end of that time, or anytime sooner if the characters attack it, the creature flies home to report what it has seen.<br>If the party has a second random encounter with a wereraven, this one presents itself to the characters as an ally and requests that they travel to the Blue Water Inn in Vallaki to meet “some new friends.” It then flies off in the direction of the town.`
                this.snippet = "a Wereraven"
            }
        }
    },
    12: repeatEncounters.direWolves,
    13: repeatEncounters.wolves,
    14: repeatEncounters.berserkers, 
    15: repeatEncounters.corpse,
    16: {
        name: "Werewolves (human form)",
        range: '1d6',
        description: "A deep voice calls out, “Who goes there?” Through the chill mist you see a large man in drab clothing wearing a tattered gray cloak. He has shaggy, black hair and thick muttonchops. He leans heavily on a spear and has a small bundle of animal pelts slung over his shoulder.",
        rules: "Werewolves in human form pretend to be trappers. If more than one is present, the others are within whistling distance.<br>They try to befriend the characters to see if they are carrying silvered weapons. If the characters appear to have no such weapons, the werewolves assume hybrid form and attack. Otherwise, they part company with the characters and leave well enough alone.",
        get init() {
            this.number = roll(this.range)
            this.snippet = `${this.number} ${this.name}`
        }
    },
    17: repeatEncounters.twigBlights,
    18: repeatEncounters.needleBlights,
    19: repeatEncounters.scarecrows,
    20: repeatEncounters.revenant
}

const nightEncounters = {
    1: repeatEncounters.bloodPine,
    2: {
        name: "Ghost",
        description: "A baleful apparition appears before you, its hollow eyes dark with anger.",
        get init() {
            let person
            if (Math.random < .5) {
                person = "man"
            }
            else {
                person = "woman"
            }
            this.rules = `Many ghosts haunt this land. This particular ghost is all that remains of a ${person} drained of life by Strahd. It appears and hisses, “No one will ever know you died here.” It then attacks. If the ghost succeeds in possessing a character, it leads its host to the gates of Ravenloft and hurls the host’s body into the chasm.`
            this.snippet = `a ${this.name}`
        }
    },
    3: repeatEncounters.huntingTrap,
    4: repeatEncounters.grave,
    5: repeatEncounters.trinket,
    6: repeatEncounters.corpse, 
    7: repeatEncounters.hiddenBundle, 
    8: repeatEncounters.skeletalRider, 
    9: {
        name: "Swarms of Bats",
        range: '1d8',
        description: "The stillness of the night is shattered by the shriek of bats and the flapping of tiny black wings.",
        rules: "These bats are the servants of Strahd. They attack the characters without provocation.",
        get init() {
            this.number = roll(this.range)
            this.snippet = `${this.number} ${this.name}`
        }
    },
    10: repeatEncounters.direWolves, 
    11: repeatEncounters.wolves,
    12: repeatEncounters.berserkers, 
    13: repeatEncounters.twigBlights, 
    14: repeatEncounters.needleBlights, 
    15: {
        name: "Werewolves (wolf form)",
        range: '1d6',
        description: "You hear the howl of a wolf some distance away.",
        get init () {
            this.rules = `Werewolves in wolf form follow the party from a safe distance for several hours. If they're able to conceal themselves from the party, the werewolves attack with surprise when the characters decide to take a short or long rest. Otherwise, they wait until the characters are weakened by another random encounter before moving in for the easy kill.<br>The werewolves’ lair is a cave complex that overlooks Lake Baratok. If you used the “Werewolves in the Mist” adventure hook to lure the characters to Barovia, captured werewolves can be forced to divulge the location of their den, where they keep their prisoners.`
            this.perception = roll('1d20+3')
            this.number = roll(this.range)
            this.snippet = `${this.number} ${this.name}`
        }
    },
    16: {
        name: "Zombies",
        range: '3d6',
        description: "The ungodly stench of rotting flesh hangs in the air. Up ahead, the walking, moaning corpses of dead men and women lumber about.",
        get init() {
            this.rules = `These unfortunate Barovians fell prey to the evils of the land and now shamble from place to place as a ravenous mob. The characters may attempt to sneak past the group of undead (DC ${roll('1d20-2')})`
            this.number = roll(this.range)
            this.snippet = `${this.number} ${this.name}`
        }
    },
    17: repeatEncounters.scarecrows, 
    18: {
        name: "Strahd Zombies",
        range: '1d8',
        description: "Not even the cloying fog can hide the stench of death that descends upon you. Something evil approaches, its footsteps betrayed by snapping twigs.",
        get init() {
            this.rules = `If the characters are moving quietly and not carrying light sources, they can try to hide from the Strahd zombies (DC ${roll('1d20-2')}). These undead soldiers once served as guards in Castle Ravenloft. They fled the castle after Strahd became a vampire but couldn’t avoid their master’s wrath. They still wear bits of tattered livery, and they attack the living on sight.`
            this.number = roll(this.range)
            this.snippet = `${this.number} ${this.name}`
        }
    },
    19: {
        name: "Will O' Wisp",
        description: "Several hundred yards away, through the fog, you see a flickering torchlight.",
        get init() {
            this.rules = `This random encounter occurs only once. If it comes up again, treat the result as no encounter.<br>If the characters follow the flickering light, read:<aside class=readAloud>The torchlight flutters as it moves away from you, but you never lose sight of it. You make your way quickly yet cautiously through the fog until you come upon the shell of a ruined tower. The upper floors of the structure have collapsed, leaving heaps of rubble and shattered timber around the tower’s base. The feeble light moves through an open doorway on the ground floor, then flickers and goes out.</aside>The light is a will-o’-wisp that enters the ruined tower and becomes invisible, hoping to lure the characters inside to their doom.<br>The floor of the tower is made of packed earth. Its interior is desecrated ground. Against the inside wall of the tower, across from the open doorway, is a closed, empty wooden chest.<br>If the characters disturb the chest, ${roll('3d6')} zombies erupt from the earthen floor and attack. Once the zombies appear, the will-o’-wisp becomes visible and joins the fray.<br><strong>Desecrated Ground:</strong> a detect evil and good spell cast within range reveals the presence of desecrated ground, and undead standing on desecrated ground have advantage on all saving throws. A vial of holy water purifies a 10-foot-square area of desecrated ground when sprinkled on it, and a hallow spell purifies desecrated ground within its area.`
            this.snippet = "The Will O' Wisp"
        }
    },
    20: repeatEncounters.revenant
}
