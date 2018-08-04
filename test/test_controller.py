from unittest import TestCase
from types import SimpleNamespace
import pygame

from pgzero import controller
from pgzero import clock

class ControllerTest(TestCase):

    def test_controller_0_joy_right_event(self):
        """ pressing first controller joystick right axis event is converted """
        # pressed
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=0, axis=0, value=1)
        result = controller.map_joy_event_key_down(event)
        self.assertEqual(result, pygame.K_RIGHT)
        # released
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=0, axis=0, value=0)
        result = controller.map_joy_event_key_up(event)
        self.assertEqual(result, pygame.K_RIGHT)

    def test_controller_1_joy_right_event(self):
        """ pressing second controller joystick right axis event is converted  """
        # pressed
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=1, axis=0, value=1)
        result = controller.map_joy_event_key_down(event)
        self.assertEqual(result, pygame.K_d)
        # released
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=1, axis=0, value=0)
        result = controller.map_joy_event_key_up(event)
        self.assertEqual(result, pygame.K_d)

    def test_controller_2_joy_right_event(self):
        """ there's no third controller mapped, try joy right """
        # pressed
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=2, axis=0, value=1)
        result = controller.map_joy_event_key_down(event)
        self.assertTrue(result is None)
        # released
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=2, axis=0, value=0)
        result = controller.map_joy_event_key_up(event)
        self.assertTrue(result is None)

    def test_controller_0_joy_left_event(self):
        """ pressing first controller joystick left axis event is converted """
        # pressed
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=0, axis=0, value=-1)
        result = controller.map_joy_event_key_down(event)
        self.assertEqual(result, pygame.K_LEFT)
        # released
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=0, axis=0, value=0)
        result = controller.map_joy_event_key_up(event)
        self.assertEqual(result, pygame.K_LEFT)

    def test_controller_1_joy_left_event(self):
        """ pressing second controller joystick left axis event is converted  """
        # pressed
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=1, axis=0, value=-1)
        result = controller.map_joy_event_key_down(event)
        self.assertEqual(result, pygame.K_a)
        # released
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=1, axis=0, value=0)
        result = controller.map_joy_event_key_up(event)
        self.assertEqual(result, pygame.K_a)

    def test_controller_2_joy_left_event(self):
        """ there's no third controller mapped, try joy left """
        # pressed
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=2, axis=0, value=-1)
        result = controller.map_joy_event_key_down(event)
        self.assertTrue(result is None)
        # released
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=2, axis=0, value=0)
        result = controller.map_joy_event_key_up(event)
        self.assertTrue(result is None)

    def test_controller_0_joy_down_event(self):
        """ pressing first controller joystick down axis event is converted to keyboard down"""
        # pressed
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=0, axis=1, value=1)
        result = controller.map_joy_event_key_down(event)
        self.assertEqual(result, pygame.K_DOWN)
        # released
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=0, axis=1, value=0)
        result = controller.map_joy_event_key_up(event)
        self.assertEqual(result, pygame.K_DOWN)

    def test_controller_1_joy_down_event(self):
        """ pressing second controller joystick down axis event is converted."""
        # pressed
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=1, axis=1, value=1)
        result = controller.map_joy_event_key_down(event)
        self.assertEqual(result, pygame.K_s)
        # released
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=1, axis=1, value=0)
        result = controller.map_joy_event_key_up(event)
        self.assertEqual(result, pygame.K_s)

    def test_controller_2_joy_down_event(self):
        """ there's no third controller mapped, try joy down axis """
        # pressed
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=2, axis=1, value=1)
        result = controller.map_joy_event_key_down(event)
        self.assertTrue(result is None)
        # released
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=2, axis=1, value=0)
        result = controller.map_joy_event_key_up(event)
        self.assertTrue(result is None)

    def test_controller_0_joy_up_event(self):
        """ pressing first controller joystick up axis event is converted """
        # pressed
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=0, axis=1, value=-1)
        result = controller.map_joy_event_key_down(event)
        self.assertEqual(result, pygame.K_UP)
        # released
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=0, axis=1, value=0)
        result = controller.map_joy_event_key_up(event)
        self.assertEqual(result, pygame.K_UP)

    def test_controller_1_joy_up_event(self):
        """ pressing second controller joystick up axis event is converted  """
        # pressed
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=1, axis=1, value=-1)
        result = controller.map_joy_event_key_down(event)
        self.assertEqual(result, pygame.K_w)
        # released
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=1, axis=1, value=0)
        result = controller.map_joy_event_key_up(event)
        self.assertEqual(result, pygame.K_w)

    def test_controller_2_joy_up_event(self):
        """ there's no third controller mapped, try joy up axis """
        # pressed
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=2, axis=1, value=-1)
        result = controller.map_joy_event_key_down(event)
        self.assertTrue(result is None)
        # released
        event = pygame.event.Event(pygame.JOYAXISMOTION, joy=2, axis=1, value=0)
        result = controller.map_joy_event_key_up(event)
        self.assertTrue(result is None)
