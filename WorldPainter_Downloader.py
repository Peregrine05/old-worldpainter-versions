def main():
    version = str(input("Enter the WorldPainter version number to download: "))
    baseURL = "https://www.worldpainter.net/files/worldpainter_"
    
    # Download the Windows x64 installer.
    download(baseURL, version, ".exe", "/Installers/Windows/x64", "/worldpainter_", "Windows x64 installer")
    
    # Download the Windows x86 installer.
    download(baseURL + "32_", version, ".exe", "/Installers/Windows/x86", "/worldpainter_32_", "Windows x86 installer")
    
    # Download the macOS installer.
    download(baseURL, version, ".dmg", "/Installers/macOS", "/worldpainter_", "macOS installer")
    
    # Download the Linux Debian installer.
    download(baseURL, version, ".deb", "/Installers/Linux/Debian", "/worldpainter_", "Linux Debain installer")
    
    # Download the Linux Red Hat installer.
    download(baseURL, version, ".rpm", "/Installers/Linux/Red Hat", "/worldpainter_", "Linux Red Hat installer")
    
    # Download the Linux Other installer.
    download(baseURL, version, ".sh", "/Installers/Linux/Other", "/worldpainter_", "Linux Other installer")
    
    # Download the Windows x64 archive.
    download(baseURL, version, ".zip", "/Archives/Windows/x64", "/worldpainter_", "Windows x64 archive")
    
    # Download the Windows x86 archive.
    download(baseURL + "32_", version, ".zip", "/Archives/Windows/x86", "/worldpainter_32_", "Windows x86 archive")
    
    # Download the macOS archive.
    download(baseURL, version, ".tgz", "/Archives/macOS", "/worldpainter_", "macOS archive")
    
    # Download the Linux archive.
    download(baseURL, version, ".tar.gz", "/Archives/Linux/Other", "/worldpainter_", "Linux Other archive")
    
    
def download(baseURL, version, extension, folderPath, filePrefix, resourceName):
    subprocess.run(["mkdir", "-p", "WorldPainter/" + version + folderPath])
    print("\nAttempting to download the " + resourceName + " for the WorldPainter version specified...")
    try:
        wget.download(baseURL + version + extension, "WorldPainter/" + version + folderPath + filePrefix + version + extension)
    except:
        print("\nFailed to download the " + resourceName + " for the version of WorldPainter specified (" + version + ").")
        subprocess.run(["rmdir", "-p", "WorldPainter/" + version + folderPath])

import wget
import subprocess

main()
