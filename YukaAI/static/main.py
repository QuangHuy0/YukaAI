from dotenv import load_dotenv
load_dotenv()
from kivy import app, clock
from yuka import Yuka

class MykivyApp(app.App):
    def build(self):
        yuka = Yuka()
        yuka.start_listening()
        
        self.update_event = clock.Clock.schedule_interval(yuka.update_circle, 1/60)
        self.btn_retation_event = clock.Clock.schedule_interval(yuka.circle.rotate_button, 1/60)
        
        return yuka
    
    
if __name__ == '__main__':
    MykivyApp = MykivyApp()
    MykivyApp.run()