# SyncOnSave

SyncOnSave is a Sublime Text package that synchronises your files when you save them.<br>
It works on SublimeText version 2 and 3.


## Installation
  ```
  cd <sublimetext_packages_directory>
  git clone https://github.com/xakutin/SublimeSyncOnSave.git
  ```

## Settings
The settings can be found in
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
          
      //Destination path where the plugin copies the saved file with its relative path respect to the local path
      "mirror": "/home/xakutin/www/",
          
      //Regular expresion for copy only the files that match the pattern
      "include_pattern": "",
          
      //Regular expresion for exclude files or paths
      "exclude_pattern": ""
    }
  ]
}
```
