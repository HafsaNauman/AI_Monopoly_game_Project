# board_config.py

from cards import (
    AdvanceIllinois,
    AdvanceRailroad,
    AdvanceStCharlesPlace,
    AdvanceToGo,
    AdvanceUtility,
    BankError,
    BankPays,
    BeautyContest,
    Birthday,
    BuildingLoadMature,
    Chairman,
    ConsultancyFees,
    CrosswordCompetition,
    DoctorFees,
    GeneralRepairs,
    GetOutJailFree,
    GoBack3Spaces,
    GoToJailCard,
    GrandOperaNight,
    HolidayFund,
    HospitalFees,
    IncomeTaxRefund,
    Inherit,
    LifeInsurance,
    PoorTax,
    SaleStock,
    SchoolFees,
    StreetRepairs,
    TripBoardwalk,
    TripReadingTrainStation,
    # Extended cards
    DoubleRent,
    SkipNextTurn,
    TaxRefundChance,
    TaxRefundCC,
)
from squares import (
    Chance,
    CommunityChest,
    ElectricCompany,
    FreeParking,
    GoToJail,
    IncomeTax,
    Jail,
    LuxuryTax,
    Property,
    PropertyGroup,
    Start,
    TrainStation,
    WaterWorks,
)

class BoardConfig:
    community_cards = [
        AdvanceToGo(),
        BankError(),
        DoctorFees(),
        SaleStock(),
        GetOutJailFree(),
        GoToJailCard(),
        GrandOperaNight(),
        HolidayFund(),
        IncomeTaxRefund(),
        Birthday(),
        LifeInsurance(),
        HospitalFees(),
        SchoolFees(),
        ConsultancyFees(),
        StreetRepairs(),
        BeautyContest(),
        Inherit(),
        # Extended Community Chest
        TaxRefundCC(),
    ]

    chance_cards = [
        AdvanceToGo(),
        AdvanceIllinois(),
        AdvanceStCharlesPlace(),
        AdvanceUtility(),
        AdvanceRailroad(),
        BankPays(),
        GetOutJailFree(),
        GoBack3Spaces(),
        GoToJailCard(),
        GeneralRepairs(),
        PoorTax(),
        TripReadingTrainStation(),
        TripBoardwalk(),
        Chairman(),
        BuildingLoadMature(),
        CrosswordCompetition(),
        # Extended Chance
        DoubleRent(),
        SkipNextTurn(),
        TaxRefundChance(),
    ]

    groups = [
        PropertyGroup("Brown Group"),
        PropertyGroup("Light Blue Group"),
        PropertyGroup("Pink Group"),
        PropertyGroup("Orange Group"),
        PropertyGroup("Red Group"),
        PropertyGroup("Yellow Group"),
        PropertyGroup("Green Group"),
        PropertyGroup("Dark Blue Group"),
    ]

    squares = [
        Start(),
        Property("Mediterranean Avenue", 60,  groups[0],
                 rent=[2, 10, 30, 90, 160, 250],
                 monopoly_rent=2, mortgage=30, building_costs=50),
        Property("Baltic Avenue",        60,  groups[0],
                 rent=[4, 20, 60, 180, 320, 450],
                 monopoly_rent=8, mortgage=30, building_costs=50),
        CommunityChest(),
        IncomeTax(),
        TrainStation("Reading Railroad"),
        Property("Oriental Avenue",     100, groups[1],
                 rent=[6, 30, 90, 270, 400, 550],
                 monopoly_rent=12, mortgage=50, building_costs=50),
        Chance(),
        Property("Vermont Avenue",      100, groups[1],
                 rent=[6, 30, 90, 270, 400, 550],
                 monopoly_rent=12, mortgage=50, building_costs=50),
        Property("Connecticut Avenue",  120, groups[1],
                 rent=[8, 40, 100, 300, 450, 600],
                 monopoly_rent=16, mortgage=60, building_costs=50),
        Jail(),
        Property("St. Charles Place",   140, groups[2],
                 rent=[10, 50, 150, 450, 625, 750],
                 monopoly_rent=20, mortgage=70, building_costs=100),
        ElectricCompany(),
        Property("States Avenue",       140, groups[2],
                 rent=[10, 50, 150, 450, 625, 750],
                 monopoly_rent=20, mortgage=70, building_costs=100),
        Property("Virginia Avenue",     160, groups[2],
                 rent=[12, 60, 180, 500, 700, 900],
                 monopoly_rent=24, mortgage=80, building_costs=100),
        TrainStation("Pennsylvania Railroad"),
        Property("St. James Place",     180, groups[3],
                 rent=[14, 70, 200, 550, 750, 950],
                 monopoly_rent=28, mortgage=90, building_costs=100),
        CommunityChest(),
        Property("Tennessee Avenue",    180, groups[3],
                 rent=[14, 70, 200, 550, 750, 950],
                 monopoly_rent=28, mortgage=90, building_costs=100),
        Property("New York Avenue",     200, groups[3],
                 rent=[16, 80, 220, 600, 800, 1000],
                 monopoly_rent=32, mortgage=90, building_costs=100),
        FreeParking(),
        Property("Kentucky Avenue",     220, groups[4],
                 rent=[18, 90, 250, 700, 875, 1050],
                 monopoly_rent=36, mortgage=110, building_costs=150),
        Chance(),
        Property("Indiana Avenue",      220, groups[4],
                 rent=[18, 90, 250, 700, 875, 1050],
                 monopoly_rent=36, mortgage=110, building_costs=150),
        Property("Illinois Avenue",     240, groups[4],
                 rent=[20, 100, 300, 750, 925, 1100],
                 monopoly_rent=40, mortgage=120, building_costs=150),
        TrainStation("B. & O. Railroad"),
        Property("Atlantic Avenue",     260, groups[5],
                 rent=[22, 110, 330, 800, 975, 1150],
                 monopoly_rent=44, mortgage=130, building_costs=150),
        Property("Ventnor Avenue",      260, groups[5],
                 rent=[22, 110, 330, 800, 975, 1150],
                 monopoly_rent=44, mortgage=130, building_costs=150),
        WaterWorks(),
        Property("Marvin Gardens",      280, groups[5],
                 rent=[24, 120, 360, 850, 1025, 1200],
                 monopoly_rent=48, mortgage=140, building_costs=150),
        GoToJail(),
        Property("Pacific Avenue",      300, groups[6],
                 rent=[26, 130, 390, 900, 1100, 1275],
                 monopoly_rent=52, mortgage=150, building_costs=200),
        Property("North Carolina Avenue", 300, groups[6],
                 rent=[26, 130, 390, 900, 1100, 1275],
                 monopoly_rent=52, mortgage=150, building_costs=200),
        CommunityChest(),
        Property("Pennsylvania Avenue", 320, groups[6],
                 rent=[28, 150, 450, 1000, 1200, 1400],
                 monopoly_rent=56, mortgage=160, building_costs=200),
        TrainStation("Short Line"),
        Chance(),
        Property("Park Place",          350, groups[7],
                 rent=[35, 175, 500, 1100, 1300, 1500],
                 monopoly_rent=70, mortgage=175, building_costs=200),
        LuxuryTax(),
        Property("Boardwalk",           400, groups[7],
                 rent=[50, 200, 600, 1400, 1700, 2000],
                 monopoly_rent=100, mortgage=200, building_costs=200),
    ]

    token = [
        "Scottish Terrier",
        "Battleship",
        "Automobile",
        "Top Hat",
        "Thimble",
        "Shoe",
        "Wheelbarrow",
        "Cat",
    ]
