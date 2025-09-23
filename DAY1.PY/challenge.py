
import random 
Names=[
  "Ariana Vale", "Kael Thorn", "Zara Lume", "Dax Irwin", "Selene Korr", 
  "Milo Venn", "Lyra Shade", "Finn Solas", "Nova Rael", "Jace Arden", "Isla Rynn",
  "Talon Creed", "Rhea Myles", "Caius Vex", "Soren Hale", "Elara Wyn", "Dorian Pike",
  "Nyx Arlow", "Riven Locke", "Mira Zeph"
]

score_list =[(name,random.randint(1,100)) for name in Names]
for names,score in score_list:
    print(f"{Names}-{score}")

ordered_list=sorted(score_list, key=lambda x: x[1],reverse=True)
for name, score in ordered_list:
    print(f"{name} - {score}")
    
with open("all_scores.txt","w") as file:
    file.write("ordered_list(Descending order):\n")
    for name, score in ordered_list:
        file.write(f"{name} - {score}\n")

with open ("all_scores.txt","r") as file:
    data=file.read() 
    print(data)

top10=ordered_list[:10]

with open("top_10.txt","w") as file:
    file.write("top10:\n")
    for name,score in top10:
        file.write(f"{name}-{score}\n")

top3=ordered_list[:3]

with open("top_3.txt","w") as file:
    file.write("top3:\n")
    for name,score in top3:
        file.write(f"{name}-{score}\n")

