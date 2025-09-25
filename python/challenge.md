# Python Challenge: Scoreboard Management System  

You are tasked with creating a **Scoreboard Management System** that generates random player data, sorts it, and manages different score files. The challenge will test your skills in **file handling, loops, conditional statements, and sorting in Python**.  

---

## Instructions  

1. **Generate Players**  
   - Create a list of **20 random player names** (you can make up names or use a fixed list).  
   - Assign each player a **random score between 1 and 100**.  

2. **Print Players**  
   - Display the players with their scores in the order they were generated.  

3. **Sort Players**  
   - Sort the players by score in **descending order** (highest first).  
   - Print the sorted list.  

4. **Write to File**  
   - Save the sorted list into a file named `all_scores.txt`.  

5. **Read from File**  
   - Read back the contents of `all_scores.txt` and print them.  

6. **Filter Top Players**  
   - Extract the **Top 10 players** and save them to `top_10.txt`.  
   - Extract the **Top 3 players** and save them to `top_3.txt`.  

7. **Final Output**  
   - Print the contents of all three files:  
     - `all_scores.txt`  
     - `top_10.txt`  
     - `top_3.txt`  

---

## Hints
- Use the `random` module for generating scores.  
- Use `with open(filename, mode)` for file handling.  
- Loop through lines when reading files.  
- Use conditionals to filter correctly (e.g., top 10, top 3).  

---

## Concepts Practiced
- **Randomization** (`random.randint`)  
- **Sorting with key functions**  
- **Loops & conditionals**  
- **File handling** (read, write, multiple files)  
- **Data filtering** 