"""
Praktisk uppgift 03: Debugging

Instruktioner:
1. Kör detta script som vanligt för att se vad det gör.
2. Avkommentera raden med 'breakpoint()' inuti loopen.
3. Kör scriptet igen. Programmet kommer pausa vid breakpoint().
4. I terminalen (pdb) kan du testa kommandon:
   - 'n' (next): Gå till nästa rad
   - 'c' (continue): Fortsätt köra till nästa breakpoint eller slut
   - 'p num': Skriv ut värdet på variabeln 'num'
   - 'p total': Skriv ut värdet på variabeln 'total'
   - 'q' (quit): Avsluta debuggern

5. Testa även att sätta en "red dot" (breakpoint) i din editor (VS Code)
   genom att klicka till vänster om radnumret, och kör med "Run and Debug".
"""

def calculate_cumulative_sum(numbers):
    total = 0
    print(f"Beräknar kumulativ summa för: {numbers}")
    
    for num in numbers:
        # --- DEBUGGING HÄR ---
        #breakpoint() 
        # ---------------------
        
        total += num
        print(f"Lade till {num}, ny total: {total}")
        
    return total

def main():
    my_numbers = [10, 20, 30, 40, 50]
    final_result = calculate_cumulative_sum(my_numbers)
    print(f"\nSlutresultat: {final_result}")

if __name__ == "__main__":
    main()
