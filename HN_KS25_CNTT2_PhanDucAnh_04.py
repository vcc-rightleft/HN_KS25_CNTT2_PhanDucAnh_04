danhsach_hoadon = [
    {
        'id': 'HD001',
        'tensp': 'Ban phim co Corsair',
        'dongia': 1800000,
        'soluong': 2,
        'giamgia': 200000,
        'tongtien': 3740000,
        'phanloai': 'Vừa'
    }
]

def main():
    print('''
--------------- THANH TOÁN HÓA ĐƠN --------------
  1. Hiển thị danh sách hóa đơn
  2. Lập hóa đơn mới
  3. Cập nhật thông tin hóa đơn
  4. Hủy hóa đơn lỗi
  5. Tìm kiếm hóa đơn
  6. Thống kê phân loại hóa đơn
  7. Thoát chương trình
-------------------------------------------------
        ''')

def tinhtien_tudong(dongia, soluong, giamgia):
    tongtien = (dongia * soluong - giamgia) * 1.1
    return tongtien

def phanloai_tudong(dongia, soluong, giamgia):
    tongtien = (dongia * soluong - giamgia) * 1.1
    if tongtien <= 1_000_000:
        return 'Nhỏ'
    elif tongtien <= 5_000_000:
        return 'Vừa'
    elif tongtien <= 15_000_000:
        return 'Lớn'
    else:
        return 'Cao cấp'

def them_hoadon():
    hoadon_moi = {}
    while True:
        id_moi = input('Mời nhập vào mã hóa đơn mới: ').strip().upper()
        if len(id_moi) == 0:
            print('Mã hóa đơn không được để trống!!!')
            continue
        flag = False
        for hoadon in danhsach_hoadon:
            if id_moi == hoadon['id']:
                flag = True
                print('ID đã tồn tại!!!')
                break
        if not flag:
            hoadon_moi['id'] = id_moi
            break

    while True:
        tensp_moi = input('Mời nhập vào tên sản phẩm mới: ').strip().title()
        if len(tensp_moi) == 0:
            print('Tên sản phẩm không được để trống!!!')
        else:
            hoadon_moi['tensp'] = tensp_moi
            break

    while True:
        try:
            dongia_moi = int(input('Mời nhập vào đơn giá sản phẩm: '))
            soluong_moi = int(input('Mời nhập vào số lượng sản phẩm: '))
            giamgia_moi = int(input('Mời nhập vào giảm giá sản phẩm: '))
            if dongia_moi < 0 or soluong_moi < 0 or giamgia_moi < 0:
                print('Các giá trị số không được âm! Vui lòng nhập lại.')
                continue
        except ValueError:
            print('Dữ liệu nhập vào phải là số nguyên!')
        else:
            hoadon_moi['dongia'] = dongia_moi
            hoadon_moi['soluong'] = soluong_moi
            hoadon_moi['giamgia'] = giamgia_moi
            hoadon_moi['tongtien'] = tinhtien_tudong(dongia_moi, soluong_moi, giamgia_moi)
            hoadon_moi['phanloai'] = phanloai_tudong(dongia_moi, soluong_moi, giamgia_moi)
            break

    danhsach_hoadon.append(hoadon_moi)
    print('Thêm hóa đơn mới thành công!!!')

def capnhat_hoadon():
    kiemtra_id = input('Mời nhập vào id cần cập nhật: ').strip().upper()
    flag = False
    for hoadon in danhsach_hoadon:
        if kiemtra_id == hoadon['id']:
            flag = True
            while True:
                try:
                    hoadon['dongia'] = int(input('Mời nhập vào đơn giá sản phẩm mới: '))
                    hoadon['soluong'] = int(input('Mời nhập vào số lượng sản phẩm mới: '))
                    hoadon['giamgia'] = int(input('Mời nhập vào giảm giá sản phẩm mới: '))
                    break
                except ValueError:
                    print("Dữ liệu phải là số! Vui lòng nhập lại.")
            
            hoadon['tongtien'] = tinhtien_tudong(hoadon['dongia'], hoadon['soluong'], hoadon['giamgia'])
            hoadon['phanloai'] = phanloai_tudong(hoadon['dongia'], hoadon['soluong'], hoadon['giamgia'])
            print('Cập nhật hóa đơn thành công!!!')
            break
            
    if not flag:
        print(f'Không tìm thấy hóa đơn có id {kiemtra_id}')

