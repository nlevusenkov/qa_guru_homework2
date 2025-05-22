from selene import browser, have


def test_google_search(setting_browser):
    browser.open('https://www.google.com')
    browser.element('[name="q"]').type('qa.guru').press_enter()
    browser.element('html').should(have.text('About this page'))
