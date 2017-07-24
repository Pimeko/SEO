# SEO


### 1. Le programme


Le programme a été développé en Python3. Afin de le lancer, il faut entrer la commande suivante :

```
$ python3 seo.py data/text1 data/text2 data/text3
```

Le programme prend en entrée le fichier de code en Python ainsi que la liste des textes à analyser.  
Le dossier data contient donc 3 fichiers d’exemple, mais il est possible de préciser d’autres fichiers.

### 2. L’algorithme

L’algorithme fonctionne de la manière suivante :  
- Le programme prend en entrée une liste de fichiers textes encodés en UTF8
- Pour chaque fichier, tous les n-grams en sont extraits, avec 2 <= n <= 7.  
Exemple : “Bonjour ça va ?”  
Résultat : “Bonjour ça”, “ça va”, “Bonjour ça va”   
- Chaque n-gram est alors stocké dans un Dictionary associant comme clé le n-gram et comme valeur un objet ayant deux clés :
  - nb_occurrences : le nombre total d’apparitions du n-gram inter-documents 
  - pages : un tableau de noms de fichiers, permettant d’avoir un suivi sur le nombre de pages contenant le n-gram  

Exemple :   

```JS
{  
 “bonjour” :   
  {  
     ‘nb_occurrences’ : 3,  
     pages :   
     [
       ‘texte A’,  
       ‘texte B’
     ]  
    }, ...  
  }  
```

- Puis, tous les n-grams sont analysés afin d’appliquer la formule de TF-IDF pour trouver w = TF * IDF, avec :  
`TF = nombre d’occurrences / nombre d’occurrences du n-gram le plus fréquent`  
`IDF = log(nombre de documents / nombre de documents contenant le n-gram) + 1`   
- Tous les w trouvés sont stockés dans un tableau associant à chaque clé de n-gram le w
- Enfin, les 10 n-grams ayant les w les plus élevés sont affichés par ordre décroissant (du plus élevé au moins élevé)
