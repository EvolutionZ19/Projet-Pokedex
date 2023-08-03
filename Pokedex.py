import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from PIL import Image, ImageTk
import pickle
import os

# Définir pokedex_info avant de charger les données
pokedex_info = {}

# Fonction pour sauvegarder les données
def sauvegarder_donnees():
    try:
        with open('pokedex_data.pkl', 'wb') as f:
            pickle.dump(pokedex_info, f)
    except Exception as e:
        showerror(title="ERREUR", message=f"Erreur lors de la sauvegarde des données : {e}")

# Fonction pour charger les données
def charger_donnees():
    global pokedex_info
    try:
        if os.path.getsize('pokedex_data.pkl') > 0:  # Vérifie si le fichier n'est pas vide
            with open('pokedex_data.pkl', 'rb') as f:
                pokedex_info = pickle.load(f)
    except FileNotFoundError:
        # Créer un fichier vide s'il n'existe pas
        sauvegarder_donnees()
    except Exception as e:
        showerror(title="ERREUR", message=f"Erreur lors du chargement des données : {e}")

# Charger les données au démarrage de l'application
charger_donnees()

fenetre = tk.Tk()
fenetre.title("Pokédex")
fenetre.geometry("1024x768")
fenetre.iconbitmap("img/Pokedex.ico")


# Fonction pour montrer les informations du pokémon
def montrer_pokemon_info(pokemon_info):
    nom_label.config(text="Nom : " + pokemon_info["nom"])
    type_label.config(text="Type : " + pokemon_info["type"])
    description_label.config(text="Description : " + pokemon_info["description"])
    capacite_label.config(text="Capacité : " + pokemon_info["capacite"])
    
    # Charger l'image du Pokémon
    img_chemin = f"img/{pokemon_info['nom']}.png" 
    try:
        img = Image.open(img_chemin)
        img = img.resize((200, 200))  
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
    pokemon_id = max(pokedex_info.keys(), default=0) + 1
    nom = nouveau_Nom_entree.get()
    type_pokemon = nouveau_type_entree.get()
    description = nouvelle_description_entree.get()
    capacite = nouvelle_capacite_entree.get()

    if nom == "" or type_pokemon == "" or description == "" or capacite == "":
        showerror(title="ERREUR", message="Des cases sont vides")
    else:
        pokedex_info[pokemon_id] = {"nom": nom, "type": type_pokemon, "description": description, "capacite": capacite}
        sauvegarder_donnees()  # Sauvegarder les données dans le fichier pokedex_data.pkl
        pokemon_liste.insert(tk.END, f"{pokemon_id}. {nom}")
        nouveau_Nom_entree.delete(0, tk.END)
        nouveau_type_entree.delete(0, tk.END)
        nouvelle_description_entree.delete(0, tk.END)
        nouvelle_capacite_entree.delete(0, tk.END)
        showinfo(title="OK", message="Pokémon ajouté avec succès")


        
# Fonction pour supprimer un pokémon
def supprimer_pokemon():
    selection_index = pokemon_liste.curselection()
    if selection_index:
        index = int(selection_index[0])
        pokemon_id = list(pokedex_info.keys())[index]
        del pokedex_info[pokemon_id]
        pokemon_liste.delete(index)
        showinfo(title="INFO", message="Pokémon supprimé avec succès")
        sauvegarder_donnees()
    

pokemon_liste = tk.Listbox(fenetre, selectmode=tk.SINGLE)
for pokemon_id, data in pokedex_info.items():
    pokemon_liste.insert(tk.END, f"{pokemon_id}. {data['nom']}")
pokemon_liste.pack()
    
    
    

pokemon_liste.pack()
pokemon_liste.insert(tk.END,)


image_logo = Image.open("img/logo.png")
image_logo = image_logo.resize((300, 150))
image_logo_label = ImageTk.PhotoImage(image_logo)
label = ttk.Label(fenetre, image=image_logo_label)
label.pack(anchor=tk.NW)



# Informations des pokemons 


info_frame = ttk.Frame(fenetre)
info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

nom_label = ttk.Label(info_frame, text="", foreground="blue",  )
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












