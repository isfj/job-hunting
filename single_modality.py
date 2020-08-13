from sklearn import svm
import numpy as np
import h5py
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from model import load_data


train_gene, val_gene, test_gene,train_patho,val_patho,test_patho,train_label,val_label,test_label = load_data()


clf = svm.SVC(C=0.8, kernel='rbf', decision_function_shape='ovr', probability=True)  
clf.fit(train_gene, np.argmax(train_label,1))
logits = clf.predict_proba(test_gene)[:, 1]

fpr, tpr, thresholds = roc_curve(np.argmax(test_label,1), logits)
roc_auc = auc(fpr, tpr)
print('roc_auc = ',roc_auc)




# plt.figure()
# lw = 2
# plt.figure(figsize=(10, 10))
# plt.plot(fpr, tpr, color = 'darkorange', lw = lw, label = 'ROC curve(area = %0.2f)' % roc_auc)
# plt.plot([0, 1], [0, 1], color = 'navy', lw = lw, linestyle = '--')
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.0])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('Receiver operating characteristic example')
# plt.legend(loc='lower right')
# # plt.show()
# plt.savefig('roc.png')

