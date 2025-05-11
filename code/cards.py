from dice import Throw
from player import Bank
from squares import Chance, CommunityChest

class Card:
    name = ""
    def action(self, board, player, *args, **kwargs):
        print("Card:", self.name)
        player.add_card(self)

class Chance(Card):
    """Chance card."""

    pass


class CommunityChest(Card):
    """Chance card."""

    pass


class AdvanceToGo(Card):

    name = "Advance to Go (Collect $200)"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        square = board.get_square_by_class(Start)
        board.move_player_to(None, None, player=player, square=square)


class BankError(CommunityChest):

    name = "Bank error in your favor - Collect $200"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), 200, player)


class DoctorFees(CommunityChest):

    name = "Doctor's Fees - Pay $50"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), -50, player)


class SaleStock(CommunityChest):

    name = "From sale of stock you get $50"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), 50, player)


class GetOutJailFree(Card):

    name = "Get Out of Jail Free - This card may be kept until needed or sold"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        player.add_card(self)


class GoToJailCard(Card):

    name = "Go to Jail - Go directly to jail - Do not pass Go - Do not collect $200"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        player.go_to_jail()


class GrandOperaNight(CommunityChest):

    name = "Grand Opera Night - Collect $50 from every player for opening night seats"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player_from_all(50, player)


class HolidayFund(CommunityChest):

    name = "Holiday Fund matures - Receive $100"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), 100, player)


class IncomeTaxRefund(CommunityChest):

    name = "Income tax refund - Collect $20"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), 20, player)


class Birthday(CommunityChest):

    name = "It is your birthday - Collect $10 from each player "

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player_from_all(20, player)


class LifeInsurance(CommunityChest):

    name = "Life insurance matures - Collect $100"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), 100, player)


class HospitalFees(CommunityChest):

    name = "Pay hospital fees of $100"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), -100, player)


class SchoolFees(CommunityChest):

    name = "Pay school fees of $150"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), -150, player)


class ConsultancyFees(CommunityChest):

    name = "Receive $25 consultancy fee"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), 25, player)


class StreetRepairs(CommunityChest):

    name = "You are assessed for street repairs - $40 per house - $115 per hotel"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), -40 * player.count_houses(), player)
        board.transaction_to_player(Bank(), -115 * player.count_hotels(), player)


class BeautyContest(CommunityChest):

    name = "You have won second prize in a beauty contest - Collect $10"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), 10, player)


class Inherit(CommunityChest):

    name = "You inherit $100"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), 100, player)


class AdvanceIllinois(Chance):

    name = "Advance to Illinois Ave. - If you pass Go, collect $200"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        square_index = board.get_square_index_by_name("Illinois Avenue")
        board.move_player_to(None, square_index, player=player)


class AdvanceStCharlesPlace(Chance):

    name = "Advance to St. Charles Place - If you pass Go, collect $200"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        square_index = board.get_square_index_by_name("St. Charles Place")
        board.move_player_to(None, square_index, player=player)


class AdvanceUtility(Chance):

    name = "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times the amount thrown"

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        target_square = board.get_square_by_class(Utility, from_square=kwargs["square"])
        owner = target_square.get_owner()
        if owner is None:
            # the user might whant to buy the square, so we just move_to
            board.move_player_to(None, None, player=player, square=target_square)
        elif owner is not player:
            # pay 3 times the through of a dice
            board.transaction_to_player(player, Throw.simple_amount() * 3, owner)
            board.move_player_to(
                None, None, player=player, square=target_square, process_square=False
            )


class AdvanceRailroad(Chance):

    name = "Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the Bank."

    def action(self, board, player, *args, **kwargs):
        """Move the player to the Go."""
        super().action(board, player, *args, **kwargs)
        target_square = board.get_square_by_class(
            TrainStation, from_square=kwargs["square"]
        )
        owner = target_square.get_owner()

        if owner is None:
            # the user might whant to buy the square, so we just move_to
            board.move_player_to(None, None, player=player, square=target_square)
        elif owner is not player:
            # pay 3 times the through of a dice
            board.transaction_to_player(player, target_square.compute_rent() * 2, owner)
            board.move_player_to(
                None, None, player=player, square=target_square, process_square=False
            )


