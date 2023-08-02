import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from PIL import Image, ImageTk

fenetre = tk.Tk()
fenetre.title("Pokédex")
fenetre.geometry("1024x768")

# Dictionnaire de pokemon 

pokedex_info = {
    1: {"nom": "Bulbizarre", "type": "Plante", "description": "Une chose verte avec un bulbe sur le dos", "capacite": "Fouet Liannes, Charge, Tranch'Herbe"},
    4: {"nom": "Salamèche", "type": "Feu", "description": "Un lézard avec une flamme au bout de la queue", "capacite": "Flammèche, Griffe"},
    7: {"nom": "Carapuce", "type": "Eau", "description": "Le meilleur starter de la première génération", "capacite": "Hydrocanon, Morsure"},
}
# Fontion pour montrer les informations du pokémon

def montrer_pokemon_info(pokemon_info):
    nom_label.config(text="Nom : " + pokemon_info["nom"])
    type_label.config(text="Type : " + pokemon_info["type"])
    description_label.config(text="Description : " + pokemon_info["description"])
    capacite_label.config(text="Capacité : " + pokemon_info["capacite"])
    
    # Charger l'image du Pokémon
    img_path = f"{pokemon_info['nom']}.png" 
    try:
        img = Image.open(img_path)
        img = img.resize((150, 150))  
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img  
    except FileNotFoundError:
        
        image_label.config(image="")
        image_label.image = None









#Fonction pour selectionner un pokémon et le récupérer (curselection)

def pokemon_selectionner(): 
    selection_index = pokemon_liste.curselection()
    if selection_index:
        index = int(selection_index[0])
        pokemon_id = list(pokedex_info.keys())[index]
        montrer_pokemon_info(pokedex_info[pokemon_id])
        
    
    

# Fonction pour ajouter un nouveau pokémon à la liste

def ajouter_nouveau_pokemon():
    pokemon_id = 4 + len(pokedex_info) +1
    nom = nouveau_Nom_entree.get()
    type = nouveau_type_entree.get()
    description = nouvelle_description_entree.get()
    capacite = nouvelle_capacite_entree.get()
    
    
    if nom == "" or type == "" or description == "" or capacite == "":
        showerror(title="ERREUR", message="Des cases sont vides")
        
    else:
        pokedex_info[pokemon_id] = {"nom": nom, "type": type, "description": description, "capacite": capacite}
        pokemon_liste.insert(tk.END, f"{pokemon_id}. {nom}")
        nouveau_Nom_entree.delete(0, tk.END)
        nouveau_type_entree.delete(0, tk.END)
        nouvelle_description_entree.delete(0, tk.END)
        nouvelle_capacite_entree.delete(0, tk.END)
        showinfo(title= "OK", message="Pokémon ajouté avec succès")
        

        
    
        
# Fonction pour supprimer un pokémon
def supprimer_pokemon():
    selection_index = pokemon_liste.curselection()
    if selection_index:
        index = int(selection_index[0])
        pokemon_id = list(pokedex_info.keys())[index]
        del pokedex_info[pokemon_id]
        pokemon_liste.delete(index)
        showinfo(title="INFO", message="Pokémon supprimé avec succès")
    
# Bulbizarre_img = ImageTk.PhotoImage(Image.open("0001Bulbasaur.png"))
# Salamèche_img = ImageTk.PhotoImage(Image.open("0004Charmander.png"))
# Carapuce_img = ImageTk.PhotoImage(Image.open("0007Squirtle.png"))


pokemon_liste = tk.Listbox(fenetre, selectmode=tk.SINGLE)
for pokemon_id, data in pokedex_info.items():
    pokemon_liste.insert(tk.END, f"{pokemon_id}. {data['nom']}")
    
    
    

pokemon_liste.pack()
pokemon_liste.insert(tk.END,)




# Informations des pokemons 


info_frame = ttk.Frame(fenetre)
info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

nom_label = ttk.Label(info_frame, text="", foreground="blue" )
nom_label.pack()

type_label = ttk.Label(info_frame, text="", foreground="blue")
type_label.pack()

description_label = ttk.Label(info_frame, text="", foreground="blue")
description_label.pack()

capacite_label = ttk.Label(info_frame, text="", foreground="blue")
capacite_label.pack()

image_label = tk.Label(fenetre, image="")
image_label.pack()

bouton_info_pokemon = tk.Button(fenetre, text="Afficher les Informations", command=pokemon_selectionner,
border="8", relief="raised", )
bouton_info_pokemon.pack()

# Nouvelle entrée des pokemons

frame_nouveau_pokemon = ttk.Frame(fenetre)
frame_nouveau_pokemon.pack(side=tk.LEFT, padx=10, pady=10)

nouveau_Nom = ttk.Label(frame_nouveau_pokemon, text="Nom :")
nouveau_Nom.grid(row=0, column=0, padx=5, pady=5)
nouveau_Nom_entree = ttk.Entry(frame_nouveau_pokemon)
nouveau_Nom_entree.grid(row=0, column=1, padx=5, pady=5)

nouveau_type =ttk.Label(frame_nouveau_pokemon, text="Type :")
nouveau_type.grid(row=1, column=0, padx=5, pady=5)
nouveau_type_entree = ttk.Entry(frame_nouveau_pokemon)
nouveau_type_entree.grid(row=1, column=1, padx=5, pady=5)

nouvelle_description = ttk.Label(frame_nouveau_pokemon, text="Description :")
nouvelle_description.grid(row=2, column=0, padx=5, pady=5)
nouvelle_description_entree = ttk.Entry(frame_nouveau_pokemon )
nouvelle_description_entree.grid(row=2, column=1, padx=5, pady=5)

nouvelle_capacite = ttk.Label(frame_nouveau_pokemon, text="Capacité :")
nouvelle_capacite.grid(row=3, column=0, padx=5, pady=5)
nouvelle_capacite_entree = ttk.Entry(frame_nouveau_pokemon)
nouvelle_capacite_entree.grid(row=3, column=1, padx=5, pady=5)

bouton_nouveau_pokemon = tk.Button(fenetre, text="Ajouter", command= ajouter_nouveau_pokemon, border="8", relief="raised")
bouton_nouveau_pokemon.pack(side=tk.LEFT, padx=10, pady=10)

bouton_supprimer_pokemon = tk.Button(fenetre, text="Supprimer", command= supprimer_pokemon, border="8", relief="raised", )
bouton_supprimer_pokemon.pack(side=tk.LEFT, padx=10, pady=10)

fenetre.mainloop()












