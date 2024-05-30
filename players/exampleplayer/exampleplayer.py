from mapLocation import MapLocation  # type: ignore
import player  # type: ignore
from robot import Robot  # type: ignore
from random import Random  # type: ignore
from direction import Direction  # type: ignore
from robotTypes import RobotType  # type: ignore


class Player(player.Player):
    # inherits a base player class
    """Example player that moves, collects, and attacks randomly."""

    def __init__(self, rc: Robot, rng: Random):
        # the robot controller and a seeded rng are passed to the bots init
        global message
        # save rc, the module which will allow your code to interface with the game
        self.rc = rc
        self.turnCount = 0
        self.rng = rng
        # saves a list of all the directions a bot could move in
        self.DIRECTIONS = Direction.allDirections()

    def update(self):
        rc = self.rc

        # check what type the robot is and run the correct function
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

    def runCastle(self, rc: Robot):
        # in a castle atempt to train knights
        target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
        # select a square to train on
        # then check if the robot can train so no error occurs
        if rc.canTrain(RobotType.KNIGHT, target):
            # if it can do it!
            rc.train(RobotType.KNIGHT, target)

    def runSiegeFoundry(self, rc: Robot):
        # in the siege foundry attempt to build a trebuchet but if it can't a catapult will have to do
        target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
        # once again chooses a direction to build in

        # check what it can train and do it
        if rc.canTrain(RobotType.TREBUCHET, target):
            rc.train(RobotType.TREBUCHET, target)
        elif rc.canTrain(RobotType.CATAPULT, target):
            rc.train(RobotType.CATAPULT, target)

    def runKnight(self, rc: Robot):
        # if the robot is a knight, sense the robots on another team within its action range
        robots = list(
            filter(
                lambda robot: robot.getTeam() != rc.getTeam(),
                rc.senseNearbyRobots(rc.getType().ACTION_RANGE),
            )
        )
        if len(robots) > 0: # check if there is a bot in its action range
            robot: Robot = robots[0]
            # if there is attempt to attack it
            if rc.canAttack(robot.getLocation()):
                rc.attack(robot.getLocation())
        # move in a random direction if the robot can
        target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
        if rc.canMove(target=target):
            rc.move(target=target)

    def runCatapult(self, rc: Robot):
        # again sense potentially attackable robots
        robots = list(
            filter(
                lambda robot: robot.getTeam() != rc.getTeam(),
                rc.senseNearbyRobots(rc.getType().ACTION_RANGE),
            )
        )
        if len(robots) > 0:
            # if there are some, attempt to attack
            robot: Robot = robots[0]
            if rc.canAttack(robot.getLocation()):
                # check if it can attack and do so
                rc.attack(robot.getLocation())
        else:
            # if there is no bot, move randomly
            target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
            if rc.canMove(target=target):
                rc.move(target=target)

    def runTrebuchet(self, rc: Robot):
        # the trebuchet does the same thing as the catapult, these should both be runSiegeEngine but Matthew didn't make this smartly
        robots = list(
            filter(
                lambda robot: robot.getTeam() != rc.getTeam(),
                rc.senseNearbyRobots(rc.getType().ACTION_RANGE),
            )
        )
        if len(robots) > 0:
            robot: Robot = robots[0]
            if rc.canAttack(robot.getLocation()):
                rc.attack(robot.getLocation())
        else:
            target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
            if rc.canMove(target=target):
                rc.move(target=target)

    def runVillage(self, rc: Robot):
        # in a village try to make a villager
        target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
        # chooses a direction
        # and attempt to train it
        if rc.canTrain(RobotType.VILLAGER, target):
            rc.train(RobotType.VILLAGER, target)

    def runVillager(self, rc: Robot):
        # move in a random direction
        target = rc.getLocation().add(self.rng.choice(self.DIRECTIONS))
        if rc.canMove(target=target):
            rc.move(target=target)

        # check if it can collect and do so
        if rc.canCollect(rc.getLocation()):
            rc.collect(rc.getLocation())
