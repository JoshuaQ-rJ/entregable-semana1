# 🗂️ Inventory Manager — Entregable Semana 3

A command-line inventory management system built in Python. It allows users to add, view, analyze, save, and reload products using a CSV file for persistent storage.

---

## 📁 Project Structure

```
entregable-semana1/
├── Inventario.py   # Shared inventory list
├── app.py          # CSV save/load logic
├── menu.py         # Main menu and program flow
├── services.py     # Input validation functions
└── data/
    └── data.csv    # Persistent storage file
```

---

## ⚙️ How It Works

The program starts from `menu.py` and runs a loop that shows the user a menu with 6 options:

1. **Add a product** — asks for name, price, and amount, then appends it to the inventory list.
2. **Show inventory** — prints all registered products with their price and stock.
3. **Calculate inventory** — computes total value, number of products, most expensive item, and item with highest stock.
4. **Save inventory** — writes the current inventory to `data/data.csv`.
5. **Upload inventory** — reads `data/data.csv` and loads it back into memory.
6. **Exit** — closes the program.

---

## 🧩 Modules

### `Inventario.py`
Defines the shared `inventory` list used across all modules.

### `services.py`
Contains input validation functions:
- `name()` — validates that the product name contains only letters.
- `price()` — validates that the price is a positive integer.
- `amount()` — validates that the amount is a positive integer.
- `option()` — validates that the menu option is between 1 and 6.

### `app.py`
Handles CSV operations:
- `save_inventory()` — writes the inventory list to `data/data.csv`.
- `read_register()` — reads the CSV and returns a list of dictionaries.
- `upload_inventory()` — loads CSV data back into the inventory list.

### `menu.py`
Main entry point. Runs the menu loop and connects all modules together.

---

## ▶️ How to Run

```bash
python menu.py
```

Make sure all files are in the same folder before running.

---

## 📋 Requirements

- Python 3.x
- No external libraries — uses only built-in `csv` module.

---

## 💾 Data Format

Products are stored in `data/data.csv` with the following columns:

| name | price | amount |
|------|-------|--------|
| arroz | 5000.0 | 25 |
| azucar | 2000.0 | 50 |

---

## 👤 Author

**Joshua**  
Universidad de la Costa (CUC)  
Systems Engineering & Graphic Design
