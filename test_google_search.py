from selene import browser, have


def test_google_search(setting_browser):
    browser.open('/')
    browser.element('[name="q"]').type('qa.guru').press_enter()
    browser.element('html').should(have.text('Мы зарегистрировали подозрительный трафик, исходящий из вашей сети. С помощью этой страницы мы сможем определить, что запросы отправляете именно вы, а не робот. Почему это могло произойти?'))


def test_google_noresult(setting_browser):
    browser.open('/')
    browser.element('[name="q"]').type('11312312ушщ12воылап3г1нш2ркотцлуавырн1шгркщотадвырашгрщывadasdasdasdasdasd').press_enter()
    browser.element('html').should(have.text('По запросу 11312312ушщ12воылап3г1нш2ркотцлуавырн1шгркщотадвырашгрщывadasdasdasdasdasd ничего не найдено.'))