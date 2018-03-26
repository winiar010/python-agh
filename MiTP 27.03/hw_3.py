# Rozbudowny program z konwersją daty

date = input("Podaj datę w formacie DD.MM.RRRR a zostanie ona przetłumaczona na DD month RRRR: ")

months = {"01": "January",
          "02": "February",
          "03": "March",
          "04": "April",
          "05": "May",
          "06": "June",
          "07": "July",
          "08": "August",
          "09": "September",
          "10": "October",
          "11": "November",
          "12": "December"}

day, month, year = date.split(".")

if len(year) == 4:
    if month in months:
        if month in ["01", "03", "05", "07", "08", "10", "12"]:
            if int(day) in range(1, 32):
                pass
            else:
                print("Podałeś niewłaściwą datę!")
                exit(1)
        elif month in ["04", "06", "09", "11"]:
            if int(day) in range(1, 31):
                pass
            else:
                print("Podałeś niewłaściwą datę!")
                exit(1)
        else:
            if int(day) in range(1, 30):
                pass
            else:
                print("Podałeś niewłaściwą datę!")
                exit(1)
    else:
        print("Podałeś niewłaściwą datę!")
        exit(1)
else:
    print("Podałeś niewłaściwą datę!")
    exit(1)

print("Twoja data po zmianie:", day, months[month], year, sep=" ")