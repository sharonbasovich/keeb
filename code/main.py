import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler  # Use your local encoder.py module
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys
keyboard = KMKKeyboard()

# Modules
layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules.append(Layers())
keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(MouseKeys())
# Matrix configuration
keyboard.col_pins = (
    board.GP2, board.GP3, board.GP4, board.GP5, board.GP6,
    board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
    board.GP12, board.GP13, board.GP14, board.GP15, board.GP16
)
keyboard.row_pins = (board.GP17, board.GP18, board.GP19, board.GP20, board.GP21)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Layer keys
FN1 = KC.MO(1)
FN2 = KC.MO(2)

# --- Layers ---
keyboard.keymap = [
    # Layer 0: Base
    [
        KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9,
        KC.N0, KC.MINUS, KC.EQUAL, KC.BSPC, KC.DEL,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O,
        KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.HOME,
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L,
        KC.SCLN, KC.QUOT, KC.ENTER, KC.NO, KC.PGUP, 
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT,
        KC.SLSH, KC.RSFT, KC.UP, KC.NO, KC.PGDN, KC.LCTL, KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.NO, KC.SPC, KC.NO, KC.NO,
        KC.RALT, FN1, FN2, KC.LEFT, KC.DOWN, KC.RGHT
    ],

    # Layer 1: FN1
    [
        KC.GRAVE, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9,
        KC.F10, KC.F11, KC.F12, KC.DEL, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.END,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.PGUP,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.PGUP, KC.NO, KC.PGDN,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.TRNS, KC.NO, KC.HOME, KC.NO, KC.END
    ],

    # Layer 2: FN2 (Media & Volume)
    [
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.MPLY, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.VOLU, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.TRNS, KC.MPRV, KC.VOLD, KC.MNXT
    ],
]

# --- Encoder Setup ---
encoder_handler.pins = [
    (board.GP27, board.GP28, board.GP26),  # Encoder 1 (A, B, Button)
    (board.GP1, board.GP0, board.GP22),    # Encoder 2 (A, B, Button)
]

encoder_handler.divisor = 4  # Optional, only needed if encoder skips steps

# encoder_handler.map = [
#     [[KC.VOLD], [KC.VOLU], [KC.MPLY]]
#     # [
#     #     [KC.LCTL, KC.MINUS],  # Represented as a list of keycodes to press together
#     #     [KC.LCTL, KC.EQUAL],
#     #     KC.PSCR,
#     # ]
# ]

# encoder_handler.map = [
#             ((KC.VOLU, KC.VOLD, KC.MPLY),),       
#             ((KC.MW_UP, KC.MW_DN, KC.PSCR),),      
#             ]

encoder_handler.map = [
    [
        (KC.VOLU,KC.VOLD,KC.MPLY),
        (KC.MW_UP, KC.MW_DN, KC.PSCR),
    ],
]

# Extra pins (handled as part of encoder buttons now — optional)
# Remove if redundant:
keyboard.extra_pins = ()
keyboard.extra_keymap = []

if __name__ == '__main__':
    keyboard.go()   
