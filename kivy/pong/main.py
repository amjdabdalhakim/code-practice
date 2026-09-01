from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongPaddle(Widget):
    score = NumericProperty(0)
    def bounce_ball(self, ball, delay=0):
        if delay > 0:
            delay -= 1
        if self.collide_widget(ball) and delay == 0:
            delay = 20
            speedup = 1.1
            offset = 0.01 * Vector(0, -abs(ball.center_y - self.center_y))
            ball.velocity = speedup * (offset + Vector(-ball.vx,ball.vy))
        return delay

class PongBall(Widget):
    vx = NumericProperty(0)
    vy = NumericProperty(0)
    velocity = ReferenceListProperty(vx, vy)
    
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    delay1, delay2 = 0, 0
    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width * 2 / 3:
            self.player2.center_y = touch.y
    def serve_ball(self, pointer=0):
        change = pointer * 180
        self.ball.center = self.center
        self.ball.velocity = Vector(0,7).rotate(randint(30 + change, 150 + change))
    def update(self, dt):
        self.ball.move()
        self.delay1 = self.player1.bounce_ball(self.ball, self.delay1)
        self.delay2 = self.player2.bounce_ball(self.ball, self.delay2) 
        if self.ball.x < 0:
            self.player2.score += 1
            self.serve_ball(1)
        if self.ball.x > self.width - self.ball.width:
            self.player1.score += 1
            self.serve_ball(0)
        if self.ball.y < 0 or self.ball.y > self.height - self.ball.height:
            self.ball.vy *= -1

class PongApp(App):
    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1/60)
        game.serve_ball()
        return game

if __name__ == '__main__':
    PongApp().run()