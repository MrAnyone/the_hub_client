from . import background
from .login import Login

login_page_thread = None
login_background_thread = None
running = False


# Initialise les objet gerant cette vue
def init_screen(pygame_instance, option):
    global login_page_thread
    global login_background_thread
    login_page_thread = Login(pygame_instance, option)
    login_background_thread = background.init_background(pygame_instance, option)


# Permet d'afficher de manière synchroniser les rendus des différents objets gérer par le module
def render_screen():
    global login_page_thread
    global login_background_thread
    login_background_thread.render_part()
    login_page_thread.render_part()


# Permet de lancer les processus de rendu
def show_screen():
    global login_page_thread
    global login_background_thread
    global running
    running = True
    # login_page_thread.start()
    login_background_thread.start()


# Arrête proprement les processus de rendu
def stop_jobs():
    global login_page_thread
    global login_background_thread
    global running
    running = False
    login_page_thread.kill()
    login_background_thread.kill()


# Permet de s'assurer que les processus de rendu sont bien terminer
def wait_job_end():
    global login_page_thread
    global login_background_thread
    login_background_thread.join()
    # login_page_thread.join()


# Permet de propager l'event key au sous procecuse
def trigger_input(key):
    global login_page_thread
    login_page_thread.spread_key_event(key)


# Permet de prpager l'event click
def trigger_click(mouse_position):
    global login_page_thread
    login_page_thread.spread_mouse_click_event(mouse_position)

