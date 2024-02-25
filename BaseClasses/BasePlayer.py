class BasePlayer:
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

    def draw(self, surface):
        """
        Draws the player on the surface.
        :param surface:
        :return:
        """
        return
