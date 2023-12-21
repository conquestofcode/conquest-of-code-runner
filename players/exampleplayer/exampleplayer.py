import player
from robot import Robot
import direction
import robotTypes
import random

class Player(player.Player):
    def __init__(self, robot: Robot, rng: random.Random):
        self.robot = robot
        self.turnCount = 0
        self.rng = rng
        self.DIRECTIONS = [
            direction.NORTHWEST,
            direction.NORTH,
            direction.NORTHEAST,
            direction.WEST,
            direction.EAST,
            direction.SOUTHWEST,
            direction.SOUTH,
            direction.SOUTHEAST
        ]

    def update(self):
        rc = self.robot
        if rc.getType() == robotTypes.CASTLE:
            self.runCastle(rc) 
        if rc.getType() == robotTypes.KNIGHT:
            self.runKnight(rc) 
        if rc.getType() == robotTypes.VILLAGE:
            self.runVillage(rc)
        if rc.getType() == robotTypes.VILLAGER:
            self.runVillager(rc)
        if rc.getType() == robotTypes.SIEGEFOUNDRY:
            self.runSiegeFoundry(rc)
        if rc.getType() == robotTypes.CATAPULT:
            self.runCatapult(rc)
        if rc.getType() == robotTypes.TREBUCHET:
            self.runTrebuchet(rc) 
    
    def runCastle(self, rc:Robot):
        target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
        if rc.canTrain(robotTypes.KNIGHT, target):
            rc.train(robotTypes.KNIGHT, target)
    
    def runSiegeFoundry(self, rc:Robot):
        target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
        if rc.canTrain(robotTypes.TREBUCHET, target):
            rc.train(robotTypes.TREBUCHET, target)
        elif rc.canTrain(robotTypes.CATAPULT, target):
            rc.train(robotTypes.CATAPULT, target)

    def runKnight(self, rc:Robot):
        robots = list(filter(lambda robot: robot.getTeam() != rc.getTeam(), rc.senseNearbyRobots(rc.getType().ACTION_RANGE)))
        if len(robots) > 0:
            robot:Robot = robots[0]
            if rc.canAttack(robot.getLocation()):
                rc.attack(robot.getLocation())
        target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
        if rc.canMove(target):
            rc.move(target)
    
    def runCatapult(self, rc:Robot):
        robots = list(filter(lambda robot: robot.getTeam() != rc.getTeam(), rc.senseNearbyRobots(rc.getType().ACTION_RANGE)))
        if len(robots) > 0:
            robot:Robot = robots[0]
            if rc.canAttack(robot.getLocation()):
                rc.attack(robot.getLocation())
        else:
            target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
            if rc.canMove(target):
                rc.move(target)
    
    def runTrebuchet(self, rc:Robot):
        robots = list(filter(lambda robot: robot.getTeam() != rc.getTeam(), rc.senseNearbyRobots(rc.getType().ACTION_RANGE)))
        if len(robots) > 0:
            robot:Robot = robots[0]
            if rc.canAttack(robot.getLocation()):
                rc.attack(robot.getLocation())
        else:
            target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
            if rc.canMove(target):
                rc.move(target)

    def runVillage(self, rc:Robot):
        target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
        if rc.canTrain(robotTypes.VILLAGER, target):
            rc.train(robotTypes.VILLAGER, target)

    def runVillager(self, rc:Robot):
        target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
        if rc.canMove(target):
            rc.move(target)
        if rc.canCollect(rc.getLocation()):
            rc.collect(rc.getLocation())
