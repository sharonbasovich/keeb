import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.rotary_encoder import RotaryEncoder

keyboard = KMKKeyboard()
layers = Layers()
keyboard.modules.append(layers)

# Rotary Encoder Module
encoder = RotaryEncoder()
keyboard.modules.append(encoder)

# Matrix pins
keyboard.col_pins = (
    board.GP2, board.GP3, board.GP4, board.GP5, board.GP6,
    board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
    board.GP12, board.GP13, board.GP14, board.GP15, board.GP16
)
keyboard.row_pins = (board.GP17, board.GP18, board.GP19, board.GP20, board.GP21)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# FN keys for layers
FN1 = KC.MO(1)
FN2 = KC.MO(2)

# --- Base Layer (Layer 0) ---
keyboard.keymap = [
    [KC.ESC, KC._1, KC._2, KC._3, KC._4, KC._5, KC._6, KC._7, KC._8, KC._9, KC._0, KC.MINUS, KC.EQUAL, KC.BSPC, KC.DEL],
    [KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.HOME],
    [KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENTER, KC.NO, KC.PGUP],
    [KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP, KC.NO, KC.PGDN],
    [KC.LCTL, KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.NO, KC.SPC, KC.NO, KC.NO, KC.RALT, FN1, FN2, KC.LEFT, KC.DOWN, KC.RGHT],
]

# --- Layer 1: FN1 (F-keys & Navigation) ---
keyboard.keymap.append([
    [KC.GRAVE, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.DEL, KC.NO],
    [KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.END],
    [KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.PGUP],
    [KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.PGUP, KC.NO, KC.PGDN],
    [KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.TRNS, KC.NO, KC.HOME, KC.NO, KC.END],
])

# --- Layer 2: FN2 (Media & Volume) ---
keyboard.keymap.append([
    [KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO],
    [KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO],
    [KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.MPLY, KC.NO, KC.NO],
    [KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.VOLU, KC.NO, KC.NO],
    [KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.TRNS, KC.MPRV, KC.VOLD, KC.MNXT],
])

# --- Rotary Encoders ---
# Encoder 1: Volume control + Play/Pause
encoder.pins = (
    (board.GP27, board.GP28),  # Encoder 1
    (board.GP1, board.GP0),    # Encoder 2
)
encoder.map = [
    # Encoder 1
    ((KC.VOLD,), (KC.VOLU,)),  # CCW = Volume Down, CW = Volume Up
    # Encoder 2
    ((KC.LCTRL(KC.MINUS),), (KC.LCTRL(KC.EQUAL),)),  # Zoom Out / Zoom In
]

# Encoder buttons
ENC1_BTN = KC.MPLY  # Play/Pause
ENC2_BTN = KC.PSCR  # Screenshot

# We'll map these buttons in matrix-less keys
keyboard.extra_pins = (board.GP26, board.GP22)
keyboard.extra_keymap = [ENC1_BTN, ENC2_BTN]

if __name__ == '__main__':
    keyboard.go()
