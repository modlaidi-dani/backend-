from rest_framework import serializers
from .models import *
from inventory.serializers import *
from reglements.serializers import *
from clientInfo.serializers import *
from user.serializers import *
from tiers.serializers import *
from produits.serializers import *
# from inventory.serializers import #EntrepotSerializer



class pointVenteSerializer(serializers.ModelSerializer):
    #entrepot=EntrepotSerializer()
    mode_payment=ModeReglementSerializer()
    store=StoreSerializer()
    class Meta:
        model=pointVente
        fields="__all__"
class EmplacementSerializer(serializers.ModelSerializer):
    store=StoreSerializer()
    class Meta:
        model=Emplacement
        fields="__all__"
class AffectationCaisseSerializer(serializers.ModelSerializer):
    emplacement=pointVenteSerializer()
    CompteTres=CompteEntrepriseSerializer()
    utilisateur=CustomUserSerializer()
    store=StoreSerializer()
    class Meta:
        model=AffectationCaisse
        fields="__all__"
class ClotureSerializer(serializers.ModelSerializer):
    # utilisateur=CustomUserSerializer()
    # store=StoreSerializer()
    username=serializers.SerializerMethodField()
    class Meta:
        model=Cloture
        fields="__all__"
    def get_username(self,obj):
        return obj.utilisateur.username
    def to_representation(self, instance):
        response = super().to_representation(instance)
        bonComptoir_objects = BonComptoire.objects.filter(user=response["utilisateur"], dateBon=response['date'])
        BonRetourComptoir_objects =BonRetourComptoir.objects.filter( user=response["utilisateur"], dateBon=response['date'])
    
        prix_to_pay_list = [bon.totalprice for bon in bonComptoir_objects]
        total_price_sum = sum(prix_to_pay_list)
        total_price_sum = total_price_sum or Decimal(0) 
        total_remise_sum = bonComptoir_objects.aggregate(Sum('totalremise'))['totalremise__sum'] or 0
        
        verssements = verssement.objects.filter( utilisateur=response["utilisateur"], date=response['date'])
        total_verssements = sum(Decimal(v.montant) if v.montant != '' else Decimal(0) for v in verssements)
        try:    
            for bon in BonRetourComptoir_objects:
                
                    myTotalPrice = sum([product.totalprice for product in bon.produits_en_bon_retourcomptoir.all()])
                    prix_rembourse_sum = sum(myTotalPrice for bon in BonRetourComptoir_objects)
            prix_encaisse_sum = sum(bon.prix_encaisse for bon in bonComptoir_objects) - prix_rembourse_sum
        except:
            prix_encaisse_sum=0
        prix_encaisse_sum += total_verssements
        response["totalprice_sum"] = total_price_sum
        response["totalremise"]= total_remise_sum
        response["total_verssemens"] = total_verssements
        response["totalprix_encaisse"]=prix_encaisse_sum
        response["totalRembourse"]=prix_rembourse_sum
        return response
class ProduitsEnBonComptoirSerializer(serializers.ModelSerializer):
    stock=ProductSerializer()
    #entrepot=EntrepotSerializer()
    class Meta:
        model=ProduitsEnBonComptoir
        fields="__all__"


