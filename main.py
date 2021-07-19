import forms



def main():
    while True:
        print("\n{0:<10}(a)\n{1:<10}(b)\n{2:<10}(c)".format("Kreis", "Quadrat", "Rechteck"))
        menu = input("\nWelche Form soll berechnet werden: ")
        
        if menu == "a":
            try:
                radius = input("Geben Sie den Radius ein: ")
                radius2 = radius.replace(",", ".")
                radius2 = float(radius2)
                circle = forms.Circle(radius2)
                circle_area = circle.get_area()
                circle_circumference = circle.get_circumference()
                print("\n{0:<15}{1:>16,.3f}\n{2:<15}{3:>16,.3f}".format("Flächeninhalt: ", circle_area, "Umfang: ", circle_circumference))
                circle.show()
            except ValueError:
                print("Nicht einmal ne Zahl kannst du eingeben...")

        elif menu == "b":
            try:
                square_length = input("Geben Sie die Seitenlänge ein: ")
                square_length2 = square_length.replace(",", ".")
                square_length2 = float(square_length2)

                square = forms.Square(square_length2)
                square_area = square.get_area()
                square_diagonal = square.get_diagonal()
                square_perimeter = square.get_perimeter()

                print("\n{0:<15}{1:>16,.3f}\n{2:<15}{3:>16,.3f}\n{4:<15}{5:>16,.3f}".format("Flächeninhalt: ", square_area, "Diagonale: ", square_diagonal, "Umfang: ", square_perimeter))

            except ValueError:
                print("Nicht einmal ne Zahl kannst du eingeben...")

        elif menu == "c":
            try:
                rectangle_length = input("Geben Sie die Länge ein: ")
                rectangle_length2 = rectangle_length.replace(",", ".")
                rectangle_length2 = float(rectangle_length2)

                rectangle_width = input("Geben Sie die Höhe ein: ")
                rectangle_width2 = rectangle_width.replace(",", ".")
                rectangle_width2 = float(rectangle_width2)

                rectangle = forms.Rectangle(rectangle_length2, rectangle_width2)
                rectangle_area = rectangle.get_area()
                rectangle_diagonal = rectangle.get_diagonal()
                rectangle_perimeter = rectangle.get_perimeter()

                print("\n{0:<15}{1:>16,.3f}\n{2:<15}{3:>16,.3f}\n{4:<15}{5:>16,.3f}".format("Flächeninhalt: ", rectangle_area, "Diagonale: ", rectangle_diagonal, "Umfang: ", rectangle_perimeter))

            except ValueError:
                print("Nicht einmal ne Zahl kannst du eingeben...")

        else:
            print("Keiner der genannten Punkte... Ich bin enttäuscht")



if __name__ == "__main__":
    main()