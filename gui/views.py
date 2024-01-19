from django.shortcuts import render,HttpResponse
from django.contrib import messages
from gui.models import pred
import joblib
import numpy as np 
lr_loaded = joblib.load('./static/lr_fcc.joblib')
xg_loaded = joblib.load('./static/xg_fcc.joblib')
etr_loaded = joblib.load('./static/etr_fcc.joblib')
gbr_loaded = joblib.load('./static/gbr_fcc.joblib')
br_loaded = joblib.load('./static/br_fcc.joblib')
rf_loaded = joblib.load('./static/rf_fcc.joblib')
lr_e_loaded = joblib.load('./static/lr_ecc.joblib')
xg_e_loaded = joblib.load('./static/xg_ecc.joblib')
etr_e_loaded = joblib.load('./static/etr_ecc.joblib')
gbr_e_loaded = joblib.load('./static/gbr_ecc.joblib')
br_e_loaded = joblib.load('./static/br_ecc.joblib')
rf_e_loaded = joblib.load('./static/rf_ecc.joblib')

def index(request):
    return render(request,'index.html')
    
def prr(request):
    if request.method=="POST":
        mo= request.POST['mod']
        out=  request.POST['out']
        fc=request.POST['fc']
        tf=request.POST['tf']
        ef=request.POST['ef']
        ar=request.POST['ar']
        ht=request.POST['ht']
        area=request.POST['area']
        predic = pred(mod=mo,out=out,fc=fc,tf=tf,ef=ef,ar=ar,ht=ht,area=area)
        print(predic)
        predic.save()
        features= [fc,tf,ef,ar,ht,area]
        final_features = np.array(features)
        prediction=0
        if mo==1 and out==1:
            pred_lr = lr_loaded.predict([final_features])
            pred_xg = xg_loaded.predict(final_features.reshape(1,-1))
            prediction= (pred_lr+pred_xg)/2
            content={
                'prediction_text':'The predicted Confined concrete strength of the sample is {}MPa'.format(prediction)
            }
            return render(request,'temp.html', content)

        elif mo==2 and out==1:
            pred_lr = lr_loaded.predict(final_features)
            pred_rf = rf_loaded.predict(final_features)
            prediction= (pred_lr+pred_rf)/2
            content={
                'prediction_text':'The predicted Confined concrete strength of the sample is {}MPa'.format(prediction)
            }
            return render(request,'temp.html', content)
        elif mo==3 and out==1:
            pred_lr = lr_loaded.predict(final_features)
            pred_gbr = gbr_loaded.predict(final_features)
            prediction= (pred_lr+pred_gbr)/2
            content={
                'prediction_text':'The predicted Confined concrete strength of the sample is {}MPa'.format(prediction)
            }
            return render(request,'temp.html', content)
        elif mo==4 and out==1:
            pred_br = br_loaded.predict(final_features)
            pred_gbr = gbr_loaded.predict(final_features)
            prediction= (pred_br+pred_gbr)/2
            content={
                'prediction_text':'The predicted Confined concrete strength of the sample is {}MPa'.format(prediction)
            }
            return render(request,'temp.html', content)
        elif mo==5 and out==1:
            pred_br = br_loaded.predict(final_features)
            pred_etr = etr_loaded.predict(final_features)
            prediction= (pred_br+pred_etr)/2
            content={
                'prediction_text':'The predicted Confined concrete strength of the sample is {}MPa'.format(prediction)
            }
            return render(request,'temp.html', content)
        elif mo==6 and out==1:
            pred_lr = lr_loaded.predict(final_features)
            pred_br = br_loaded.predict(final_features)
            prediction= (pred_lr+pred_br)/2
            content={
                'prediction_text':'The predicted Confined concrete strain of the sample is {}mm/mm'.format(prediction)
            }
            return render(request,'temp.html', content)
            
        elif mo==1 and out==2:
            pred_lr = lr_e_loaded.predict(final_features)
            pred_br = br_e_loaded.predict(final_features)
            prediction= (pred_lr+pred_br)/2
            content={
                'prediction_text':'The predicted Confined concrete strain of the sample is {}mm/mm'.format(prediction)
            }
            return render(request,'temp.html', content)
        elif mo==2 and out==2:
            pred_lr = lr_e_loaded.predict(final_features)
            pred_rf = rf_e_loaded.predict(final_features)
            prediction= (pred_lr+pred_rf)/2
            content={
                'prediction_text':'The predicted Confined concrete strain of the sample is {}mm/mm'.format(prediction)
            }
            return render(request,'temp.html', content)
        elif mo==3 and out==2:
            pred_lr = lr_e_loaded.predict(final_features)
            pred_gbr = gbr_e_loaded.predict(final_features)
            prediction= (pred_lr+pred_gbr)/2
            content={
                'prediction_text':'The predicted Confined concrete strain of the sample is {}mm/mm'.format(prediction)
            }
            return render(request,'temp.html', content)
        elif mo==4 and out==2:
            pred_br = br_e_loaded.predict(final_features)
            pred_gbr = gbr_e_loaded.predict(final_features)
            prediction= (pred_br+pred_gbr)/2
            content={
                'prediction_text':'The predicted Confined concrete strain of the sample is {}mm/mm'.format(prediction)
            }
            return render(request,'temp.html', content)
        elif mo==5 and out==2:
            pred_br = br_e_loaded.predict(final_features)
            pred_etr = etr_e_loaded.predict(final_features)
            prediction= (pred_br+pred_etr)/2
            content={
                'prediction_text':'The predicted Confined concrete strain of the sample is {}mm/mm'.format(prediction)
            }
            return render(request,'temp.html', content)
        elif mo==6 and out==2:
            pred_lr = lr_loaded.predict(final_features)
            pred_br = br_loaded.predict(final_features)
            prediction= (pred_lr+pred_br)/2
            content={
                'prediction_text':'The predicted Confined concrete strain of the sample is {}mm/mm'.format(prediction)
            }
            return render(request,'temp.html', content)
        else:
            content = {
                "err":"please fill all the inputs.."
            }
            return render(request,'error.html',content)

        
        
        
        
        
        
# Create your views here.
