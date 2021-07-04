from sklearn.metrics import roc_auc_score, roc_curve, auc
import numpy as np


def calc_roc(y_true, y_score, num_thresholds=10):
    desc_score_indices = np.argsort(y_score, kind="mergesort")[::-1]  # 降序排序
    y_score = np.asarray(y_score)[desc_score_indices]
    y_true = np.asarray(y_true)[desc_score_indices]

    # 去除重复的概率值
    distinct_value_indices = np.where(np.diff(y_score))[0]
    threshold_idxs = np.r_[distinct_value_indices, y_true.size - 1]

    y_score = y_score[threshold_idxs]
    y_true = y_true[threshold_idxs]

    kepsilon = 1e-7
    thresholds = [
        (i + 1) * 1.0 / (num_thresholds - 1) for i in range(num_thresholds - 2)
    ]  # thresholds是在[0-1]中分num_thresholds个段，而首尾加一个微量值避免0和1.
    thresholds = [0.0 + kepsilon] + thresholds + [1.0 - kepsilon]

    tpr_list = []
    fpr_list = []
    for threshold in thresholds:
        fpr, tpr = get_tpr_fpr(y_true, y_score, threshold)
        tpr_list.append(tpr)
        fpr_list.append(fpr)

    return np.asarray(tpr_list), np.asarray(fpr_list), np.asarray(thresholds)


def get_tpr_fpr(y_true, y_score, threshold):
    y_pred = np.zeros(len(y_true))
    y_pred[np.where(np.asarray(y_score) >= threshold)] = 1
    tp_count = np.sum(np.logical_and(y_true, y_pred))
    tpr = tp_count / (np.sum(y_true))

    fp_count = np.sum((y_pred - np.asarray(y_true)) > 0)
    fpr = fp_count / (len(y_true) - np.sum(y_true))
    return fpr, tpr


if __name__ == "__main__":
    label_all = [1, 0, 1, 1, 0, 1, 1, 0, 0, 1]
    # pred_all = [1,0,1,0,0,1,1,0,0,1]
    pred_all = [0.0574996, 0.54140656, 0.55947868, 0.83510934, 0.67950011, 0.22965501, 0.48261028, 0.2607179,
                0.86764296, 0.91937525]
    print(label_all)
    print(pred_all)

    # auc = roc_auc_score(label_all,pred_all)
    # print("auc:%f" % auc)

    fpr, tpr, thresholds = roc_curve(label_all, pred_all)
    # print(fpr)
    # print(tpr)
    # print(thresholds)

    auc0 = auc(fpr, tpr)
    print(auc0)

    fpr1, tpr1, thresholds1 = calc_roc(label_all, pred_all)
    # print(fpr1)
    # print(tpr1)
    # print(thresholds1)

    auc1 = auc(fpr1, tpr1)
    print(auc1)
