danhsach_hoadon=[
  {
    'id':'HD001',
    'tensp': 'Ban phim co Corsair',
    'dongia': 1800000,
    'soluong': 2,
    'giamgia': 200000,
    'tongtien': 3740000,
    'phanloai': 'Lớn'
  }
]
def main():
  print('''
--------------- THANH TOÁN HÓA ĐƠN --------------
  1.Hiển thị danh sách hóa đơn
  2.Lập hóa đơn mới
  3.Cập nhật thông tin hóa đơn
  4.Hủy hóa đơn lỗi
  5.Tìm kiếm hóa đơn
  6.Thống kê phân loại hóa đơn
  7.Thoát chương trình
-------------------------------------------------
        ''')
def tinhtien_tudong(dongia,soluong,giamgia):
  tongtien=(dongia*soluong-giamgia)*1.1
  return tongtien
def phanloai(dongia,soluong,giamgia):
  tongtien=(dongia*soluong-giamgia)*1.1
  if tongtien < 1_000_000:
    phanloai = 'Nhỏ'
  elif 1_000_000 < tongtien <5_000_000:
    phanloai = 'Vừa'
  elif 5_000_000 < tongtien < 15_000_000:
    phanloai = 'Lớn'
  elif tongtien > 15_000_000:
    phanloai = 'Cao cấp'
  return phanloai
def them_hoadon():
  hoadon_moi={}
  while True:
    id_moi=input('Mời nhập vào mã hóa đơn mới: ').strip().upper()
    flag=False
    for hoadon in danhsach_hoadon:
      if id_moi == hoadon['id']:
        flag = True
        print('ID đã tồn tại!!!')
    if not flag:
      hoadon_moi['id']= id_moi
      break
  while True:
    tensp_moi=input('Mời nhập vào tên sản phẩm mới: ').strip().title()
    if len(tensp_moi)==0:
      print('Tên sản phẩm không được để trống!!!')
    else:
      hoadon_moi['tensp']=tensp_moi
      break
  while True:
    try:
      dongia_moi=int(input('Mời nhập vào đơn giá sản phẩm: '))
      soluong_moi=int(input('Mời nhập vào số lượng sản phẩm: '))
      giamgia_moi=int(input('Mời nhập vào giảm gia sản phẩm: '))
    except ValueError:
      print('Dữ liệu nhập vào phải là số')
    else:
      hoadon_moi['dongia']=dongia_moi
      hoadon_moi['soluong']=soluong_moi
      hoadon_moi['giamgia']=giamgia_moi
      hoadon_moi['tongtien']=tinhtien_tudong(dongia_moi,hoadon_moi,giamgia_moi)
      hoadon_moi['phanloai']=phanloai(dongia_moi,hoadon_moi,giamgia_moi)
      break
  danhsach_hoadon.append(hoadon_moi)
  print('Thêm sản phẩm mới thành công!!!')
def capnhat_hoadon():
  kiemtra_id=input('Mời nhập vào id cần cập nhật: ').strip().upper()
  flag=False
  for hoadon in danhsach_hoadon:
    if  kiemtra_id == hoadon['id']:
      flag = True
      hoadon['dongia']=int(input('Mời nhập vào đơn giá sản phẩm: '))
      hoadon['soluong']=int(input('Mời nhập vào số lượng sản phẩm: '))
      hoadon['giamgia']=int(input('Mời nhập vào giảm gia sản phẩm: '))
      hoadon['tongtien']=tinhtien_tudong(hoadon['dongia'],hoadon['soluong'],hoadon['giamgia'])
      hoadon['phanloai']=phanloai(hoadon['dongia'],hoadon['soluong'],hoadon['giamgia'])
      print('Cập nhật hóa đơn thành công!!!')
  if not flag:
      print(f'Không tìm thấy hóa đơn có id {kiemtra_id}')
def huy_hoadon():
  kiemtra_id=input('Mời nhập vào id cần hủy: ').strip().upper()
  flag=False
  for vitri,hoadon in enumerate(danhsach_hoadon):
    if  kiemtra_id == hoadon['id']:
      flag = True
      xacnhan=input('Bạn có chắc muốn hủy và xóa hóa đơn này không? (Y/N): ').strip().upper()
      if xacnhan == 'Y':
        danhsach_hoadon.pop(vitri)
        print('Đã hủy hóa đơn thành công')
      else:
        print('Hủy hóa đơn không thành công!!!')
  if not flag:
      print(f'Không tìm thấy hóa đơn có id {kiemtra_id}')

