class Product:
    def __init__(self, id, name, price, quantity_sold, discount):
        self.id = id
        self.name = name
        self.price = price
        self.quantity_sold = quantity_sold
        self.discount = discount

        self.total_revenue = 0
        self.revenue_type = ""

        self.calculate_revenue()
        self.classify_revenue()

    def calculate_revenue(self):
        total = self.price * self.quantity_sold - self.discount
        if total < 0:
            total = 0

        self.total_revenue = total

    def classify_revenue(self):
        if self.total_revenue < 5000000:
            self.revenue_type = 'Thấp'
        elif self.total_revenue < 20000000:
            self.revenue_type = 'Trung bình'
        elif self.total_revenue < 50000000:
            self.revenue_type = 'Khá'
        else:
            self.revenue_type = 'Cao'


class ProductManager:
    def __init__(self):
        self.products = []

    def check_duplicate_id(self, id):
        for product in self.products:
            if product.id == id:
                return product
        return None

    def add_product(self):
        print('--- THÊM SẢN PHẨM ---')
        while True:
            new_id = input('Nhập mã sản phẩm: ').strip().upper()

            if not new_id:
                print('Mã sản phẩm không được để trống')
                continue

            if self.check_duplicate_id(new_id):
                print('Mã đã tồn tại! Hãy thử mã khác!')
                continue

            break

        while True:
            new_name = input('Nhập tên sản phẩm: ').strip()

            if not new_name:
                print("Tên sản phẩm không được để trống!")
                continue

            break

        new_price = input_float('Nhập giá bán: ')

        new_quantity = input_int('Nhập số lượng đã bán: ')

        new_discount = input_float('Nhập giảm giá: ')

        product = Product(new_id, new_name, new_price,
                          new_quantity, new_discount)

        self.products.append(product)

        print('Thêm sản phẩm thành công.')

    def show_all(self):
        if not self.products:
            print('Danh sách sản phẩm đang rỗng!')
        else:
            show_row_one()
            for product in self.products:
                print(f'{product.id:<12} | {product.name:<20} | {product.price:<10,.0f} | {product.quantity_sold:<15} | {product.discount:<10,.0f} | {product.total_revenue:<15,.0f} | {product.revenue_type:<14} |')
                print('-' * 120)

    def update_product(self):
        update_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()

        product = self.check_duplicate_id(update_id)

        if not product:
            print("Không tìm thấy sản phẩm cần cập nhật!")
            return

        product.price = input_float('Cập nhật giá bán: ')

        product.quantity = input_int('Cập nhật số lượng đã bán: ')

        product.discount = input_float('Cập nhật giảm giá: ')

        product.calculate_revenue()
        product.classify_revenue()

        print("Cập nhật sản phẩm thành công!")

    def delete_product(self):
        remove_id = input("NHập mã sản phẩm cần xóa: ").strip().upper()

        product = self.check_duplicate_id(remove_id)

        if not product:
            print("Không tìm thấy sản phẩm cần xóa")
            return

        confirm = input(
            "Bạn có chắc chắn muốn xóa sản phẩm này không? (Y/N): ").strip().lower()

        if confirm == 'y':
            self.products.remove(product)
            print("Xóa sản phẩm thành công!")

        elif confirm == 'n':
            print("Đã hủy thao tác xóa!")

        else:
            print("Lựa chọn không hợp lệ!")

    def search_product(self):
        search_name = input("Nhập từ khóa tìm kiếm: ").strip()

        result = []

        for product in self.products:
            if search_name in product.name.lower():
                result.append(product)

        if not result:
            print("Không tìm thấy sản phẩm phù hợp!")
            return

        show_row_one()
        for product in result:
            print(f'{product.id:<12} | {product.name:<20} | {product.price:<10,.0f} | {product.quantity_sold:<15} | {product.discount:<10,.0f} | {product.total_revenue:<15,.0f} | {product.revenue_type:<14} |')
            print('-' * 120)

    def statistics(self):
        if not self.products:
            print('Chưa có dữ liệu để thống kê')

        else:
            count_thap = 0
            count_tb = 0
            count_kha = 0
            count_cao = 0

            for product in self.products:
                if product.revenue_type == 'Thấp':
                    count_thap += 1
                elif product.revenue_type == 'Trung bình':
                    count_tb += 1
                elif product.revenue_type == 'Khá':
                    count_kha += 1
                else:
                    count_cao += 1

            print("-" * 55)
            print("             --- THỐNG KÊ ---")
            print("-" * 55)
            print(f"{'Phân loại doanh thu':<25} | {'Số lượng sản phẩm':<20} |")
            print("-" * 55)
            print(f'{'Thấp':<25} | {count_thap:<20} |')
            print("-" * 55)
            print(f'{'Trung bình':<25} | {count_tb:<20} |')
            print("-" * 55)
            print(f'{'Khá':<25} | {count_kha:<20} |')
            print("-" * 55)
            print(f'{'Cao':<25} | {count_cao:<20} |')
            print('-'*55)


def input_float(prompt, min_value=0):
    while True:
        try:
            value = float(input(prompt))

            if value < min_value:
                print(f'Giá trị phải >= {min_value}')
                continue

            return value

        except ValueError:
            print('Vui lòng nhập số hợp lệ')


def input_int(prompt, min_value=0, max_value=10000):
    while True:
        try:
            value = int(input(prompt))

            if value < min_value or value > max_value:
                print(f'Giá trị phải từ {min_value} đến {max_value}')
                continue

            return value

        except ValueError:
            print("Vui lòng nhập số hợp lệ")


def show_row_one():
    print('-' * 120)
    print(f'{'Mã sản phẩm':<12} | {'Tên sản phẩm':<20} | {'Giá bán':<10} | {'Số lượng đã bán':<15} | {'Giảm giá':<10} | {'Tổng doanh thu':<15} | {'Loại danh thu':<14} |')
    print('-' * 120)


def show_menu():
    print(""" 
================ MENU ================
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật sản phẩm
4. Xóa sản phẩm
5. Tìm kiếm sản phẩm
6. Thống kê doanh thu
7. Thoát
=====================================
 """)


def main():
    manager = ProductManager()

    manager.products.extend([
        Product("SP001", "Laptop Dell", 15000000, 3, 2000000),
        Product("SP002", "Chuột Logitech", 350000, 20, 500000),
        Product("SP003", "Bàn phím cơ AKKO", 1200000, 10, 1000000),
        Product("SP004", "Màn hình Samsung", 4500000, 5, 0),
        Product("SP005", "Tai nghe Sony", 2500000, 1, 0)
    ])

    while True:
        show_menu()
        choice = input('Nhập lựa chọn của bạn: ').strip()

        if choice == "1":
            manager.show_all()

        elif choice == "2":
            manager.add_product()

        elif choice == "3":
            manager.update_product()

        elif choice == "4":
            manager.delete_product()

        elif choice == "5":
            manager.search_product()

        elif choice == "6":
            manager.statistics()

        elif choice == "7":
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý sản phẩm!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
