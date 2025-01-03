import asyncio
import websockets

class MonitorController:
    async def fetch_crypto_price(self, symbol: str):
        # 連接到加密貨幣價格的 WebSocket 並訂閱指定的符號
        async with websockets.connect("wss://crypto-price-websocket.example") as ws:
            await ws.send(f"SUBSCRIBE {symbol}")
            response = await ws.recv()
            return response

    def update_ui(self, ui_element, data):
        # 用於更新 UI 元件
        ui_element.setText(str(data))