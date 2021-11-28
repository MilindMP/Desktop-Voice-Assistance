import datetime
import winsound


def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing, "%I:%M %p"))
    # print(altime)
    altime = altime[11:-3]
    # print(altime)
    Hrtime = altime[:2]
    Hrtime = int(Hrtime)
    Mntime = altime[3:5]
    Mntime = int(Mntime)
    print(f"Done, alarm is set for {Timing}")

    while True:
        if Hrtime == datetime.datetime.now().hour:
            if Mntime == datetime.datetime.now().minute:
                print("alarm is running...")
                winsound.PlaySound('abc', winsound.SND_LOOP)
            elif Mntime < datetime.datetime.now().minute:
                break


if __name__ == '__main__':
    alarm("06:09 PM")
