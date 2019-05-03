from .splash import Splash

splash_page = None
running = False


# Initialise les objet gerant cette vue
def init_screen(option):
    global splash_page

    splash_page = Splash(option)


# Permet d'afficher de manière synchroniser les rendus des différents objets gérer par le module
def render_screen(window):
    global splash_page

    splash_page.render_part(window)


# Permet de lancer les processus de rendu
def show_screen():
    global splash_page
    global running

    running = True
    splash_page.start()


# Arrête proprement les processus de rendu
def stop_jobs():
    global splash_page
    global running

    running = False
    splash_page.kill()


# Permet de s'assurer que les processus de rendu sont bien terminer
def wait_job_end():
    global splash_page

    splash_page.join()


# Permet de propager l'event key au sous procecuse
def trigger_input(key):
    global splash_page

    splash_page.spread_key_event(key)


# Permet de prpager l'event click
def trigger_click(mouse_position):
    global splash_page

    splash_page.spread_mouse_click_event(mouse_position)

