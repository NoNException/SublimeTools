import sublime
import sublime_plugin 

def insert_at_first(view,edit,position,content):
	view.insert(edit,position,content)


class aCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		insert_at_first(self.view,edit,0,"aCommand")
		line_all=self.Region(0,-1)
		self.view.erase(line_all)
		
