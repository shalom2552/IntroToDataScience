import random


class CrossValidation:
    def __init__(self):
        self._folds = []

    def run_cv(self, data, n_folds, classifier, scoring_function, print_final_score=True, print_fold_score=False):
        """
        Runs cross validation
        :param n_folds: number of folds(int)
        :param classifier: model supporting train and predict functions
        :param data: list of Point
        :param scoring_function: function receiving arguments [real, predicted] and returning number
        :param print_final_score: prints average cross fold score
        :param print_fold_score: prints score per fold
        :return: average score
        """
        # Create folds
        self._folds = []
        random.seed(0)
        shuffled = list(data)
        random.shuffle(shuffled)
        fold_size = round(len(data) / n_folds)
        for i in range(n_folds):
            self._folds.append(shuffled[i * fold_size: (i + 1) * fold_size])

        average_score = 0
        for out_fold_index in range(n_folds):
            # Create train/test
            test_set = self._folds[out_fold_index]
            train_set = []
            for inner_index in range(n_folds):
                if inner_index != out_fold_index:
                    train_set += self._folds[inner_index]

            # Train and predict
            classifier.train(train_set)
            real = [x.label for x in test_set]
            predicted = classifier.predict(test_set)

            # Score
            score = scoring_function(real, predicted)
            average_score += score
            if print_fold_score:
                print('{} of fold {} : {:.2f}'.format(scoring_function.__name__, out_fold_index, score))

        average_score /= n_folds
        if print_final_score:
            print(scoring_function.__name__, average_score)
        return average_score
