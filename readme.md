### **1. Utilisation du polymorphisme (lien dans votre code) + définition**

Le polymorphisme est un concept fondamental de la programmation orientée objet (POO). Il désigne la capacité d'une méthode à prendre plusieurs formes. Plus concrètement, il s'agit de la capacité d'une classe à hériter d'une classe parente et d'implémenter ou de modifier ses méthodes selon ses propres besoins.

**Exemple :** Les classes **WordUppercase et WordLowercase** ré-implémente la méthode **\_transform** de la classe parent **WordTransform**.

---

### **2. Utilisation de l'encapsulation (lien dans votre code) + définition**

L'encapsulation est un concept qui permet de restreindre l'accès direct aux attributs et méthodes d'une classe depuis l'extérieur de celle-ci. L'encapsulation vise à garantir l'intégrité des données et à cacher les détails d'implémentation internes d'une classe.

#### **a. Utilisation de visibilité publique**

Les **attributs et méthodes publics** sont accessibles depuis n'importe où dans le code. Ils sont définis sans préfixe particulier et peuvent être consultés ou modifiés librement.

**Exemple :** Dans la **classe Password** par exemple les attributs ou méthodes qui ne sont pas précédés d'un underscore sont publique.

#### **b. Utilisation de visibilité privée**

Les **attributs et méthodes privés** sont définis en utilisant un double underscore en préfixe (par exemple, \_\_attribut). Ils sont destinés à être utilisés uniquement à l'intérieur de la classe qui les déclare, et leur accès depuis l'extérieur est bloqué.

**Exemple :** Dans la **classe Word** par exemple l'attribut words est privé parce qu'il est précédé de deux underscore. Ou encore **\_\_convert_to_leet** est une méthode privé dans la classe LeetConverter

#### **c. Utilisation de visibilité protégée**

Les **attributs et méthodes protégés** sont définis en utilisant un underscore en préfixe (par exemple, \_attribut). Ils indiquent que l'accès à ces éléments doit être restreint aux sous-classes de la classe actuelle et aux autres classes du même module.

**Exemple :** Dans la **classe Password** par exemple les attributs ou méthodes qui sont précédés d'un underscore sont protégés

---

### **3. Utilisation de composition (lien dans votre code) + définition**

La composition est un concept de programmation orientée objet (POO) qui traite des relations entre différentes classes. Elle permet à une classe d'utiliser les fonctionnalités d'une autre classe, sans hériter de celle-ci.

**Exemple :** Dans la class Word, je fais de la composition dans le constructeur en instancient les class **RemoveAccent, WordUppercase, WordLowercase et WordCapitalize.**

---

### **4. Utilisation de l'héritage (lien dans votre code) + définition**

L'héritage est le principe d'avoir une classe enfant qui hérite d'une classe parent et de ses attributs et méthodes (si pas privé)

**Exemple :** Par exemple la classe **WordTransform** est une classe parent pour les classes enfant **WordUppercase et WordLowercase**.

---

### **5. Utilisation d'interface (lien dans votre code) + définition**

Dans la programmation orientée objet, une interface est une collection de méthodes abstraites (méthodes sans corps) et de constantes. Une classe qui implémente une interface doit définir toutes les méthodes abstraites qui sont déclarées dans l'interface. En d'autres termes, une interface définit un contrat que les classes qui l'implémentent doivent respecter.

**Exemple :** J'ai la classe WordInterface qui définit des méthodes abstracts. j'ai implémenté cette class sur Word, Word doit donc implémenter les class présente dans l'interface.

---

### **6. Utilisation de méthodes et attributs d'objets (lien dans votre code) + définition**

Un attribut d'objet est une variable qui est spécifique à une instance particulière de la classe. Chaque objet a son propre ensemble de valeurs d'attributs d'objet, qui peuvent être affectées et récupérées à travers l'objet. Les attributs d'objet peuvent être initialisés lors de la création de l'objet ou lors de l'appel d'une méthode spéciale appelée constructeur.

**Exemple :** Dans la classe Password, j'instancie la classe **LeetConverter** et j'utilise l'objet de class leet_converter_object pour faire appel à la méthode d'object **convert_words_to_leet**. (Ligne 34)

---

### **7. Utilisation de méthodes et attributs statiques (lien dans votre code) + définition**

Les attributs ou méthodes statiques sont des attributs/méthodes qui sont fais pour agir sur une classe et non sur un objet.
Un attribut statique appartient à la classe et non à un objet. Ainsi, tous les objets auront accès à cet attribut auront la même valeur.
Les attributs statiques sont souvent utilisés pour stocker des informations globales qui sont indépendantes de toute instance de la classe. C'est la même logique pour les méthodes.

**Exemple :** Dans main, je fais appel à la méthode static **encouragement** de la classe Message qui print un message.

---

### **8. Utilisation de méthodes et attributs de classe (lien dans votre code) + définition**

Le fonctionnement est le même que pour les attributs/méthodes static, la seule différence peut être liée à la façon dont ces attributs sont accédés. L'attribut de classe peut être accessible via les instances de la classe, ainsi que via la classe elle-même, tandis que l'attribut statique peut être accessible uniquement via la classe elle-même.

**Exemple :** Dans main, je fais appel à la méthode de classe **retry** de la classe Message qui print un message.
