import subprocess
import time

payload ={"contact_name":"", "message":""}

cmds = {
    "wake_up":{"cmd":"adb shell input keyevent KEYCODE_WAKEUP"},
    "unlock":{"cmd":"adb shell input swipe 524 1505 554 904 && adb shell input text saimsucharith && adb shell input keyevent 66"},
    "navigate":{"cmd":"adb shell input swipe 524 1505 554 904 && adb shell input tap 315 217 && adb shell input text whatsa && adb shell input tap 127 1064"},
    "whatspwd":{"cmd":"adb shell input tap 529 785 && adb shell input text saimsucharith && adb shell input tap 971 2111"},
    "person":{"cmd":"adb shell input tap 891 135 && adb shell input text {} && adb shell input tap 423 305", "payload": "person"},
    "process_1":{"cmd":"adb shell input tap 329 2143"},
    "process_2":{"cmd":"adb shell input text {} && adb shell input tap 975 2125","payload":"msg"}}


def perform(action, input=None):
    data = ""
    if action.get("payload"):
        if action.get("payload") == "person":
            data = action.get("cmd").format(input["person"])
        elif action.get("payload") == "msg":
            data = action.get("cmd").format(input["msg"])
    else:
        data = action.get("cmd")
    subprocess.call(data, shell=True)

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
text = text.replace(" ", "%s")
text = text.replace("'", "")
request = {"person":"Vishanth", "msg":text}
for i in cmds:
    print(i)
    perform(cmds[i],request)
    time.sleep(1)

