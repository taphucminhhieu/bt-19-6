class Employee:
    def __init__(self, id, name, salary_day, work_days, allowance):
        self.id = id
        self.name = name
        self.salary_day = salary_day
        self.work_days = work_days
        self.allowance = allowance

        self.total_income = 0
        self.income_type = ""

        self.calculate_income()
        self.classify_income()

    # Tính tổng thu nhập
    def calculate_income(self):
        self.total_income = (self.salary_day * self.work_days) + self.allowance

    # Phân loại thu nhập
    def classify_income(self):
        if self.total_income < 9000000:
            self.income_type = "Thấp"
        elif self.total_income < 15000000:
            self.income_type = "Trung bình"
        elif self.total_income < 30000000:
            self.income_type = "Khá"
        else:
            self.income_type = "Cao"
        return self.income_type


class EmployeeManager:
    def __init__(self):
        self.employees = []

    # Tìm mã nhân viên
    def find_id(self, id):
        for employee in self.employees:
            if employee.id == id:
                return employee
        return None

    # Hiển thị danh sách
    def show_all(self):
        print("\n===== DANH SÁCH NHÂN VIÊN =====")

        if not self.employees:
            print("Danh sách nhân viên trống")
            return

        print("-" * 110)
        print(f'{"Mã NV":<12} | {"Họ tên":<20} | {"Lương ngày":<12} | {"Ngày công":<12} | {"Phụ cấp":<12} | {"Tổng thu nhập":<15} | {"Loại thu nhập":<14} |')
        print("-" * 110)

        for employee in self.employees:
            print(print(f'{employee.id:<12} | {employee.name:<20} | {employee.salary_day:<12,.0f} | {employee.work_days:<12} | {employee.allowance:<12,.0f} | {employee.total_income:<15,.0f} | {employee.income_type:<14} |'))

    # Thêm nhân viên
    def add_employee(self):

        while True:
            input_id = input("Nhập mã nhân viên: ").strip().upper()

            if input_id == "":
                print("Mã nhân viên không được để trống")
                continue

            if self.find_id(input_id):
                print("Mã nhân viên đã tồn tại")
                continue

            break

        while True:
            try:
                input_name = input("Nhập họ tên: ").strip().title()

                if input_name == "":
                    print("Tên không được để trống")
                    continue

                input_salary_day = int(input("Nhập lương ngày: ").strip())
                input_work_days = int(input("Nhập số ngày công: ").strip())
                input_allowance = int(input("Nhập phụ cấp: ").strip())

                if input_salary_day < 0:
                    print("Lương ngày phải >= 0")
                    continue

                if input_allowance < 0:
                    print("Phụ cấp phải >= 0")
                    continue

                if input_work_days < 0 or input_work_days > 31:
                    print("Ngày công phải từ 0 -> 31")
                    continue

                employee = Employee(
                    input_id,
                    input_name,
                    input_salary_day,
                    input_work_days,
                    input_allowance
                )

                self.employees.append(employee)

                print("Thêm nhân viên thành công")
                break

            except ValueError:
                print("Dữ liệu không hợp lệ")

    # Cập nhật nhân viên
    def update_employee(self):

        while True:
            find_id_input = input(
                "Nhập mã nhân viên cần cập nhật: "
            ).strip().upper()

            employee = self.find_id(find_id_input)

            if not employee:
                print("Không tìm thấy nhân viên")
                continue

            break

        while True:
            try:
                input_salary_day = int(input("Nhập lương ngày mới: "))

                input_work_days = int(input("Nhập ngày công mới: "))

                input_allowance = int(input("Nhập phụ cấp mới: "))

                if input_salary_day < 0:
                    print("Lương ngày phải >= 0")
                    continue

                if input_allowance < 0:
                    print("Phụ cấp phải >= 0")
                    continue

                if input_work_days < 0 or input_work_days > 31:
                    print("Ngày công phải từ 0 -> 31")
                    continue

                employee.salary_day = input_salary_day
                employee.work_days = input_work_days
                employee.allowance = input_allowance

                employee.calculate_income()
                employee.classify_income()

                print("Cập nhật thành công")
                break

            except ValueError:
                print("Dữ liệu không hợp lệ")

    # Xóa nhân viên
    def delete_employee(self):

        while True:
            find_id_input = input(
                "Nhập mã nhân viên cần xóa: ").strip().upper()

            employee = self.find_id(find_id_input)

            if not employee:
                print("Không tìm thấy nhân viên")
                continue

            break

        while True:
            choice = input(
                "Bạn có chắc muốn xóa nhân viên này không? (Y/N): ").strip().upper()

            if choice == "Y":
                self.employees.remove(employee)
                print("Xóa thành công")
                break

            elif choice == "N":
                print("Hủy thao tác")
                break

            else:
                print("Lựa chọn không hợp lệ")

    # Tìm kiếm nhân viên
    def search_employee(self):
        keyword = input("Nhập tên cần tìm: ").strip().lower()

        result = []

        for employee in self.employees:
            if keyword in employee.name.lower():
                result.append(employee)

        if not result:
            print("Không tìm thấy nhân viên phù hợp")
            return

        print("-" * 110)

        for employee in result:
            print(f'{employee.id:<12} | {employee.name:<20} | {employee.salary_day:<12,.0f} | {employee.work_days:<12} | {employee.allowance:<12,.0f} | {employee.total_income:<15,.0f} | {employee.income_type:<14} |')

    # Thống kê
    def statistics(self):

        if not self.employees:
            print("Danh sách trống")
            return

        count_thap = 0
        count_tb = 0
        count_kha = 0
        count_cao = 0

        for employee in self.employees:
            if employee.income_type == "Thấp":
                count_thap += 1
            elif employee.income_type == "Trung bình":
                count_tb += 1
            elif employee.income_type == "Khá":
                count_kha += 1
            else:
                count_cao += 1

        print("===== THỐNG KÊ =====")
        print(f"Thấp       : {count_thap}")
        print(f"Trung bình : {count_tb}")
        print(f"Khá        : {count_kha}")
        print(f"Cao        : {count_cao}")


def show_menu():
    print("""
================ MENU ================
1. Hiển thị danh sách nhân viên
2. Thêm nhân viên mới
3. Cập nhật nhân viên
4. Xóa nhân viên
5. Tìm kiếm nhân viên
6. Thống kê thu nhập
7. Thoát
======================================
""")


def main():

    manager = EmployeeManager()

    manager.employees.extend([
        Employee("NV001", "Nguyen Van A", 500000, 26, 1000000),
        Employee("NV002", "Tran Van B", 400000, 25, 500000),
        Employee("NV003", "Le Thi C", 700000, 28, 2000000)
    ])

    while True:

        show_menu()

        choice = input(
            "Nhập lựa chọn của bạn: "
        ).strip()

        match choice:

            case "1":
                manager.show_all()

            case "2":
                manager.add_employee()

            case "3":
                manager.update_employee()

            case "4":
                manager.delete_employee()

            case "5":
                manager.search_employee()

            case "6":
                manager.statistics()

            case "7":
                print(
                    "Cảm ơn bạn đã sử dụng hệ thống quản lý nhân sự!"
                )
                break

            case _:
                print("Lựa chọn không hợp lệ")


if __name__ == "__main__":
    main()
