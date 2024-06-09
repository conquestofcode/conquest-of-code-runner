# Formal Specification

**Welcome to Conquest of Code: Season 1.**
This is an overview of this season. We recommend that you read through this whole document before writing bots. Please join our discord server for more info, to ask questions abot the game, and to communicate with your fellow competitors: https://discord.gg/bqWrhP9C96. <br>
_This document and the game it describes may be tweaked as the season progresses. We will try to keep changes to a minimum, but we may have to make balancing changes._

# Objective

In Conquest of Code, you will write code to control your army of robots and buildings.

Eliminate other players through brute force to seize victory.

Good luck!

# Board Overview

Each Conquest of Code game is played on a board (also called a map). The board is a 2-dimensional rectangular grid using a coordinate system, where 0, 0 is the top right corner. Coordinates are represented using the MapLocation class holding the x and y values of the location. No two units may occupy the same square.

## Passible and Impassible squares

All squares on the board are either passible or impassible. Units may not move onto or be built onto impassible squares.

## Distances

A square’s distance from another square is calculated using the following formula:

$D(a, b) = √(abs(a.x-b.x)^2+abs(a.y-b.y)^2)$

Where D is the distance between two map locations a and b.

# Resource Types

Creating **units** requires **resources**. In **Conquest of Code**, there are many types of **resources** that can be **collected** by your **units**.

Each unit has a **seperate** inventory of resources. This means that you will probably want to **transfer** resources between your **units**, in order to produce more **units**.

## Metal

**Metal** is required to build most **units**. It can be collected from **Mines**. **Metal** is measured in **pounds/lbs**.

## Wood

**Wood** is required to build most **buildings**. It can be collected from **Forests**. **Wood** is measured in **planks**.

## Stone

**Stone** is required to build most combat-type **buildings**. It can be collected from **Quarries**. **Stone** is measured in **pounds/lbs**.

## Gold

**Gold** is required to build **Elite** and **Master** units. It can be collected from **Deep Layers** of **Mines**. **Gold** is measured in **pounds/lbs**.

# Collecting Resources

Your units can collect resources from natural infinite sources.

## Mines

There are 7 different **layers** of **Mines**; **Tin**, **Copper**, **Iron**, and **Silver** (**Shallow Layers/Mines**) and **Gold**, **Jewel**, and **Diamond** (**Deep Layers/Mines**).

The base collecting value for Mines are:
**Tin**: 1 lb of Metal/round
**Copper**: 3 lbs of Metal/round
**Iron**: 5 lbs of Metal/round
**Silver**: 10 lbs of Metal/round
**Gold**: 10 lbs of Metal and 1 lb of Gold/round
**Jewel**: 10 lbs of Metal and 3 lb. of Gold/round
**Diamond**: 10 lbs of Metal and 5 lbs of Gold/round

Mines are upgraded to the next layer (**Tin** -> **Copper** -> **Iron** -> **Silver** -> **Gold** -> **Jewel** -> **Diamond**), when a certain number of pounds have been collected from them, as shown below:
**Tin** -> **Copper**: 500 lbs
**Copper** -> **Iron**: 1,500 lbs
**Iron** -> **Silver**: 5,000 lbs
**Silver** -> **Gold**: 10,000 lbs
**Gold** -> **Jewel**: 25,000 lbs
**Jewel** -> **Diamond**: 75,000 lbs

## Forests

The base collecting value for **Forests** is 5 **planks** of **Wood**/round.

## Quarries

There are two different layers of **Quarries**: **Shallow Quarries** and **Deep Quarries**.

The base collecting values for Quarries are:
**Shallow**: 1 lb of Stone/round
**Deep**: 3 lbs of Stone/round

**Shallow Quarries** are upgraded to **Deep Quarries** when 500 lbs have been collected from them.

## Resource Cycling

Robots have a maximum amount of resources they can carry, however, they can still collect while they’re at that limit. The collected resources will immediately disappear, but it will still count toward Source upgrades.

# Training

