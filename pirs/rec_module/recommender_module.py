import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel,cosine_similarity
from django.contrib.staticfiles.storage import staticfiles_storage


def rec_main(usr_tags):
    url = staticfiles_storage.path('rec_module/pirs_cbf.csv')
    print(url)
    ds = pd.read_csv(url)
    ds=ds.append({'name':'usr_input','tags':usr_tags},ignore_index=True)
    ds.drop(3)
    tf = TfidfVectorizer()
    x1=tf.fit_transform(ds['tags'])
    #cs=cosine_similarity(x,x)
    #tf.get_feature_names()
    print(x1.shape)
    df=pd.DataFrame(x1.toarray().transpose(),index=tf.get_feature_names())
    df.columns=ds['name']
    cosine_similarities = linear_kernel(x1,x1)
    results = {}
    for idx, row in ds.iterrows():
        similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
        similar_items = [(cosine_similarities[idx][i], ds['name'][i]) for i in similar_indices] 
        results[row['name']] = similar_items[1:]
    def item(name):
        return ds.loc[ds['name'] == name]['name']
    def recommend(name, num):
        print("Recommending " + str(num) + " destinations as per user input...")
        print("-------")
        l=[]
        recs = results[name][:num]
        for rec in recs:
            #print("Recommended: " + item(rec[1]) + " (score:" + str(rec[0]) + ")")
            l.append(str(rec[1]))
        return l
    list=recommend(name='usr_input', num=5)
    return list
#rec_main(usr_tags)