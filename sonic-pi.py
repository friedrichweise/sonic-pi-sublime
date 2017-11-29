import sublime, sublime_plugin
import sys 
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "pythonosc"))
from pythonosc import osc_message_builder
from pythonosc import udp_client

sender = udp_client.SimpleUDPClient('127.0.0.1', 4557)

class SonicPi(sublime_plugin.EventListener):
    def on_post_save(self, view):
        text = view.substr(sublime.Region(0, view.size()))
        sender.send_message('/run-code', ['0', text])

