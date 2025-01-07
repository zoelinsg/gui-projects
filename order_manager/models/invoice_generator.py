# 檔案名稱：order_manager/models/invoice_generator.py
# 發票生成邏輯

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

class InvoiceGenerator:
    def __init__(self):
        pass

    def generate(self, invoice_id, customer_name, orders):
        # 使用發票號碼命名 PDF 文件
        file_name = f"{invoice_id}.pdf"
        # 創建 PDF 文件
        pdf = canvas.Canvas(file_name, pagesize=A4)
        pdf.setTitle("Invoice")

        # 標題
        pdf.drawString(100, 800, f"Invoice for {customer_name}")
        pdf.drawString(100, 780, f"Invoice ID: {invoice_id}")

        # 訂單明細
        y = 750
        for order in orders:
            pdf.drawString(100, y, f"Order ID: {order['order_id']}, Item: {order['item']}, Quantity: {order['quantity']}, Total: ${order['total']:.2f}")
            y -= 20

        # 保存 PDF 文件
        pdf.save()