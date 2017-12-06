import sublime, sublime_plugin
import sys 
import os
# import open osc
sys.path.append(os.path.join(os.path.dirname(__file__), "pythonosc"))
from pythonosc import osc_message_builder
from pythonosc import udp_client

#import http client
import http.client, urllib

#
# Setup for local Sonic Pi Server
#
sender = udp_client.SimpleUDPClient('127.0.0.1', 4557)

#
# Setup for Collaboration Webserver
#
url = '0.0.0.0:3000'
currentName = 'friedrich'
headers = {'Content-Type': 'text/plain'}
connection = http.client.HTTPConnection(url)


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
            sendCodeToCollabServer(currentName, code)
#
# Commands
#
class SpRunFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        code = getCurrentTextSelection(self.view)
        sendCodeToLocalServer(self.view.id(), code)

class SpStopAllJobsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sendStop()
        sublime.message_dialog('Sonic Pi: Stopped all jobs on the server')

class SpRunFileOnServerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        code = getCurrentTextSelection(currentName, self.view)
        sendCodeToCollabServer(currentName, code)



#
# helper functions
# 
def sendCodeToLocalServer(id, code):
    print('send: ', code)
    sender.send_message('/run-code', ['my_client', code])
def sendStop():
    sender.send_message('/stop-all-jobs', [])

def sendCodeToCollabServer(id, code):
    headers = {"Content-type": "text/plain"}
    connection.request('POST', '/run-code/'+id, code, headers)
    response = connection.getresponse()
    response.read()

def getCurrentTextSelection(view):
    return view.substr(sublime.Region(0, view.size()))


