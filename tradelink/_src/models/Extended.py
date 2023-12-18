from typing import Optional
from pydantic import BaseModel


class ListElement(BaseModel):
    timestamp: int
    value: float  # Should be converted to the datetime
    

class OrderElement(BaseModel):
    abs: int | float
    rel: int | float
    

class SymbolElement(BaseModel):
    symbol: str
    volume: dict[str, float]
    pnl: dict[str, float]
    qty: dict[str, int | float]
    direction: dict[str, OrderElement | float]
    

class FeeStats(BaseModel):
    paid: float
    rebate: float
    total: float
    fundingP: float
    fundingN: float
    fundingNet: float
    volume: float
    refs: float
    wths: float
    deps: float
    stake: float
    unstake: float
    unstakeFee: float
    optionVol: float
    optionFeeN: float
    optionFeeP: float
    

class User(BaseModel):
    links: list[Optional[dict[str, str]]]
    name: str
    avatar: None | str
    

class Orders(BaseModel):
    withRealizedPnl: bool
    type: dict[str, OrderElement]
    direction: dict[str, OrderElement | float]
    volume: dict[str, float]
    distribution: dict[str, list[OrderElement]]
    symbols: list[Optional[SymbolElement]]


class Extended(BaseModel):
    # Charts
    balances: list[Optional[ListElement]]
    balancesR: list[Optional[ListElement]]
    profits: list[Optional[ListElement]]
    profitsR: list[Optional[ListElement]]
    monthly: list[Optional[ListElement]]
    weekly: list[Optional[ListElement]]
    daily: list[Optional[ListElement]]
    dailyPnL: list[Optional[ListElement]]
    indexDaily: list[Optional[ListElement]]
    indexWeekly: list[Optional[ListElement]]
    indexMonthly: list[Optional[ListElement]]
    maxDDHistory: list[Optional[ListElement]]
    maxDDDHistory: list[Optional[ListElement]]
    monthDDHistory: list[Optional[ListElement]]
    
    icp: list[Optional[ListElement]]
    longPositions: list[Optional[ListElement]]
    shortPositions: list[Optional[ListElement]]
    longPositionsIcp: list[Optional[ListElement]]
    shortPositionsIcp: list[Optional[ListElement]]
    
    lastMonthlyProfit: Optional[ListElement]
    lastWeeklyProfit: Optional[ListElement]
    lastDailyProfit: Optional[ListElement]
    lastMonthlyNetProfit: Optional[ListElement]
    lastWeeklyNetProfit: Optional[ListElement]
    lastDailyNetProfit: Optional[ListElement]

    # Indicators
    feeStat: FeeStats
    weeklyFeeStat: FeeStats
    sourceFor: list[str]
    orders: Orders
    user: User
    tournament: dict[str, bool]

    activeDays: int
    ohr: float
    cagr: float
    trackingDays: int
    tradingDays: int
    maxDD: float
    maxDDDuration: int
    firstTrade: int  # Should be converted to the datetime
    winningDays: int
    losingDays: int
    breakevenDays: int
    winrate: float
    totalProfit: float
    totalLoss: float
    netProfit: float
    lastProfit: float
    lastWeekBalance: float
    lastWeekProfit: float
    lastWeekAverageMonthlyProfit: float
    averageMonthlyProfit: float
    averageDailyProfit: float
    averageProfit: float
    averageLoss: float
    profitRatio: float
    recoveryFactor: float
    expectedValue: float
    kSortino: float
    kSharp: float
    kCalmar: float
    betaRatio: float
    ADL: float
    volatility: float
    rSquared: float
    informationRatio: float
    treynorRatio: float
    sterlingRatio: float
    schwagerRatio: float
    safetyFirstRatio: float
    averageBalance: float
    firstBalance: float
    maxBalance: float
    minBalance: float
    lastBalance: float    
    maxIcp: float    
    avgIcp: float 
    lastMonthGrowth: float
    lastQuarterGrowth: float
    lastYearGrowth: float
    growthRate: float
    VaR: float
    maxdddRatio: float
    betaRating: float   
    usedMarkets: int
    totalTrades: int

    # Other
    keyId: str
    stockName: str
    stockNames: list[str]
    accountIds: list[str]
    baseAsset: str
    keyName: str
    keyStatus: bool
    active: bool
    progressPercent: int
    firstValidDataDate: str
    lastValidDataDate: str
    updatedAt: None | str
    startDate: str
    endDate: str
    beginMoment: str
    selfPower: None | float
    selfProfitRate: float
    integralEvaluation: float
    riskFreeRate: float