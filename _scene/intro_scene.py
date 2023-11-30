from scene import Scene
from _visual.intro_visual import IntroVisual
from _logic.intro_logic import IntroLogic
class IntroScene(Scene):
    def run_first_time(self,screen):
        self.intro_scene = IntroVisual(screen)
        # self.intro_scene.draw_background()
        self.intro_scene.draw_logo()
        self.intro_scene.draw_loading_bar_background()
        self.intro_logic = IntroLogic()
        pass

    def run_all_time(self,event):
        elapsed_time = self.intro_logic.handle_event(event)
        self.intro_scene.draw_loading_bar(elapsed_time)
        self.intro_logic.check_time()
        pass