def tim_hoadon():
  while True:
    luachon=int(input(
    '''-------------TÌM HÓA ĐƠN--------------
        1.Tìm mã hóa đơn
        2.Tim tên hóa đơn
        3.Thoát
      ---------------------------------------
        Mời nhập vào lựa chọn: '''))
    match luachon:
      case 1:
        check_id=input('Nhập mã hóa đơn cần tìm: ').strip().upper()
        flag=False
        for hoadon in danhsach_hoadon:
          if check_id == hoadon['id']:
            flag=True
            print('-------------- DANH SÁCH HÓA ĐƠN ---------------')
            print(f"|{'Mã hóa đơn':<11}|{'Tên sản phẩm':<20}|{'Đơn giá':<15}|{'Số lượng':<9}|{'Giảm giá':<10}|{'Tổng tiền':<15}|{'Phân loại':<11}|")
            print(f"|{hoadon['id']:<11}|{hoadon['tensp']:<20}|{hoadon['dongia']:<15}|{hoadon['soluong']:<9}|{hoadon['giamgia']:<10}|{hoadon['tongtien']:<15}|{hoadon['phanloai']:<11}|")
        if not flag:
          print(f'Không tìm thấy hóa đơn có id {check_id}')
      case 2:
        tim_ten=input('Nhập tên hóa đơn cần tìm: ').strip().upper()
        flag=False
        for hoadon in danhsach_hoadon:
          if tim_ten in hoadon['tensp'].upper():
            flag=True
            print(f"|{hoadon['id']:<11}|{hoadon['tensp']:<20}|{hoadon['dongia']:<15}|{hoadon['soluong']:<9}|{hoadon['giamgia']:<10}|{hoadon['tongtien']:<15}|{hoadon['phanloai']:<11}|")
        if not flag:
          print(f'Không tìm thấy hóa đơn có id {check_id}')
      case 3:
        break
      case _:
        print("Dữ liệu nhập vào không hợp lệ!!!")
def phanloai_hoadon():
  sum_caocap=0
  sum_lon=0
  sum_vua=0
  sum_nho=0
  for hoadon in danhsach_hoadon:
    if hoadon['phanloai']=='Cao cấp':
      sum_caocap+=1
    if hoadon['phanloai']=='Nhỏ':
      sum_nho+=1
    if hoadon['phanloai']=='Vừa':
      sum_vua+=1
    if hoadon['phanloai']=='Lớn':
      sum_lon+=1
  print('---------Phân Loại---------')
  print(f'|Đơn cao cấp:{sum_caocap}')
  print(f'|Đơn lớn:{sum_lon}')
  print(f'|Đơn vừa:{sum_vua}')
  print(f'|Đơn nhỏ:{sum_nho}')


def hienthi():
  if len(danhsach_hoadon)==0:
    print('DANH SÁCH HÓA ĐƠN TRỐNG!!!')
  else:
    print('-------------- DANH SÁCH HÓA ĐƠN ---------------')
    print(f"|{'Mã hóa đơn':<11}|{'Tên sản phẩm':<20}|{'Đơn giá':<15}|{'Số lượng':<9}|{'Giảm giá':<10}|{'Tổng tiền':<15}|{'Phân loại':<11}|")
    for i in danhsach_hoadon:
      print(f"|{i['id']:<11}|{i['tensp']:<20}|{i['dongia']:<15}|{i['soluong']:<9}|{i['giamgia']:<10}|{i['tongtien']:<15}|{i['phanloai']:<11}|")

while True:
  main()
  choice=int(input('Mời nhập vào lựa chọn: '))
  match choice:
    case 1:
      hienthi()
    case 2:
      them_hoadon()
    case 3:
      capnhat_hoadon()
    case 4:
      huy_hoadon()
    case 5:
      tim_hoadon()
    case 6:
      phanloai_hoadon()
    case 7:
      print('Hẹn gặp lại!!!')
      break
    case _:
      print('Dữ liệu không hợp lệ!!! Vui lòng nhập lại!!!')
      print()
