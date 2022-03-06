"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pixo-Memo"
SPRITE_SCALING_RED = 0.5

# Variables used in the game

answer = []
sequence = []
number_of_colours = 4
colours = {
  1 : "red",
  2 : "green",
  3 : "blue",
  4 : "yellow"
}

class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # If you have sprite lists, you should create them here,
        # and set them to None

        self.red_list = None
        self.red_sprite = None

        # Sets coordinates for coloured squares. One on-screen, and one off-screen.
        self.red_x = 300
        self.red_y = 400
        self.deep_red_x = -100
        self.deep_red_y = -100

        self.green_x = 500
        self.green_y = 400
        self.deep_green_x = -100
        self.deep_green_y = -100

        self.yellow_x = 300
        self.yellow_y = 200
        self.deep_yellow_x = -100
        self.deep_yellow_y = -100
        
        self.blue_x = 500
        self.blue_y = 200
        self.deep_blue_x = -100
        self.deep_blue_y = -100

        arcade.set_background_color(arcade.color.BLACK)

        


    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here

        self.red_list = arcade.SpriteList()
        
        img = "D:/Programming/Pixo-Memo/images/red.png"
        self.red_sprite = arcade.Sprite(img, SPRITE_SCALING_RED)
        self.red_sprite.center_x = 300
        self.red_sprite.center_y = 400
        self.red_list.append(self.red_sprite)
        

                
    def on_draw(self):
        """
        Render the screen.
        """
                
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        
        # Call draw() on all your sprite lists below

        arcade.draw_rectangle_filled(self.red_x, self.red_y, 100, 100, arcade.color.RED, 90)
        self.red_list.draw()
        arcade.draw_rectangle_filled(self.deep_red_x, self.deep_red_y, 100, 100, arcade.color.BURGUNDY, 90)    

        arcade.draw_rectangle_filled(self.green_x, self.green_y, 100, 100, arcade.color.GREEN, 90)
        arcade.draw_rectangle_filled(self.deep_green_x, self.deep_green_y, 100, 100, arcade.color.CADMIUM_GREEN, 90)  

        arcade.draw_rectangle_filled(self.yellow_x, self.yellow_y, 100, 100, arcade.color.YELLOW, 90)
        arcade.draw_rectangle_filled(self.deep_yellow_x, self.deep_yellow_y, 100, 100, arcade.color.DARK_GOLDENROD, 90)  

        arcade.draw_rectangle_filled(self.blue_x, self.blue_y, 100, 100, arcade.color.BLUE, 90)
        arcade.draw_rectangle_filled(self.deep_blue_x, self.deep_blue_y, 100, 100, arcade.color.DARK_MIDNIGHT_BLUE, 90)  

        



        # arcade.finish_render()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        if sequence == answer:
            print("YAY!")
            exit()
        


    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        # Check the mouse coordinates when LEFt button is clicked,
        # if it is within a certain area move the second square on top.
        # This gives the illusion that the button is being clicked.
        

        if button == arcade.MOUSE_BUTTON_LEFT:
            if x >= 250 and x <= 350 and y >= 350 and y <= 450:
                self.deep_red_x = self.red_x
                self.deep_red_y = self.red_y
                sequence.append("red")
                print("Red")
            elif x >= 450 and x <= 550 and y >= 350 and y <= 450:
                self.deep_green_x = self.green_x
                self.deep_green_y = self.green_y
                sequence.append("green")
                print("Green")
            elif x >= 450 and x <= 550 and y >= 150 and y <= 250:
                self.deep_blue_x = self.blue_x
                self.deep_blue_y = self.blue_y
                sequence.append("blue")
                print("Blue")
            elif x >= 250 and x <= 350 and y >= 150 and y <= 250:
                self.deep_yellow_x = self.yellow_x
                self.deep_yellow_y = self.yellow_y
                sequence.append("yellow")
                print("Yellow")
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse button pressed at", x, y)
            print(sequence)
            print(answer)


    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """

        # Moves the second darker square off of the screen,
        # This give the illusion the button is being released.
        self.deep_red_x = -100
        self.deep_red_y = -100

        self.deep_green_x = -100
        self.deep_green_y = -100

        self.deep_blue_x = -100
        self.deep_blue_y = -100

        self.deep_yellow_x = -100
        self.deep_yellow_y = -100

    def game(self):
        for i in range(number_of_colours):
            x = randint(1,4)
            colour = colours[x]
            answer.append(colour)



def main():
    """ Main function """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    game.game()
    arcade.run()
    


if __name__ == "__main__":
    main()
