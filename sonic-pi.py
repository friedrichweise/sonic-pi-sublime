import sublime, sublime_plugin
import sys 
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "pythonosc"))
from pythonosc import osc_message_builder
from pythonosc import udp_client

sender = udp_client.SimpleUDPClient('127.0.0.1', 4557)

#
# Global Plugin Running Commands
#
pluginRunning = False
class SpStartPlugin(sublime_plugin.ApplicationCommand):
    def run(self):
        print('Sonic Pi: Started Live Mode')
        global pluginRunning
        pluginRunning = True

class SpStopPlugin(sublime_plugin.ApplicationCommand):
    def run(self):
        print('Sonic Pi: Stopped Live Mode')
        global pluginRunning
        pluginRunning = False
    
class SaveListener(sublime_plugin.EventListener):
    def on_pre_save_async(self, view):
        code = getCurrentTextSelection(view)
        print(pluginRunning)
        if (pluginRunning):
            sendCode(view.id(), code)
#
# Commands
#
class SpRunFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        code = getCurrentTextSelection(self.view)
        sendCode(self.view.id(), code)

class SpStopAllJobsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sendStop()
        sublime.message_dialog('Sonic Pi: Stopped all jobs on the server')

#
# helper functions
# 
def sendCode(id, code):
    sender.send_message('/run-code', [id, code])
def sendStop():
    sender.send_message('/stop-all-jobs', [])

def getCurrentTextSelection(view):
    return view.substr(sublime.Region(0, view.size()))


