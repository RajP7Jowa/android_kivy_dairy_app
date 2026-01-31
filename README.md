# MilkShree 🥛
A professional KivyMD mobile application designed for dairy management. MilkShree automates the milk collection process by calculating rates based on Fat/SNF parameters and providing instant billing solutions for Android 11+ devices.
## 🚀 Features
 * Automated Billing: Calculate milk prices instantly using a customizable Fat & SNF rate list.
 * Thermal Printing: Integrated with the Quick Printer (ESC/POS) app for driver-less receipt printing.
 * Transaction History: Maintain a local digital record of all invoices for easy auditing.
 * Android 11+ Ready: Fully compatible with Android SDK 30+ requirements.
 * Modern UI: A clean, Material Design interface built for high-speed data entry.
## 🛠 Technical Overview
 * Framework: KivyMD (Python)
 * Database: SQLite for persistent storage of rates and invoice history.
 * Printing Method: Utilizes Android Intents to send data to the Quick Printer application.
 * Platform: Android (Compiled via Buildozer).
## 📥 External Dependencies
To enable printing functionality, this app works in tandem with:
 * MilkShree Web: Visit Project Page
 * Printing Service: Quick Printer (ESC/POS)
   * Note: Install this from the Play Store to handle Bluetooth/USB thermal printer communication without additional drivers.
## ⚙️ How it Works
 * Setup: Define your Fat and SNF price matrix within the app settings.
 * Collection: Input the milk quantity and quality (Fat/SNF) during collection.
 * Print: The app generates the receipt data and passes it to Quick Printer via an intent to produce the physical slip.
 * Save: The transaction is automatically logged into the local history for future reference.
