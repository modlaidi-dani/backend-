from rest_framework import serializers
from .models import *
# from clientInfo.serializers import * 
from django.db.models import Sum
class BanqueSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banque
        fields="__all__"
class AgenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Agence
        fields="__all__"
class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fournisseur
        fields="__all__"
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Region
        fields="__all__"
class ClientSerializer(serializers.ModelSerializer):
    name_user=serializers.SerializerMethodField()
    categorie_client=serializers.SerializerMethodField()
    EtatClient=serializers.SerializerMethodField()
    total_amount=serializers.SerializerMethodField()
    class Meta:
        model=Client
        fields="__all__"
    def get_categorie_client(self,obj):
        from clientInfo.serializers import typeClientSerializer
        data=typeClientSerializer(instance=obj.categorie_client ).data
        return data
    def get_name_user(self,obj):
        return obj.user.username
        
    def get_EtatClient(self,obj):
        if len(obj.ma_prospection.all()) >0:
            if obj.ma_prospection.last().etatProspection == 'confirme':
                return 'true' if obj.valide else 'false'
            else:
                return obj.ma_prospection.last().etatProspection          
        else:
                return 'true' if obj.valide else 'false' 
                
    
    def get_total_amount(self,obj):
        # from ventes.serializers import BonSortieSerializer
        total=0
        for bon in obj.client_bonS.exclude(idBon__startswith='BECH'):
            try:
                price_part = bon.produits_en_bon_sorties.aggregate(total_price=Sum('totalprice'))['total_price']
                print(price_part)
                total+=price_part
            except:
                total=total
              
        return total
    
    
    def total_rembourse(self,obj):
        return sum(Decimal(reglement.montant) for reglement in obj.client_reglements.filter(BonS__isnull=False, type_reglement ="Remboursement"))
        
    
    def total_annule(self,obj):
        filtered_bons_retour = [bon for bon in obj.client_bons_retour.filter(valide=True) if bon.reintegrated]

        result_sum = sum(Decimal(bon.total_price_retour) * Decimal(1.19) for bon in filtered_bons_retour)
        return result_sum

    
    def total_avoir(self,obj):
        filredbl= obj.client_bonS.all()
        totalavoir = 0
        for bl in filredbl:
            totalavoir+=bl.get_total_avoir()
        return totalavoir
    
    def total_avoir_old(self,obj):
        filredbl= obj.avoirsA_client.all()
        totalavoir = 0
        for avoir in filredbl:
            totalavoir+=Decimal(avoir.montant) * Decimal('1.19')
        return totalavoir
    
    
    def remaining_amount(self,obj):
        return round(obj.total_amount + obj.solde - (obj.total_paid_amount + obj.total_avoir + obj.total_avoir_old + obj.total_rembourse + obj.total_annule),0)
    
    
    def total_paid_amount(self,obj):
        return sum(Decimal(reglement.montant) for reglement in obj.client_reglements.all())
    
    
    def total_amount_facture(self,obj):
        return sum(Decimal(bon.get_total_price) for bon in obj.client_facture.all())
    
    
    def remaining_amount_facture(self,obj):
        return obj.total_amount_facture - obj.total_paid_amount_facture
    
    
    def total_paid_amount_facture(self,obj):
        return sum(Decimal(reglement.montant) for reglement in obj.client_reglements.filter(facture__isnull=False))
    
    def get_CA(obj):
        client_bons = obj.client_bonS.all()
        total_CA= 0
        for bon in client_bons:
              total_CA += bon.totalPrice

        return total_CA   
      
    
    def Solde_comptoir(self,obj):
        client_bons = obj.mesbons_comptoir.all()
        bons_retourcompt = obj.bonsretour_compt.all()
        total_CA = sum(bon.totalprice for bon in client_bons) - sum(bon.myTotalPrice for bon in bons_retourcompt)
        return total_CA
        
    
    def mon_credit(self,obj):
        # Create a list to store dictionaries with dateBon and montant
        credit_by_date = []
        for bon in obj.bonsretour_compt.all():
            # Check if the bon is not paid
            date_str = bon.dateBon.strftime("%Y-%m-%d")
            montant_float = float(bon.myTotalPrice)
            caisse = bon.bon_comptoir_associe.pointVente.pos_affectation.first().CompteTres.label

            credit_by_date.append({'dateBon': date_str, 'caisse':caisse, 'montant': montant_float})
        
        for bon in obj.client_bonS.exclude(idBon__startswith='BECH'):            
            if len(bon.bonS_reglements.filter(type_reglement ="Remboursement")) > 0:
                for reglement in bon.bonS_reglements.filter(type_reglement ="Remboursement"):
                    date_str = reglement.dateReglement.strftime("%Y-%m-%d")
                    prix_payed_float = float(reglement.montant)
                    
                    caisse = reglement.CompteEntreprise.label
                
                    # Check if both dateReglement and caisse already exist in the list
                    entry_exists = any(
                        entry['dateBon'] == date_str and entry['caisse'] == caisse
                        for entry in credit_by_date
                    )

                    if entry_exists:
                        # Update the existing entry with the sum of prix_payed
                        for entry in credit_by_date:
                            if entry['dateBon'] == date_str and entry['caisse'] == caisse:
                                entry['prix_payed'] += prix_payed_float
                                break
                    else:
                        # Add a new entry to the list
                        credit_by_date.append({'dateBon': date_str, 'caisse': caisse, 'montant': prix_payed_float})
                        
        return credit_by_date 
    
    def myproductssold(self,obj):
        # Create a list to store dictionaries with dateBon and montant
        stats = []
        components = ['cpu', 'mb', 'ram', 'cpuc', 'ssd', 'psu', 'gpu', 'case', 'casef' ,'moniteur', 'claviers', 'souris']
        for bon in obj.client_bonS.exclude(idBon__startswith='BECH'):  
            if len(bon.produits_en_bon_sorties.all()) >0:        
                for produit_sold in bon.produits_en_bon_sorties.all(): 
                    comp = produit_sold.stock.category.pc_component if produit_sold.stock.category is not None else '' 
                    qte = produit_sold.quantity
                    
                    date_str = bon.dateBon.strftime("%Y-%m-%d")
                    entry_exists = any(
                        entry['dateBon'] == date_str and entry['composant'] == comp
                        for entry in stats
                    )

                    if entry_exists:
                        # Update the existing entry with the sum of prix_payed
                        for entry in stats:
                            if entry['dateBon'] == date_str and entry['composant'] == comp:
                                entry['quantity_sold'] += qte
                                entry['montant_sold'] += qte * float(produit_sold.unitprice) * float(1.19)
                                
                                break
                    else:
                        # Add a new entry to the list
                        stats.append({'dateBon': date_str, 'composant': comp, 'quantity_sold': qte, 'montant_sold': qte * float(produit_sold.unitprice) * float(1.19)})         
        return stats 
        
    def mon_debit(self,obj):
        # Create a list to store dictionaries with dateBon and prix_payed
        debit_by_date = []

        # Iterate through BonComptoir instances related to the client
        for bon in obj.mesbons_comptoir.all():
            # print(bon.idBon)
            if not bon.par_verssement:
                # Convert datetime.date to string and Decimal to float
                date_str = bon.dateBon.strftime("%Y-%m-%d")
                caisse = bon.pointVente.pos_affectation.first().CompteTres.label
                prix_payed_float = float(bon.prix_payed- bon.totalremise)

                # Check if both dateBon and caisse already exist in the list
                entry_exists = any(
                    entry['dateBon'] == date_str and entry['caisse'] == caisse
                    for entry in debit_by_date
                )

                if entry_exists:
                    # Update the existing entry with the sum of prix_payed
                    for entry in debit_by_date:
                        if entry['dateBon'] == date_str and entry['caisse'] == caisse:
                            entry['prix_payed'] += prix_payed_float
                            break
                else:
                    # print("pris payer")
                    # if bon.totalremise != 0:
                    #     print(bon.prix_payed)
                    #     print(bon.totalremise)
                        
                        
                    #     print(prix_payed_float)
                    
                    
                    
                    # Add a new entry to the list
                    debit_by_date.append({'dateBon': date_str, 'caisse': caisse, 'prix_payed': prix_payed_float})
            else:
                verssements = bon.verssements.all() 
                for verssement in verssements:  
                    # print("verment")
                    montant_v = 0
                    date_str =verssement.date.strftime("%Y-%m-%d")
                    caisse = bon.pointVente.pos_affectation.first().CompteTres.label
                    montant_v = float(verssement.montant or 0)
                    # print(montant_v)
                    
                    debit_by_date.append({'dateBon': date_str, 'caisse': caisse, 'prix_payed': montant_v})
                    
        for bon in obj.client_bonS.exclude(idBon__startswith='BECH'):            
            if len(bon.bonS_reglements.all()) > 0:
                for reglement in bon.bonS_reglements.all():
                    date_str = reglement.dateReglement.strftime("%Y-%m-%d")
                    prix_payed_float = float(reglement.montant)
                    
                    caisse = reglement.CompteEntreprise.label
                
                    # Check if both dateReglement and caisse already exist in the list
                    entry_exists = any(
                        entry['dateBon'] == date_str and entry['caisse'] == caisse
                        for entry in debit_by_date
                    )

                    if entry_exists:
                        # Update the existing entry with the sum of prix_payed
                        for entry in debit_by_date:
                            if entry['dateBon'] == date_str and entry['caisse'] == caisse:
                                entry['prix_payed'] += prix_payed_float
                                break
                    else:
                        # Add a new entry to the list
                        debit_by_date.append({'dateBon': date_str, 'caisse': caisse, 'prix_payed': prix_payed_float})

        verssements = obj.client_reglements.filter(facture__isnull=True, BonS__isnull=True) 
        for verssement in verssements:  
            montant_v = 0
            date_str =verssement.dateReglement.strftime("%Y-%m-%d")
            caisse = verssement.CompteEntreprise.label
            montant_v = float(verssement.montant or 0)
            debit_by_date.append({'dateBon': date_str, 'caisse': caisse, 'prix_payed': montant_v})
        return debit_by_date
     
     
    def margin_total(self,obj):
        debit_by_date = []
        for bon in obj.client_bonS.exclude(idBon__startswith='BECH'):
                # Convert datetime.date to string and Decimal to float
                date_str = bon.dateBon.strftime("%Y-%m-%d")
                entrepot_str = bon.entrepot.name
                prix_payed_float = float(bon.ma_marge)

                # Check if both dateBon and caisse already exist in the list
                entry_exists = any(
                    entry['dateBon'] == date_str and
                    entry['entrepot'] == entrepot_str
                    for entry in debit_by_date
                )

                if entry_exists:
                    # Update the existing entry with the sum of prix_payed
                    for entry in debit_by_date:
                        if entry['dateBon'] == date_str :
                            entry['montant'] += prix_payed_float
                            break
                else:
                    # Add a new entry to the list
                    debit_by_date.append({'dateBon': date_str, 'entrepot': entrepot_str, 'user': obj.user.username, 'montant': prix_payed_float})  
        return debit_by_date      
    
    def get_chiffre_affaire(self,obj):
        debit_by_date = []
        for bon in obj.client_bonS.exclude(idBon__startswith='BECH'):
                # Convert datetime.date to string and Decimal to float
                date_str = bon.dateBon.strftime("%Y-%m-%d")
                entrepot_str = bon.entrepot.name
                prix_payed_float = float(bon.get_total_price) * float(1.19) 

                # Check if both dateBon and caisse already exist in the list
                entry_exists = any(
                    entry['dateBon'] == date_str and
                    entry['entrepot'] == entrepot_str
                    for entry in debit_by_date
                )

                if entry_exists:
                    # Update the existing entry with the sum of prix_payed
                    for entry in debit_by_date:
                        if entry['dateBon'] == date_str :
                            entry['montant'] += prix_payed_float
                            break
                else:
                    # Add a new entry to the list
                    debit_by_date.append({'dateBon': date_str,'entrepot': entrepot_str, 'user': obj.user.username, 'montant': prix_payed_float, 'montantA': float(bon.price_annule)})  
        return debit_by_date      
             
    def loyalty_points(self,obj):
        client_bonc = obj.mesbons_comptoir.all()
        client_bons = obj.client_bonS.exclude(idBon__startswith='BECH')
        total_CA = obj.Solde_comptoir
        return total_CA // 1000
        
    def getNifDoc(self,obj):
        if obj.NifDoc:
                return obj.NifDoc.url
        else:
                return ''
    def getNisDoc(self,obj):
        if obj.NisDoc:
                return obj.NisDoc.url
        else:
                return ''
    def getNifDoc(self,obj):
        if obj.NifDoc:
                return obj.NifDoc.url
        else:
                return ''
    def getRCDoc(self,obj):
        if obj.RCDoc:
                return obj.RCDoc.url
        else:
                return ''
    def getAIDoc(self,obj):
        if obj.AIDoc:
                return obj.AIDoc.url
        else:
                return ''
class ProspectionClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProspectionClient
        fields="__all__"
class TentativesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tentatives
        fields="__all__"
class CompteBancaireSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompteBancaire
        fields="__all__"
