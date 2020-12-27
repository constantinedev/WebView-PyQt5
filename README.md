# WebView-PyQt5<br>
---------------------------------------------------------------------------------------------
I have try to build a WebView Application using python<br>
So What I have to try pywebview and PyQt5 are most popular of the network Framwork had to been used.<br>
But I have try all the update with PyQt5 and pywebview buit to run on #Win10<br>
So why we most we have too much problum are using in with the #PyInstaller
<br><br>
Most FW are not work after the pyinstaller with the new python3.7+ and pywebview<br>
<br>
I just only can make it work with PyQt5 and running well in Window10
So what are the code?<br>
The run.py are just the Core WebView of the PyQt5 Updated FW <br>
Even you can buid with you own with PyInstaller<br>
<br><br><br>
==WHAT HAVE YOU SHOUD INSTALL==<br>
<code>python3 -m pip install PyQt5 PyQt5-tools pyqtwebengine PyInstaller</code><br>
run the pip to install the top also (It just taget for Window in main)<br>
<br><br><br>
==CAN IT WORK ON OSX OR LINUX==<br>
It should be work but may be some of the API and patch you should be make it by your own<br>
<br><br><br>
==PyInstaller Builder==<br>
To build the code to EXE file from PyInstaller<br>
---------------------------------------------------------------------------------------------
you should have to install the pyinstaller from pip befor<br>
----------------------------------------
<code>python3.8 -m pip install PyInstaller</code><br>
----------------------------------------
--build the exe--<br>
(For Windows)<br>
--------------------------------------------
<code>pyinstaller -wF -n DemoWebView .\run.py</code><br>
--------------------------------------------
The file will output to the 'dist' folder<br>
The file should be bigger the 100M so I can't try to upload the demo EXE file you<br>
If you have any problem try asking us in Issues<br>
Open question<br>
<br>
I really want to make the webview just for pywebview<br>
But I don't know why what are the pyinstaller can't execute the view after build<br>
If you have and idea of make it on pywebview and work for after pyinstaller builder<br>
Let each other know! You are Welcome<br>
<br>
I have teset again with Raspberry Pi 3B+ and Pi4<br>
it should revommand to run with the python3.6 version the 3.7+ are not support the qt5 better as well<br>
