def accuracy_score(real, predicted):
    return sum([real[i] == predicted[i] for i in range(len(real))])/len(real)
