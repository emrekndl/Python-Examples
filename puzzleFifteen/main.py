from pynput import keyboard
from time import sleep
from board import board

b = board()

def main():
    b.shuffle()
    b.refresh()

    #print(b)
    # collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()



def on_press(key):
    b.refresh()

def on_release(key):
    if key == keyboard.Key.esc:
        #stop listener
        return False
    elif key == keyboard.Key.up:
        b.board1, b.empty_loc = b.move_up(b.board1, b.empty_loc)
    elif key == keyboard.Key.right:
        b.board1, b.empty_loc = b.move_right(b.board1, b.empty_loc)
    elif key == keyboard.Key.down:
        b.board1, b.empty_loc = b.move_down(b.board1, b.empty_loc)
    elif key == keyboard.Key.left:
        b.board1, b.empty_loc = b.move_left(b.board1, b.empty_loc)
    elif key == keyboard.Key.shift:
        print("Thinking...")
        moves = b.solve()
        for m in moves:
            b.moves[m](b.board1, b.empty_loc)
            b.refresh()
            sleep(1)


    return b.refresh()


if __name__ == "__main__":
    main()
