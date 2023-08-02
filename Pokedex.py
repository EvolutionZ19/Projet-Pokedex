import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

fenetre = tk.Tk()
fenetre.title("Pokédex")
fenetre.geometry("700x700")

pokedex_info = {
    1: {"nom": "Bulbizarre", "type": "Plante", "description": "Une chose verte avec un bulbe sur le dos", "capacite": "charge, charge, charge"},
    4: {"nom": "Salamèche", "type": "Feu", "description": "Un lézard avec une flamme au bout de la queue", "capacite": "charge, charge"},
    7: {"nom": "Carapuce", "type": "Eau", "description": "Le meilleur starter de la première génération", "capacite": "charge, charge"},
}

def montrer_pokemon_info(pokemon_info):
    nom_label.config(text="Nom : " + pokemon_info["nom"])
    type_label.config(text="Type : " + pokemon_info["type"])
    description_label.config(text="Description : " + pokemon_info["description"])
    capacite_label.config(text="Capacité : " + pokemon_info["capacite"])

def pokemon_selectionner(): 
    selection_index = pokemon_liste.curselection()
    if selection_index:
        index = int(selection_index[0])
        pokemon_id = list(pokedex_info.keys())[index]
        montrer_pokemon_info(pokedex_info[pokemon_id])

pokemon_liste = tk.Listbox(fenetre, selectmode=tk.SINGLE)
for pokemon_id, data in pokedex_info.items():
    pokemon_liste.insert(tk.END, f"{pokemon_id}. {data['nom']}")

pokemon_liste.pack()

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


bouton_info_pokemon = tk.Button(fenetre, text="Afficher les Informations", command=pokemon_selectionner)
bouton_info_pokemon.pack()

fenetre.mainloop()












