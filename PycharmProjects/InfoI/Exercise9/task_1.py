# To do:
# System writes data to file but in-memory functionality (with dictionary) should not be deleted
# Notification of customers by call or email - add new possibilities next to smsSender
# Pull all car wash information together into a single class (this class should wrap customer, car and job_id
# Add properties (contact_details, notification_message) to CarWashJob
# Pull new_job_id functionallity inside CarWashJob - modify the constructor such that if no id is given, a new one is created

"""class CarWash(object):
    job_counter = 0

    def __init__(self):
        self.persistence = {}
        self.sms_sender = SmsSender()

    def register_car_for_wash(self, car, customer):
        job_id = CarWash.new_job_id()
        self.persistence[job_id] = (car, customer)
        return job_id

    def complete_wash(self, job_id):
        car, customer = self.persistence[job_id]
        phone_number = customer.mobile_phone
        msg = f'Job {job_id}, Car {car.plate} washed.'
        self.sms_sender.send(phone_number, msg)

    @staticmethod
    def new_job_id():
        job_id = CarWash.job_counter
        CarWash.job_counter += 1
        return f'#{job_id}'


class Customer(object):

    def __init__(self, name, mobile_phone):
        self.name = name
        self.mobile_phone = mobile_phone


class Car(object):

    def __init__(self, plate):
        self.plate = plate


class SmsSender(object):

    def send(self, phone_number, msg):
        print(f'Sending text message to {phone_number}: {msg}')
        # ... do some weird SMS magic


if __name__ == '__main__':
    car_wash = CarWash()
    car1 = Car('ZH 123456')
    car2 = Car('AG 654321')
    customer1 = Customer('Foo', '079 xxx xxxx')
    customer2 = Customer('Bar', '078 xxx xxxx')

    job_id1 = car_wash.register_car_for_wash(car1, customer1)
    job_id2 = car_wash.register_car_for_wash(car2, customer2)
    assert job_id1 != job_id2

    car_wash.complete_wash(job_id1)"""

from abc import ABC, abstractclassmethod

class CarWash(object):
    """Process of washing a car"""

    def __init__(self):
        self.persistence = {}
        self.sms_sender = SmsSender()
        self.email_sender = EMailSender
        self.caller = Caller

    def register_car_for_wash(self, car, customer):
        CarWashJob.Car = car
        CarWashJob.Customer = customer
        job = CarWashJob(car, customer)
        self.persistence[job.job_id] = job
        return job.job_id

    def complete_wash(self, job_id):
        job = self.persistence[job_id]
        #safe completed job to file
        with open ("persistence.csv", "w") as file:
            file.write(job_id)
        self.sms_sender.send(job.contact_details, job.notification_message
    )

class CarWashJob(ABC):
    """pulls together all car wash information"""
    job_counter = 0

    @staticmethod
    def new_job_id():
        job_id = CarWashJob.job_counter
        CarWashJob.job_counter += 1
        return f'#{job_id}'

    @property
    def contact_details(self):
        return self.mobile_number

    @property
    def notification_message(self):
        msg = (f' Job {job_id}, Car {plate} washed')
        return msg

    @abstractclassmethod
    def Customer(self, plate):
        self.plate = plate


class Customer(CarWashJob):
    def __init__(self, name, mobile_number):
        self.name = name
        self.mobile_number = mobile_number

class Car(CarWashJob):
    def __init__(self, plate):
        self.plate = plate


class SmsSender(object):
    """Sends a sms to the customer"""
    def send(self, phone_number):
        print(f'Sending text message to {phone_number}: {CarWashJob.notification_message}')
        # ... do some weird SMS magic

class EMailSender(object):
    """Sends a e_mail to the customer"""
    def send(self, e_mail):
        print(f'Sending text message to {e_mail}: {CarWashJob.notification_message}')

class Caller(object):
    """Makes a call to the customer"""
    def call(self, phone_number):
        print(f'Call the number {phone_number} and tell them {CarWashJob.notification_message}')


if __name__ == '__main__':
    car_wash = CarWash()

    car1 = Car('ZH 123456')
    car2 = Car('AG 654321')
    customer1 = Customer('Foo', '079 xxx xxxx')
    customer2 = Customer('Bar', '078 xxx xxxx')

    job_id1 = car_wash.register_car_for_wash(car1, customer1)
    job_id2 = car_wash.register_car_for_wash(car2, customer2)

    car_wash.complete_wash(job_id2)
    car_wash.complete_wash(job_id1)