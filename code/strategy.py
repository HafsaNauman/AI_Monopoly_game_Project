import random
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def decide_purchase(self, board, player, square) -> bool: pass

    @abstractmethod
    def decide_bid_auction(self, board, player, square, current_bids) -> int: pass

    @abstractmethod
    def propose_trade(self, board, player, other) -> dict: pass

    @abstractmethod
    def accept_trade(self, board, player, offer) -> bool: pass

    @abstractmethod
    def decide_mortgage(self, board, player) -> bool: pass

    @abstractmethod
    def decide_build_house(self, board, player, square) -> bool: pass

class RandomStrategy(Strategy):
    def __init__(self, buy_prob=0.5, trade_prob=0.5, mortgage_prob=0.5, build_prob=0.5):
        self.buy_prob = buy_prob
        self.trade_prob = trade_prob
        self.mortgage_prob = mortgage_prob
        self.build_prob = build_prob

    def decide_purchase(self, board, player, square):
        return random.random() < self.buy_prob

    # def decide_bid_auction(self, board, player, square, current_bids):
    #     return random.randint(0, player.get_cash()) if random.random() < 0.5 else 0
    
    def decide_bid_auction(self, board, player, square, current_bids):
        # Prevent bidding when cash is non-positive
        max_cash = max(int(player.get_cash()), 0)
        if random.random() < 0.5 and max_cash > 0:
            return random.randint(0, max_cash)
        return 0
    
    def propose_trade(self, board, player, other):
        return None

    def accept_trade(self, board, player, offer):
        return random.random() < self.trade_prob

    def decide_mortgage(self, board, player):
        return player.get_cash() < player.min_cash_threshold() and random.random() < self.mortgage_prob

    def decide_build_house(self, board, player, square):
        return player.get_cash() > getattr(square, "building_costs", float('inf')) and random.random() < self.build_prob

class MinimaxStrategy(Strategy):
    def __init__(self, depth=2): self.depth = depth

    def decide_purchase(self, board, player, square):
        # stub: simple affordability check
        return player.get_cash() >= getattr(square, "price", 0)

    def decide_bid_auction(self, board, player, square, current_bids): return 0
    def propose_trade(self, board, player, other): return None
    def accept_trade(self, board, player, offer): return False
    def decide_mortgage(self, board, player): return False
    def decide_build_house(self, board, player, square): return False

class MCTStrategy(Strategy):
    def __init__(self, iterations=100): self.iterations = iterations

    def decide_purchase(self, board, player, square): return False
    def decide_bid_auction(self, board, player, square, current_bids): return 0
    def propose_trade(self, board, player, other): return None
    def accept_trade(self, board, player, offer): return False
    def decide_mortgage(self, board, player): return False
    def decide_build_house(self, board, player, square): return False

class RLStrategy(Strategy):
    def __init__(self, model=None): self.model = model

    def decide_purchase(self, board, player, square): return False
    def decide_bid_auction(self, board, player, square, current_bids): return 0
    def propose_trade(self, board, player, other): return None
    def accept_trade(self, board, player, offer): return False
    def decide_mortgage(self, board, player): return False
    def decide_build_house(self, board, player, square): return False

HumanRandom = RandomStrategy