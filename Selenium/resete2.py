from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://recordtv.r7.com/power-couple-brasil-5')
#driver.find_element_by_class_name('.voting-button--hidden').click()
driver.find_element_by_xpath('//*[@id="box_60a59bf643527f0c0f000fa2"]/div/div/div/div/section/div[2]/figure[1]/button').click()

'''<button class="voting-button--hidden" type="button" data-id="960" data-element="button-vote">
        Votar
      </button>

<li role="option" id="selectable-960" data-alternative-id="960" data-alternative-name="Deborah e Bruno" class="card-selectable active" tabindex="-1" data-element="selectable" aria-selected="true">
      <figure class="card-secondary " data-element="participant-modal" style="box-shadow: rgb(255, 255, 255) 0px 0px 0px 2px;">
      <div class="card-secondary__wrapper">
        <span class="shadow"></span>
        <img src="https://img.r7.com/images/deborah-e-bruno-18052021192439597?dimensions=222x124&amp;crop_position=c" class="card-secondary__photo" alt="Deborah e Bruno" data-element="participant-modal-photo">
      </div>
      <figcaption class="card-secondary__name" data-element="participant-modal-name" style="font-weight: bold;">
        <div class="card-secondary__option-wrap" data-card-secondary-color="#00BC8B">
          <span class="card-secondary__external-circle" data-element="radio" style="border-color: rgb(0, 188, 139);">
          </span>
          <span class="card-secondary__internal-circle" data-element="radio-active" style="visibility: visible; background-color: rgb(0, 188, 139);">
          </span>
        </div>Deborah e Bruno
      </figcaption>
    </figure>

    </li>

      '''
