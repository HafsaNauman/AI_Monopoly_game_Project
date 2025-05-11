import random
from dice import Throw
from player import Player
from strategy import HumanRandom
from board_config import BoardConfig
from squares import Jail, Start, GoToJail

class Board(BoardConfig):
    def __init__(self, num_players=4, strategies=None):
        super().__init__()
        random.shuffle(self.chance_cards)
        random.shuffle(self.community_cards)

        if strategies is None:
            strategies = [HumanRandom() for _ in range(num_players)]
        self.players = [
            Player(uid=i, token=self.token[i], strategy=strategies[i])
            for i in range(num_players)
        ]
        self.positions = [0] * num_players
        self.current = 0

        # GUI log
        self.last_move_msg = ""

    def play_single_turn(self):
        """Perform one turn and return (die1, die2)."""
        player = self.players[self.current]

        # Skip flag
        if getattr(player, "skip_next_turns", 0) > 0:
            player.skip_next_turns -= 1
            self.last_move_msg = f"{player} skips their turn."
            roll = (0, 0)
        else:
            throw = Throw()
            # always two dice in our setup
            d1, d2 = throw.values[0], throw.values[1]
            self._move(player, throw.amount, throw)
            square = self.squares[self.positions[self.current]]
            self.last_move_msg = (
                f"{player} rolls {d1}+{d2}={throw.amount}, lands on {square}"
            )
            roll = (d1, d2)

        # Bankruptcy check
        if player.get_cash() < 0:
            b = self.players.pop(self.current)
            self.positions.pop(self.current)
            self.last_move_msg = f"{b} has gone bankrupt!"
            if self.current >= len(self.players):
                self.current = 0
        else:
            self.current = (self.current + 1) % len(self.players)

        return roll

    def _log(self, msg: str):
        """Print to console and save as last_event."""
        print(msg)
        self.last_event = msg

    def _take_turn(self, player):
        self._log(f"\n-- {player}'s turn --")
        throw = Throw()
        while True:
            steps = throw.get_amount()
            self._log(f"{player} rolls {steps}")
            self._move(player, steps, throw)
            if not throw.is_double():
                break
            self._log(f"{player} rolled doubles and goes again!")
            throw = Throw()

    def _move(self, player, steps, throw):
        idx = self.players.index(player)
        new_pos = (self.positions[idx] + steps) % len(self.squares)
        self.positions[idx] = new_pos
        square = self.squares[new_pos]
        self._log(f"{player} lands on {square}")
        
        
        # 1) Own property → maybe build house
        if square.is_owner(player):
            if player.strategy.decide_build_house(self, player, square):
                self._buy_house(player, square)
            return

        # 2) Unowned property → buy or auction
        if square.can_be_bought():
            if player.strategy.decide_purchase(self, player, square):
                self._buy_property(player, square)
            else:
                self._auction(square)
            return

        # 3) Pay rent
        owner = square.get_owner()
        if owner:
            self._handle_rent(player, square)
            return

        # 4) Chance
        if isinstance(square, type(self.chance_cards[0])):
            card = self.chance_cards.pop(0)
            self._log(f"{player} draws Chance: {card.name}")
            card.action(self, player)
            self.chance_cards.append(card)
            return

        # 5) Community Chest
        if isinstance(square, type(self.community_cards[0])):
            card = self.community_cards.pop(0)
            self._log(f"{player} draws Community Chest: {card.name}")
            card.action(self, player)
            self.community_cards.append(card)
            return

        # 6) Special
        self._handle_special(square, player)

    def _buy_property(self, player, square):
        price = square.get_price()
        self._log(f"{player} buys {square} for ${price}")
        player.transfer(-price)
        square.set_owner(player)
        player.add_property(square)

    def _handle_rent(self, player, square):
        owner = square.get_owner()
        rent = square.compute_rent(thr=Throw()) if hasattr(square, "compute_rent") else square.get_rent_amount()
        if owner.double_rent:
            rent *= 2
            owner.double_rent = False
            self._log(f"{owner}'s Double Rent → rent x2 = ${rent}")
        self._log(f"{player} pays ${rent} rent to {owner}")
        player.transfer(-rent)
        owner.transfer(rent)

    def _handle_special(self, square, player):
        # Income / Luxury Tax
        if hasattr(square, "cash_on_land"):
            tax = -square.cash_on_land
            self._log(f"{player} pays ${tax} tax")
            player.transfer(square.cash_on_land)

        # Passing Go
        if isinstance(square, Start):
            reward = square.cash_on_pass
            self._log(f"{player} collects ${reward} for passing Go")
            player.transfer(reward)

        # Go To Jail
        if isinstance(square, GoToJail):
            jail_idx = next(i for i, s in enumerate(self.squares) if isinstance(s, Jail))
            self._log(f"{player} goes directly to Jail")
            self.positions[self.players.index(player)] = jail_idx

    def _auction(self, square):
        self._log(f"Auction for {square}")
        current_bids = {}
        active = set(self.players)

        while True:
            bids_this_round = False
            for p in list(active):
                bid = p.strategy.decide_bid_auction(self, p, square, current_bids)
                prev = current_bids.get(p, 0)
                if bid > prev and bid <= p.get_cash():
                    current_bids[p] = bid
                    bids_this_round = True
                    self._log(f"{p} bids ${bid}")
                else:
                    active.discard(p)
                    self._log(f"{p} passes")
            if not bids_this_round or len(active) <= 1:
                break

        if not current_bids:
            self._log(f"No bids for {square}, auction ends unsold")
            return

        winner = max(current_bids, key=current_bids.get)
        winning_bid = current_bids[winner]
        self._log(f"{winner} wins auction for {square} at ${winning_bid}")
        winner.transfer(-winning_bid)
        square.owner = winner
        winner.property_list.append(square)

    def _trade_phase(self, player):
        for other in self.players:
            if other is player:
                continue
            offer = player.strategy.propose_trade(self, player, other)
            if offer:
                self._log(f"{player} proposes trade to {other}: {offer}")
                if other.strategy.accept_trade(self, other, offer):
                    self._execute_trade(offer)
                    self._log("Trade executed")
                else:
                    self._log(f"{other} rejects trade")

    def _execute_trade(self, offer):
        giver = offer["from"]
        receiver = offer["to"]
        for sq in offer.get("give", []):
            sq.owner = receiver
            giver.property_list.remove(sq)
            receiver.property_list.append(sq)
        for sq in offer.get("receive", []):
            sq.owner = giver
            receiver.property_list.remove(sq)
            giver.property_list.append(sq)
        cash = offer.get("cash", 0)
        if cash:
            giver.transfer(-cash)
            receiver.transfer(cash)

    def _remove_player(self, idx):
        self.players.pop(idx)
        self.positions.pop(idx)
