import collections
import numbers
from functools import partial

import pygame

import pgzero.keyboard

_pressed = set()
GAMEPADS = {
    0: {
        "id": 0,
        "keybindings": {
            "dpadleft": pygame.K_LEFT,
            "dpadright": pygame.K_RIGHT,
            "dpadup": pygame.K_UP,
            "dpaddown": pygame.K_DOWN,
        }
    },
    1: {
        "id": 1,
        "keybindings": {
            "dpadleft": pygame.K_a,
            "dpadright": pygame.K_d,
            "dpadup": pygame.K_w,
            "dpaddown": pygame.K_s,
        }
    },
}


def _joy_axis_release(joy=0, axis=0):
    # joy axis release events are the same for right&left or up&down
    # so look into _pressed set to see what was previously pressed.
    # but be wary:
    #  on joystick initialize the 'release' events for both axes are sent
    # TODO: we might want to not add those events to _pressed set
    dpads = ("dpadleft", "dpadright") if axis == 0 else ("dpadup", "dpaddown")
    option1 = GAMEPADS.get(joy, {}).get("keybindings", {}).get(dpads[1])
    option2 = GAMEPADS.get(joy, {}).get("keybindings", {}).get(dpads[0])
    if option1 in _pressed:
        return option1
    if option2 in _pressed:
        return option2
    return None


JoystickAxisEvent = collections.namedtuple(
    'JoystickAxisEvent',
    'type,joy,axis,value'
)

JOYSTICK_MAPPING_PRESSED = {
    # gamepad 0
    JoystickAxisEvent(
        type=pygame.JOYAXISMOTION, joy=0, axis=0, value=-1
    ): GAMEPADS.get(0, {}).get("keybindings", {}).get("dpadleft"),
    JoystickAxisEvent(
        type=pygame.JOYAXISMOTION, joy=0, axis=0, value=1
    ): GAMEPADS.get(0, {}).get("keybindings", {}).get("dpadright"),
    JoystickAxisEvent(
        type=pygame.JOYAXISMOTION, joy=0, axis=1, value=-1
    ): GAMEPADS.get(0, {}).get("keybindings", {}).get("dpadup"),
    JoystickAxisEvent(
        type=pygame.JOYAXISMOTION, joy=0, axis=1, value=1
    ): GAMEPADS.get(0, {}).get("keybindings", {}).get("dpaddown"),

    # gamepad 1
    JoystickAxisEvent(
        type=pygame.JOYAXISMOTION, joy=1, axis=0, value=-1
    ): GAMEPADS.get(1, {}).get("keybindings", {}).get("dpadleft"),
    JoystickAxisEvent(
        type=pygame.JOYAXISMOTION, joy=1, axis=0, value=1
    ): GAMEPADS.get(1, {}).get("keybindings", {}).get("dpadright"),
    JoystickAxisEvent(
        type=pygame.JOYAXISMOTION, joy=1, axis=1, value=-1
    ): GAMEPADS.get(1, {}).get("keybindings", {}).get("dpadup"),
    JoystickAxisEvent(
        type=pygame.JOYAXISMOTION, joy=1, axis=1, value=1
    ): GAMEPADS.get(1, {}).get("keybindings", {}).get("dpaddown"),
}


JOYSTICK_MAPPING_RELEASED = {
    # gamepad 0
    JoystickAxisEvent(
        type=pygame.JOYAXISMOTION, joy=0, axis=0, value=0
    ): partial(_joy_axis_release, joy=0, axis=0),
    JoystickAxisEvent(
        type=pygame.JOYAXISMOTION, joy=0, axis=1, value=0
    ): partial(_joy_axis_release, joy=0, axis=1),

    # gamepad 1
    JoystickAxisEvent(
        type=pygame.JOYAXISMOTION, joy=1, axis=0, value=0
    ): partial(_joy_axis_release, joy=1, axis=0),
    JoystickAxisEvent(
        type=pygame.JOYAXISMOTION, joy=1, axis=1, value=0
    ): partial(_joy_axis_release, joy=1, axis=1),
}


def initialize_joysticks():
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    for joystick in joysticks:
        print ("initializing joystick {}".format(joystick))
        joystick.init()


def _get_joy_event_elems(event):
    axis = getattr(event, 'axis', None)
    value = getattr(event, 'value', None)
    joy = getattr(event, 'joy', None)
    return axis, value, joy


def map_joy_event_key_down(event):
    axis, value, joy = _get_joy_event_elems(event)
    if value is None or not isinstance(value, numbers.Number):
        return
    key = JOYSTICK_MAPPING_PRESSED.get((event.type, joy, axis, round(value)))
    if key:
        _pressed.add(key)
    return key


def map_joy_event_key_up(event):
    axis, value, joy = _get_joy_event_elems(event)
    if value is None or not isinstance(value, numbers.Number):
        return
    partial_func = JOYSTICK_MAPPING_RELEASED.get((event.type, joy, axis, round(value)))
    key = partial_func() if callable(partial_func) else None
    if key:
        _pressed.remove(key)
    return key


def process_event(event):
    was_joystick_down = pgzero.controller.map_joy_event_key_down(event)
    was_joystick_up = pgzero.controller.map_joy_event_key_up(event)
    if was_joystick_down:
        pgzero.keyboard.keyboard._press(was_joystick_down)
        new_event = pygame.event.Event(pygame.KEYDOWN, key=was_joystick_down)
        pygame.event.post(new_event)
        return True
    elif was_joystick_up:
        pgzero.keyboard.keyboard._release(was_joystick_up)
        new_event = pygame.event.Event(pygame.KEYUP, key=was_joystick_up)
        pygame.event.post(new_event)
        return True
    return False