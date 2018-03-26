from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    def get_next_link(self):
        '''
        :return: Query param ex : ?page=1
        '''
        if not self.page.has_next():
            return None
        return '?page=' + str(self.page.next_page_number())

    def get_previous_link(self):
        '''
        :return: Query param ex : ?page=1
        '''
        if not self.page.has_previous():
            return None
        return '?page=' + str(self.page.previous_page_number())
