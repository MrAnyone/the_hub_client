from threading import Thread


# Gére le contenue principale de la page de connection
class Login(Thread):

    def __init__(self, pygame_instance, screen_option):
        Thread.__init__(self)
        self.ready = True

    def run(self):
        while self.ready:
            # todo: affichage des champs de saisie de donnée + bouton de connexion + creation de compte et mdp oublier
            pass

    def kill(self):
        self.ready = False

    def render_part(self):
        pass
