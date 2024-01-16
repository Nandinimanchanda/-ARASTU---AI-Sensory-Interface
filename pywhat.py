import pywhatkit
# Send a WhatsApp Message to a Contact at 1:30 PM
pywhatkit.sendwhatmsg("+91 79881 13487", "ok", 20,6,True ,3)

# # Same as above but Closes the Tab in 2 Seconds after Sending the Message
# pywhatkit.sendwhatmsg("++91 7206671031", "Hi", 19, 40, 18, True, 2)

# # Send an Image to a Group with the Caption as Hello
# # pywhatkit.sendwhats_image("testgroup", "C:\Users\nandi\.vscode\ascii_art\laptop.jpg", "Hello")

# # Send an Image to a Contact with the no Caption
# # pywhatkit.sendwhats_image("+917206671031", "C:\Users\nandi\.vscode\ascii_art\laptop.jpg")

# # Send a WhatsApp Message to a Group at 12:00 AM
# pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

# Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly("testgroup", "Hey All!")

# Play a Video on YouTube
# pywhatkit.playonyt("PyWhatKit")