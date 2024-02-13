import player
from robot import Robot
import random
from common import *

class Player(player.Player):
    """Example player that moves, collects, and attacks randomly."""

    def __init__(self, rc: Robot, rng: random.Random):
        self.rc = rc
        self.turnCount = 0
        self.rng = rng
        self.DIRECTIONS = Direction.allDirections()

    def update(self):
        rc = self.rc
        if rc.getType() == RobotType.CASTLE:
            self.runCastle(rc) 
        elif rc.getType() == RobotType.KNIGHT:
            self.runKnight(rc) 
        elif rc.getType() == RobotType.VILLAGE:
            self.runVillage(rc)
        elif rc.getType() == RobotType.VILLAGER:
            self.runVillager(rc)
        elif rc.getType() == RobotType.SIEGEFOUNDRY:
            self.runSiegeFoundry(rc)
        elif rc.getType() == RobotType.CATAPULT:
            self.runCatapult(rc)
        elif rc.getType() == RobotType.TREBUCHET:
            self.runTrebuchet(rc) 
    
    def runCastle(self, rc:Robot):
        target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
        if rc.canTrain(RobotType.KNIGHT, target):
            rc.train(RobotType.KNIGHT, target)
    
    def runSiegeFoundry(self, rc:Robot):
        target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
        if rc.canTrain(RobotType.TREBUCHET, target):
            rc.train(RobotType.TREBUCHET, target)
        elif rc.canTrain(RobotType.CATAPULT, target):
            rc.train(RobotType.CATAPULT, target)

    def runKnight(self, rc:Robot):
        robots = list(filter(lambda robot: robot.getTeam() != rc.getTeam(), rc.senseNearbyRobots(rc.getType().ACTION_RANGE)))
        if len(robots) > 0:
            robot:Robot = robots[0]
            if rc.canAttack(robot.getLocation()):
                rc.attack(robot.getLocation())
        target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
        if rc.canMove(target=target):
            rc.move(target=target)
    
    def runCatapult(self, rc:Robot):
        robots = list(filter(lambda robot: robot.getTeam() != rc.getTeam(), rc.senseNearbyRobots(rc.getType().ACTION_RANGE)))
        if len(robots) > 0:
            robot:Robot = robots[0]
            if rc.canAttack(robot.getLocation()):
                rc.attack(robot.getLocation())
        else:
            target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
            if rc.canMove(target=target):
                rc.move(target=target)
    
    def runTrebuchet(self, rc:Robot):
        robots = list(filter(lambda robot: robot.getTeam() != rc.getTeam(), rc.senseNearbyRobots(rc.getType().ACTION_RANGE)))
        if len(robots) > 0:
            robot:Robot = robots[0]
            if rc.canAttack(robot.getLocation()):
                rc.attack(robot.getLocation())
        else:
            target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
            if rc.canMove(target=target):
                rc.move(target=target)

    def runVillage(self, rc:Robot):
        target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
        if rc.canTrain(RobotType.VILLAGER, target):
            rc.train(RobotType.VILLAGER, target)

    def runVillager(self, rc:Robot):
        target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
        if rc.canMove(target=target):
            rc.move(target=target)
        if rc.canCollect(rc.getLocation()):
            rc.collect(rc.getLocation())
