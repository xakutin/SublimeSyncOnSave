#
# SyncOnSavePlugin
#
import sublime
import sublime_plugin
import os
import shutil
import re
SETTINGS_FILE = "SyncOnSave.sublime-settings"


class SyncOnSavePlugin(sublime_plugin.EventListener):

    def _print_status(self, message):
        """ Prints a message in the SublimeText status bar """
        message = "SyncOnSave: " + message
        print(message)
        sublime.set_timeout(lambda: sublime.status_message(message), 2000)

    def _can_sync(self, source_file, directory):
        """
        Checks if a file can be copied to a synced directory
        """
        if (directory.get("sync_on_save", False)):
            try:
                #checks the file is in the include pattern
                regexp = directory.get("include_pattern", "")
                if (regexp and not re.match(regexp, source_file)):
                    return False
                #checks the file is in the exclude pattern
                regexp = directory.get("exclude_pattern", "")
                if (regexp and re.match(regexp, source_file)):
                    return False

            except Exception as err:
                self._print_status("Invalid pattern. Error: " + str(err))

            #checks the file is in the synchronized dir
            local_dir = directory.get("local", "")
            if (local_dir and source_file.find(local_dir) != -1):
                return True
        return False

    def _get_target_file(self, source_file, source_dir, target_dir):
        """
        Gets the path+filename where the source_file will be copied
        """
        rel_path = os.path.relpath(source_file, source_dir)
        return os.path.join(target_dir, rel_path)

    def _copy_file(self, source_file, source_dir, target_dir):
        """
        Copies a file to a target directory.
        It also creates the missing directories.
        """
        #gets the target file (with its full path)
        target_file = self._get_target_file(source_file, source_dir, target_dir)
        target_dir, file_name = os.path.split(target_file)
        try:
            #creates the path
            if (os.access(target_dir, os.F_OK) is False):
                os.makedirs(target_dir)

            #copies the file
            shutil.copy(source_file, target_file)
            self._print_status("'" + file_name + "' copied to '" + target_file + "'")

        except Exception as err:
            self._print_status(str(err))

    def _copy(self, source_file):
        """
        Copies a file to the mirror directories
        """
        settings = sublime.load_settings(SETTINGS_FILE)
        sync_directories = settings.get("sync_directories", [])
        #Loops the synchronized directories
        if len(sync_directories) > 0:
            for sync_directory in sync_directories:
                #checks the file must be copied to the mirror directory
                if (self._can_sync(source_file, sync_directory)):
                    local_dir = sync_directory.get("local", "")
                    mirror_dir = sync_directory.get("mirror", "")
                    if (local_dir and mirror_dir):
                        self._copy_file(source_file, local_dir, mirror_dir)

    def on_post_save(self, view):
        """When a file is saved, copy it to the mirror directories"""
        self._copy(view.file_name())
