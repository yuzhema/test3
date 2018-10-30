from home_page.models import Books


class Catalogue:
    def __init__(self,book,amount):
        self.book=book
        self.amount=amount
        self.per_sum = self.book.dang_price*self.amount
class Cart2:
    def __init__(self):
        self.catalogue=[]
        self.total_price=0
        self.save_price=0



    def sum(self):
        self.total_price=0
        self.save_price=0
        for i in self.catalogue:
            self.total_price+=int(i.book.dang_price*i.amount)
            self.save_price+=(i.book.price-i.book.dang_price)*i.amount
    def add(self,book_id,num):
        book=Books.objects.get(pk=book_id)

        self.catalogue.append(Catalogue(book,num))
        self.sum()
    def delete(self,book_id):
        for i in self.catalogue:
            if i.book.id==book_id:
                self.catalogue.remove(i)
                self.sum()