Units can train robots in an adjacent square by calling `train`. This create the specified robot at the target square.

# Building

Units can build building foundations in an adjacent square by calling `build`. This will first place an empty foundation at the target square if none exists, then transfer all resources the robot has in the new building's cost to the foundation at the target square.

A foundation runs your player's code, however cannot perform most actions until they are assembled into buildings. A foundation can call `assemble` to assemble itself into a building.

# Winning

A player is out if they:

- Go 100 rounds without having any Robots
- Have no Robots or Buildings (not counting Foundations) for 1 round

The game is over when there are one or less players remaining in the game (not out). All players are then ranked based on the round they went out, with the latest being better. (The player who survived the longest is first, second longest is second, etc.)

If the extremely rare event occurs of multiple players going out at the same time, they are assigned to the queue in a random order.

# Units

All units have a certain amount of health (also known as life, hp, or such). At the end of a round, if any robot's health is less then or equals to 0, the robot is removed from the game.

Units are assigned a random id between 10,000 and 19,999 (inclusive).

**Note that your player's module will be reloaded for each robot, meaning that module variables will not be shared.**

Below is a general overview of all units. More detailed statistics can be found later.

- Castle
  - Trains Knights
  - Tiny attack in a short range
- Knight
  - Basic offensive unit
  - Medium attack
  - Simple
  - Boring
  - Attacks every turn
- Elite Knight
  - Knight but better
  - Twice as much health
  - Large attack
  - Slightly more advanced
  - Slightly less boring
  - Attacks every turn and sometimes attacks
    more
- Master Knight
  - Elite Knight but even better
  - Twice as much health
  - Giant attack (takes out Knights in two hits)
  - Very advanced
  - Cool
  - Attacks twice every turn
  - Longer reach
- Village
  - Makes Villagers
  - Cannot attack
  - Defenseless
  - You always start with at least one
- Villager
  - Collects resources
  - Keep up the economy
  - Vital for survival
  - Miniscule attack
  - Not quite defenseless
- Archery Range
  - Makes Archers
  - Contains targets
  - Cannot attack
  - Not defenseless because it can make defense
- Archer
  - Small, long range attack
  - Attacks twice every turn
  - Moves twice every turn
- Siege Foundry
  - Makes weapons of war
  - Cannot attack
  - Cool
- Catapult
  - Devestating attack with a long range
  - Makes a big boom
  - Can't see very far
  - Slow
- Ballista
  - great attack at large distances
  - shoots a cool spear thing
  - absolutely awesome
  - Slow
  - Tiny health
  - Big action cooldown
- Trebuchet
  - Supreme to a Catapult
  - Expensive
  - Even more devestating attack with an even longer range
  - Makes an even bigger boom
  - Can see further but still not that far
  - Moves slower but attacks quicker
- Watchtower
  - Trains spies
  - Large vision range to watch stuff
- Spy
  - Can disguise itself
  - No attack
  - Fast
  - Extremely tiny health
  - Would lose in direct combat against one villager if it didn't run away

# Communication

Each robot has a list of 8 non-negative numbers between 0 and 2<sup>16</sup>, called comms, used to communicate with other robots.

All nearby units can read the robot's comms.

# Actions and cooldowns

A unit has 3 different cooldowns - **Action**, **Movement**, and **Special**.

- **Movement cooldown** is associated with the **Move** action.
- **Action cooldown** is associated with the **Attack**, **Train**, **Collect**, **Transfer**, **Build** actions.
- **Special cooldown** is associated with the **Disguise** action.

To perform most actions, a robot's action cooldown has to be less than 10. At the end of a a turn, all robots' cooldowns decrease by 10, to a minimum of 0.

For example, if you take an action A with action cooldown 10, you'll be able to take it every turn.

