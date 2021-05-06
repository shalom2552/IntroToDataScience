import sys

# argv[0] = /home/student/your_path/main.py,
# argv[1] = /home/student/your_path/dpc-covid19-ita-regioni.csv
from data import Data
from districts import Districts


def main(argv):
    path = argv[1]

    data = Data(path)
    dataset = Districts(data)
    question_1(dataset)
    data = Data(path)
    dataset = Districts(data)
    question_2(dataset)


def question_1(dataset):
    """
    In this question we will be interested in the group of districts D.
    These are the districts whose name begins with S or L.
    This function calculates the mean and median for those districts with the given features below.
    :param dataset: dict of data from csv file
    """
    district_D = ['S', 'L']
    dataset.filter_district(district_D)
    features = ['hospitalized_with_symptoms', 'intensive_care', 'total_hospitalized', 'home_insulation']
    print("Question 1:")
    dataset.print_details(features, ['mean', 'median'])
    print()


def question_2(dataset):
    """
    In this question we will help the Italian Corona Cabinet decide whether to impose a curfew on Italian
    closure policy. We will define a good day for the district if the number of recoverers in it was higher than the
    number of newly diagnosed, otherwise it will be considered a bad day. We will define a district as a green district
    if the number of good days recorded in the data is greater than 340. It was decided that if the number of non-green
    districts documented in the data is greater than 10 a closure will be imposed on the whole state otherwise a closure
    will be imposed only on the non-green districts.
    :param dataset: dict of data from csv file
    """
    print("Question 2:")
    dataset.determine_day_type()
    num_of_districts = len(dataset.get_districts_class())
    print("Number of districts: " + str(num_of_districts))
    green_districts = dataset.get_districts_class()
    num_of_not_green_districts = sum(1 for district in green_districts if green_districts[district] == 'not green')
    print("Number of not green districts: " + str(num_of_not_green_districts))
    do_closure = 'Yes' if (num_of_not_green_districts > 10) else 'No'
    print("Will a lockdown be forced on whole of Italy?: " + str(do_closure))


if __name__ == "__main__":
    main(sys.argv)
