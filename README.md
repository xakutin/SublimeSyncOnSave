# SyncOnSave

Sublime Text package that synchronises your files when you save them. When you save a file it is copied to the mirror directories with its relative path.<br>
It works on SublimeText version 2 and 3.


## Installation
* Using Package Control (recommended) <br>
  Search for "SyncOnSave" and install it

* Manually
  ```
  cd <sublimetext_packages_directory>
  git clone https://github.com/xakutin/SublimeSyncOnSave.git
  ```

## Settings
After installing the package its default settings can be found in
`Preferences > Package Settings > SyncOnSave > Settings Default`.
Remember to put your own settings in `Settings - User`

Here is an example of a settings file with comments that explains the meaning of each property:

```
{
    "sync_directories": [
        {
        	//Flag that indicates if the path must be synced or not
            "sync_on_save": true,
        	//Path to be synchronized
            "local": "/home/xakutin/Projects/deTapeo/src/",
            //Destination path where the plugin copies the saved file
            //with its relative path respect to the local path
            "mirror": "/home/xakutin/www/",
            //Regular expresion for copy only the files that match the pattern
            "include_pattern": "",
            //Regular expresion for exclude files or paths
            //eg:
            //.*(\\.sublime-settings|\\.py)$
            //.*(/old/|/bak/).*
            "exclude_pattern": ""
        }
    ]
}
```
