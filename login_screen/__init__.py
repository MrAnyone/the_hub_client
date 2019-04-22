from . import background
from .login import Login

login_page_thread = None
login_background_thread = None
running = False


def init_screen(pygame_instance, option):
    global login_page_thread
    global login_background_thread
    login_page_thread = Login(pygame_instance, option)
    login_background_thread = background.init_background(pygame_instance, option)


def show_screen():
    global login_page_thread
    global login_background_thread
    global running
    running = True
    login_page_thread.start()
    login_background_thread.start()


def stop_jobs():
    global login_page_thread
    global login_background_thread
    global running
    running = False
    login_page_thread.kill()
    login_background_thread.kill()


def wait_job_end():
    global login_page_thread
    global login_background_thread
    login_background_thread.join()
    login_page_thread.join()
