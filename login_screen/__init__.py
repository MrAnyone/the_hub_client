import sound_manager
from . import background
from .login import Login
from .password_forget import PasswordForget
from .create_account import CreateAccount

splash_page = None
running = False
login_background_thread = None
sub_part_to_render = [None, None, None]
sub_part_to_render_index = 0


# Initialise les objet gerant cette vue
def init_screen(option):
    global login_background_thread
    global sub_part_to_render
    sub_part_to_render[0] = Login(option)
    sub_part_to_render[1] = CreateAccount(option)
    sub_part_to_render[2] = PasswordForget(option)
    login_background_thread = background.init_background(option)
    sound_manager.SoundMgr.load_new_sound(name='main_theme',
                                          path='./common_assets/sound/musics/Out of my dreams NES.wav')
    sound_manager.SoundMgr.volume(name='main_theme', volume=0.2)


# Permet d'afficher de manière synchroniser les rendus des différents objets gérer par le module
def render_screen(window):
    global sub_part_to_render_index
    global sub_part_to_render
    global login_background_thread
    login_background_thread.render_part(window)
    sub_part_to_render[sub_part_to_render_index].render_part(window)


# Permet de lancer les processus de rendu
def show_screen():
    global sub_part_to_render_index
    global sub_part_to_render
    global login_background_thread
    global running
    running = True
    sub_part_to_render[sub_part_to_render_index].run()
    login_background_thread.start()
    sound_manager.SoundMgr.run_track('main_theme', -1)


# Arrête proprement les processus de rendu
def stop_jobs():
    global sub_part_to_render_index
    global sub_part_to_render
    global login_background_thread
    global running
    running = False
    sub_part_to_render[sub_part_to_render_index].kill()
    login_background_thread.kill()


# Permet de s'assurer que les processus de rendu sont bien terminer
def wait_job_end():
    global sub_part_to_render_index
    global sub_part_to_render
    global login_background_thread
    login_background_thread.join()
    # login_page_thread.join()


# Permet de propager l'event key au sous procecuse
def trigger_input(key):
    global sub_part_to_render_index
    global sub_part_to_render
    sub_part_to_render[sub_part_to_render_index].spread_key_event(key)


# Permet de prpager l'event click
def trigger_click(mouse_position):
    global sub_part_to_render_index
    global sub_part_to_render
    sub_part_to_render[sub_part_to_render_index].spread_mouse_click_event(mouse_position, sub_part_to_render_index)

