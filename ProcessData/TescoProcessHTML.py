from bs4 import BeautifulSoup
from ProcessData.Soup import createSoup
from itertools import islice
from ProcessData.FindBestValue import TescoFindBestValue

class TescoProcessHTML:
    def __init__(self, data):
        self.soup = createSoup(data)
        # Tesco puts their sponsored items at the top of the site, ussually they're irrelevant
        self.noOfSponsors = self.findNumberOfSponsoredItems()

    def findNumberOfSponsoredItems(self):
        sponsoredItems = self.soup.find_all('strong', class_ = "styled__FlashSashText-sc-9znnul-1")
        return len(sponsoredItems)

    def tescoGetFirstName(self):
        return self.tescoGetNames()[self.noOfSponsors: self.noOfSponsors + 1][0]

    def tescoGetFirstPrice(self):
        return self.tescoGetPrices()[self.noOfSponsors: self.noOfSponsors + 1][0]

    def tescoGetFirstImage(self):
        return self.tescoGetImages()[self.noOfSponsors: self.noOfSponsors + 1][0]

    def tescoGetFirstValue(self):
        return self.tescoGetValues()[self.noOfSponsors: self.noOfSponsors + 1][0]

    #product-tile--title
    def tescoGetNames(self):
        # Find all <h3> elements with the specified data-auto attribute value
        divs = self.soup.find_all('div', class_ = 'product-details--wrapper')

        names = []

        # Iterate over the list of <div> elements
        for div in divs:
            # Find the <span> element within the <div>
            span_element = div.find('span', class_='styled__Text-sc-1xbujuz-1 ldbwMG beans-link__text')

            # Get the text value of the <span> element
            span_value = span_element.get_text(strip=True)

            names.append(span_value)

        return names


    def tescoGetPrices(self):
        ps = self.soup.find_all("p", class_="styled__StyledHeading-sc-119w3hf-2 jWPEtj styled__Text-sc-8qlq5b-1 lnaeiZ beans-price__text")

        prices = []

        # Iterate over the list of <p> elements
        for p in ps:
            # Get the text value of the <p> element
            p_text = p.get_text(strip=True)

            prices.append(p_text)

        return prices

    def tescoGetImages(self):
        images = []
        img_elements = self.soup.find_all('img',
                                     class_="styled__Image-sjvkdn-0 bJErKA product-image beans-responsive-image__image")
        for img in img_elements:
            images.append(img["srcset"].replace("&", "&amp;"))

        return images

    def tescoGetValues(self):
        values = []
        p_elements = self.soup.find_all('p', class_="styled__StyledFootnote-sc-119w3hf-7 icrlVF styled__Subtext-sc-8qlq5b-2 bNJmdc beans-price__subtext")

        for p in p_elements:
            values.append(p.text)

        return values


    def tescoBestValue(self):
        names = self.tescoGetNames()
        prices = self.tescoGetPrices()
        images = self.tescoGetImages()
        values = self.tescoGetValues()
        combined = [{"name": name, 'price': price, "value": value, 'image': image} for name, price, value, image in zip(names, prices, values, images)]
        bestValue = TescoFindBestValue(combined)
        return bestValue


    def tescoGetFirst(self):
        name = self.tescoGetFirstName()
        price = self.tescoGetFirstPrice()
        image = self.tescoGetFirstImage()
        value = self.tescoGetFirstValue()
        combined_data = {"name": name, "price": price, "value": value, "image": image}
        return combined_data