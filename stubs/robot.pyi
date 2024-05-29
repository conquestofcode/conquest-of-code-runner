# THIS FILE IS AUTOMATICALLY GENERATED, DO NOT EDIT.

import board
import common  # type: ignore
import direction
import mapLocation
import resourceTypes
import robot
import robotInfo
import robotTypes
import sourceInfo
import team

class Robot:
    def getMoveCooldown(self) -> int: ...
    def getActionCooldown(self) -> int: ...
    def canMove(
        self,
        targetDir: direction.Direction = ...,
        target: mapLocation.MapLocation = ...,
    ) -> bool: ...
    def move(
        self,
        targetDir: direction.Direction = ...,
        target: mapLocation.MapLocation = ...,
    ) -> None: ...
    def getLocation(self) -> mapLocation.MapLocation: ...
    def getType(self) -> robotTypes.RobotType: ...
    def getBoard(self) -> board.Board: ...
    def getTeam(self) -> team.Team: ...
    def getResources(self) -> dict[resourceTypes.ResourceType, int]: ...
    def getWeight(self) -> int: ...
    def getID(self) -> int: ...
    def canTrain(
        self, t: robotTypes.RobotType, target: mapLocation.MapLocation
    ) -> bool: ...
    def train(
        self, t: robotTypes.RobotType, target: mapLocation.MapLocation
    ) -> None: ...
    def canUpgrade(self, toUpgrade: robotTypes.RobotType) -> bool: ...
    def upgrade(self, toUpgrade: robotTypes.RobotType) -> None: ...
    def canAttack(self, target: mapLocation.MapLocation) -> bool: ...
    def attack(self, target: mapLocation.MapLocation) -> None: ...
    def canCollect(self, target: mapLocation.MapLocation) -> bool: ...
    def collect(self, target: mapLocation.MapLocation) -> None: ...
    def canTransfer(
        self, target: mapLocation.MapLocation, resources: dict = ...
    ) -> bool: ...
    def transfer(
        self, target: mapLocation.MapLocation, resources: dict = ...
    ) -> None: ...
    def canBuild(
        self, t: robotTypes.RobotType, target: mapLocation.MapLocation
    ) -> bool: ...
    def build(
        self, t: robotTypes.RobotType, target: mapLocation.MapLocation
    ) -> None: ...
    def canAssemble(self) -> bool: ...
    def assemble(self) -> None: ...
    def senseNearbyRobots(self, radius: int = ...) -> list[robotInfo.RobotInfo]: ...
    def senseNearbySources(self, radius: int = ...) -> list[sourceInfo.SourceInfo]: ...
    def isLocationPassable(self, location: mapLocation.MapLocation) -> bool: ...
    def getFoundationAt(self, x: int, y: int) -> robot.Robot | common.EMPTY: ...
    def canSenseLocation(self, location: mapLocation.MapLocation) -> bool: ...
    def toRobotInfo(self, last: bool = ...) -> robotInfo.RobotInfo: ...
    def canSenseRobotAtLocation(
        self, location: mapLocation.MapLocation
    ) -> robotInfo.RobotInfo: ...
    def senseRobotAtLocation(
        self, location: mapLocation.MapLocation
    ) -> robotInfo.RobotInfo: ...
    def canDisguise(
        self,
        rType: robotTypes.RobotType = ...,
        rTeam: team.Team = ...,
        resources: dict[resourceTypes.ResourceType, int] = ...,
        built: bool = ...,
        hp: int = ...,
    ) -> bool: ...
    def disguise(
        self,
        rType: robotTypes.RobotType = ...,
        rTeam: team.Team = ...,
        resources: dict[resourceTypes.ResourceType, int] = ...,
        built: bool = ...,
        hp: int = ...,
    ) -> None: ...
    def damage(self, damage: int) -> None: ...
    def disintegrate(self) -> None: ...
    def getHP(self) -> int: ...
    def getTeam(self) -> team.Team: ...
    def getBuilt(self) -> bool: ...
    def getComms(self) -> list[int]: ...
    def isMovementReady(self) -> bool: ...
    def isActionReady(self) -> bool: ...
    def isSpecialReady(self) -> bool: ...
    def setComms(self, num: int, pos: int) -> None: ...
    def setIndicatorString(self, s: str) -> None: ...
    def getBytecodesUsed(self) -> int: ...
    def getBytecodesRemaining(self) -> int: ...
    def getAttacks(self) -> list[mapLocation.MapLocation]: ...
