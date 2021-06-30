import forms

def main():
    while True:
        print("\n{0:<10}(a)\n{1:<10}(b)\n{2:<10}(c)".format("Kreis", "Quadrat", "Rechteck"))
        menu = input("\nWelche Form soll berechnet werden: ")
        
        if menu == "a":
            try:
                radius = float(input("Geben Sie den Radius ein: "))
                circle = forms.Circle(radius)
                circle_area = circle.get_area()
                circle_circumference = circle.get_circumference()
                print("\n{0:<15}{1:>16,.3f}\n{2:<15}{3:>16,.3f}".format("Flächeninhalt: ", circle_area, "Umfang: ", circle_circumference))
            except ValueError:
                print("Nicht einmal ne Zahl kannst du eingeben...")
        elif menu == "b":
            pass
        elif menu == "c":
            pass
        else:
            print("Keiner der genannten Punkte... Ich bin enttäuscht")




if __name__ == "__main__":
    main()