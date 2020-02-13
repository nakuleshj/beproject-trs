import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel,cosine_similarity

'''l=[]
l.append(input("Enter season:").lower())
c=input("Going with?\n1.Family\n2.Friends\n3.Romantic\n4.Solo\nEnter option number:\n")
going_with=['family','friends','romantic','solo']
bm=['beaches','mountains']
interest=['adventure','sightseeing']
l.append(going_with[int(c)-1])
usr_tags = ','.join(l)
if input("Wish to enter additional preferences to improve recommendations?\n Enter y/n:\n")=='y':
    c=input("Do you prefer:\n1. Beaches\n2.Mountains\n")
    l.append(bm[int(c)-1])
    c=input("Enter purpose of your visit: 1.Adventure\n2.Sightseeing\n Enter option number:\n")
    l.insert(1,interest[int(c)-1])
else:
    l.insert(1,'adventure,sightseeing')
    l.insert(2,'beaches,mountains')         
usr_tags = ','.join(l)
print(usr_tags)
#budget=input("Enter your approximate budget:")'''
def rec_main(usr_tags):
    ds = pd.read_csv("pirs_cbf.csv")
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
            l.append(str(rec[1]).capitalize())
        return l
    list=recommend(name='usr_input', num=3)
    return list
#rec_main(usr_tags)