# from faker import Faker
from random import choice, randint
from datetime import datetime, timedelta


def get_id_and_cd_request():
    return 57595, "F7E62EC7"


# def get_fake_data():
#     '''
#     gender: `m` - male or `f` - female
#     '''
#     faker = Faker(locale='ru_RU')
#     start_date = datetime.strptime('01/01/1970', '%d/%m/%Y')
#     end_date = datetime.strptime('01/01/2000', '%d/%m/%Y')
#     birthday = faker.date_between(start_date=start_date, end_date=end_date)
#     gender = choice(['MR', 'MS'])
#     if gender == "MR":
#         first_name = faker.first_name_male()
#         middle_name = faker.middle_name_male()
#         last_name = faker.last_name_male()
#     else:  # gender == "MS"
#         first_name = faker.first_name_female()
#         middle_name = faker.middle_name_female()
#         last_name = faker.last_name_female()
#     return {
#         "gender": gender,
#         "name": first_name,
#         "middle_name": middle_name,
#         "surname": last_name,
#         "email": faker.email(),
#         "year": birthday.year,
#         "month": birthday.month,
#         "day": birthday.day,
#         "phone": "+662" + str(randint(1111111, 8888888))
#     }


# if __name__ == '__main__':
#     print(get_fake_data())
