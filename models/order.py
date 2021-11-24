class Order:

    def __init__(self, customer_name, order_date, quantity, boardgame_name, num_of_players, description):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.boardgame_name = boardgame_name
        self.num_of_players = num_of_players
        self.description = description