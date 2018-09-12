#Nhap so tien trinh tu ban phim
numberOfProcess = int(input("Nhap vao so tien trinh: "))
#Nhap cac thong tin cho tung tien trinh nhu
#thoi gian thuc hien exc_time va appear_time
exc_col = []
appear_col = []
process = []

def nhapTienTrinh():
    for i in range(1, numberOfProcess + 1):
        print('-'*20)
        print('Tien trinh P{}'.format(i))
        exc_t = float(input('Nhap thoi gian CPU: '))
        appear_t = float(input('Nhap thoi diem vao RL: '))
        exc_col.append(exc_t)
        appear_col.append(appear_t)
        process.append('P{}'.format(i))
#hien thi danh sach tien trinh
def hienThiDanhSachTienTrinh():
    print('-'*66)
    print('Tien trinh', '\tThoi gian CPU', '\tThoi diem vao RL', '\tDo uu tien')
    for i,j,k in zip(exc_col, appear_col, range(0, numberOfProcess)):
        print(process[k], "\t\t", i, "\t\t", j, end='\n')
    print('-'*66)
#sap xep 3 danh sach tien trinh theo thoi gian xuat hien tang dan
def insertionSort(alist, blist, clist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position], alist[position-1] = alist[position-1], alist[position]
         blist[position], blist[position-1] = blist[position-1], blist[position]
         clist[position], clist[position-1] = clist[position-1], clist[position]
         position = position-1
#cai dat thua toan FCFS
fcfs = {}
def FCFS():
	#dung dictionary de luu lai cac P1...Pn va thoi gian CPU cua no   
    fcfs[process[0]] = 0
    for index in range(1, numberOfProcess):
        fcfs[process[index]] = exc_col[index-1]
        for subindex in range(0,index-1):
            fcfs[process[index]] += exc_col[subindex]

    print('-'*66)
    print('Tu dien luu cac tien trinh va thoi diem bat dau tien trinh: \n', fcfs)
    hienThiDanhSachTienTrinh()
    time_tb = 0
    print('Tien trinh', '\tThoi gian cho')
    print('{0}\t\t{1}'.format(process[0], 0))
    for i in range(1, numberOfProcess):
        print('{0}\t\t{1}'.format(process[i], fcfs[process[i]] - appear_col[i]))
        time_tb += fcfs[process[i]] - appear_col[i]
    time_tb = float(time_tb/numberOfProcess)
    print('Thoi gian trung binh cho moi tien trinh la: ', time_tb)

if __name__ == '__main__':
    nhapTienTrinh()
    insertionSort(appear_col, exc_col, process)
    FCFS()

