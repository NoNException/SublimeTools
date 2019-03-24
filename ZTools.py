import sublime
from sublime import Region
import sublime_plugin

def insert_at_first(view,edit,position,content):
	view.insert(edit,position,content)


class ToolsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		all_rigion = sublime.Region(0, self.view.size())
		content = self.view.substr(all_rigion)
		content_list=content.split("\n")
		content_set=set(content_list)
		content_set=[x.strip() for x in content_set if x.strip()!='']
		content_list = list(content_set)
		content_list.sort()
		content_list="\n".join(content_list)
		self.view.erase(edit,all_rigion)
		insert_at_first(self.view,edit,0,str(content_list))

class AroundWithQuteCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		all_rigion = sublime.Region(0, self.view.size())
		content = self.view.substr(all_rigion)
		content_list=content.split("\n")
		new_content_list=['"'+x+'",' for x in content_list]
		new_content_list[-1]=new_content_list[-1][0:-1]
		self.view.erase(edit,all_rigion)
		new_content_list="\n".join(new_content_list)
		insert_at_first(self.view,edit,0,str(new_content_list))

