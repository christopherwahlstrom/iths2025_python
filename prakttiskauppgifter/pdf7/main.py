import sr_api
import sr_utils


def main(): 
     while True:
          print("\n=== Sveriges Radio API ===")
          print("1. Hämta och visa kanaler")
          print("2. Avsluta")

          choice = input("Välj ett alternativ:")

          if choice == "1":
               print("Hämtar kanaler...")

               channels = sr_api.get_channels()

               sr_utils.print_channels(channels)

          elif choice == "2":
               print("Avslutar programmet.")
               break
          else:
               print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
     main()