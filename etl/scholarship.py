import enum


@enum.unique
class FillStatus(str, enum.Enum):
    COMPLETE = 'COMPLETE'

    INCOMPLETE = 'INCOMPLETE'


@enum.unique
class FundingType(str, enum.Enum):
    COMPLETE = 'COMPLETE'

    PARTIAL = 'PARTIAL'


@enum.unique
class AcademicLevel(str, enum.Enum):
    UNDERGRADUATE = 'UNDERGRADUATE'

    POSTGRADUATE = 'POSTGRADUATE'

    OTHERS = 'OTHERS'

    BOTH = 'BOTH'
