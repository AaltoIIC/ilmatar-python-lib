# Crane library

This git repository is python library for [Ilmatar](https://aalto.fi/ilmatar) crane located at [AIIC](https://www.aalto.fi/aiic) premises.  
It contains functions to get crane's location and move the crane via its OPC UA Interface.  

The current version works with following OPC UA interfaces versions:
* Control Interface V1.2
* Interface V1.5

Table of contents
====
* [Crane library](#crane-library)
* [Table of contents](#table-of-contents)
* [Getting ready](#getting-ready)
  * [Cloning git repository](#cloning-git-repository)
  * [Installing python libraries](#installing-python-libraries)
* [Examples](#examples)
* [Contributors](#contributors)
* [License](#license)
* [Build with](#build-with)

# Getting ready

## Cloning git repository
Git repository can be cloned with following command:  
`git clone git@github.com:AaltoIIC/ilmatar-python-lib.git`

## Installing python libraries
Program needs following python libraries to work:  
* [FreeOpcUa](https://github.com/FreeOpcUa/opcua-asyncio)

These can be installed with command from repository's root folder:
* `pip3 install -r requirements.txt`

# Examples

Examples can be found from folder [examples](/examples)

# Contributors
[Contributors](/CONTRIBUTORS.md)

# License
* [MIT](/LICENSE.txt)  

# Built with
* [FreeOpcUa](https://github.com/FreeOpcUa/python-opcua)