However, if you have an action B with action cooldown 7:
Round 1, 0 action cooldown: We take action B, increasing our cooldown to 7. However, because our cooldown is still less than 10, we can take action B again, increasing our cooldown to 14. At the end of our turn, our cooldown decreases by 10 to 4.
Round 2, 4 action cooldown: We take action B, increasing our cooldown to 11. Now that our cooldown is over 10, we can take no more actions. At the end of our turn, our cooldown decreases to 1.
Round 3, 1 action cooldown: Taking action B increases our cooldown to 8, allowing us to take it again, increasing our cooldown to 15. At the end of our turn, our cooldown decreases to 5.
Et cetera.

Each turn units can:

- **Move** (`canMove`/`move`): A unit that can move can move itself to an empty, adjacent (including diagonally) square if their movement cooldown is less than 10. This increases their movement cooldown according to their type.
- **Attack** (`canAttack`/`attack`): A unit that can attack can attack a square within their action range if their action cooldown is less than 10. This deals damage equal to their attack value to the unit on that square, if such a unit exists. This increases their action cooldown according to their type. Note that there is friendly fire, meaning that units can attack and deal damage to other units on their team. A unit can attack a square even if it has no unit on it. Foundations may not be attacked.
- **Train** (`canTrain`/`train`): A unit can train a unit their type is able to train to an empty, adjacent (including diagonally) square if their action cooldown is less than 10 and they have sufficient resources. This increases their action cooldown according to their type.
- **Upgrade** (`canUpgrade`/`upgrade`): A unit can get an upgrade if they have sufficient resources.
- **Collect** (`canCollect`/`collect`): A unit that can collect can collect from an adjacent (including diagonally) square if their action cooldown is less than 10. This increases their action cooldown according to their type.
- **Transfer** (`canTransfer`/`transfer`): A unit can transfer resources to an adjacent (including diagonally) unit if their action cooldown is less than 10. This increases their action cooldown according to their type.
- **Build** (`canBuild`/`build`): A unit can build to a square containing either no foundation or a foundation on their team if their action cooldown is less than 10. This increases their action cooldown according to their type.
- **Assemble** (`canAssemble`/`assembly`): An unbuilt unit can assemble itself if it has enough resources.
- **Disguise** (`canDisguise`/`disguise`): Spies may disguise their RobotType, Team, resources, build status, and hp. This does not change their actual stats, but they will appear as the new unit when sensed by any unit.

**At the end of each turn, each unit's action, movement, and special cooldowns decrease by 10, to a minimum of 0.**

# Bytecode and Textcode limits

Units are limited in the amount of computation they can perform without exploding.

At the end of a unit's turn, if they have used more computational power (measured in approximate bytecodes) than allotted to their type (currently 10,000 for all units), the unit will explode. In addition, if a player's robot folder has more then 10,000 tokens, or textcodes (not including .pyc files), the unit will explode upon creation.

# Appendix A: Making your bot

When making your bot, there are a few things to keep in mind.

# Banned Modules

To ensure gameplay is fair some modules are banned.

