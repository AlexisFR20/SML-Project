# import pandas as pd

# versiones = pd.read_html('http://jumxlmsl03/lms/versiones/')
# versiones = versiones[0].iloc[2:]
# versiones = versiones.iloc[::,1:]
# versiones = versiones.iloc[:-1:]
# print(versiones)
# proxcapc

# Abrir un exe
# import subprocess
# p = subprocess.Popen("C:\WINDOWS\CCM\ClientUX\SCClient.exe")


# abrir softwarecenter en winscp
# import webbrowser
# webbrowser.open("softwarecenter:SoftwareID=ScopeId_C37154BF-A1F4-4B62-B5FF-0CC6F41A762B/Application_a7748e45-eae3-42ae-bc24-999e58c00df7", new=2, autoraise=True)


# verificar permisos 
# import ctypes, os
# from sys import exit
 
 
# def is_admin():
#     is_admin = False
#     try:
#         is_admin = os.getuid() == 0
#     except AttributeError:
#         is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
 
#     print ("Admin privileges: {}".format(is_admin))
#     return is_admin

# is_admin()
