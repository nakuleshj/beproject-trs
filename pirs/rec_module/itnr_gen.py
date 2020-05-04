import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from django.contrib.staticfiles.storage import staticfiles_storage
def itnr_main(plc):
        s='rec_module/dataset/'+plc+'.csv'
        urld = staticfiles_storage.path(s)
        data=pd.read_csv(urld)
        act=data['activity_name'].copy()
        dur=int(len(act)/3)
        data.drop('activity_name',axis=1,inplace=True)
        data=data.rename_axis('ID').values
        ac = AgglomerativeClustering(n_clusters=dur, affinity='precomputed', linkage='complete')
        clusters = ac.fit_predict(data)
        final_itnr={}
        for f in range(1,dur+1):
                plcs=[]
                k='Day '+str(f)
                for i,e in enumerate(clusters):
                        if e==(f-1):
                                plcs.append(act[i])
                final_itnr[k]=plcs
        return final_itnr