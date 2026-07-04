from bin_to_json import StfTestVector
from jam_types import (
    Null,
    ReportedWorkPackage,
    Struct,
    Vec,
    RecentBlocks,
    BlockInfo,
)
from jam_types import class_name as n


class ReportedWorkPackages(Vec):
    sub_type = n(ReportedWorkPackage)
  
class HistoryState(Struct):
    type_mapping = [
        # The most recent blocks information (𝛽)
        ('beta', n(RecentBlocks))
    ]

class HistoryInput(BlockInfo):
    pass

class HistoryOutput(Null):
    pass

class HistoryTestVector(StfTestVector):
    state_class = n(HistoryState)
    input_class = n(HistoryInput)
    output_class = n(HistoryOutput)
