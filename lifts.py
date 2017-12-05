

class ElevatorSystem:
    def __init__(self,elevator_id, floor_num):
 
        self.elevator_id=elevator_id
        self.floor_num=floor_num
        self.target_floor_num=''
        self.current_direction=''

        self.target_floor_num_list=[]

        self.other_step_list=[]
        self.step_list=[]


    #может будет показывать историю всех поездок по-порядку. Там из списка удалился, а сюда добавился
    def status(self):
        
        return [self.floor_num, self.target_floor_num]
        


    '''
    elevator_id - номер лифта
    floor_num - текущее положение лифта
    target_floor_num - этаж, к которому направляется лифт (берем в виде списка (или лучше 'set' упорядоченный)
    '''
    def update(self, elevator_id, floor_num, target_floor_num):
        #target_floor_num=self.target_floor_num
        #print ('Elevator={}; current floor={}; destination floor={}'.format(elevator_id, floor_num, target_floor_num))
        return {elevator_id:(floor_num,target_floor_num)}
    
    
    '''
    floor_num - человек вызвал лифт с определённого этажа
    direction -если человеку нужно вниз - нажимает кнопку вниз (-1), вверх - нажимает вверх (1)
    target_floor_number - этаж, на который нужно попасть человеку. Скрыт, пока человек не войдет в лифт. Тоже
        должен приниматься во внимание
    '''
    def pickup(self, floor_num, direction):#, target_floor_number):

        
        self.target_floor_num_list.append([floor_num, direction])

        self.step()
        return 'Вызов получен с этажа {}, направление {}'.format(floor_num, direction)

        
        
    

    #time stepping. Что имеется ввиду?
    def step(self):
        if len(self.target_floor_num_list)==1:
            self.current_direction=self.target_floor_num_list[0][1]
            self.target_floor_num = self.target_floor_num_list[0][0]
            self.step_list.append(self.target_floor_num_list[0])
            self.update('lift#1',self.floor_num, self.target_floor_num)

            
        #it works!!!
        elif len(self.target_floor_num_list)>1:
            if self.current_direction==-1:
                if self.target_floor_num_list[-1][1]!=-1:
                    self.other_step_list.append(self.target_floor_num_list[-1])
                    self.other_step_list.sort()
                    #self.step_list.append(self.target_floor_num_list[-1])
                elif self.target_floor_num_list[-1][1]==-1 and self.target_floor_num_list[-1][0]<=self.floor_num and self.target_floor_num_list[-1][0]>self.step_list[0][0]:
                    self.step_list.insert(0,self.target_floor_num_list[-1]) #+++
                    #self.target_floor_num=self.target_floor_num_list[-1][0]
                elif self.target_floor_num_list[-1][1]==-1 and self.target_floor_num_list[-1][0]<self.step_list[0][0]:
                    #self.step_list.append(self.target_floor_num_list[-1])    #+++
                    for i in self.step_list:
                        if i[0]<=self.target_floor_num_list[-1][0]:
                            self.step_list.insert(self.step_list.index(i),self.target_floor_num_list[-1])
                            #self.target_floor_num=self.target_floor_num_list[-1][0]
                            break
                        elif i[0]>self.target_floor_num_list[-1][0] and len(self.step_list)==self.step_list.index(i)+1:
                            self.step_list.append(self.target_floor_num_list[-1])
                            #self.other_step_list.append(self.target_floor_num_list[-1])#предыдуш поменял на эту
                            break
                        elif i[0]>self.target_floor_num_list[-1][0]:
                             continue
                        else:
                            print ('something wrong with step_list when direction is -1')

                elif self.target_floor_num_list[-1][1]==-1 and self.target_floor_num_list[-1][0]>self.floor_num and self.target_floor_num_list[-1][0]>self.step_list[0][0]:
                    self.step_list.insert(0,self.target_floor_num_list[-1])
      
                else:
                    print ('something wrong with direction')



            elif self.current_direction==1:
                self.other_step_list.append(self.target_floor_num_list[-1])
                self.other_step_list.sort()

                self.current_direction=-1
                





            else: print('something wrong with direction')
                
            

        else: print('something wrong with step')

        
        




            

class Time():
    def __init__(self):
        self.time=0
    def add(self,num):
        self.time+=num
        return self.time
        
        



if __name__== '__main__':


    time=Time()
    lift=ElevatorSystem('lift#1',10)
    print (lift.pickup(7,-1))

    print (lift.pickup(8,1))

    print (lift.pickup(5,-1))

    print (lift.pickup(2,-1))

    print (lift.pickup(7,1))

    print (lift.pickup(4,-1))

    print (lift.pickup(6,1))

    print (lift.pickup(14,-1))

    print (lift.pickup(2,1))

    print (lift.pickup(6,-1))



    print ()
    print ('Очередь вызовов лифта:\n', lift.target_floor_num_list)
    print ('Очередь движения лифта:\n', lift.step_list+[0]+lift.other_step_list)




    
