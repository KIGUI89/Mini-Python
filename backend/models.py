from django.db import models

class Article(models.Model):
    nom = models.CharField(max_length = 100)
    prix = models.DecimalField(max_digits = 10, decimal_places=2)
    code = models.IntegerField(null=False,blank = False, unique = True)
    dateExp = models.DateTimeField(null=False, blank = False)
    qantiteStock = models.IntegerField(null = False, blank = False)

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    nbrArticle = models.IntegerField(null = False, blank = False)
    article = models.ForeignKey(Article, on_delete = models.CASCADE )

class Stock(models.Model):
    article = models.CharField(max_length = 100)
    quantite = models.IntegerField(null= False, blank = False)
    dateExpiProduit = models.DateField(null = False, blank = False)
    dateCreationStock = models.DateField(null = False, blank = False)
    codeArticle = models.IntegerField(null = False, blank = False)
    article = models.ForeignKey(Article, on_delete = models.CASCADE )
    categorie = models.ForeignKey(Categorie, on_delete = models.CASCADE )

class Vente(models.Model):
    dateVente = models.DateField(null = False, blank = False)
    article = models.ForeignKey(Article, on_delete = models.CASCADE )
    quantite = models.IntegerField(null = False, blank = False)
    prixUnitaire = models.IntegerField(null = False, blank = False)
    prixTotal = models.IntegerField(null = False, blank = False)

class Factures (models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE )
    dateEmise = models.DateField(null = False, blank = True)
    dateEcheance = models.DateField(null = False, blank = False)
    montantHT = models.IntegerField(null = False, blank = False)
    montantTTC = models.IntegerField(null = False, blank = False)
    Statut = models.CharField(null = True, blank = False)
    modePaiement = models.CharField(null = False, blank = False)

    
