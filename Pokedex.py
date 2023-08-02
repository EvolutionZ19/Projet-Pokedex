import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

fenetre = tk.Tk()
fenetre.title("Pokédex")
fenetre.geometry("1024x768")
# liste de pokemon 

pokedex_info = {
    1: {"nom": "Bulbizarre", "type": "Plante", "description": "Une chose verte avec un bulbe sur le dos", "capacite": "charge, charge, charge"},
    4: {"nom": "Salamèche", "type": "Feu", "description": "Un lézard avec une flamme au bout de la queue", "capacite": "charge, charge"},
    7: {"nom": "Carapuce", "type": "Eau", "description": "Le meilleur starter de la première génération", "capacite": "charge, charge"},
}
# Fontion pour montrer les informations du pokémon

def montrer_pokemon_info(pokemon_info):
    nom_label.config(text="Nom : " + pokemon_info["nom"])
    type_label.config(text="Type : " + pokemon_info["type"])
    description_label.config(text="Description : " + pokemon_info["description"])
    capacite_label.config(text="Capacité : " + pokemon_info["capacite"])

#Fonction pour selectionner un pokémon et le récupérer (curselection)

def pokemon_selectionner(): 
    selection_index = pokemon_liste.curselection()
    if selection_index:
        index = int(selection_index[0])
        pokemon_id = list(pokedex_info.keys())[index]
        montrer_pokemon_info(pokedex_info[pokemon_id])
        
# Fonction des images pokemon associées

def montrer_image(choice,):
    if choice == {1}:
        image_label.config(image=Bulbizarre_img)
    elif choice == {4}:
        image_label.config(image=Salamèche_img)
    elif choice == {7}:
        image_label.config(image=Carapuce_img)

# Fonction pour ajouter un nouveau pokémon à la liste

def ajouter_nouveau_pokemon():
    pokemon_id = len(pokedex_info) + 1
    nom = nouveau_Nom_entree.get()
    type = nouveau_type_entree.get()
    description = nouvelle_description_entree.get("1.0", "end-1c")
    capacite = nouvelle_capacite_entree.get()
    
    if nom == "" or type == "" or description == "" or capacite == "":
        tk.messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
    else:
        pokedex_info[pokemon_id] = {"nom": nom, "type": type, "description": description, "capacite": capacite}
        pokemon_liste.insert(tk.END, f"{pokemon_id}. {nom}")
        nouveau_Nom_entree.delete(0, tk.END)
        nouveau_type_entree.delete(0, tk.END)
    
    
    
        

    
Bulbizarre_img = ImageTk.PhotoImage(Image.open("0001Bulbasaur.png"))
Salamèche_img = ImageTk.PhotoImage(Image.open("0004Charmander.png"))
Carapuce_img = ImageTk.PhotoImage(Image.open("0007Squirtle.png"))


pokemon_liste = tk.Listbox(fenetre, selectmode=tk.SINGLE)
for pokemon_id, data in pokedex_info.items():
    pokemon_liste.insert(tk.END, f"{pokemon_id}. {data['nom']}")

pokemon_liste.pack()

# Informations des pokemons 


info_frame = ttk.Frame(fenetre)
info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

nom_label = ttk.Label(info_frame, text="")
nom_label.pack()

type_label = ttk.Label(info_frame, text="")
type_label.pack()

description_label = ttk.Label(info_frame, text="")
description_label.pack()

capacite_label = ttk.Label(info_frame, text="")
capacite_label.pack()

image_label = tk.Label(fenetre, image="")
image_label.pack()

bouton_info_pokemon = tk.Button(fenetre, text="Afficher les Informations", command=pokemon_selectionner)
bouton_info_pokemon.pack()

# Nouvelle entrée des pokemons

frame_nouveau_pokemon = ttk.Frame(fenetre)
frame_nouveau_pokemon.pack(side=tk.LEFT, padx=10, pady=10)

nouveau_Nom_label = ttk.Label(frame_nouveau_pokemon, text="Nom :")
nouveau_Nom_label.grid(row=0, column=0, padx=5, pady=5)
nouveau_Nom_entree = ttk.Entry(frame_nouveau_pokemon)
nouveau_Nom_entree.grid(row=0, column=1, padx=5, pady=5)

nouveau_type_label =ttk.Label(frame_nouveau_pokemon, text="Type :")
nouveau_type_label.grid(row=1, column=0, padx=5, pady=5)
nouveau_type_entree = ttk.Entry(frame_nouveau_pokemon)
nouveau_type_entree.grid(row=1, column=1, padx=5, pady=5)

nouvelle_description_label = ttk.Label(frame_nouveau_pokemon, text="Description :")
nouvelle_description_label.grid(row=2, column=0, padx=5, pady=5)
nouvelle_description_entree = tk.Text(frame_nouveau_pokemon, width=25, height=12)
nouvelle_description_entree.grid(row=2, column=1, padx=5, pady=5)

nouvelle_capacite_label = ttk.Label(frame_nouveau_pokemon, text="Capacité :")
nouvelle_capacite_label.grid(row=3, column=0, padx=5, pady=5)
nouvelle_capacite_entree = ttk.Entry(frame_nouveau_pokemon)
nouvelle_capacite_entree.grid(row=3, column=1, padx=5, pady=5)

bouton_nouveau_pokemon = tk.Button(fenetre, text="Ajouter", command= ajouter_nouveau_pokemon)
bouton_nouveau_pokemon.pack(side=tk.LEFT, padx=10, pady=10)


fenetre.mainloop()












