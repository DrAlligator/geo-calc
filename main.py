import forms



def main():
    """the menu for the calculater
    """
    while True:
        print("\n{0:<10}(a)\n{1:<10}(b)\n{2:<10}(c)".format("Kreis", "Quadrat", "Rechteck"))
        menu = input("\nWelche Form soll berechnet werden: ")
        
        if menu == "a":
            while True:
                try:
                    radius = input("Geben Sie den Radius ein: ")
                    radius = float(radius.replace(",", "."))
                    break
                except ValueError:
                    print("Nicht einmal ne Zahl kannst du eingeben...")

            circle = forms.Circle(radius)

            print("\n{0:<15}{1:>16,.3f}\n{2:<15}{3:>16,.3f}".format("Flächeninhalt: ", circle.get_area(), "Umfang: ", circle.get_circumference()))
            circle.show()
            del circle

            

        elif menu == "b":
            while True:
                try:
                    square_length = input("Geben Sie die Seitenlänge ein: ")
                    square_length = float(square_length.replace(",", "."))
                    break
                except ValueError:
                    print("Nicht einmal ne Zahl kannst du eingeben...")

            square = forms.Square(square_length)

            print("\n{0:<15}{1:>16,.3f}\n{2:<15}{3:>16,.3f}\n{4:<15}{5:>16,.3f}".format("Flächeninhalt: ", square.get_area(), "Diagonale: ", square.get_diagonal(), "Umfang: ", square.get_perimeter()))
            square.show()
            del square

        elif menu == "c":
            while True:
                try:
                    rectangle_length = input("Geben Sie die Länge ein: ")
                    rectangle_length = float(rectangle_length.replace(",", "."))
                    rectangle_width = input("Geben Sie die Höhe ein: ")
                    rectangle_width = float(rectangle_width.replace(",", "."))
                    break
                except ValueError:
                    print("Nicht einmal ne Zahl kannst du eingeben...")

            rectangle = forms.Rectangle(rectangle_length, rectangle_width)

            print("\n{0:<15}{1:>16,.3f}\n{2:<15}{3:>16,.3f}\n{4:<15}{5:>16,.3f}".format("Flächeninhalt: ", rectangle.get_area(), "Diagonale: ", rectangle.get_diagonal(), "Umfang: ", rectangle.get_perimeter()))
            rectangle.show()
            del rectangle

        else:
            print("Keiner der genannten Punkte... Ich bin enttäuscht")



if __name__ == "__main__":
    main()