class BankPays(Chance):

    name = "Bank pays you dividend of $50"

    def action(self, board, player, *args, **kwargs):
        """Make the transaction."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), 50, player)


class GoBack3Spaces(Chance):

    name = "Go Back 3 Spaces"

    def action(self, board, player, *args, **kwargs):
        """Make the transaction."""
        super().action(board, player, *args, **kwargs)
        board.move_player_n_square(None, -3, player=player)


class GeneralRepairs(Chance):

    name = "Make general repairs on all your property - For each house pay $25 - For each hotel $100"

    def action(self, board, player, *args, **kwargs):
        """Make the transaction."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), -25 * player.count_houses(), player)
        board.transaction_to_player(Bank(), -100 * player.count_hotels(), player)


class PoorTax(Chance):

    name = "Pay poor tax of $15"

    def action(self, board, player, *args, **kwargs):
        """Make the transaction."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), -15, player)


class TripReadingTrainStation(Chance):

    name = "Take a trip to Reading Railroad - If you pass Go, collect $200"

    def action(self, board, player, *args, **kwargs):
        """Make the transaction."""
        super().action(board, player, *args, **kwargs)
        square_index = board.get_square_index_by_name("Reading Railroad")
        board.move_player_to(None, square_index, player=player)


class TripBoardwalk(Chance):

    name = "Take a walk on the Boardwalk - Advance token to Boardwalk"

    def action(self, board, player, *args, **kwargs):
        """Make the transaction."""
        super().action(board, player, *args, **kwargs)
        square_index = board.get_square_index_by_name("Boardwalk")
        board.move_player_to(None, square_index, player=player)


class Chairman(Chance):

    name = "You have been elected Chairman of the Board - Pay each player $50"

    def action(self, board, player, *args, **kwargs):
        """Make the transaction."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player_from_all(-50, player)


class BuildingLoadMature(Chance):

    name = "Your building loan matures - Collect $150"

    def action(self, board, player, *args, **kwargs):
        """Make the transaction."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), -150, player)


class CrosswordCompetition(Chance):

    name = "You have won a crossword competition - Collect $10"

    def action(self, board, player, *args, **kwargs):
        """Make the transaction."""
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), 10, player)

class DoubleRent(Card):
    """Your next rent collection is doubled."""
    name = "Double Rent: Next rent you collect is doubled"
    def action(self, board, player, *args, **kwargs):
        super().action(board, player, *args, **kwargs)
        player.double_rent = True


class SkipNextTurn(Card):
    """You lose your next turn."""
    name = "Skip Next Turn: You lose your next turn"
    def action(self, board, player, *args, **kwargs):
        super().action(board, player, *args, **kwargs)
        player.skip_next_turns = getattr(player, "skip_next_turns", 0) + 1


class TaxRefundChance(Card):
    """Receive $100 refund from the bank."""
    name = "Tax Refund: Receive $100 from the bank"
    def action(self, board, player, *args, **kwargs):
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), 100, player)


class TaxRefundCC(Card):
    """Receive $75 refund from the bank."""
    name = "Tax Refund: Receive $75 from the bank"
    def action(self, board, player, *args, **kwargs):
        super().action(board, player, *args, **kwargs)
        board.transaction_to_player(Bank(), 75, player)



class DoubleRent(Chance):
    name = "Double Rent – Next rent you collect is doubled"
    def action(self, board, player, *args, **kwargs):
        super().action(board, player)
        player.double_rent = True
        print(f"{player} will collect double rent on next rent")

class SkipNextTurn(Chance):
    name = "Miss Next Turn – Skip your next turn"
    def action(self, board, player, *args, **kwargs):
        super().action(board, player)
        player.skip_next_turns += 1
        print(f"{player} will skip their next turn")

class TaxRefundChance(Chance):
    name = "Property Tax Refund (Chance)"
    def action(self, board, player, *args, **kwargs):
        super().action(board, player)
        refund = sum(sq.cash_on_land for sq in board.squares
                     if hasattr(sq, "cash_on_land") and sq.owner == player and sq.cash_on_land > 0)
        if refund:
            board.transaction_to_player(Bank(), refund, player)
            print(f"{player} receives ${refund} tax refund (Chance)")
        else:
            print(f"{player} has no taxes to refund")

class TaxRefundCC(CommunityChest):
    name = "Property Tax Refund (Community Chest)"
    def action(self, board, player, *args, **kwargs):
        super().action(board, player)
        refund = sum(sq.cash_on_land for sq in board.squares
                     if hasattr(sq, "cash_on_land") and sq.owner == player and sq.cash_on_land > 0)
        if refund:
            board.transaction_to_player(Bank(), refund, player)
            print(f"{player} receives ${refund} tax refund (Community Chest)")
        else:
            print(f"{player} has no taxes to refund")