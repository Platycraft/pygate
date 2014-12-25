import subprocess
import os
from core import lob

path = {'minecraft_path': '/root/Minecraft/'}


def installer():

    # Install Script
    V = True
    while V:
        version = raw_input("What version will you like to install? ")
        if version == "1.8":
            m_v = "Offical Minecraft 1.8"
            m_d = "https://s3.amazonaws.com/Minecraft.Download/versions/1.8/minecraft_server.1.8.jar"
            break
        elif version == "Tekkit":
            m_v = version['Tekkit']
            m_d = version['Tekkit']
            break
        else:
            lob.output_r("Invalid Version")
    server = raw_input("Server Name: ")
    if os.path.exists(server):
        lob.output_b("Server {} Already Exist".format(server))
        pass
    else:
        ram = raw_input("Ram: ")
        c = path['minecraft_path']+server
        os.makedirs(c)

        lob.output_b("Opening Minecraft Port")

        subprocess.call("ufw allow 25565", shell=True)

        lob.output_b("Creating Directory")
        lob.output_b("Created Directory {}".format(c))

        lob.output_b("Downloading {}".format(m_v))
        # Need to add logic to check for pre downloaded minecraft jar
        subprocess.call("wget {}".format(m_d), shell=True)

        lob.output_b("Creating Startup Script")
        subprocess.call("echo 'java -Xmx{}M -Xms{}M -jar minecraft_server -nogui' > {}/start.sh".format(c, ram, ram, c), shell=True)
        subprocess.call("echo eula=true > eula.txt", shell=True)

        lob.output_b("Moving files to {}".format(c))
        subprocess.call("mv minecraft_server.1.8.jar {}/minecraft_server.jar".format(c), shell=True)
        subprocess.call("mv eula.txt {}".format(c), shell=True)

        lob.output_b("Setting Permissons for {}".format(c))

        lob.output_b("Before")
        subprocess.call("ls -la {}".format(c), shell=True)
        subprocess.call("chmod 755 {}/start.sh".format(c), shell=True)

        lob.output_b("After")
        subprocess.call("ls -la {}".format(c), shell=True)

        lob.output_b("Complete")
        lob.output_b("The server is now installed in {}".format(c))