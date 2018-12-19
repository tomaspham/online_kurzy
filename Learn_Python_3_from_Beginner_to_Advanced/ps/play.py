from Learn_Python_3_from_Beginner_to_Advanced.ps.controller import Controller
from Learn_Python_3_from_Beginner_to_Advanced.ps.ps import Ps
from pynput.keyboard import Key, Listener

ps = Ps()
game_list = ['GTA V', 'Crossout', 'Rocket League']
for game in game_list:
    ps.load_game(game)

controller = Controller()

# games = controller.list_games()
# controller.start_game(game)
# controller.ps_status()
# controller.end_game(game)
# controller.turn_off()

print("Start PS ? (y/n)")


def on_press(key):
    games = None
    status = controller.ps_status()

    if key.char == 'y' and status == 'off':
        print('PS started and controller is connected')
        controller.connect(ps)
        controller.turn_on()

        games = controller.list_games()

    elif key.char == 'l' and status == 'on':
        print('Choose your game to play')
        for game in games:
            print(f"Press: {game['id']} for {game['name']}")

    elif key.char in games.keys() and status == 'on':
        controller.start_game(key.char)

    # TODO: add end game + check if game is running
    # Code here:

    # TODO: add action to see what game are we currently playing
    # Code here:


def on_release(key):
    if key == Key.esc:
        print('Turning off PS')
        controller.turn_off()
        # Stop listener
        return False


# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