def huy_hoadon():
    kiemtra_id = input('Mời nhập vào id cần hủy: ').strip().upper()
    flag = False
    for vitri, hoadon in enumerate(danhsach_hoadon):
        if kiemtra_id == hoadon['id']:
            flag = True
            xacnhan = input('Bạn có chắc muốn hủy và xóa hóa đơn này không? (Y/N): ').strip().upper()
            if xacnhan == 'Y':
                danhsach_hoadon.pop(vitri)
                print('Đã hủy hóa đơn thành công')
            else:
                print('Đã giữ lại hóa đơn.')
            break
    if not flag:
        print(f'Không tìm thấy hóa đơn có id {kiemtra_id}')

def in_tieude_bang():
    print('-------------- DANH SÁCH HÓA ĐƠN ---------------')
    print(f"|{'Mã hóa đơn':<11}|{'Tên sản phẩm':<20}|{'Đơn giá':<15}|{'Số lượng':<9}|{'Giảm giá':<10}|{'Tổng tiền':<15}|{'Phân loại':<11}|")

def in_dong_hoadon(hoadon):
    print(f"|{hoadon['id']:<11}|{hoadon['tensp']:<20}|{hoadon['dongia']:<15}|{hoadon['soluong']:<9}|{hoadon['giamgia']:<10}|{hoadon['tongtien']:<15.0f}|{hoadon['phanloai']:<11}|")

def tim_hoadon():
    while True:
        print('''-------------TÌM HÓA ĐƠN--------------
        1. Tìm mã hóa đơn
        2. Tìm tên sản phẩm trong hóa đơn
        3. Thoát tìm kiếm
---------------------------------------''')
        try:
            luachon = int(input('Mời nhập vào lựa chọn: '))
        except ValueError:
            print("Vui lòng nhập số từ 1 đến 3!")
            continue

        match luachon:
            case 1:
                check_id = input('Nhập mã hóa đơn cần tìm: ').strip().upper()
                flag = False
                for hoadon in danhsach_hoadon:
                    if check_id == hoadon['id']:
                        if not flag:
                            in_tieude_bang()
                        flag = True
                        in_dong_hoadon(hoadon)
                if not flag:
                    print(f'Không tìm thấy hóa đơn có id {check_id}')
            case 2:
                tim_ten = input('Nhập tên sản phẩm cần tìm: ').strip().upper()
                flag = False
                for hoadon in danhsach_hoadon:
                    if tim_ten in hoadon['tensp'].upper():
                        if not flag:
                            in_tieude_bang()
                        flag = True
                        in_dong_hoadon(hoadon)
                if not flag:
                    print(f'Không tìm thấy hóa đơn nào có chứa tên: {tim_ten}')
            case 3:
                break
            case _:
                print("Dữ liệu nhập vào không hợp lệ!!!")

def phanloai_hoadon():
    sum_caocap = 0
    sum_lon = 0
    sum_vua = 0
    sum_nho = 0
    for hoadon in danhsach_hoadon:
        if hoadon['phanloai'] == 'Cao cấp':
            sum_caocap += 1
        elif hoadon['phanloai'] == 'Lớn':
            sum_lon += 1
        elif hoadon['phanloai'] == 'Vừa':
            sum_vua += 1
        elif hoadon['phanloai'] == 'Nhỏ':
            sum_nho += 1
            
    print('---------Phân Loại---------')
    print(f'| Đơn cao cấp: {sum_caocap}')
    print(f'| Đơn lớn:    {sum_lon}')
    print(f'| Đơn vừa:    {sum_vua}')
    print(f'| Đơn nhỏ:    {sum_nho}')

def hienthi():
    if len(danhsach_hoadon) == 0:
        print('DANH SÁCH HÓA ĐƠN TRỐNG!!!')
    else:
        in_tieude_bang()
        for i in danhsach_hoadon:
            in_dong_hoadon(i)

while True:
    main()
    try:
        choice = int(input('Mời nhập vào lựa chọn: '))
    except ValueError:
        print('Dữ liệu không hợp lệ!!! Vui lòng nhập số từ 1 đến 7!!!\n')
        continue

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
            print('Lựa chọn nằm ngoài danh mục!!! Vui lòng nhập lại!!!\n')
