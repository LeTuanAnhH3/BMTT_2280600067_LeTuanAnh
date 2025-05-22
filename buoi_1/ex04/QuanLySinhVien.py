from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        # Khởi tạo listSinhVien trong constructor để nó là thuộc tính của instance
        self.listSinhVien = [] 

    def generateID(self):
        maxID = 0  # Khởi tạo maxID bằng 0 hoặc 1 tùy logic của bạn
        if (self.soluongSinhVien() > 0):
            maxID = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxID < sv._id):
                    maxID = sv._id
        maxID = maxID + 1
        return maxID

    def soluongSinhVien(self):
        # Sửa lỗi: Trả về độ dài của list trực tiếp
        return len(self.listSinhVien) 

    def nhapSinhVien(self):
        svID = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        # Xử lý lỗi khi người dùng nhập không phải số
        try:
            diemTB = float(input("Nhap diem cua sinh vien: "))
        except ValueError:
            print("Diem trung binh phai la mot so. Vui long nhap lai.")
            return # Thoát khỏi hàm nếu nhập sai

        sv = SinhVien(svID, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
        print("Them sinh vien thanh cong!")

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if (sv is not None): # Dùng 'is not None' thay vì '!= None'
            print(f"Cap nhat thong tin sinh vien ID: {ID}")
            name = input(f"Nhap ten sinh vien moi (hien tai: {sv._name}): ") or sv._name
            sex = input(f"Nhap gioi tinh moi (hien tai: {sv._sex}): ") or sv._sex
            major = input(f"Nhap chuyen nganh moi (hien tai: {sv._major}): ") or sv._major
            
            try:
                diemTB_str = input(f"Nhap diem moi (hien tai: {sv._diemTB}): ")
                if diemTB_str: # Chỉ cập nhật nếu người dùng nhập giá trị
                    diemTB = float(diemTB_str)
                else:
                    diemTB = sv._diemTB # Giữ nguyên điểm cũ nếu không nhập
            except ValueError:
                print("Diem trung binh phai la mot so. Giu nguyen diem cu.")
                diemTB = sv._diemTB

            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
            print("Cap nhat thong tin sinh vien thanh cong!")
        else:
            print(f"Sinh vien co ID = {ID} khong ton tai.")

    def sortByID(self):
        if self.soluongSinhVien() > 0:
            self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
            print("Danh sach sinh vien da duoc sap xep theo ID.")
        else:
            print("Danh sach sinh vien trong, khong the sap xep.")

    def sortByName(self):
        if self.soluongSinhVien() > 0:
            self.listSinhVien.sort(key=lambda x: x._name.lower(), reverse=False) # Sắp xếp không phân biệt chữ hoa/thường
            print("Danh sach sinh vien da duoc sap xep theo ten.")
        else:
            print("Danh sach sinh vien trong, khong the sap xep.")

    def sortByDiemTB(self):
        if self.soluongSinhVien() > 0:
            self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=True) # Sắp xếp giảm dần theo điểm
            print("Danh sach sinh vien da duoc sap xep theo diem trung binh (giam dan).")
        else:
            print("Danh sach sinh vien trong, khong the sap xep.")

    def findByID(self, ID):
        searchResult = None
        if (self.soluongSinhVien() > 0):
            for sv in self.listSinhVien: # Sửa lỗi: Lặp qua listSinhVien
                if (sv._id == ID):
                    searchResult = sv
                    break # Tìm thấy thì thoát vòng lặp
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if (self.soluongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV

    def deleteByID(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv is not None): # Dùng 'is not None' thay vì '!= None'
            self.listSinhVien.remove(sv)
            isDeleted = True
            print(f"Da xoa sinh vien co ID = {ID}.")
        else:
            print(f"Khong tim thay sinh vien co ID = {ID}.")
        return isDeleted

    def xepLoaiHocLuc(self, sv: SinhVien):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung binh"
        else:
            sv._hocLuc = "Yeu"

    def showSinhVien(self, listSV):
        if not listSV: # Kiểm tra listSV rỗng
            print("Khong co sinh vien nao trong danh sach.")
            return

        print("{:<8}{:<20}{:<10}{:<20}{:<10}{:<15}".format("ID", "Ten", "Gioi tinh", "Chuyen nganh", "Diem TB", "Hoc Luc"))
        print("-" * 83) # Dòng kẻ ngang để dễ nhìn
        for sv in listSV:
            print("{:<8}{:<20}{:<10}{:<20}{:<10.2f}{:<15}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien