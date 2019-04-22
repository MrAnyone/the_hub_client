from threading import Thread


class Login(Thread):

    def __init__(self, pygame_instance, screen_option):
        Thread.__init__(self)
        self.ready = True

    def run(self):
        while self.ready:
            # todo: affichage des champs de saisie de donnée + boutton de connexion + creation de compte et mdp oublier
            pass

    def kill(self):
        self.ready = False
