class BasePlayer:
    def __init__(self, game_init_det=None):
        """

        :param game_init_det: The necessary details provided by game while creating player object.
        """
        return
    def event_parse(self, event):
        """
        Parses the pygame event to specific format if player wants.
        :param event:
        :return: Parsed event.
        """
        return event

    def update(self, *args, **kwargs):
        """
        Updates the state of player according to the parameters provided by the game.
        :param kwargs: The paramters provided by the game.
        :return:
        """
        return

    def get_player_checks(self):
        """
        Returns the parameters neccessary for the game to check if player is in some special position(game over, etc).
        :return:
        """
        return

    def draw(self, surface):
        """
        Draws the player on the surface.
        :param surface:
        :return:
        """
        return