- Using the random module (other than for [type hinting](https://docs.python.org/3/library/typing.html)) is banned to ensure matches are the same every time. A seeded rng is passed to your robots’ `__init__` function for random use.
- The os and sys modules are banned to ensure that the game can carry out until a winner is declared.
- Pygame and other graphics modules are banned to ensure that the game has only one window that displays the true content of the game.
- Communication between robots (ex. writing to files) other then using the comms functionality is banned. **Note that your player is reimported for each robot, so module variables will not be shared.**
- Using modules such as `traceback` to read the print history is banned.
- Changing any game classes or files, or attributes of the same (ex `robot.Robot`, `robot.py`, `resourceTypes.RESOURCE_TYPES`) is banned.
- **Catching game exceptions such as `OutOfBytecodeException` and `DisintegrateException` is banned (GameActionException can be caught)**

## Fair Gameplay

If you are not sure if something qualifies as "in the rules", please ask us before submitting your bot.

# Appendix B: Detailed Statistics

## Unit Types

Each unit is either a Robot or a Building. Detailed descriptions of each unit can be found below.

## Robot

**Type**: Group

**Can Move**: Yes<br>
**Can Collect**: No<br>
**Can Disguise**: No<br>
**Max Weight**: 0

The general group of Robots include Villagers, Archers, and such. Robots can move around the map.

## Building

**Type**: Group<br>
**Can Move**: No<br>
**Can Collect**: No<br>
**Can Disguise**: No<br>
**Max Weight**: Infinity

The general group of Buildings includes Castles, Villages, and such. Buildings cannot move.

## Castle

**Type**: Building<br>
**Cost**: 1,000 Wood, 9,000 Stone<br>
**Health**: 10,000<br>
**Attack**: 10<br>
**Action Range**: 3<br>
**Vision Range**: 4<br>
**Action Cooldown**: 2<br>
**Trains**: Knight

## Knight

**Type**: Robot<br>
**Cost**: 125 Metal<br>
**Health**: 200<br>
**Attack**: 25<br>
**Action Range**: 1<br>
**Vision Range**: 3<br>
**Movement Cooldown**: 10<br>
**Action Cooldown**: 10<br>
**Trained From**: Castle

## Elite Knight

**Type**: Robot<br>
**Cost**: 150 Metal, 100 Gold<br>
**Health**: 350<br>
**Attack**: 40<br>
**Action Range**: 1<br>
**Vision Range**: 4<br>
**Movement Cooldown**: 10<br>
**Action Cooldown**: 8
**Trained From**: Castle

## Master Knight

**Type**: Robot<br>
**Cost**: 250 Metal, 250 Gold<br>
**Health**: 500<br>
**Attack**: 70<br>
**Action Range**: 2<br>
**Vision Range**: 5<br>
**Movement Cooldown**: 10<br>
**Action Cooldown**: 5<br>
**Trained From**: Castle

## Village

**Type**: Building<br>
**Cost**: 1,000 Wood<br>
**Health**: 1,000<br>
**Can Attack**: No<br>
**Action Range**: 1<br>
**Vision Range**: 1<br>
**Action Cooldown**: 10<br>
**Trains**: Villager

## Villager

**Type**: Robot<br>
**Cost**: 100 Metal<br>
**Health**: 100<br>
**Attack**: 2<br>
**Can Collect**: Yes<br>
**Action Range**: 1<br>
**Vision Range**: 5<br>
**Movement Cooldown**: 10<br>
**Action Cooldown**: 10<br>
**Max Weight**: 50<br>
**Trained From**: Village

## Archery Range

**Type**: Building<br>
**Cost**: 500 Stone, 4,500 Wood<br>
**Health**: 5,000<br>
**Can Attack**: No<br>
**Action Range**: 1<br>
**Vision Range**: 5<br>
**Action Cooldown**: 10<br>
**Trains**: Archer

## Archer

**Type**: Robot<br>
**Cost**: 100 Wood, 25 Metal<br>
**Health**: 100<br>
**Attack**: 10<br>
**Action Range**: 5<br>
**Vision Range**: 7<br>
**Movement Cooldown**: 9<br>
**Action Cooldown**: 5<br>
**Trained From**: Archery Range

## Elite Archer

**Type**: Robot<br>
**Cost**: 110 Wood, 40 Metal, 100 Gold<br>
**Health**: 200<br>
**Attack**: 15<br>
**Action Range**: 7<br>
**Vision Range**: 10<br>
**Movement Cooldown**: 7<br>
**Action Cooldown**: 3<br>
**Trained From**: Archery Range

## Master Archer

**Type**: Robot<br>
**Cost**: 160 Wood, 90 Metal, 250 Gold<br>
**Health**: 320<br>
**Attack**: 25<br>
**Action Range**: 10<br>
**Vision Range**: 15<br>
**Movement Cooldown**: 5<br>
**Action Cooldown**: 2<br>
**Trained From**: Archery Range

## Siege Foundry

**Type**: Building<br>
**Cost**: 2,000 Stone, 500 Metal<br>
**Health**: 2,500<br>
**Can Attack**: No<br>
**Action Range**: 1<br>
**Vision Range**: 1<br>
**Action Cooldown**: 50<br>
**Trains**: Catapult

## Catapult

**Type**: Robot<br>
**Cost**: 100 Stone, 100 Wood, 25 Metal<br>
**Health**: 200<br>
**Attack**: 500<br>
**Action Range**: 10<br>
**Vision Range**: 1<br>
**Movement Cooldown**: 25<br>
**Action Cooldown**: 40<br>
**Trained From**: Siege Foundry

## Ballista

**Type**: Robot<br>
**Cost**: 175 Wood, 120 Metal<br>
**Health**: 75<br>
**Attack**: 300<br>
**Action Range**: 10<br>
**Vision Range**: 8<br>
**Movement Cooldown**: 20<br>
**Action Cooldown**: 80<br>
**Trained From**: Siege Foundry

## Trebuchet

**Type**: Robot<br>
**Cost**: 500 Stone, 300 Wood, 100 Metal<br>
**Health**: 235<br>
**Attack**: 1500<br>
**Action Range**: 15<br>
**Vision Range**: 2<br>
**Movement Cooldown**: 30<br>
**Action Cooldown**: 30<br>
**Trained From**: Siege Foundry

## Watchtower

**Type**: Building<br>
**Cost**: 2,000 Metal, 2,000 Stone, 2,000 Wood<br>
**Health**: 6,000<br>
**Can Attack**: No<br>
**Action Range**: 3<br>
**Vision Range**: 10<br>
**Action Cooldown**: 10<br>
**Trains**: Spy

## Spy

**Type**: Robot<br>
**Cost**: 50 Metal, 50 Wood, 50 Stone, 100 Gold<br>
**Health**: 1<br>
**Can Attack**: No<br>
**Can Disguise**: Yes<br>
**Action Range**: 1<br>
**Vision Range**: 5<br>
**Movement Cooldown**: 2<br>
**Action Cooldown**: N/A<br>
**Trained From**: Watchtower<br>

# Appendix C: Tech Trees

## Siege Foundry

### Trebuchets

**Cost**: 750 Stone, 500 Wood<br>
**Allows Train**: Catapult

## Castle

### Elite Knights

**Cost**: 50 Gold<br>
**Allows Train**: Elite Knight

### Master Knights

**Cost**: 250 Gold<br>
**Allows Train**: Master Knight

## Archery Range

### Elite Archers

**Cost**: 50 Gold<br>
**Allows Train**: Elite Archer

### Master Archers

**Cost**: 250 Gold<br>
**Allows Train**: Master Archer

# Appendix D: Using the Visualizer

In the middle of the visualizer is the board. The board contains all the units, foundations, sources, impassible squares (represented by mountains), etc, on the current game. Units will have dots indicating the resources they're carrying. **Left**-clicking on a unit will select it. **Right**-clicking on a source will select it. **Middle**-clicking (usually performed by clicking the middle mouse button, pressing the left and right buttons at the same time, or three finger clicking on a touchpad) on a foundation will select it.

In the top left corner, you can view information such as the **version**, **TPS** (ticks per second), **FPS** (frames per second), **Round**, and **Seed**. Changing the seed will restart the game with a different rng seed.

In the middle left, you can view game stats.<br>

- **Units**: The totals and ratios of each teams' robot count (not including foundations).
- **Total Health**: The ratios of the sums of each teams' robots' health (not including foundations).
- **Resources**: The totals and ratios of all resources carried by each teams' robots (not including foundations).

In the bottom left, you can view specific stats for a unit or source once you select it.

In the top right, you can change the current frame you're viewing, save and load games, and change the current map. Changing the map will restart the game.

In the top middle, you can change the players in the game. Changing the players will restart the game.

# Hotkeys

**Space/Up Arrow**: Pause/unpause
**Left Arrow (when paused)**: Step backward
**Right Arrow (when paused)**: Step forward
**Left Arrow (when unpaused)**: Half speed
**Right Arrow (when unpaused)**: Double speed
**Down Arrow**: Reverse
**,**: Jump to beginning
**.**: Jump to end
**/**: Restart
**Esc**: Exit
**G**: Toggle Gridlines