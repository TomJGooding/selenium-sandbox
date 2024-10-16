from pages.webform import WebFormPage


def test_webform(driver) -> None:
    webform_page = WebFormPage(driver)
    webform_page.load()

    submitted_page = webform_page.type_text_input("Selenium").click_submit()

    assert submitted_page.get_message_text() == "Received!"