class BonComptoireSerializer(serializers.ModelSerializer):
    produit=ProduitsEnBonComptoirSerializer(many=True)
    pointVente=pointVenteSerializer()
    caisse=CompteEntrepriseSerializer()
    store=StoreSerializer()
    user=CustomUserSerializer()
    client=ClientSerializer()
    retourBill=serializers.SerializerMethodField()
    prix_encaisse=serializers.SerializerMethodField()
    prix_payed=serializers.SerializerMethodField()
    prix_to_pay=serializers.SerializerMethodField()
    regle=serializers.SerializerMethodField()
    prixtotal=serializers.SerializerMethodField()
    par_verssement=serializers.SerializerMethodField()
    montantrestant=serializers.SerializerMethodField()
    class Meta:
        model=BonComptoire
        fields="__all__"
    def get_retourBill(self,obj):
        bons_retours = obj.bons_retour_compt.all()
        if bons_retours :
            return True
        else:
            return False
    def get_prix_encaisse(self,obj):
        if (obj.totalprice > 0):
            return obj.totalprice - obj.totalremise
        else:
            return obj.totalprice
    def get_prix_payed(self,obj):
        if (obj.totalprice > 0):
            return obj.totalprice
        else:
            mes_verssements = obj.verssements.all()
            total_priceversed = sum(Decimal(v.montant) for v in mes_verssements if isinstance(v.montant, (int, float, str)) and v.montant.strip())
            return total_priceversed
    def get_prix_to_pay(self,obj):
        sum_of_total_prices = obj.produits_en_bon_comptoir.aggregate(models.Sum('totalprice'))['totalprice__sum'] or 0
        return sum_of_total_prices  - obj.totalremise
    def get_prixtotal(self,obj):
        sum_of_total_prices = obj.produits_en_bon_comptoir.aggregate(models.Sum('totalprice'))['totalprice__sum'] or 0
        return sum_of_total_prices
    def get_regle(self,obj):
        total_price = obj.prix_to_pay - (obj.totalprice - obj.totalremise)
        
        if total_price == Decimal('0'):
            return True
        else:
            mes_verssements = obj.verssements.all()
            total_priceversed = sum(Decimal(v.montant) if v.montant != '' else Decimal(0) for v in mes_verssements)
            total_priceversed = obj.prix_to_pay - total_priceversed

            if total_priceversed == Decimal('0'):
                return True
            else:
                return False
    def get_par_verssement(self,obj):
        if len(obj.verssements.all())>0:
            return True
        else:
            return False
    def get_prixtotal(self,obj):
        sum_of_total_prices = obj.produits_en_bon_comptoir.aggregate(models.Sum('totalprice'))['totalprice__sum'] or 0
        return sum_of_total_prices
        
    def get_montantrestant(self,obj):
        if (obj.totalprice > 0):
         restant = obj.prix_to_pay - obj.totalprice
        else:
           mes_verssements = obj.verssements.all()
           total_priceversed = sum(Decimal(v.montant) for v in mes_verssements if isinstance(v.montant, (int, float, str)) and v.montant.strip())
           restant = obj.prix_to_pay - total_priceversed
        return max(0, restant)

class ProduitsEnBonRectifSerializer(serializers.ModelSerializer):
    stock=ProductSerializer()
    #entrepot=#EntrepotSerializer()
    class Meta:
        model=ProduitsEnBonRectif
        fields="__all__"        
