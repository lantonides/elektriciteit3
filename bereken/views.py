from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import InvulForm
from .models import Netbeheerderkosten,Kosten,Algemenekosten
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def bereken(request):
        if request.method=='POST':
                form=InvulForm(request.POST)
                if form.is_valid():
			huidig_prijs_kw=form.cleaned_data['huidig_prijs_kw']
			huidig_prijs_m3=form.cleaned_data['huidig_prijs_m3']
                        gasverbruik=form.cleaned_data['gasverbruik']
                        kw_verbruik=form.cleaned_data['kw_verbruik']
#                        leverancier=form.cleaned_data['leverancier']
#                        netbeheerder=form.cleaned_data['netbeheerder']
                        heffingskorting=Algemenekosten.objects.get(jaar='2016').heffingskorting_elektriciteit
                        capaciteitstarief_elektriciteit_25A=Netbeheerderkosten.objects.get(netbeheerder=netbeheerder).capaciteitstarief_elektriciteit_25A_bemeten_per_jaar
                        capaciteitstarief_gas=Netbeheerderkosten.objects.get(netbeheerder=netbeheerder).capaciteitstarief_gas
#                        kw_prijs=Kosten.objects.get(leverancier=leverancier).prijs_per_Kw
#                        gasprijs=Kosten.objects.get(leverancier=leverancier).gasprijs_per_m3
#                        ODE_per_kw_inclBTW=Algemenekosten.objects.get(jaar='2016').ODE_per_kw_inclBTW
#                        ODE_per_m3_inclBTW=Algemenekosten.objects.get(jaar='2016').ODE_per_m3_inclBTW
#                        energiebelasting_per_kw_inclBTW=Algemenekosten.objects.get(jaar='2016').energiebelasting_per_kw_inclBTW
#                        energiebelasting_per_m3_inclBTW=Algemenekosten.objects.get(jaar='2016').energiebelasting_per_kw_inclBTW
#                        totaal_elektriciteitskosten=float(kw_verbruik)*(kw_prijs+ODE_per_kw_inclBTW+energiebelasting_per_kw_inclBTW)+capaciteitstarief_elektriciteit_25A-heffingskorting
#                        totaal_gaskosten=float(gasverbruik)*(gasprijs+ODE_per_m3_inclBTW+energiebelasting_per_m3_inclBTW)+capaciteitstarief_gas
#                        prijs_per_m3=totaal_gaskosten/float(gasverbruik)
#                        prijs_per_kw=totaal_elektriciteitskosten/float(kw_verbruik)

                        jaar=[]
                        jaarkosten_gas=[]
                        jaarkosten_el=[]
                        jg=totaal_gaskosten
                        je=totaal_elektriciteitskosten
                        for x in range(0,25):
                                jaarkosten_gas1=jg*x
                                jaarkosten_el1=je*x
                                jaar.append(x)
                                jaarkosten_gas.append(jaarkosten_gas1)
                                jaarkosten_el.append(jaarkosten_el1)

                        plt.clf()
                        plt.plot(jaar,jaarkosten_el,label='Huidige elektriciteits situatie')
                        plt.plot(jaar,jaarkosten_gas,label='Huidige gas situatie')

                        plt.ylabel('Euro')
                        plt.xlabel('Jaren')

                        lgd = plt.legend(loc='upper center', bbox_to_anchor=(0.5,-0.1))
                        plt.title('Energie kosten')

                        buf = BytesIO()
                        plt.savefig(buf, format='png', bbox_extra_artists=(lgd,),bbox_inches='tight')
                        out = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
                        img_tag = "data:image/png;base64,{0}".format(out)
                        buf.close()

                        return render(request,'bereken/resultaat.html',{'gasverbruik':gasverbruik, 'leverancier':leverancier, 'kw_verbruik':kw_verbruik,'netbeheerder':netbeheerder,'heffingskorting':heffingskorting,'capaciteitstarief_elektriciteit_25A':capaciteitstarief_elektriciteit_25A,'capaciteitstarief_gas':capaciteitstarief_gas,'kw_prijs':kw_prijs, 'gasprijs':gasprijs,'ODE_per_kw_inclBTW':ODE_per_kw_inclBTW,'ODE_per_m3_inclBTW':ODE_per_m3_inclBTW,'energiebelasting_per_kw_inclBTW':energiebelasting_per_kw_inclBTW,'energiebelasting_per_m3_inclBTW':energiebelasting_per_kw_inclBTW,'totaal_elektriciteitskosten':totaal_elektriciteitskosten,'totaal_gaskosten':totaal_gaskosten,'prijs_per_m3':prijs_per_m3,'prijs_per_kw':prijs_per_kw,'img_tag':img_tag})

        else:
                form=InvulForm()
        return render(request, 'bereken/invul.html',{'form':form})
