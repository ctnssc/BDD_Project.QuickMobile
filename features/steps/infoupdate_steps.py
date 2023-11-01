#Infoupdate_steps este un fisier de tipul step definition file si ajuta la
# implementarea tehnica  a scenariilor descrise in infoupdate_steps.feature.


from behave import *
from features.pages.info_page import InfoPage

@when('I press info button "Informatii cont"')
def step_impl(context):
    context.infopage = InfoPage()
    context.infopage.click_info()

@then('I should be on the info page')
def step_impl(context):
    assert context.infopage.INFO_PAGE_URL == context.infopage.get_current_url()
    assert context.infopage.INFO_PAGE_MESSAGE  in context.infopage.get_infopage_message()

@when('I enter text on "Prenume" field')
def step_impl(context):
    context.infopage.enter_firstname()

@when('I enter text on  "Nume" field')
def step_impl(context):
    context.infopage.enter_lastname()

@when('I enter a phone number on "Telefon" field')
def step_impl(context):
    context.infopage.enter_phone()

@when('I select an option from "Judet/Sector" hidden list')
def step_impl(context):
    context.infopage.select_county()

@when('I select an option from "Oras" hidden list')
def step_impl(context):
    context.infopage.select_city()

@when('I enter text on "Adresa" text box')
def step_impl(context):
    context.infopage.enter_address()

@when('I press save button "Salveaza"')
def step_impl(context):
    context.infopage.click_save()

@then('I shoud see my new data saved')
def step_impl(context):
    context.infopage.verify_saved_data()


@when('I enter a "{letters_or_simbols}" on "Telefon" field')
def step_impl(context, letters_or_simbols):
    context.infopage.enter_invalid_phone(letters_or_simbols)

@then('The new phone number:"{letters_or_simbols}" should not be saved')
def step_impl(context, letters_or_simbols):
   context.infopage.verify_saved_phone(letters_or_simbols)



@when('I select "Bucuresti" option from "Judet/Sector" hidden list')
def step_impl(context):
    context.infopage.select_bucuresti()

@then('I should see Sector 1 to 6 on the "Oras" hidden list')
def step_impl(context):
    context.infopage.verify_if_sectors_appear_on_bucuresti()


@when('I try to change the email address')
def step_impl(context):
    context.infopage.enter_email()


@then('I should not to be able to change it')
def step_impl(context):
    pass


@when('I let the "Prenume" field empty')
def step_impl(context):
    context.infopage.empty_firstname()
@when('I let the "Nume" field empty')
def step_impl(context):
    context.infopage.empty_lastname()
@then('I shoud see an error message')
def step_impl(context):
    assert context.infopage.ERROR_MESSAGE in context.infopage.verify_error_message(), 'Error message not found.'


@then('I Logout')
def step_impl(context):
    context.infopage.click_logout()
