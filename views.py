from search_object import search_object

class CreateMixin:
    
    def _get_or_set_objects_and_id(self):
        try:
            self.id
            self.objects
        except (NameError, AttributeError):
            self.objects = []
            self.id = 0
            
    def __init__(self) -> None:
        self._get_or_set_objects_and_id()     
    
    def check_data(self, car):
        data_of_issue = car['date_of_issue']
        engine_capacity = car['engine_capacity']
        mileage = car['mileage']
        price = car['price']
        
        if not data_of_issue.isdigit():
            return 'Не верно введена дата!'
        if int(data_of_issue) not in range(1960, 2024):
            return 'Не верно введена дата!'
        if not mileage.isdigit():
            return 'Не верно введен пробег машины!'
        
        try:
            float(engine_capacity)
        except ValueError:
            return 'Не верно введен объем двигателя!'
        try:
            float(price)
        except ValueError:
            return 'Не верно введена цена машины!'
        
        
        return 'isCorrect'
    
    def post(self, car):
        check = self.check_data(car)
        
        if check == 'isCorrect':
            self.id += 1
            car['engine_capacity'] = round(float(car['engine_capacity']), 1)
            car['price'] = round(float(car['price']), 2)
            obj = dict(id=self.id, **car)
            self.objects.append(obj)
            return {'status': '201 created', 'msg': obj}
        else:
            return {'status': 'InputError', 'msg': check}

class ListingMixin:
    def list_(self):
        if not self.id:
            return 'Записей нет!'
        # res = [{'id': obj['id'], 'marka': obj['marka'], 'date_of_issue': obj['date_of_issue'], 'engine_capacity': obj['engine_capacity'], 'color': obj['color'], 'body_type': obj['body_type'], 'mileage': obj['mileage'], 'price': obj['price']} for obj in self.objects]
        # return {'status': '200 OK', 'msg': res}
        return self.objects


class RetriaveMixin:
    @search_object
    def retriave(self, id, **kwargs):
        obj = kwargs['object_']
        
        if obj:
            return {'status': '200 OK!', 'msg': obj}
        return {'status': '404 Not Found!'}  
    
class UpdateMixin:
    @search_object
    def patch(self, id, field, new_info, **kwargs):
        obj = kwargs.pop('object_')
        
        try:
            obj[field] = new_info
            return {'status': '200 OK!', 'msg': obj}
        except:
            return {'status': '404 Not Found!'} 
        
class DeleteMixin:
    @search_object
    def delete_(self, id, **kwargs):
        obj = kwargs['object_']
        if obj:
            self.objects.remove(obj)
            return {'status': '204 No Content', 'msg': 'Deleted'}
        return {'status': '404 Not Found!'}
        
        

