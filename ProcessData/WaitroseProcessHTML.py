from ProcessData.Soup import createSoup
from RetrieveData.RetrieveData import *
from ProcessData.Driver import *
from ProcessData.FindUnit import *
from ProcessData.FindBestValue import *

# product-pod-price for price
# data-test-id="product-pod" for entire product

class WaitroseProcessHTML:
    def __init__(self, data):
        self.driver = CreateDriver()
        self.soup = createSoup(data)

    def waitroseGetFirstName(self):
        return self.soup.find(attrs={'data-product-name': True})['data-product-name']

    def waitroseGetFirstPrice(self):
        return self.soup.find('span', {'data-test': 'product-pod-price'})\
            .find("span").text

    def waitroseGetFirstImage(self):
        image = self.soup.find('img', alt=self.waitroseGetFirstName())
        src = image['src']
        return src

    def waitroseGetFirstItem(self):
        name = self.waitroseGetFirstName()
        price = self.waitroseGetFirstPrice()
        image = self.waitroseGetFirstImage()
        combined_data = {"name" : name, "price" : price, "image": image}
        return combined_data

    def waitroseGetNames(self):
        # Find all elements with the 'data-product-name' attribute
        product_elements = self.soup.find_all(attrs={'data-product-name': True})
        # Iterate over the filtered elements
        product_names = []
        for element in product_elements:
            product_names.append(element['data-product-name'])
        return product_names

    def waitroseGetPrices(self):
        # Find all occurrences of the innermost span elements
        inner_spans = self.soup.find_all('span', {'data-test': 'product-pod-price'})

        # Extract the values from each inner span and remove the unwanted character
        values = [span.find('span').text.replace('Â', '') for span in inner_spans]

        return values

    def waitroseGetImages(self):
        images = []
        for name in self.waitroseGetNames():
            img_elements = self.soup.find_all('img', alt=name)

            # Get the src attribute of the first matching img element
            if img_elements:
                src = img_elements[0]['src']
                images.append(src)
            else:
                raise Exception("img not found: " + name)

        return images

    def waitroseGetValues(self):
        spans = self.soup.find_all("span", class_="pricePerUnit___a1PxI priceInfo___ThE1M")
        values = [s.text for s in spans]
        return values

    def waitroseCleanValues(self, values):
        """
        Values are currently in the value Price per unit£1.39/litre
        :param values: a list of raw data values e.g {"name": "milk", "price": "£1.33", "image": "", "value" : 'Price per unit£2.10/litre'},
        :return: a clean list of data values e.g {"name": "milk", "price": "£1.33", "image": "", "value" : '£2.10/litre'}
        """
        cleanValues = [{**obj, 'value': obj["value"].replace("Price per unit", "")} for obj in values]

        return cleanValues

    def waitroseBestValue(self):
        names = self.waitroseGetNames()
        prices = self.waitroseGetPrices()
        images = self.waitroseGetImages()
        values = self.waitroseGetValues()

        combined = [{"name": name, 'price': price, "value": value, 'image': image} for name, price, value, image in zip(names, prices, values, images)]

        # Clean data
        clean_data = self.waitroseCleanValues(combined)

        # Find most common unit
        common_units = FindCommonUnit(clean_data)

        # Find best value from common_units
        best_value = WaitroseFindBestValue(common_units)

        return best_value

    def processWaitroseHtml(self):
        names = self.waitroseGetNames()
        prices = self.waitroseGetPrices()
        images = self.waitroseGetImages()
        combined_data = {"name" : names[0], "prices" : prices[0], "image": prices[0]}
        return combined_data




