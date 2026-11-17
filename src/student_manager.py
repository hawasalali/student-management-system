import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="hawas",
    password="Bbq987654321...",
    database="my_database"
)

cursor = connection.cursor()

while True:

    print("\n STUDENT MANAGEMENT ")
    print("1. Student hinzufügen")
    print("2. Studenten anzeigen")
    print("3. Student bearbeiten")
    print("4. Student löschen")
    print("5. Statistik")
    print("0. Beenden")

    choice = input("\nAuswahl: ")

    if choice == "1":

        first_name = input("Vorname: ")
        last_name = input("Nachname: ")
        age = int(input("Alter: "))
        email = input("E-Mail: ")

        cursor.execute("""
        INSERT INTO students
        (first_name,last_name,age,email)
        VALUES(%s,%s,%s,%s)
        """, (first_name,last_name,age,email))

        connection.commit()

        print("Gespeichert")

    elif choice == "2":

        cursor.execute(
            "SELECT * FROM students"
        )

        students = cursor.fetchall()

        print("\n--- Studenten ---")

        for student in students:

            print(
                f"ID:{student[0]} | "
                f"{student[1]} {student[2]} | "
                f"Alter:{student[3]} | "
                f"{student[4]}"
            )

    elif choice == "3":

        student_id = input("ID: ")
        new_email = input("Neue E-Mail: ")

        cursor.execute("""
        UPDATE students
        SET email=%s
        WHERE id=%s
        """, (new_email, student_id))

        connection.commit()

        print("Aktualisiert")

    elif choice == "4":

        student_id = input("ID löschen: ")

        cursor.execute("""
        DELETE FROM students
        WHERE id=%s
        """, (student_id,))

        connection.commit()

        print("Gelöscht")

    elif choice == "5":

        cursor.execute(
            "SELECT COUNT(*) FROM students"
        )

        count = cursor.fetchone()[0]

        print(
            f"\n Anzahl Studenten: {count}"
        )

    elif choice == "0":

        break

cursor.close()
connection.close()

print("Programm beendet.")