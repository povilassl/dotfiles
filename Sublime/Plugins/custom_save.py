import sublime
import sublime_plugin
import datetime


class CustomSaveCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        original_default_dir = self.view.settings().get("default_dir")
        original_default_filename = self.view.settings().get("default_filename")

        custom_path = ""  # Replace with desired path
        self.view.settings().set("default_dir", custom_path)

        current_time = datetime.datetime.now()
        custom_filename = current_time.strftime("%Y%m%d%H%M%S") + ".txt"
        
        self.view.set_name(custom_filename)

        self.view.run_command("save")

        self.view.settings().set("default_dir", original_default_dir)
        self.view.settings().set("default_filename", original_default_filename)