# THIS FILE IS AUTOMATICALLY GENERATED, DO NOT EDIT.

import mapLocation
import sourceTypes

class SourceInfo:
    def getLocation(self) -> mapLocation.MapLocation: ...
    def getType(self) -> sourceTypes.sourceType: ...
    def toNext(self) -> int|None: ...
    def getID(self) -> int: ...
