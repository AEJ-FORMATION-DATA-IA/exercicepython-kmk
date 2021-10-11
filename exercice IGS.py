#!/usr/bin/env python
# coding: utf-8

# In[92]:


A = 15
B = 4
C = A + B
print("le résultat de ", A, "+", B," est ",C)


# In[93]:


#la multiplication des deux variables
D = A * B
print("le résultat de la multiplication de ", A,"*",B ," est ",D)
#la puissance
E = A**B
print("le resultat de la puissance de ", A,"**", B ,"est ",E)
#la division retournant la partie decimal
F = A / B
print("le resultat de cette opération ", A,"/",B," est ",F)
#la division retournant la partie entier
G = A // B
print("le resultat de cette opération ", A,"//",B," est ",G)
#le reste de notre division
H = A % B
print("le reste cette opération ", A,"%",B," est ",H)


# In[94]:


#creation d'un dictionnaire et remplissage par defaut 
dico_igs = {
  A + B : C,
  A * B : D,
  A**B : E,
  A/B : F,
  A//B : G,
  A%B : H
}
print([A+B])


# In[96]:


#Ajouter un objet dans dictionnaire
dico_igs["IA"]="Groupe 1"
print(dico_igs)


# In[98]:


#modifier un objet du dictionaire

dico_igs["IA"]="Data IA Groupe 1"
print(dico_igs)


# In[99]:


#suppression d'un objet dans le dictionnaire
dico_igs.pop(A+B)
print(dico_igs)


# In[101]:


#afficher la liste des clés d'un dictionnaire
for cle in dico_igs.keys():
    print (cle)


# In[102]:


#afficher la liste des valeurs d'un dictionnaire
for valeur in dico_igs.values():
    print(valeur)


# In[103]:


#afficher la liste cle-valeur du dictionnaire
for cle,valeur in dico_igs.items():
    print(cle,":", valeur)


# In[107]:


# creation de notre tuple
tuple_igs = (A,B,C)
print(tuple_igs)


# In[108]:


#ajout de valeur a notre tuple
#on ne peut pas ajouter de valeur dans un tuples car On utilisera un tuple pour définir des sortes de constantes qui n'ont donc pas vocation à changer.


# In[133]:


#les listes
#creation d'une liste

list_igs=["A","B","C","D"]
print(list_igs)


# In[135]:


liste1 = ["A","B","C","D"]


# In[134]:


liste2 = [A, B, C, D]
print(liste2)


# In[136]:


liste3 = [liste1, liste2]
print(liste3)


# In[137]:


#ajouter E et F a la liste1
liste1.append("E, F")
print(liste3)


# In[138]:


#Supprimer B de la liste1
liste1.remove('B')
print(liste1)


# In[140]:


liste1[0]=('G')
print(liste1)

