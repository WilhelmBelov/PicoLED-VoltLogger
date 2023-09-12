import machine
import utime

# Konfiguration der Pins
pin_GP26 = machine.ADC(26)
pin_GP27 = machine.ADC(27)
adc_width = 3.3       # Maximale Spannung in Volt (3.3V für Raspberry Pi Pico)

def measure_voltage(pin):
    raw_value = pin.read_u16()
    voltage = (raw_value / 65535) * adc_width
    return voltage

# Anzahl der Messungen
num_measurements = 2

# Benutzereingabe für die zusätzliche Zeile
datName = input("Bitte geben Sie den Name Datei mit Dateierwartungen '.txt' ein: ")
print("'\n")
print("Die Datei namens ", datName, " wird geschafft.")
print("\n")
user_line = input("Bitte geben Sie den Name Messungen ein: ")

# dateiaufgaben nennen
with open(datName, "a") as file:  # "a" zum Anhängen an die Datei
    if file.tell() != 0:  # Überprüfen, ob die Datei nicht leer ist
        file.write("\n" * 3)  # Drei Zeilenumbrüche hinzufügen
    file.write(user_line + "\n")  # Benutzerdefinierte Zeile hinzufügen

while True:
    input("Drücken Sie Enter, um eine Messung durchzuführen...")
    
    results = []
    for _ in range(num_measurements):
        voltage1 = measure_voltage(pin_GP26)  # Annahme: 3.3V Referenzspannung
        voltage2 = measure_voltage(pin_GP27)  # Annahme: 3.3V Referenzspannung
        diff_voltage = voltage1 - voltage2
        current = voltage2 / 0.098  # Annahme: Umrechnungsfaktor 0.098
        results.append((diff_voltage, current))
        utime.sleep(1)  # Eine Sekunde warten
        print(f"Differenzspannung: {diff_voltage:.4f} V, Strom: {current:.4f} A")

    # Ergebnisse in Datei speichern
    with open(datName, "a") as file:  # "a" zum Anhängen an die Datei
        for diff_voltage, current in results:
            file.write(f"Differenzspannung: {diff_voltage:.4f} V, Strom: {current:.4f} A\n")

    print("Messungen abgeschlossen und Ergebnisse in 'kennlinien.txt' gespeichert.")
