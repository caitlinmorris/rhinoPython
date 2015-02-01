## **RHINO+PYTHON**

###SLIDES

Slides from the workshop are available for view at the following link. Note that there are some links to reference sites in the slide comments!  A few links are also listed below.

**Slides:**

https://docs.google.com/presentation/d/15P91Es9HF49vPTRwVHxFhThQj9mXQTtJo2PhxgjfbSI/edit?usp=sharing

**rhinoPython reference:**

http://4.rhino3d.com/5/ironpython/index.html

**Random library reference:**

https://docs.python.org/2/library/math.html

###**DOWNLOAD**

Working with Rhino and Python on OSX requires Rhinoceros 3D, the Python source library, and a text editor.

The (currently free) OSX version of Rhino can be downloaded from here:

**http://www.rhino3d.com/download/rhino-for-mac/5.0/wip**

Komodo Edit is recommended as a text editor because it enables autocomplete and syntax support for IronPython and RhinoScript functions. 

Komodo Edit is free and open source, available for download here:

**http://komodoide.com/download/edit-osx/**

Other Python-compatible text editors like XCode, Sublime, TextWrangler etc will also work (but without Rhino syntax recognition).

The rhinoPython source library can be downloaded here:

**https://github.com/mcneel/rhinopython**

###**INSTALL**

Install the rhinopython folder at path:

**User/Library/Application Support/McNeel/Rhinoceros/scripts/**

To enable Rhino syntax support in Komodo Edit, open Komodo Edit and navigate to the Python language preference window:

**Komodo->Preferences->Languages->Python**

Under "Additional Python Import Directories", add a new directory path and point to the python lib folder:

**User/Library/Application Support/McNeel/Rhinoceros/MacPlugIns/IronPython/settings/lib**
