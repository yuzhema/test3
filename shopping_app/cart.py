from home_page.models import Books


class Catalogue:
    def __init__(self,book,amount):
        self.book=book
        self.amount=amount

class Cart:
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
        for i in self.catalogue:
            if i.book.id==int(book_id):
                i.amount+=num
                self.sum()
                break
        else:
            book=Books.objects.get(pk=book_id)
            self.catalogue.append(Catalogue(book,num))
            self.sum()

    def modify(self,book_id,amount):
        for i in self.catalogue:
            if book_id==i.book.id:
                i.amount=amount
                self.sum()
                return {'book':i.book}
    def delete(self,book_id):
        for i in self.catalogue:
            if i.book.id==book_id:
                self.catalogue.remove(i)
                self.sum()
