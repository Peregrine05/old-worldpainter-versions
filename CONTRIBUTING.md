# Contributing

You can contribute by either creating an issue with the WorldPainter installers and archives attached, or creating a pull request (PR) with the files organized properly.

## Issue

If you are less experienced with GitHub, then you can contribute by creating an issue with the WorldPainter installers and archives that you have saved attached to the issue. Someone will eventually add them to the repository. An issue template for uploading WorldPainter installers and archives exists; you can use that. This template is located [here](https://github.com/Peregrine05/old-worldpainter-versions/issues/new?assignees=&labels=file+upload&template=worldpainter-installer-archive-upload.md&title=Upload+WorldPainter+%5Breplace+with+WorldPainter+version+number%5D).

Please attach installers and archives for only a single WorldPainter version to an issue. If you have installers and archives for more than one WorldPainter version, then please create separate issues for uploading installers and archives of each version of WorldPainter. If you have more than one installer or archive for a single version of WorldPainter, or if GitHub refuses to upload the file based on its file extension, then it is recommended to pack the installer(s) and/or archive(s) into a ZIP file and then attach that ZIP file.

If this process is too difficult for you, then you may simply attach the installers and archives that you have saved into a single issue; someone else can sort everything out later.

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

Place the installers and archives that you haved saved into the proper folders. Please do not create an empty folder if you do not have the corresponding installer / archive; this is to avoid confusing users browsing the repository. Additionally, please close any open issues that this PR would solve when merged; then submit your PR.
