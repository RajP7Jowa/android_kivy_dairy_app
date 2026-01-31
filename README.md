# MilkShree: KivyMD Dairy Management System

**MilkShree** is a professional mobile application built with **Python and KivyMD**, specifically designed for dairy owners and milk collection centers. Optimized for **Android 11+ (SDK 30+)**, the app automates the milk procurement process through intelligent price calculation and instant thermal printing.

---

## 🚀 Key Features

* **Smart Rate Engine:** Automatically calculates milk prices based on a pre-saved **Fat and SNF (Solid-Not-Fat)** price list.
* **Driver-less Printing:** Seamlessly generates physical receipts using the **Quick Printer (ESC/POS)** bridge.
* **Invoice History:** Maintains a complete local record of all transactions for easy auditing and history tracking.
* **Modern Material UI:** Features a high-performance, responsive interface optimized for fast data entry in field conditions.
* **Modern Android Support:** Fully compatible with Android 11+ scoped storage and permission sets.

---

## 🛠 Technical Stack

* **Frontend:** [KivyMD](https://kivymd.readthedocs.io/) (Material Design components).
* **Backend:** Python with **SQLite** for relational data storage.
* **Target OS:** Android SDK 30+ (Android 11 and above).
* **Integration:** Android Intents for communication with external printing services.

---

## 📥 External Dependencies

To enable the printing functionality, the following resources are required:

1.  **MilkShree Portal:** [Project Web Page](https://rajp7jowa.github.io/krashishakti/milkshree.html)
2.  **Printing Utility:** [Quick Printer (ESC/POS) on Play Store](https://play.google.com/store/apps/details?id=pe.diegoveloper.printerserverapp)
    * *Note: This utility allows the app to communicate with Bluetooth/USB thermal printers without custom drivers.*

---

## ⚙️ Operational Workflow

1.  **Rate Configuration:** Users save their specific Fat/SNF price matrix into the local app database.
2.  **Data Entry:** Input the milk quantity and quality (Fat/SNF) during the collection process.
3.  **Receipt Generation:** The app computes the total amount ($Price = Quantity \times Rate$) and triggers the **Quick Printer** app.
4.  **Archive:** Every transaction is saved to the **Invoice History** for future reference and reporting.

---

## 🔗 Project Links

* **Developer Website:** [KrashiShakti](https://rajp7jowa.github.io/krashishakti/milkshree.html)
* **Required Printer App:** [Download Quick Printer](https://play.google.com/store/apps/details?id=pe.diegoveloper.printerserverapp)

---
*Created for general-purpose dairy management and efficient milk collection.*
