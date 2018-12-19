from Learn_Python_3_from_Beginner_to_Advanced.ps.ps import Ps


class Controller:
    def __init__(self):
        self.ps = None

    def connect(self, ps: Ps):
        """
        connect controller to PS
        :param ps: PS object that will be controlled with this controller
        :return: set self.ps to PS
        """
        pass

    def turn_on(self):
        pass

    def list_games(self):
        pass

    def start_game(self, game_id: int):
        pass
