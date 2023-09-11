# Deatt
Das Programm soll die Spannung an den Pins GP26 und GP27 des Raspberry Pi Pico messen, anschließend die Differenz zwischen der ersten und der zweiten Spannung berechnen. Danach soll das Programm die Spannung an GP27 durch 0,098 teilen, um den Strom zu ermitteln. Diese Ergebnisse sollen in der Datei "kennlinien.txt" gespeichert werden. Die elektrische Schaltung ist in der ![Referenz](https://github.com/WilhelmBelov/PicoLED-VoltLogger/blob/ae2cec705087d61e3e561ab251a777a426438ce2/Schaltplan.drawio.png) zu finden.