class BonRectificationSerializer(serializers.ModelSerializer):
    produit=ProduitsEnBonRectifSerializer(many=True)
    pointVente=pointVenteSerializer()
    caisse=CompteEntrepriseSerializer()
    store=StoreSerializer()
    client=ClientSerializer()
    retourBill=serializers.SerializerMethodField()
    prix_encaisse=serializers.SerializerMethodField()
    prix_payed=serializers.SerializerMethodField()
    prix_to_pay=serializers.SerializerMethodField()
    regle=serializers.SerializerMethodField()
    prixtotal=serializers.SerializerMethodField()
    par_verssement=serializers.SerializerMethodField()
    montantrestant=serializers.SerializerMethodField()
    class Meta:
        model=BonRectification
        fields="__all__"

    def get_retourBill(self,obj):
        bons_retours = obj.bons_retour_compt.all()
        if bons_retours :
            return True
        else:
            return False
    def get_prix_encaisse(self,obj):
        if (obj.totalprice > 0):
            return obj.totalprice - obj.totalremise
        else:
            return obj.totalprice
        
    def get_prix_payed(self,obj):
        if (obj.totalprice > 0):
            return obj.totalprice
        else:
            mes_verssements = obj.verssements.all()
            total_priceversed = sum(Decimal(v.montant) for v in mes_verssements if isinstance(v.montant, (int, float, str)) and v.montant.strip())
            return total_priceversed
        
    def get_prix_to_pay(self,obj):
        sum_of_total_prices = obj.produits_en_bon_rectification.aggregate(models.Sum('totalprice'))['totalprice__sum'] or 0
        return sum_of_total_prices  - obj.totalremise

    def get_prixtotal(self,obj):
        sum_of_total_prices = obj.produits_en_bon_rectification.aggregate(models.Sum('totalprice'))['totalprice__sum'] or 0
        return sum_of_total_prices

    def get_regle(self,obj):
        total_price = obj.prix_to_pay - (obj.totalprice - obj.totalremise)
        
        if total_price == Decimal('0'):
            return True
        else:
            mes_verssements = obj.verssements.all()
            total_priceversed = sum(Decimal(v.montant) if v.montant != '' else Decimal(0) for v in mes_verssements)
            total_priceversed = obj.prix_to_pay - total_priceversed

            if total_priceversed == Decimal('0'):
                return True
            else:
                return False
    def get_par_verssement(self,obj):
        if len(obj.verssements.all())>0:
            return True
        else:
            return False
            
    def montantrestant(self,obj):
        if (obj.totalprice > 0):
            restant = obj.prix_to_pay - obj.totalprice
        else:
            mes_verssements = obj.verssements.all()
            total_priceversed = sum(Decimal(v.montant) for v in mes_verssements if isinstance(v.montant, (int, float, str)) and v.montant.strip())
            restant = obj.prix_to_pay - total_priceversed
        return max(0, restant)
    
    
class verssementSerializer(serializers.ModelSerializer):
    utilisateur=CustomUserSerializer()
    bon_comptoir_associe=BonComptoireSerializer()
    bon_rectification_associe=BonRectificationSerializer()
    remaining_amount_after_payment=serializers.SerializerMethodField()
    remaining_amount_after_paymentrectif=serializers.SerializerMethodField()
    store=StoreSerializer()
    class Meta:
        model=verssement
        fields="__all__"
    def get_remaining_amount_after_payment(self,obj):
        previous_verssements = verssement.objects.filter(
            bon_comptoir_associe=obj.bon_comptoir_associe,
            date__lte=obj.date
        )
        total_previous_payments = sum(
            Decimal(v.montant) for v in previous_verssements
            if isinstance(v.montant, (int, float, str)) and v.montant.strip()
        )
        remaining_amount = obj.bon_comptoir_associe.prix_to_pay - total_previous_payments

        return remaining_amount
    def get_remaining_amount_after_paymentrectif(self,obj):
        # Get all previous verssements for the associated bon_comptoir_associe
        previous_verssements = verssement.objects.filter(
            bon_comptoir_associe=obj.bon_rectification_associe,
            date__lte=obj.date
        )

        # Calculate the total amount of previous payments
        total_previous_payments = sum(
            Decimal(v.montant) for v in previous_verssements
            if isinstance(v.montant, (int, float, str)) and v.montant.strip()
        )

        # Calculate the remaining amount after this payment
        remaining_amount = obj.bon_rectification_associe.prix_to_pay - total_previous_payments

        return remaining_amount
class ProduitsEnBonRetourComptoirSerializer(serializers.ModelSerializer):
    produit=ProductSerializer()
    class Meta:
        model=ProduitsEnBonRetourComptoir
        fields="__all__"
class BonRetourComptoirSerializer(serializers.ModelSerializer):
    produit=ProduitsEnBonRetourComptoirSerializer(many=True)
    client=ClientSerializer()
    user=CustomGroupSerializer()
    bon_comptoir_associe=BonComptoireSerializer()
    bon_rectification_associe=BonRectification()
    myTotalPrice=serializers.SerializerMethodField()
    class Meta:
        model=BonRetourComptoir
        fields="__all__"
    def get_myTotalPrice(self,obj):
        total_price = sum([product.totalprice for product in obj.produit])
        return total_price

