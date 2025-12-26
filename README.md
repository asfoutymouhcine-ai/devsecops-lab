# DevSecOps Lab 
Ce projet **DevSecOps Lab** est un laboratoire pédagogique conçu pour démontrer l’intégration de la **sécurité dans une pipeline CI/CD**. Il contient volontairement du **code vulnérable** afin de tester des outils de sécurité comme **SAST, SCA, Trivy, Bandit et CodeQL**.

---

##  Objectifs du projet:

* Comprendre les principes **DevSecOps**
* Identifier des vulnérabilités applicatives (OWASP Top 10)
* Mettre en place une **pipeline CI/CD sécurisée avec GitHub Actions**
* Bloquer automatiquement le pipeline en cas de failles critiques

---

##  Architecture du projet:

```
.
├── app.py                         # API Flask volontairement vulnérable
├── requirements.txt               # Dépendances Python
├── Dockerfile                     # Image Docker de l'application
├── users.db                       # Base SQLite (exemple)
├── .github/
│   └── workflows/
│       └── devsecops.yml          # Pipeline CI/CD DevSecOps
└── README.md
```

---

## Vulnérabilités présentes (volontaires)

* SQL Injection
* Command Injection
* Insecure Deserialization (pickle)
* Hardcoded secrets
* Weak cryptography (MD5)
* Path Traversal
* Information Disclosure
* Log Injection

 **Ce code ne doit jamais être utilisé en production.**

---

## Sécurité dans la pipeline CI/CD

La pipeline GitHub Actions (`devsecops.yml`) intègre obligatoirement :

###  1. SAST (Static Application Security Testing)

* **CodeQL**
* Analyse statique du code source

###  2. Analyse de sécurité Python

* **Bandit**
* Détection des mauvaises pratiques Python

###  3. Scan des dépendances applicatives (SCA)

* **pip-audit** / Trivy FS
* Détection des vulnérabilités dans `requirements.txt`

###  4. Scan de vulnérabilités de l’image Docker

* **Trivy Image Scan**
* Analyse OS + dépendances applicatives

### 5. Blocage automatique

*  Pipeline échoue si :

  * Vulnérabilités **CRITICAL** détectées
  * Seuil de sévérité dépassé

---

##  Lancer le projet en local

### 1️ Cloner le dépôt

```bash
git clone https://github.com/asfoutymouhcine-ai/devsecops-lab.git
cd devsecops-lab
```

### 2️ Construire l’image Docker

```bash
docker build -t devsecops-api .
```

### 3️ Lancer le conteneur

```bash
docker run -p 5000:5000 devsecops-api
```

### 4️ Tester l’API

```bash
curl http://localhost:5000/hello
```

---

##  Outils utilisés

* **Flask** – API Python
* **Docker** – Conteneurisation
* **GitHub Actions** – CI/CD
* **CodeQL** – SAST
* **Bandit** – Sécurité Python
* **Trivy** – Scan image & dépendances

---

##  Contexte pédagogique

Projet réalisé dans un cadre **académique / formation DevSecOps**, destiné à :

* Étudiants
* Démonstrations
* Tests de pipelines sécurisées

---

##  Auteur

**Mouhcine Asfouty**
Étudiant / Ingénierie DevSecOps & Cybersécurité

🔗 GitHub : [https://github.com/asfoutymouhcine-ai](https://github.com/asfoutymouhcine-ai)

---

##  Avertissement

> Ce projet contient volontairement des failles de sécurité.
> Il est strictement destiné à un usage pédagogique.
