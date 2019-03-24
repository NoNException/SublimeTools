import sublime
from sublime import Region
import sublime_plugin 

def insert_at_first(view,edit,position,content):
	view.insert(edit,position,content+"\n")


class ToolsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		insert_at_first(self.view,edit,0,"and")
		line_all=Region(0,-1)
		a = self.view.lines(line_all)
		insert_at_first(self.view,edit,0,str(a))
