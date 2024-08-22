from behave import given, when, then

class Car:
    def __init__(self):
        self.door_closed = False
    
    def close_door(self):
        self.door_closed = True

    def is_door_closed(self):
        return self.door_closed

    def door_status_indicator(self):
        return "Door is closed" if self.door_closed else "Door is open"

# contexto
@given('the car door is open')
def step_given_car_door_is_open(context):
    context.car = Car()
    context.car.door_closed = False

@when('the user closes the car door')
def step_when_user_closes_car_door(context):
    context.car.close_door()

@then('the car door should be closed')
def step_then_car_door_should_be_closed(context):
    assert context.car.is_door_closed() is True

@then('the car should indicate the door is closed')
def step_then_car_should_indicate_door_is_closed(context):
    assert context.car.door_status_indicator() == "Door is closed"
