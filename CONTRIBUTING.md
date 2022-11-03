# Contributing

You can contribute by either creating an issue with the WorldPainter installers and archives attached, or creating a pull request (PR) with the files organized properly.

## Issue

If you are less experienced with GitHub, then you can contribute by creating an issue with the WorldPainter installers and archives that you have saved attached to the issue. Someone will eventually add them to the repository.

## Pull Request (PR)

If you want to create a pull request, then please organize the files properly.

First of all, please keep the original names of the installers. Do not rename them, and if they have ever been renamed, then please try to name them like the other installers / archives.

The directory (folder) tree should be as follows:

```
/WorldPainter
  - <version number>
    - Windows
      - x64
        - worldpainter_<version number>.exe
        - worldpainter_<version number>.zip
      - x86
        - worldpainter_32_<version number>.exe
        - worldpainter_32_<version number>.zip
    - macOS
      - worldpainter_<version number>.dmg
      - worldpainter_<version number>.tgz
    - Linux
      - Debian
        - worldpainter_<version number>.deb
      - Red Hat
        - worldpainter_<version number>.rpm
      - Other
        - worldpainter_<version number>.sh
        - worldpainter_<version number>.tar.gz
```

Place the installers and archives that you haved saved into the proper folders, and then submit your pull request. Please do not create an empty folder if you do not have the corresponding installer / archive; this is to avoid confusing users browsing the repository.
