#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyaudio, wave, sys, time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class DigitalClock(QLCDNumber):
    def __init__(self, parent=None):
        super(DigitalClock, self).__init__(parent)

        self.setSegmentStyle(QLCDNumber.Filled)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()

        self.setWindowTitle("Digital Clock")

        btn_start = QPushButton('Starten', self)
        btn_start.move(50, 100)
        btn_start.setToolTip("Ansage starten...")
        btn_start.clicked.connect(self.play)

        self.resize(150, 60)
        self.show()

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]

        self.display(text)


    def closeEvent(self, event):
        dialog = QMessageBox.question(self, 'Nachricht', "Soll die Anwendung geschlossen werden?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if dialog == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def play(self, event):
        deke = True
        zeit = QTime.currentTime()
        #stunde = time.toString('hh')
        stunde = time.strftime("%I") #%I = 12format / %H = 24format
        minute = zeit.toString('mm')

        self.play_audio_file("wave\\seht.wav")
        self.play_audio_file("wave\\" + stunde + ".wav")

        if int(minute) == 0:
            deke = False
            pass
        elif int(minute) <= 20 and int(minute) >= 1:
            self.play_audio_file("wave\\" + minute + ".wav")
        elif "21" in minute:
            self.play_audio_file("wave\\20.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\01.wav")
        elif "22" in minute:
            self.play_audio_file("wave\\20.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\02.wav")
        elif "23" in minute:
            self.play_audio_file("wave\\20.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\03.wav")
        elif "24" in minute:
            self.play_audio_file("wave\\20.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\04.wav")
        elif "25" in minute:
            self.play_audio_file("wave\\20.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\05.wav")
        elif "26" in minute:
            self.play_audio_file("wave\\20.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\06.wav")
        elif "27" in minute:
            self.play_audio_file("wave\\20.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\07.wav")
        elif "28" in minute:
            self.play_audio_file("wave\\20.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\08.wav")
        elif "29" in minute:
            self.play_audio_file("wave\\20.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\09.wav")

        if int(minute) == 30:
            self.play_audio_file("wave\\30.wav")
        elif "31" in minute:
            self.play_audio_file("wave\\30.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\01.wav")
        elif "32" in minute:
            self.play_audio_file("wave\\30.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\02.wav")
        elif "33" in minute:
            self.play_audio_file("wave\\30.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\03.wav")
        elif "34" in minute:
            self.play_audio_file("wave\\30.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\04.wav")
        elif "35" in minute:
            self.play_audio_file("wave\\30.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\05.wav")
        elif "36" in minute:
            self.play_audio_file("wave\\30.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\06.wav")
        elif "37" in minute:
            self.play_audio_file("wave\\30.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\07.wav")
        elif "38" in minute:
            self.play_audio_file("wave\\30.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\08.wav")
        elif "39" in minute:
            self.play_audio_file("wave\\30.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\09.wav")

        if int(minute) == 40:
            self.play_audio_file("wave\\40.wav")
        elif "41" in minute:
            self.play_audio_file("wave\\40.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\01.wav")
        elif "42" in minute:
            self.play_audio_file("wave\\40.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\02.wav")
        elif "43" in minute:
            self.play_audio_file("wave\\40.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\03.wav")
        elif "44" in minute:
            self.play_audio_file("wave\\40.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\04.wav")
        elif "45" in minute:
            self.play_audio_file("wave\\40.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\05.wav")
        elif "46" in minute:
            self.play_audio_file("wave\\40.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\06.wav")
        elif "47" in minute:
            self.play_audio_file("wave\\40.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\07.wav")
        elif "48" in minute:
            self.play_audio_file("wave\\40.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\08.wav")
        elif "49" in minute:
            self.play_audio_file("wave\\40.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\09.wav")

        if int(minute) == 50:
            self.play_audio_file("wave\\50.wav")
        elif "51" in minute:
            self.play_audio_file("wave\\50.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\01.wav")
        elif "52" in minute:
            self.play_audio_file("wave\\50.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\02.wav")
        elif "53" in minute:
            self.play_audio_file("wave\\50.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\03.wav")
        elif "54" in minute:
            self.play_audio_file("wave\\50.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\04.wav")
        elif "55" in minute:
            self.play_audio_file("wave\\50.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\05.wav")
        elif "56" in minute:
            self.play_audio_file("wave\\50.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\06.wav")
        elif "57" in minute:
            self.play_audio_file("wave\\50.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\07.wav")
        elif "58" in minute:
            self.play_audio_file("wave\\50.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\08.wav")
        elif "59" in minute:
            self.play_audio_file("wave\\50.wav")
#            self.play_audio_file("wave\\u.wav")
            self.play_audio_file("wave\\09.wav")

        if deke:
            self.play_audio_file("wave\\deqe.wav")


    def play_audio_file(self, file):
        wf = wave.open(file, 'rb')
        wf_data = wf.readframes(wf.getnframes())
        audio = pyaudio.PyAudio()
        stream_out = audio.open(
            format=audio.get_format_from_width(wf.getsampwidth()),
            channels= wf.getnchannels(),
            rate=wf.getframerate()+2500,
            input=False,
            output=True,
            frames_per_buffer = 0,
            )
        stream_out.start_stream()
        stream_out.write(wf_data)
        #time.sleep(0.2)
        #stream_out.stop_stream()
        #stream_out.close()
        #audio.terminate() 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    app.quit
    sys.exit(app.exec_())
