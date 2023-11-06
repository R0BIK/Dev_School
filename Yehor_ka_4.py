class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return(len(self.collection))

    def page_count(self):
        pages = len(self.collection) / self.items_per_page
        if pages != int(pages):
            return(int(pages) + 1)
        return(pages)

    def page_item_count(self, page_index):
        ANumberOfPages = self.page_count()
        if len(self.collection) == 0 or page_index >= ANumberOfPages or page_index < 0:
            return (-1)
        if page_index == ANumberOfPages - 1:
            return(len(self.collection) - (ANumberOfPages - 1) * self.items_per_page)
        else:
            return(self.items_per_page)

    def page_index(self, item_index):
        if item_index > len(self.collection) - 1 or item_index < 0:
            return(-1)
        return((item_index) // self.items_per_page)
